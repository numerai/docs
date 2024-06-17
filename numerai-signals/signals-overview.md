---
description: Everything you need to know about Numerai Signals.
---

# Overview

## Introduction

While the [Numerai Tournament](https://numer.ai) provides free data, [Numerai Signals](https://signals.numer.ai) asks you to bring your own data - your own unique signal. A signal in the stock market is a feed of information. It is numerical data about stocks that can be used by quantitative hedge funds like Numerai. These feeds of information are used to model the stock market and construct portfolios (collections of stock holdings).

Examples of stock market signals include:

* [Fundamental signals](https://www.investopedia.com/terms/f/fundamentalanalysis.asp) ([P/E ratio](https://www.investopedia.com/terms/p/price-earningsratio.asp), [dividend yield](https://www.investopedia.com/terms/d/dividendyield.asp), [analyst ratings](https://www.investopedia.com/terms/r/rating.asp))
* [Technical signals](https://www.investopedia.com/terms/t/technicalindicator.asp) ([MACD](https://www.investopedia.com/terms/m/macd.asp), [RSI](https://www.investopedia.com/terms/r/rsi.asp), [MFI](https://www.investopedia.com/terms/m/mfi.asp))
* [Alternative data signals](https://en.wikipedia.org/wiki/Alternative\_data\_\(finance\)) ([credit card transactions](https://secondmeasure.com/), [satellite images](https://www.theatlantic.com/magazine/archive/2019/05/stock-value-satellite-images-investing/586009/), [social media sentiment](https://www.swaggystocks.com/dashboard/wallstreetbets/realtime))
* [Blended signals](https://www.investopedia.com/terms/m/multifactor-model.asp) ([Barra risk factors](https://www.investopedia.com/terms/b/barra-risk-factor-analysis.asp), [Fama French factors](https://www.investopedia.com/terms/f/famaandfrenchthreefactormodel.asp))

If you're a data provider you can submit unique features directly as signals. If you're a data scientist, you can model unique data to submit predictions as signals. Signals are then scored against our targets and other submitted signals. Signals can be staked with the NMR cryptocurrency to earn (or burn) NMR based on performance.

Numerai Signals is one part of the Numerai master plan to build the world's last hedge fund. Read the [Medium Post](https://medium.com/numerai/building-the-last-hedge-fund-introducing-numerai-signals-12de26dfa69c) and watch [the short film](https://youtu.be/GWeC2PK4yXQ) to learn more about how it all fits together.

## Data

You can get started with the Signals V1 Data:

```python
from numerapi import NumerAPI
import pandas as pd

napi = NumerAPI()
# Use int8 to save on storage and memory
napi.download_dataset("signals/v1.0/train.parquet")
training_data = pd.read_parquet("signals/v1.0/train.parquet")
```

This data is primarily meant to be used to either add to your own data or [neutralize](signals-overview.md#neutralization) your signal, because it's data we already have and know how to use. **You will need to acquire distinct and unique stock market data to generate a high quality signal.** There are a number of other data providers you can also use to get started such as [Yahoo Finance](https://finance.yahoo.com/), [Quandl](https://www.quandl.com/) and [Koyfin](https://www.koyfin.com/). There are also platforms that make it easy to create signals such as [QuantConnect](https://www.quantconnect.com/), and [Alpaca](https://alpaca.markets/). Check out this [forum thread](https://forum.numer.ai/t/free-or-cheap-data-for-erasure-numerai-quant/350) for a list of data sources, platforms, and tools.

If you don't have stock market data, try the [Numerai Tournament](https://numer.ai/) instead.

## Modeling

If you're not sure where to start with modeling your data, there are a list of tutorial models [here](../numerai-tournament/models.md). We also highly recommend learning how to do [basic modeling ](../numerai-tournament/models.md)over on the Numerai Tournament. Once you're confident in your modeling skills, they should transfer to Signals.

Here is a an example of a Signals model:

```python
import lightgbm as lgb

features = [
      f for f in training_data.columns
      # there are two non-numerical feature cols
      if "feature" in f and f not in ("feature_country", "feature_exchange_code")
]

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

{% hint style="warning" %}
**Note:** This model is incredibly basic and will likely have no performance as it's trained against the basic data we already have.
{% endhint %}

## Submissions

Signals submissions are very similar to the Numerai Tournament (see [here](../numerai-tournament/submissions/)), except you use stock tickers instead of ids. Your signals should be a list of stock tickers each with a numerical value:

![An example stock market signal](<../.gitbook/assets/group-42-2 (1).png>)

The list of stock tickers in your submission are defined by the **Numerai Signals stock market universe.** And the numerical values should be between 0 and 1.

Here is an example of how you generate and upload live predictions in Python:

```python
# Use API keys to authenticate
sapi = SignalsAPI("[your api public id]", "[your api secret key]")

# Download latest live features
sapi.download_dataset(f"signals/v1.0/live.parquet")
live_data = pd.read_parquet(f"signals/v1.0/live.parquet")

# Generate live predictions
live_predictions = model.predict(live_data[features])

# Format and save submission
submission = pd.Series(
    live_predictions, index=live_features.index
).to_frame("prediction")
submission.to_csv(f"submission.csv")

# Upload submission
sapi.upload_predictions(f"submission.csv")
```

Read more about submissions [here](signals-overview.md#submissions).

## Scoring

Scoring signals is also very similar to the Numerai Tournament (see [here](../numerai-tournament/scoring/)).

The primary difference is that Numerai first neutralizes each signal to our own existing signals - extracting the unique component of each signal. The targets used to evaluate signals are also neutralized to these signals. This highlights the key unique aspect of Signals: Numerai Signals is not about predicting stock returns, it is about finding original signals that Numerai doesn't already have.

Furthermore, Signals Grandmasters has different tier qualifications.

See the [Scoring](scoring/) section for more details.

## Staking <a href="#staking" id="staking"></a>

Just as with the Numerai Tournament, you can optionally `stake` [NMR](https://www.coinbase.com/price/numeraire) on your model to earn or burn based on performance. For more information please read [the Staking docs](../numerai-tournament/staking.md).

{% hint style="info" %}
It is important to note that the opportunity to stake your signal is not an offer by Numerai to participate in an investment contract, a security, a swap based on the return of any financial assets, an interest in Numerai’s hedge fund, or in Numerai itself or any fees we earn. Payouts will be made at our discretion, based on a blackbox target that will not be disclosed to users. Fundamentally, Numerai Signals is a service offered by Numerai that allows users to assess the value of their signals, using NMR staking as a way to validate “real” signals. In return, Numerai uses the staked signals and related data in the Numerai hedge fund. Users with different expectations should not stake signals.

**Please read our** [**Terms of Service**](https://numer.ai/terms) **for further information.**
{% endhint %}

## FAQ

**What is a "Ticker" or "Symbol"?**

A stock ticker / symbol is an arrangement of characters—usually letters—representing publicly-traded securities on an exchange.

**What is a stock universe?**

A set of stock tickers / symbols that can be traded. Numerai wants predictions for only these symbols. See [here](submissions.md) for details.

**What is the difference between Numerai Tournament and Numerai Signals?**

Bring your own data. For Signals, users have to use their own features. Numerai provides a [historical targets](https://numerai-signals-public-data.s3-us-west-2.amazonaws.com/signals\_train\_val\_bbg.csv) file to train the models and evaluate on validation data, but signals users must collect and process their own features to train models.

**Where can I find stock price data and data in general?**

Check out [this discussion at the forum](https://forum.numer.ai/t/free-or-cheap-data-and-tools-for-numerai-signals/350/8)

**Is my code / data protected from Numerai?**

Yes. Numerai does not view the code that builds your data or predictions. Numerai only receives the predictions themselves. Reverse-engineering your code is nearly impossible and Numerai is uninterested in doing this.

**Do I have to stake NMR in order to participate?**

No. You can submit your prediction file and receive performance without staking.

**Why shouldn't I just trade on my own?**

You can and we can't stop. However, Numerai is equipped to tell you if your signal is already known and being used by everyone else - it's not very valuable to trade a signal that everyone else is already trading. [Learn more in this Medium post](https://medium.com/numerai/building-the-last-hedge-fund-introducing-numerai-signals-12de26dfa69c).

**Can you tell me if my diagnostics are good?**

No. It's trivial to overfit a signal on validation and it would be impossible to tell purely based on diagnostics. We recommend that you submit your predictions without stake and view the live out-of-sample performance over time. This is often called "paper trading" and frequent timely submissions will give you plenty of feedback beyond diagnostics.

**Do I need know coding / finance in order to participate?**

While example models and exploratory notebooks are available to get started, people new to coding and finance are encouraged to try [Numerai Tournament](../) rather than Signals. Signals requires a high-level of coding and finance knowledge to be successful.

## Support

Find us on [Discord](https://discord.gg/numerai) for questions, support, and feedback!
