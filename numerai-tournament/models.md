# Models

## Tutorials

The best way to learn about building models on our data is through our tutorials:

1. [Hello Numerai](https://numer.ai/tutorial/hello-numerai)
2. [Feature Neutralization](https://numer.ai/tutorial/feature-neutralization)
3. [Target Ensembles](https://numer.ai/tutorial/target-ensemble)

## Benchmark Models

Numerai Benchmark Models are a set of standard models that the Numerai team built.  Their predictions are then given out every round so that anyone can easily submit them and stake on them if they want. These models are an easy way to compare your model to the current state-of-the-art.

The list of models and their recent performance is here:  [numer.ai/\~benchmark\_models](https://numer.ai/\~benchmark\_models)

### Download

The validation and live predictions are available through the [api](https://github.com/uuazed/numerapi).

```python
from numerapi import NumerAPI
napi = NumerAPI()
napi.download_dataset("v4.3/train_benchmark_models.parquet", "train_benchmark_models.parquet")
napi.download_dataset("v4.3/validation_benchmark_models.parquet", "validation_benchmark_models.parquet")
napi.download_dataset("v4.3/live_benchmark_models.parquet", "live_benchmark_models.parquet")
```

### How they are made

**Walk Forward Cross Validation**

All predictions are made using a Walk-Forward framework.  This means all predictions are made using models which were trained only on data which was available prior to the date of the prediction being made.&#x20;

Specifically, the data is split up into chunks of 156 eras.  Then for each chunk of eras, the predictions are given by a model which is trained up to first\_era\_of\_chunk - purge\_eras.  The number of purge\_eras is always 8 for 20D targets, and 16 for 60D targets. &#x20;

So a model is trained on eras 1 through 148, then purge eras 149 through 156, and then predict eras 157 through 312. Next, train on eras 1 through 304, purge 305 through 312, predict 313 through 468, and so on.  Your walk-forward validation windows should look something like this:

| Window | Train Start | Train End | Val Start | Val End |
| ------ | ----------- | --------- | --------- | ------- |
| 1      | 1           | 148       | 157       | 312     |
| 2      | 1           | 304       | 313       | 468     |
| 3      | 1           | 460       | 469       | 624     |
| 4      | 1           | 616       | 625       | 780     |
| ...    | ...         | ...       | ...       | ...     |

**Standard Large LGBM params**

All of the models use the following LGBM parameters:

```python
standard_large_lgbm_params = {
  "n_estimators": 20000,
  "learning_rate": 0.001,
  "max_depth": 6,
  "num_leaves": 2**6,
  "colsample_bytree": 0.1,
}
```

We've found that having more trees can be helpful, and we've found that having less trees with more depth can also achieve similar results with lower compute requirements.  You can read more about this hyper-parameter research in [this forum post](https://forum.numer.ai/t/super-massive-lgbm-grid-search/6463).

After the release of v5 data, we announced the higher performance "deep" parameters:

```python
deep_lgbm_params = {
  "n_estimators": 30000,
  "learning_rate": 0.001,
  "max_depth": 10,
  "num_leaves": 1024,
  "colsample_bytree": 0.1,
  "min_data_in_leaf": 10000
}
```

**Ensembles**

All of the ensembles use the following steps:

1. gaussianize each of the predictions on a per-era basis
2. standardize to standard deviation 1
3. dot-product the predictions with a weights vector representing the desired weight on each model
4. gaussianize the resulting vector
5. (if applicable) neutralize the vector

Steps 1 through 4 look something like this:

```python
def rank_gauss_pow1(s: pd.Series) -> pd.Series:
  # do rank-normalize
  s_rank = rank_keep_ties_keep_na(s)

  # gaussianize
  s_rank_norm = pd.Series(stats.norm.ppf(s_rank), index=s_rank.index)

  # Standardize to 1 std
  result_series = s_rank_norm / s_rank_norm.std()

  return result_series


ensemble_cols = ["V4_LGBM_NOMI20", "V42_RAIN_ENSEMBLE"]
weight_vector = [0.1, 0.9]
for col in X[ensemble_cols]:
  if "era" in X.columns:
      X[col] = X.groupby("era", group_keys=False)[col].transform(lambda s1: rank_gauss_pow1(s1))
  else:
      # check X contains only a single era
      assert 1800 < X.shape[0] < 6000
      X[col] = rank_gauss_pow1(X[col])
return X[ensemble_cols].dot(weight_vector)
```

**Neutralization**

A couple of the models have some neutralization involved.  This is basically doing a regression to find out your predictions' exposures to each feature, and then subtracting those exposures from your predictions vector such that the result is a vector which is orthogonal to all of those features.

Here's the code to neutralize some set of vectors (columns) by some list of features (neutralizers):

```python
def neutralize(
  df, columns, neutralizers=None, proportion=1.0, era_col="era"
):
  if neutralizers is None:
      neutralizers = []
  unique_eras = df[era_col].unique()
  computed = []
  for u in unique_eras:
      df_era = df[df[era_col] == u]
      scores = df_era[columns].values
      scores2 = []
      for x in scores.T:
          x = pd.Series(x)
          x = (x.rank(method="first") - 0.5) / len(x.dropna())
          x = stats.norm.ppf(x)
          scores2.append(x)
      scores = np.array(scores2).T
      exposures = (
          df_era[neutralizers]
          .fillna(df_era[neutralizers].median())
          .fillna(0.5)
          .values
      )

      scores -= proportion * exposures.dot(
          np.linalg.pinv(exposures.astype(np.float32), rcond=1e-6).dot(
              scores.astype(np.float32)
          )
      )

      scores /= pd.DataFrame(scores).std(ddof=0, axis=0, skipna=True).values

      computed.append(scores)

  return pd.DataFrame(np.concatenate(computed), columns=columns, index=df.index)
```

### What are they?

The naming formula for many benchmarks is as follows:

**{data\_version}\_LGBM\_{target}**

There are many models that have some combination of a data version (V2, V3, V4, V41, V42, V43, V5) and a target (e.g. cyrusd\_20, teager2b\_20, etc.). These are models trained in the standard walk-forward way, with standard LGBM parameters, using the specified data version and target. That's all!



There are also unique models we created that don't have that naming scheme:&#x20;

**V5\_LGBM\_CT\_BLEND (coming soon)**

This is a simple 50/50 blend of V5\_LGBM\_TEAGER2B20 and V5\_LGBM\_CYRUSD20



**V{42 | 43}\_LGBM\_CT\_BLEND**

This is a simple 50/50 blend of V{42 | 43}\_LGBM\_TEAGER20 and V{42 | 43}\_LGBM\_CYRUS20



**V42\_RAIN\_ENSEMBLE**&#x20;

This is an ensemble of 22 different standard models. It uses the 11 best targets that we had made as of the release of the Rain dataset, with an emphasis on Cyrus, the scoring target, and twice as much weight on 20D targets as on 60D targets. The target weights are:

Cyrus20: 33%, Ralph20: 3.3%, Jeremy20: 3.3%, Waldo20: 3.3%, Tyler20: 3.3%, Victor20: 3.3%

Cyrus60: 17%, Ralph60: 1.7%, Jeremy60: 1.7%, Waldo60: 1.7%, Tyler60: 1.7%, Victor60: 1.7%

Alpha20: 3.3%, Bravo20: 3.3%, Charlie20: 3.3%, Delta20: 3.3%, Echo20: 3.3%

Alpha60: 1.7%, Bravo60: 1.7%, Charlie60: 1.7%, Delta60: 1.7%, Echo60: 1.7%



**V42\_RAIN\_ENSEMBLE2**

This is the same as v42\_RAIN\_ENSEMBLE, but with no weight on the 60D versions.

It is also neutral to the serenity set of features. &#x20;



**V42\_EXAMPLE\_PREDS**

This is a standard model using V42 data and Cyrus20 target.&#x20;



**V41\_EXAMPLE\_PREDS**

This is what was once the Sunshine Example Model.  It uses standard models built on 6 different targets: Nomi20, Jerome60, Ralph20, Victor20, Waldo20, Tyler20.

These models are equal weight in the ensemble and the final predictions are neutralized at a proportion of 50% to the V4.1 "medium" feature set.



**V3\_EXAMPLE\_PREDS**

This is a standard model trained on the v3 equivalent feature set and the Ralph20 target.



**V2\_EXAMPLE\_PREDS**

This is a standard model trained on the v2 equivalent feature set and the Nomi20 target.



The following models are on the Benchmark Models page, but their predictions aren't present in the predictions files because they are either obsolete or easily reproducible:

**V4\_EXAMPLE\_PREDS** - A standard model on V4 data and Nomi20, and is neutral to the 50 "riskiest features" calculated by which features have the biggest change in mean correlation with Nomi between half1 and half2 of the training data.&#x20;

**INTEGRATION\_TEST** - Submits our favorite model at the time. For years, this was V2 example predictions, but with the advent of v3 and v4 datasets it evolves over time. At the time of writing this, it is submitting RAIN\_ENSEMBLE predictions.

**NB\_HELLO\_NUMERAI** - Submits the model created by the default Hello Numerai tutorial notebook.

**NB\_FEATURE\_NEUTRAL** - Submits the model created by the feature neutralization tutorial notebook.

**NB\_TARGET\_ENSEMBLE** - Submits the model created by the target ensemble tutorial notebook.

**NB\_EXAMPLE\_MODEL** - Submits the model created by the barebones example\_model notebook.

