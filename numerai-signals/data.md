# Data

## Data Structure

The Numerai Signals dataset is a tabular dataset that describes the global stock market over time.

At a high level, each row represents a stock at a specific point in time identified by its `numerai_ticker` or `composite_figi` and the `date`. The `date` represents the day that market close data was used to generate the features - in the context of rounds and live data, this is the day before a round opens. The `target` is a measure of future returns (eg. after 20 days) relative to the `date`.

### Features

The Signals dataset contains:

1. Factors, which are similar to the factors which the target is neutral to. Use these to determine if your model is sufficiently unique, use them to neutralize your predictions, or use them as additional features in your dataset.
2. Some starter features, which are relatively simple classic quant features constructed from returns series.

#### V1 Features

The features in the V1 dataset are:

```
feature_adv_20d_factor
feature_beta_factor
feature_book_to_price_factor
feature_country
feature_dividend_yield_factor
feature_earnings_yield_factor
feature_growth_factor
feature_impact_cost_factor
feature_market_cap_factor
feature_momentum_12w_factor
feature_momentum_26w_factor
feature_momentum_52w_factor
feature_momentum_52w_less_4w_factor
feature_ppo_60d_130d_country_ranknorm
feature_ppo_60d_90d_country_ranknorm
feature_price_factor
feature_rsi_130d_country_ranknorm
feature_rsi_60d_country_ranknorm
feature_rsi_90d_country_ranknorm
feature_trix_130d_country_ranknorm
feature_trix_60d_country_ranknorm
feature_value_factor
feature_volatility_factor
```

Features with `{n}(d|w)` in the name (for example, `feature_adv_20d_factor`) are time-series features that are computed over `n` days or `n` weeks.

Features with `country_ranknorm` in the name are grouped by country, then ranked, then gaussianized.

Features with `factor` in the name refer to risk factors that most of the targets are neutral to. Price factor is grouped by country, then ranked.

PPO is a percentage price oscillator that compares shorter and longer moving averages in a ratio

RSI is the relative strength index usually used as an overbought/oversold indicator

TRIX is a triple exponential moving average indicator usually used as momentum or reversal feature

momentum\_52w\_less\_4w refers to one year return of a stock excluding the last 4 weeks.

### Targets

The target of the dataset is specifically engineered to match the strategy of the hedge fund.&#x20;

Given our hedge fund is market/country/sector and factor neutral, you can basically interpret the target as stock-specific returns that are not explained by broader trends in the market/country/sector or well known factors. In simple terms: what we are after is "alpha".

#### Primary Targets

Signals has three different targets that can be used to help tune your model performance.

**target\_raw\_return**&#x20;

It can be difficult for even an experienced data scientist to build a subsequent return column correctly if they are calculating it themselves from publicly available data. This is due to complications with returns such as stock splits and dividends. This target handles all of those complications, and then bins the returns into Numerai’s standard distribution.

This target is used to score ICv2.

**target\_factor\_neutral**

This is a target which has been neutralized to a selection of standard factors: country, sector, beta, momentum, and size.

This target is used to calculate RIC and MMC. Since Numerai’s hedge funds are neutral to these factors, RIC is much closer to what Numerai actually wants from signals than IC.

**target\_factor\_feat\_neutral**

This target is neutral to a large set of factors and all of the features in the [Numerai v4 dataset](../numerai-tournament/data.md).

This is the mian `target` in the Signals dataset, and is used to score CORRv4 and FNCv4.&#x20;

#### Auxiliary Targets

Apart from the main target we provide many auxiliary targets that are different types of stock specific returns. Like the main target, these auxiliary targets are also based on stock specific returns but are different in what is residualized (eg. market/country vs sector/factor) and time horizon (eg. 20 day vs 60 days).  &#x20;

Even though our objective is to predict the main target, we have found it helpful to also model these auxiliary targets. Sometimes, a model trained on an auxiliary target can even outperform a model trained on the main target. In other scenarios, we have found that building an ensemble of models trained on different targets can also help with performance. &#x20;

Note: some auxiliary target values can be NaN but the main `target` will never be NaN. This is because some target data is just not available at that point in time, and instead of making up a fake value we are letting you choose how to deal with it yourself.

## Data API

The best way to access the Signals dataset is via the data API.

### Files

The Numerai dataset is made up of many different files.

Here is how to query the data API to see what files are available and how to download a file.

```python
from numerapi import NumerAPI
napi = NumerAPI()

DATA_VERSION = "signals/v2.0"

[f for f in napi.list_datasets() if f.startswith(DATA_VERSION)] 

[f'{DATA_VERSION}/live.parquet',
 f'{DATA_VERSION}/live_example_preds.csv',
 f'{DATA_VERSION}/live_example_preds.parquet',
 f'{DATA_VERSION}/train.parquet',
 f'{DATA_VERSION}/validation.parquet',
 f'{DATA_VERSION}/validation_example_preds.csv',
 f'{DATA_VERSION}/validation_example_preds.parquet']
 
# Download the training data 
napi.download_dataset(f'{DATA_VERSION}/train.parquet')
```

* `train.parquet` contains the historical data with tickers, features, and targets
* `validation.parquet` contains more historical data with tickers, features and targets
* `live.parquet` contains the latest ticker universe and live features with no targets of the current round
* `live_example_preds.parquet` contains the latest live predictions of the example model&#x20;
* `validation_example_preds.parquet` contains the validation predictions of the example model

