---
description: Everything you need to know to get started in under 5 minutes
---

# Overview

## Introduction

The Numerai Data Science tournament is where data scientists from around the world build machine learning models on Numerai's obfuscated financial dataset to predict the stock market.&#x20;

If you are just getting started, this is the overview for you!

## Data

The Numerai dataset is a tabular dataset that describes the global stock market over time.

![Numerai's obfuscated dataset](.gitbook/assets/ex\_data.png)

Each row represents a stock at a specific point in time, where `id` is the stock id and the `era` is the date. The  `features` describe the known attributes of the stock at the time (eg. P/E ratio) and the `target` represents a measure of future returns (eg. after 20 days).

Here is how to download the data in Python using [NumerAPI](https://github.com/uuazed/numerapi):

{% code lineNumbers="true" %}
```python
# NumerAPI is the official Python client
from numerapi import NumerAPI
napi = NumerAPI()

# Download training data
napi.download_dataset("v4.1/train.parquet")
training_data = pd.read_parquet("v4.1/train.parquet")
```
{% endcode %}

See the [Data](numerai-tournament/data/) section for more details and examples.&#x20;

## Modeling

Your objective is to build machine learnings models to predict the target.

Here is an example model in Python using [LightGBM](https://lightgbm.readthedocs.io/en/latest/pythonapi/lightgbm.LGBMRegressor.html):

```python
import lightgbm as lgb

model = lgb.LGBMRegressor(
      n_estimators=2000,
      learning_rate=0.01,
      max_depth=5,
      num_leaves=2 ** 5,
      colsample_bytree=0.1
)
model.fit(
      training_data[f for f in training_data.columns if "feature" in f],
      training_data["target"]
)
```

See the [Models](numerai-tournament/models/) section for more advanced example models.

## Submissions

The tournament is organized into rounds starting Saturday, Tuesday, Wednesday, Thursday and Friday every week.&#x20;

Each round goes through 4 stages over the span of a month:

* Open: live features released and submission window open
* Closed: submission window closed
* Scoring: submissions begin scoring
* Resolved: scoring complete and payouts resolved

To compete in the tournament you must submit live predictions in every round.

Here is an example of how to make a submission in Python using [NumerAPI](https://github.com/uuazed/numerapi):

```python
# Authenticate
napi = numerapi.NumerAPI("api-public-id", "api-secret-key")

# Get current round
current_round = napi.get_current_round()

# Download latest live features
napi.download_dataset(f"v4.1/live_{current_round}.parquet")
live_data = pd.read_parquet(f"v4.1/live_{current_round}.parquet")
live_features = live_data[f for f in live_data.columns if "feature" in f]

# Generate live predictions
live_predictions = model.predict(live_features)
live_predictions.to_csv(f"prediction_{current_round}.csv")

# Submit predictions 
napi.upload_predictions(f"prediction_{current_round}.csv", model_id="your-model-id")
```

See the [Submissions](numerai-tournament/submissions/) section for more details and examples.

## Scoring

There are two main scores:

* [Correlation](https://docs.numer.ai/tournament/correlation-corr) (`CORR`): Your prediction's correlation to the target
* [True contribution](https://docs.numer.ai/tournament/true-contribution-tc) (`TC`):  Your prediction's contribution to the hedge fund's returns&#x20;

Here are the `CORR` and `TC` scores of our example model over the past 1 year of submissions.

<figure><img src=".gitbook/assets/image (98).png" alt=""><figcaption><p><a href="https://numer.ai/integration_test/">https://numer.ai/integration_test</a></p></figcaption></figure>

See the [Scoring](./#scoring) section for more details.

## Staking

You can stake [NMR](https://www.coinbase.com/price/numeraire) on your model to earn payouts based on performance.&#x20;

Your payout is a primarily a function of your scores. If you have a positive score you will get a payout. If you have a negative score a portion of your stake will burn.

The maximum payout or burn per round is capped at ±5%

```python
payout = stake * clip(payout_factor * (corr * corr_mult + tc * tc_mult), -0.05, 0.05) 
```

* `stake` is the your model's stake value at the `close` of the round
* `payout_factor` is a dynamic value that scales inversely with total NMR staked
* `corr_mult` and `tc_mult` are configured by you to control your exposure to each score

See the [Staking](numerai-tournament/staking.md) section for more details.&#x20;

## Leaderboard

The 1 year average score is also called `reputation` and your rank on the leaderboard is based on your model's 1 year average `TC` score.&#x20;

<figure><img src=".gitbook/assets/image (97) (1).png" alt=""><figcaption><p>numer.ai/leaderboard</p></figcaption></figure>

## Support

We are here to help.

Find us on [Discord](https://discord.gg/numerai) for questions, support, and feedback!
