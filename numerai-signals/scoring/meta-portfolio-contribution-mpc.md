---
description: >-
  One of the primary scores of Signals using the Stake-Weighted Portfolio and
  the 60D2L chili target.
---

# Meta Portfolio Contribution (MPC)

With the invention of [Alpha](alpha.md), Signals also needed a metric that is similar to MMC, but uses the same neutralizers matrix and sample weights vector that Alpha uses. An analog to the Meta Model could be the Stake-Weighted Portfolio (**SWP**). In this case, Meta Portfolio Contribution evaluates the extent to which a signal enhances the Alpha of the SWP.

To find an individual user’s contribution, we could then increase their stake in the SWP slightly and measure the change in Alpha of the SWP. This is basically just a gradient of SWP Alpha with respect to a users stake.

Given the following data:

* signals matrix _**S**_ (NaNs filled w/ 0.5)
* stake-weights _**p**_
* neutralization matrix _**N**_
* weight vector _**v**_

We generate neutral weights per signal:

```
s` = normalize(rank(s))^1.5
neutral_preds = s` - (N @ (N.T @ (v * s`)))
neutral_weights = neutral_preds * v
```

Next, stake-weight-average them into the **SWP** and normalize total weight:

```
SWP = (p * user_stakes).sum()
SWP = SWP - SWP.mean()
SWP = SWP / sum(abs(SWP))
```

Then, we can calculate the Alpha of the SWP:

```
SWP_Alpha = SWP * target
```

Finally, MPC is the gradient of SWP Alpha with respect to stakes:

```
MPC = gradient(SWP_Alpha, p)
```

When paid on MPC, data scientists will be incentivized to stake on signals that push the Numerai Signals tournament to be valuable to the Numerai hedge fund. [Visit the numerai-tools repository](https://github.com/numerai/numerai-tools/blob/eb4252237b92f379fcd8c4dc2e0b546fae218f10/numerai_tools/scoring.py#L577-L620) if you're interested in reading the code for MPC.
