---
description: Everything you need to know about Numerai Crypto.
---

# Overview

## Introduction

Similar to [Numerai Signals](broken-reference), [Numerai Crypto](https://crypto.numer.ai) asks you to bring your own data - your own unique signal. A signal in the crypto market (or "CryptoSignal") is a feed of information. It is numerical data about tokens that can be used by crypto traders. These feeds of information are used to model the crypto market and construct the Numerai Crypto Meta Model, which we give back to you **free of charge.**

Examples of crypto market signals include:

* [Technical signals](https://www.investopedia.com/terms/t/technicalindicator.asp) ([MACD](https://www.investopedia.com/terms/m/macd.asp), [RSI](https://www.investopedia.com/terms/r/rsi.asp), [MFI](https://www.investopedia.com/terms/m/mfi.asp))
* [Alternative data signals](https://en.wikipedia.org/wiki/Alternative\_data\_\(finance\)) ([credit card transactions](https://secondmeasure.com/), [satellite images](https://www.theatlantic.com/magazine/archive/2019/05/stock-value-satellite-images-investing/586009/), [social media sentiment](https://www.swaggystocks.com/dashboard/wallstreetbets/realtime))
* [Blended signals](https://www.investopedia.com/terms/m/multifactor-model.asp) ([Barra risk factors](https://www.investopedia.com/terms/b/barra-risk-factor-analysis.asp), [Fama French factors](https://www.investopedia.com/terms/f/famaandfrenchthreefactormodel.asp))

If you're a data provider you can submit unique features directly as signals. If you're a data scientist, you can model unique data to submit predictions as signals. Signals are then scored against our targets and other submitted signals. Signals can be staked with the NMR cryptocurrency to earn (or burn) NMR based on performance.

## Data

You can get started with the the Numerai Data API:

```python
from numerapi import NumerAPI
import pandas as pd

napi = NumerAPI()
napi.download_dataset("crypto/v1.0/historical_targets.parquet")
training_data = pd.read_parquet("crypto/v1.0/historical_targets.parquet")
```

**You will need to acquire distinct and unique crypto market data to generate a high quality signal.** There are a number of other data providers you can also use to get started such as [Messari](https://messari.io/api) and [CoinMarketCap](https://coinmarketcap.com/api)<mark style="background-color:yellow;">.</mark>

If you don't have crypto market data, but are still interested in Numerai, try the [Numerai Tournament](https://numer.ai/) instead to predict the stock market using our data.

## Modeling

If you're not sure where to start with modeling your data, we highly recommend learning how to do [basic modeling ](../numerai-tournament/models.md)over on the Numerai Tournament. Once you're confident in your modeling skills, they should transfer to Numerai Crypto. Here is a basic example of a tree-based model:

```python
import lightgbm as lgb
import pandas as pd
import random
from numerapi import NumerAPI
from typing import List

napi = NumerAPI()


def generate_training_features(df: pd.DataFrame) -> List[str]:
    # TODO: Get your data and create features
    df['fake_feature_1'] = df.groupby(["symbol", "date"])['symbol'].transform(lambda x: random.uniform(0, 1))
    return ['fake_feature_1']


# Historical targets file contains ["symbol", "date", "target"] columns
napi.download_dataset("crypto/1.0/historical_targets.parquet")
train_df = pd.read_parquet("crypto/1.0/historical_targets.parquet")

# Add training features for each (symbol, date)
feature_cols = generate_training_features(train_df)

model = lgb.LGBMRegressor(
    n_estimators=2000,
    learning_rate=0.01,
    max_depth=5,
    num_leaves=2 ** 5,
    colsample_bytree=0.1
)

model.fit(
    train_df[feature_cols],
    train_df["target"]
)

```

## Submissions

Numerai Crypto submissions are very similar to Numerai Signals (see [here](../numerai-signals/submissions.md)), except you use token symbols instead of stock tickers. Your submission should be a list of symbols each with a numerical value predicting **returns**:

![An example crypto market signal](../.gitbook/assets/cryptosignals\_ex\_sub.png)

The list of symbols in your submission are defined by the **Numerai Crypto token universe.** And the numerical values should be between 0 and 1.

Here is an example of how you generate and upload live predictions in Python:

```python
def generate_features(df: pd.DataFrame):
    # TODO: Get your data and create features for live universe
    df['fake_feature_1'] = df['symbol'].transform(lambda x: random.uniform(0, 1))

# Use API keys to authenticate
napi = NumerAPI("[your api public id]", "[your api secret key]")

# Download latest live universe
napi.download_dataset("crypto/v1.0/live_universe.parquet")
live = pd.read_parquet("crypto/v1.0/live_universe.parquet")

# Generate features for the live universe
generate_features(live)

# Get live predictions
live["signal"] = model.predict(live[feature_cols])

# Predictions must be between 0 and 1
live["signal"] = live["signal"].rank(pct=True)

# Format and save submission
live[['symbol', 'signal']].to_parquet("submission.parquet")

# Upload submission
napi.upload_predictions("submission.parquet", tournament=12)
```

Read more about submissions [here](submissions.md).

## Scoring

Scoring is also very similar to the Numerai Tournament (see [here](../numerai-tournament/scoring/)).

Numerai Crypto is not only about predicting token returns, it is about finding original signals that other models don't already have.

See the [Scoring](scoring/) section for more details.

## Staking <a href="#staking" id="staking"></a>

Just as with the Numerai Tournament, you can optionally `stake` [NMR](https://www.coinbase.com/price/numeraire) on your model to earn or burn based on performance. For more information please read [the Staking docs](../numerai-tournament/staking.md).

{% hint style="info" %}
It is important to note that the opportunity to stake your signal is not an offer by Numerai to participate in an investment contract, a security, a swap based on the return of any financial assets, an interest in Numerai’s hedge fund, or in Numerai itself or any fees we earn. Numerai's hedge fund has no relation whatsoever to Numerai Crypto, it does not trade cryptocurrencies, and does it does not use the Numerai Crypto Meta Model. Payouts will be made at our discretion, based on a blackbox target that may not be disclosed to users. Fundamentally, Numerai Crypto is a service offered by Numerai that allows users to assess the value of their CryptoSignals, using NMR staking as a way to validate “real” signals. Users with different expectations should not stake.

**Please read our** [**Terms of Service**](https://numer.ai/terms) **for further information.**
{% endhint %}

## FAQ

**What is a token universe?**

A set of well-known cryptocurrency token symbols that can be traded. Numerai wants predictions for only these symbols. See [here](../numerai-signals/submissions.md) for details.

**What is the difference between Numerai Tournament, Numerai Signals, and Numerai Crypto?**

Numerai Tournament and Numerai Signals are tournaments for users to predict the stock market. Numerai Crypto is for predicting the cryptocurrency market. Numerai Crypto is most similar to Signals, where users must use their own features. Numerai provides a [historical targets](data.md) file to train the models and evaluate on validation data, but users must collect and process their own features to train models.

**Is my code / data protected from Numerai?**

Yes. Numerai does not view the code that builds your data or predictions. Numerai only receives the predictions themselves. Reverse-engineering your code is nearly impossible and Numerai is uninterested in doing this.

**Do I have to stake NMR in order to participate?**

No. You can submit your prediction file and receive performance without staking.

**Why shouldn't I just trade on my own?**

You can and we can't stop. However, Numerai is equipped to tell you if your signal is already known and being used by everyone else - it's not very valuable to trade a signal that everyone else is already trading. [Learn more in this Medium post](https://medium.com/numerai/building-the-last-hedge-fund-introducing-numerai-signals-12de26dfa69c).

**Do I need know coding / finance in order to participate?**

While example models and exploratory notebooks are available to get started, people new to coding and finance are encouraged to try [Numerai Tournament](../) rather than Numerai Crypto. Numerai Crypto requires a high-level of coding and market knowledge to be successful.

#### Does Numerai trade cryptocurrencies?

No. Numerai does not trade cryptocurrencies nor does Numerai's hedge fund(s).

#### Does Numerai use the Numerai Crypto Meta Model?

No. None of Numerai's other products, assets, or services consume, use, blend, or are effected by the Numerai Crypto Meta Model.

#### Are predictions or data from Numerai Crypto used in Numerai's hedge fund?

No. Numerai's hedge fund is completely divorced from Numerai Crypto and nothing from Numerai Crypto effects the hedge fund in any way.

## Support

Find us on [Discord](https://discord.gg/numerai) for questions, support, and feedback!
