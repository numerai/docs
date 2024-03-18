# Meta Model Contribution (MMC)

## What is MMC (and BMC)?

Meta Model Contribution (MMC) is the covariance of a model with the target, after its predictions have been neutralized to the Meta Model. Similarly, Benchmark Model Contribution (BMC) is the covariance of a model with the target, after its predictions have been neutralized to the stake-weighted [Benchmark Models](https://numer.ai/\~benchmark\_models).

These metrics tell us how the unique component of a model contributes to the correlation of the Meta Model (or the Benchmark Models in the case of BMC). By neutralizing the model's predictions by the Meta Model or Benchmark Models, the remaining orthogonal component's covariance with the target is that model's contribution.

## Calculation

To calculate a user's MMC for a given round we

* Normalize the predictions in their submission
* Normalize the Meta Model
* Neutralize their submission to the Meta Model
* Find the covariance of the neutral submission with the target

````python
```python
def contribution(
    predictions: pd.DataFrame,
    meta_model: pd.Series,
    live_targets: pd.Series,
) -> pd.Series:
    """Calculate the contributive correlation of the given predictions
    wrt the given meta model.

    Then calculate contributive correlation by:
    1. tie-kept ranking each prediction and the meta model
    2. gaussianizing each prediction and the meta model
    3. orthogonalizing each prediction wrt the meta model
    4. multiplying the orthogonalized predictions and the targets

    Arguments:
        predictions: pd.DataFrame - the predictions to evaluate
        meta_model: pd.Series - the meta model to evaluate against
        live_targets: pd.Series - the live targets to evaluate against

    Returns:
        pd.Series - the resulting contributive correlation
                    scores for each column in predictions
    """
    # filter and sort preds, mm, and targets wrt each other
    meta_model, predictions = filter_sort_index(meta_model, predictions)
    live_targets, predictions = filter_sort_index(live_targets, predictions)
    live_targets, meta_model = filter_sort_index(live_targets, meta_model)

    # rank and normalize meta model and predictions so mean=0 and std=1
    p = gaussian(tie_kept_rank(predictions)).values
    m = gaussian(tie_kept_rank(meta_model.to_frame()))[meta_model.name].values

    # orthogonalize predictions wrt meta model
    neutral_preds = orthogonalize(p, m)
    
    # center the target
    live_targets -= live_targets.mean()

    # multiply target and neutralized predictions
    # this is equivalent to covariance b/c mean = 0
    mmc = (live_targets @ neutral_preds) / len(live_targets)

    return pd.Series(mmc, index=predictions.columns)
```
````

## BMC in Diagnostics

In Diagnostics, BMC is calculated not against the stake-weighted Benchmark Models, but instead against a single model - the benchmark model with the highest stake (see [here](https://numer.ai/\~benchmark\_models)). There is a difference between BMC on the Leaderboard and BMC in Diagnostics because:

* The Leaderboard (LB) show **live performance** - this means the BMC calculated here is in the context of what Numerai and data scientists knew at the time so it's fair to judge models against stake-weighted benchmark models **at the time**. For example, early rounds the only benchmark model were the v2 example predictions, but recent rounds have more sophisticated models.
* Diagnostics show **validation performance** - this means you might be using better modeling techniques with better data and better targets and it would be misleading to judge you against example predictions from the v2 dataset. Instead, we should be judging you against the latest greatest model we can make.

If you still aren't sure why BMC is different between the LB and diagnostics, please take a look at our [target ensemble notebook](https://github.com/numerai/example-scripts/blob/master/target\_ensemble.ipynb) which touches on these ideas.

## Discussion

Read more about MMC & BMC [here](https://forum.numer.ai/t/mmc-staking-starts-jan-2-2024/6827).
