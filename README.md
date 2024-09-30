---
description: Everything you need to know to get started in under 5 minutes!
---

# Overview

## Introduction

Numerai is a data science competition where you build machine learning models to predict the stock market. You are provided with free, high quality data that you can use to train models and submit predictions daily. Numerai computes the performance of these predictions over the following month and you can stake NMR on your model, to earn (or burn) based on your model's performance.

You can [sign up](https://numer.ai/signup) and visit your [home page](https://numer.ai/home) for a full suite of tutorials.

## Data

Numerai's free dataset is made of clean and regularized financial data. The dataset is _**obfuscated**_ so that it can be given out for free and modeled without any financial domain knowledge. This also means that models you build on this data cannot be used outside of the Numerai tournament.

Here is an example of the general structure of our dataset:

![Numerai's obfuscated dataset](.gitbook/assets/ex\_data.png)

Each row in the dataset corresponds to a specific stock at a specific point in time. The point in time is noted by the `era` - each represents a week. The IDs are unique in each era such that you cannot match stocks across eras - this is necessary for the obfuscation. The `features` are quantitative attributes known about the stock at the time (e.g P/E ratio, ADV, etc.). The `target` is a measure of stock market returns 20 days into the future where low means bad performance and high means good performance.

Here is an example of how to get our dataset:

```python
from numerapi import NumerAPI
import pandas as pd

napi = NumerAPI()
napi.download_dataset("v5.0/train.parquet")
training_data = pd.read_parquet("v5.0/tra.parquet")
```

See the [Data](numerai-tournament/data.md) section for more details.&#x20;

## Modeling

Your objective is to build machine learning models to predict the `target` given the `features`. You can use any language or framework that you like.

Here is an example model in Python using [LightGBM](https://lightgbm.readthedocs.io/en/latest/pythonapi/lightgbm.LGBMRegressor.html):

```python
import lightgbm as lgb

features = [f for f in training_data.columns if "feature" in f]

model = lgb.LGBMRegressor(
      n_estimators=2000,
      learning_rate=0.01,
      max_depth=5,
      num_leaves=2 ** 5,
      colsample_bytree=0.1
)
model.fit(
      training_data[features],
      training_data["target"]
)
```

See the [Models](broken-reference) section for more examples.

## Submissions

Each day (Tuesday through Saturday), new `live data` is released. This represents the current state of the stock market. You must generate `live predictions` and submit them to Numerai. You are asked to submit a prediction value for each id in the `live` data.

This is what a submission might look like:

<figure><img src=".gitbook/assets/image (89).png" alt="" width="290"><figcaption></figcaption></figure>

Here is an example of how you generate and upload live predictions in Python:

```python
# Use API keys to authenticate
napi = NumerAPI("[your api public id]", "[your api secret key]")

# Download latest live features
napi.download_dataset(f"v5.0/live.parquet")
live_data = pd.read_parquet(f"v5.0/live.parquet")
features = [f for f in live_data.columns if "feature" in f]
live_features = live_data[features]

# Generate live predictions
live_predictions = model.predict(live_features)

# Format and save submission
submission = pd.Series(
    live_predictions, index=live_features.index
).to_frame("prediction")
submission.to_csv(f"submission.csv")

# Upload submission
napi.upload_predictions(f"submission.csv")
```

Behind the scenes, Numerai combines the predictions of all models into the S_take-Weighted_ _Meta Model_, which in turn is fed into the Numerai Hedge Fund for trading.&#x20;

See the [Submissions](numerai-tournament/submissions/) section for more details and examples.

## Scoring

Submissions are scored against two main metrics:

* [Correlation](numerai-tournament/scoring/correlation-corr.md) (`CORR`): Your prediction's correlation to the target
* [Meta Model Contribution](numerai-tournament/scoring/meta-model-contribution-mmc.md) (`MMC`):  Your prediction's contribution to the Meta Model&#x20;

Since the `target` is a measure of 20 business days of stock market returns, it takes about 1 month for each submission to be fully scored.

See the [Scoring](numerai-tournament/scoring/) section for more details.

## Staking

When you are ready and confident in your model's performance, you may stake on it with [NMR](https://www.coinbase.com/price/numeraire) - Numerai's cryptocurrency. After the 20 days of scoring for each submission, models with positive scores are rewarded with more NMR, while those with negative scores have a portion of their staked NMR _burned_ (destroyed such that no one, not even Numerai, can access it).&#x20;

Staking serves two important functions:

1. "Skin in the game" allows Numerai to trust the quality of staked predictions.   &#x20;
2. Payouts and burns continuously improve the weights of the Meta Model.      &#x20;

See the [Staking](numerai-tournament/staking.md) section for more details.&#x20;

## FAQ

### Do I have to stake?

No. You can submit your prediction file and receive performance without staking.

### Why wouldn't I just trade it myself?

You can't trade the predictions for the Numerai Tournament. Since our data is obfuscated, it's impossible to use it for your own trading.

### Why not pay in USD?

USD cannot be burned. NMR was designed to be burned and thus can be sent to a null address, making it completely unusable by anyone. This is important because if NMR is burned due to bad performance, you can be sure that the NMR is disappearing, not simply being sent to another user.

## Support

Find us on [Discord](https://discord.gg/numerai) for questions, support, and feedback!
