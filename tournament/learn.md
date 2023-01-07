---
description: The official rules and getting started guide to the Numerai Tournament
---

# Numerai Tournament Overview

## Introduction

The Numerai Tournament is where you build machine learning models on abstract financial data to predict the stock market. Your models can be staked with the NMR cryptocurrency to earn rewards based on performance.

The staked models of Numerai are combined to form the Meta Model which controls the capital of the [Numerai hedge fund](https://numerai.fund/) across the global stock market.

Watch this short film to learn how it all fits together:

{% embed url="https://www.youtube.com/watch?v=dhJnt0N497c" %}

## Summary

1. Sign up at [https://numer.ai/](https://numer.ai/)
2. Download the dataset with training data and example scripts
3. Build your model and submit your predictions back to Numerai
4. Stake NMR on your models to earn/burn based on performance
5. Automate your weekly submissions and grow your stake over time

## Data

At the core of the Numerai Tournament is the free dataset. It is made of high quality financial data that has been cleaned and regularized and obfuscated.

![](../.gitbook/assets/ex\_data.png)

Each `id` corresponds to a stock at a specific time `era`. The `features` describe the various quantitative attributes of the stock at the time. The `target` represents an abstract measure of performance \~4 weeks into the future.\
\
Visit [numer.ai/data](https://numer.ai/data) for details about the newest available dataset and how to download them.&#x20;

## Modeling

Your objective is to build a model to predict the future target using live features that correspond to the current stock market.

Here is a basic example using XGBoost in Python. We train the model using the historical training data, and make predictions on the live tournament data.

```python
import pandas as pd
from xgboost import XGBRegressor

# training data contains features and targets
training_data = pd.read_csv("numerai_training_data.csv").set_index("id")

# tournament data contains features only
tournament_data = pd.read_csv("numerai_tournament_data.csv").set_index("id")
feature_names = [f for f in training_data.columns if "feature" in f]

# train a model to make predictions on tournament data
model = XGBRegressor(max_depth=5, learning_rate=0.01, \
                     n_estimators=2000, colsample_bytree=0.1)
model.fit(training_data[feature_names], training_data["target"])

# submit predictions to numer.ai
predictions = model.predict(tournament_data[feature_names])
predictions.to_csv("predictions.csv")
```

You can use any language or framework to build your model.&#x20;

Our [example-scripts](https://github.com/numerai/example-scripts) have more advanced modeling ideas using the latest data available. Also check out the [forum](https://forum.numer.ai) for the latest research topics from the team and community.

## Diagnostics

You can use the diagnostics tool to understand the performance and risk characteristics of your model over the historical validation eras in the dataset.

{% hint style="warning" %}
Using this historical evaluation tool repeatedly can quickly lead to overfitting. Treat diagnostics only as a final check in your model research process.
{% endhint %}

![](<../.gitbook/assets/dignostics (1).gif>)

Read more about model diagnostic in this [forum post](https://forum.numer.ai/t/model-diagnostics-update/902).

## Submissions

On every Tuesday, Wednesday, Thursday, Friday, and Saturday of the week, a new `round` is open and new tournament data is released. To participate in the round you need to download the latest tournament data, generate new predictions, and upload those predictions back to Numerai.

{% hint style="info" %}
Rounds open no earlier than 13:00 UTC. Weekday submission windows are open for 1 hour. Weekend windows open Saturday and close on Monday at 14:00 UTC.
{% endhint %}

You can use our [GraphQL API](https://api-tournament.numer.ai/) or our [Python](https://github.com/uuazed/numerapi) and [R](https://github.com/Omni-Analytics-Group/Rnumerai) api clients to download the dataset and upload your predictions. Here is a basic example in Python.

```python
from numerapi import NumerAPI
napi = NumerAPI("public_id", "secret_key")

# download data
napi = NumerAPI()
napi.download_dataset("v4.1/train.parquet", "train.parquet")
napi.download_dataset("v4.1/live.parquet", "live.parquet")
napi.download_dataset("v4.1/live_example_preds.parquet", "live_example_preds.parquet")

# upload predictions (for example, the live_example_preds, but formatted as a csv) 
napi.upload_predictions("predictions.csv", model_id="model_id")
```

Once you have your model pipeline working, you can deploy it to AWS using the [Numerai Compute](https://github.com/numerai/numerai-cli) framework to automatically participate in every round. &#x20;

## Scoring

Submissions are scored against the live target in a number of ways

* Correlation (`CORR`)
* [True contribution](https://docs.numer.ai/tournament/true-contribution-tc) (`TC`)&#x20;
* [Feature neutral correlation](https://docs.numer.ai/tournament/feature-neutral-correlation) (FNC)
* ... and more!

Your model's live scores can be viewed publicly on its model profile page. Here is an example of a model's final scores over the past 20 rounds.

![](<../.gitbook/assets/image (82) (1).png>)

The live target of the round is constructed using 20 days of returns skipping the first two days of returns, also known as `20D2L`. On each of those 20 days, Numerai will compute a daily update of your submissions score. Here is an example of a submission's 20 score updates within a single round.&#x20;

![](<../.gitbook/assets/image (84) (1).png>)

## Staking

You can optionally stake [NMR](https://www.coinbase.com/price/numeraire) cryptocurrency on your model to earn payouts based on your `CORR` and/or `TC` scores.&#x20;

In order to qualify for payouts in a round, you must be staked at the submission deadline of that round.

<img src="../.gitbook/assets/image (37).png" alt="" data-size="original">

Once NMR is staked, it will remain locked until you release it. Staked NMR can only be released after the resolution of any ongoing rounds. While pending release, NMR will not count towards upcoming rounds.

![](<../.gitbook/assets/image (27).png>)

There are a few advanced options that you can also configure on your stake like your `payout mode` which determines where your payout goes and your `score multipliers` which determine how much each score impacts your payouts.&#x20;

![](<../.gitbook/assets/image (8).png>)

## Payouts

Payouts are a function of your stake value and scores. The higher your stake value and the higher your scores, the more you will earn. If you have a negative score, then a portion of your stake will be burned. &#x20;

```python
payout = at_risk_stake * MAX(-0.25, MIN(0.25, payout_factor * (corr * corr_multiplier + tc * tc_multiplier)))
```

The `at_risk_stake` is the value of your stake at the round's submission deadline.

The maximum combined score per round is clamped at ±0.25

The `payout_factor` is number that scales with the total NMR staked across all models in the tournament. The higher the total NMR staked above the 300K threshold the lower the payout factor.

![](<../.gitbook/assets/image (89) (1).png>)

The `corr_multiplier` and `tc_multiplier` are configured by you to control your exposure to each score. You are given the following multiplier options.

|                             |                           |
| --------------------------- | ------------------------- |
| **corr multiplier options** | **tc multiplier options** |
| 1.0x                        | 0.0x, 0.5x, 1.0x, 2.0x    |

{% hint style="info" %}
The payout factor curve and available multiplier options may and will be updated by Numerai in the future alongside major tournament releases.
{% endhint %}

Here are some example payout calculations. The first 2 examples show the impact of adjusting score multipliers. The 3rd example shows how a negative score can cause a burn. The 4th example shows how the stake is capped at ±25% of the stake value and payout factor applied.

| stake value | payout factor | corr  | corr multiplier | tc    | tc multiplier | payout    |
| ----------- | ------------- | ----- | --------------- | ----- | ------------- | --------- |
| 100 NMR     | 0.8           | 0.02  | 1.0x            | 0.002 | 2.0x          | 1.92 NMR  |
| 100 NMR     | 0.8           | 0.02  | 1.0x            | 0.002 | 0.0x          | 1.6 NMR   |
| 100 NMR     | 0.8           | -0.03 | 1.0x            | 0.002 | 0.5x          | -2.32 NMR |
| 100 NMR     | 0.8           | 0.15  | 1.0x            | 0.1   | 2.0           | 20 NMR    |

With every daily score update, a new daily update on your payout is also computed. These daily payouts are also just updates and only the final payout of a round counts.&#x20;

Your stake value will grow as long as you continue to have positive scores. Here are some example payout projections assuming that the model gets the same positive scores every round for 52 rounds.

![](<../.gitbook/assets/image (74) (1).png>)

## Leaderboard

The leaderboard can be sorted by the reputation of model's `CORR`, `FNC`, `FNCv3`, and `TC`. [Reputation](https://docs.numer.ai/tournament/reputation) is the weighted average of a given metric over the past 20 rounds.![](<../.gitbook/assets/Screen Shot 2022-04-19 at 2.57.29 PM.png>)

Keep an eye on the leaderboard to see how your models compare to all other models in terms of performance and returns from staking.

![](<../.gitbook/assets/Screen Shot 2022-04-19 at 2.57.29 PM.png>)

## Support

We are here to help.

Find us on [RocketChat](https://community.numer.ai) for questions, support, and feedback!
