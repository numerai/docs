# Feature Neutral Correlation

## Motivation

Feature neutral correlation \(FNC\) is the correlation of a model with the target, after its predictions have been neutralized to all of Numerai’s features.

A model that is overly reliant on a small set of features will have a low FNC, but might still have a high correlation in the short term. However, it is also more likely to burn significantly in the long term.

A model that uses a diverse set of features and is still correlated with the targets will have a high FNC, and is more likely to have consistent performance over the long term.

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

## Discussion

Read more about feature neutralization and feature exposure [here](https://forum.numer.ai/t/model-diagnostics-feature-exposure/899).

