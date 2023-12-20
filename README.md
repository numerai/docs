---
description: Everything you need to know to get started in under 5 minutes!
---

# Overview

## Introduction

Numerai is a data science competition where you build machine learning models to predict the stock market.

## Data

Start with Numerai's free dataset made of clean and regularized financial data.&#x20;

The dataset is _obfuscated_ so that it can be given out for free and modeled without any financial domain knowledge.

![Numerai's obfuscated dataset](.gitbook/assets/ex\_data.png)

Each row in the dataset corresponds to a stock at a specific point in time, represented by the `era`. The `features` are quantitative attributes (e.g P/E ratio) known about the stock at the time, and the `target` is a measure of stock market returns 20 days into the future. &#x20;

See the [Data](numerai-tournament/data/) section for more details.&#x20;

## Modeling

Your objective is to build machine learning models to predict the `target`.

Here is an example model in Python using [LightGBM](https://lightgbm.readthedocs.io/en/latest/pythonapi/lightgbm.LGBMRegressor.html), but you can use any language or framework that you like.

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
      training_data[[f for f in training_data.columns if "feature" in f]],
      training_data["target"]
)
```

See the [Models](numerai-tournament/benchmark\_models.md) section for more examples.

## Submissions

Every business day, new `live features` are released which represent the current state of the stock market. Your job is to generate `live predictions` and submit them to Numerai.

Here is an example of how you generate and upload live predictions in Python:

```python
# Authenticate
napi = numerapi.NumerAPI("api-public-id", "api-secret-key")

# Get current round
current_round = napi.get_current_round()

# Download latest live features
napi.download_dataset(f"v4.2/live_int8_{current_round}.parquet")
live_data = pd.read_parquet(f"v4.2/live_int8_{current_round}.parquet")
live_features = live_data[[f for f in live_data.columns if "feature" in f]]

# Generate live predictions
live_predictions = model.predict(live_features)

# Format submission
submission = pd.Series(live_predictions, index=live_features.index).to_frame("prediction")
submission.to_csv(f"prediction_{current_round}.csv")

# Upload submission 
napi.upload_predictions(f"prediction_{current_round}.csv", model_id="your-model-id")
```

This is what a submission looks like:

![](<.gitbook/assets/image (89).png>)

See the [Submissions](numerai-tournament/submissions/) section for more details and examples.

## Scoring

Submissions are scored against two main metrics:

* [Correlation](https://docs.numer.ai/tournament/correlation-corr) (`CORR`): Your prediction's correlation to the target
* [True contribution](https://docs.numer.ai/tournament/true-contribution-tc) (`TC`):  Your prediction's contribution to the hedge fund's returns&#x20;

Since the `target` is a measure of 20 day stock market returns, it takes 20 days for each submission to be scored.

See the [Scoring](./#scoring) section for more details.

## Staking

When you are ready and confident in your model's performance, you may stake it with [NMR](https://www.coinbase.com/price/numeraire) - Numerai's cryptocurrency.&#x20;

After the 20 days of scoring for each submission, models with positive scores are rewarded with more NMR, while those with negative scores have a portion of their staked NMR _burned_.&#x20;

Behind the scenes, Numerai combines the predictions of all staked models into the _stake-weighted_ _Meta Model_, which in turn is fed into the Numerai Hedge Fund for trading.&#x20;

Staking serves two important functions:

1. "Skin in the game" allows Numerai to trust the quality of staked predictions.   &#x20;
2. Payouts and burns continuously improve the weights of the Meta Model.      &#x20;

See the [Staking](numerai-tournament/staking.md) section for more details.&#x20;

## Support

Find us on [Discord](https://discord.gg/numerai) for questions, support, and feedback!
