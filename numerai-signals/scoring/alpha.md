---
description: One of the primary scores of Signals using the 60D2L chili target.
---

# Alpha

CORR, FNC, and MMC are all imperfect metrics for paying Signals users. This is because users can be good at these scores, but backtest poorly. To better align the Numerai Signals tournament with the Numerai hedge fund, the performance of a submission must align with it's backtest performance.

The Numerai research team invented 2 pieces of data that provides a way to do this:

* Neutralizers Matrix: a 200-column condensed matrix used to produce a neutralize signal
* Sample Weights Vector: a weight vector used for sampling a signal to produce a set of stock weights that accounts for real-world trading constraints such as adv

Using these, we can create a set of "**neutralized weights**" from a signal as follows:

Given the following data:

* signal _**s**_ (NaNs filled w/ 0.5)
* neutralization matrix _**N**_
* weight vector _**v**_

We first create normalized signal _**s’**_:

```
s` = normalize(rank(s))^1.5
```

Then generate neutralize predictions and sample them:

```python
neutral_preds = s` - (N @ (N.T @ (v * s`)))
neutral_weights = neutral_preds * v
```

Finally, we use the 60D2L target `chili` to derive the final `alpha` value:

```python
alpha = neutral_weights @ target_chili_60
```

This value provides us some insight into how a signal might perform in a backtest and more closely aligns the Signals Tournament with the hedge fund.
