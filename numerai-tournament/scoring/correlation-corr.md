# Correlation (CORR)

## What is CORR?

The primary scoring metric on Numerai is the correlation between your model's predictions and the target.&#x20;

Numerai uses a special variation of correlation we call "Numerai Corr". At a high level, this metric is designed to be a good proxy for actual portfolio returns if the predictions were used in live trading.

## How is CORR computed?

```python
def numerai_corr(preds, target):
  # rank (keeping ties) then Gaussianize predictions to standardize prediction distributions
  ranked_preds = (preds.rank(method="average").values - 0.5) / preds.count()
  gauss_ranked_preds = stats.norm.ppf(ranked_preds)
  
  # make targets centered around 0
  centered_target = target - target.mean()
  
  # raise both preds and target to the power of 1.5 to accentuate the tails
  preds_p15 = np.sign(gauss_ranked_preds) * np.abs(gauss_ranked_preds) ** 1.5
  target_p15 = np.sign(centered_target) * np.abs(centered_target) ** 1.5
  
  # finally return the Pearson correlation
  return np.corrcoef(preds_p15, target_p15)[0, 1]
```

* First the predictions are gauss ranked. We do this to match our live trading process where all model predictions are standardized this way before being ensembled together in the meta model.
* Then the target is centered around 0. We do this to match the guass ranked predictions which are now centered around 0.
* Finally both the gauss ranked predictions and the centered target are raised to the power of 1.5 before calculating the Pearson correlation. We do this to accentuate the tails as hedge fund tends to only trade the stocks with highest or lowest predicted returns.

The key takeaway here is that your prediction's distribution does not matter. You are only evaluated on your prediction's ranks. And your score depends more on the tails than a typical rank-correlation.

## CORR on the website

You may see different variations of CORR on the website&#x20;

* `CORR20V2` - the latest CORR score against the 20 day version of main target&#x20;
* `CORRJ60` - correlation to the 60 day version of the auxiliary target named Jerome &#x20;
* `CORR20` - the legacy CORR score soon to be deprecated
