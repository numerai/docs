# Data

## Data Structure

The Numerai dataset is a tabular dataset that describes the global stock market over time.

<figure><img src="../../.gitbook/assets/Ex_data.png" alt=""><figcaption></figcaption></figure>

At a high level, each row represents a stock at a specific point in time, where `id` is the stock id and the `era` is the date. The  `features` describe the attributes of the stock (eg. P/E ratio) known on the date and the `target` is a measure of future returns (eg. after 20 days) relative to the date.

### Features

There are many features in the dataset, ranging from fundamentals like P/E ratio, to technical signals like RSI, to market data like short interest, to secondary data like analyst ratings, and much more.

Each feature has been meticulously designed and engineered by Numerai to be predictive of the target or additive to other features that are. We have taken special care to clean and prepare the data       &#x20;

### Targets&#x20;

The target of the dataset is specifically engineered to match the strategy of the hedge fund.&#x20;

Given our hedge fund is market/country/sector and factor neutral, you can basically interpret the target as stock-specific returns that are not explained by broader trends in the market/country/sector or well known factors. In simple terms: what we are after is "alpha".

Apart from the main target we provide many auxiliary targets that are different types of stock specific returns. Like the main target, these auxiliary targets are also based on stock specific returns but are different in what is residualized (eg. market/country vs sector/factor) and time horizon (eg. 20 day vs 60 days).  &#x20;

Even though our objective is to predict the main target, we have found it helpful to also model these auxiliary targets. Sometimes, a model trained on an auxiliary target can even outperform a model trained on the main target. In other scenarios, we have found that building an ensemble of models trained on different targets can also help with performance. &#x20;

### Eras

Eras represents different points in time, where feature values are as-of that point in time, and target values as forward looking relative to the point in time.

In historical data (train, validation), eras are 1 week apart but the target values can be forward looking by 20 days or 60 days. This means that the target values are "overlapping" so special care must be taken when applying cross validation. See this [forum post](https://forum.numer.ai/t/era-wise-time-series-cross-validation/791) for more information. &#x20;

## Data API

The best way to access the Numerai dataset is via the data API.&#x20;

### Files

The Numerai dataset is made up of many different files.

Here is how to query the data API to see what files are available and how to download a file.

```python
from numerapi import NumerAPI
napi = NumerAPI()

# Let's see what files are available for download in the latest v4.1 dataset
[f for f in napi.list_datasets() if f.startswith("v4.1")] 

['v4.1/features.json',
 'v4.1/live.parquet',
 'v4.1/live_example_preds.csv',
 'v4.1/live_example_preds.parquet',
 'v4.1/live_int8.parquet',
 'v4.1/meta_model.parquet',
 'v4.1/train.parquet',
 'v4.1/train_int8.parquet',
 'v4.1/validation.parquet',
 'v4.1/validation_example_preds.csv',
 'v4.1/validation_example_preds.parquet',
 'v4.1/validation_int8.parquet']
 
# Download the training data 
napi.download_dataset("v4.1/train.parquet")
```

* `train.parquet` contains the historical data with features and targets
* `validation.parquet` contains more historical data with features and targets
* `live.parquet` contains the latest live features with no targets of the current round
* `features.json` contains metadata about the features and feature sets
* `meta_model.parquet` contains the meta model predictions of past rounds
* `live_example_preds.parquet` contains the latest live predictions of the example model&#x20;
* `validation_example_preds.parquet` contains the validation predictions of the example model

### File formats

The main file format of our data API is [Parquet](https://parquet.apache.org/), which works great for large columnar data. But you can also find CSV versions of all files if you prefer.

By default, features and targets in all files are stored as floats ranging from 0 to 1, but you can also find versions of the files that store them as integers which are useful for lowering memory usage.

## Data Releases

The Numerai dataset is a living and breathing dataset that is constantly improving. In general, if you are building a new model you are encouraged to use the latest version.&#x20;

Improvements to the dataset are released as new versions of the dataset to preserve backwards compatibility of models trained on older versions.

* [V4.1 (Sunshine)](https://forum.numer.ai/t/super-massive-data-sunshine/5977)
* [V4 (Titan)](https://forum.numer.ai/t/v4-tournament-data-announcement/5163)
* [V3 (Supermassive)](https://forum.numer.ai/t/super-massive-data-release-deep-dive/4053)
* V2 (Legacy)
