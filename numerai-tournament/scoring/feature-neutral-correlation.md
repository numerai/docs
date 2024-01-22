# Feature Neutral Correlation (FNC)

## What is FNC?

Feature neutral correlation (FNC) is the correlation of a model with the target, after its predictions have been neutralized to Numerai's features.

Since features are known to be inconsistent on their own, models with too much linear exposure to features are expected to perform poorly. By neutralizing this linear exposure to features, FNC isolates the predictive performance of the model that isn't just from the feature exposure.

## Calculation

To calculate a user's FNC for a given round we

* Normalize the predictions in their submission
* Neutralize their submission to Numerai's features for that round
* Calculate the Spearman rank-order correlation of their neutralized submission to the target

```python
def calculate_fnc(sub, targets, features):
    """    
    Args:
        sub (pd.Series)
        targets (pd.Series)
        features (pd.DataFrame)
    """
    
    # Normalize submission
    sub = (sub.rank(method="first").values - 0.5) / len(sub)

    # Neutralize submission to features
    f = features.values
    sub -= f.dot(np.linalg.pinv(f).dot(sub))
    sub /= sub.std()
    
    sub = pd.Series(np.squeeze(sub)) # Convert np.ndarray to pd.Series

    # FNC: Spearman rank-order correlation of neutralized submission to target
    fnc = np.corrcoef(sub.rank(pct=True, method="first"), targets)[0, 1]

    return fnc
```

## FNC on the website

The current version of FNC shown on the website is called `FNCv3` which is neutral to the "medium" subset of features in the V3 data.

## Discussion

Read more about feature neutralization and feature exposure [here](https://forum.numer.ai/t/model-diagnostics-feature-exposure/899).
