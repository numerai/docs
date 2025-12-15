# Data

## Data Structure

The Numerai Crypto dataset is a tabular dataset that describes a token universe and their returns over time.

At a high level, each row represents a token at a specific point in time identified by its `symbol` and the `date`. The `date` represents the day that "market close" (23:59 UTC on a given day) data was used to generate the features - in the context of rounds and live data, this is the day before a round opens. The `target` is a measure of future returns (eg. after 30 days) relative to the `date`.

### Target

Numerai Crypto has one target, which is the returns of the token after 30 days. For each round, the 30 day returns for each token in the universe are ranked, gaussianized, then bucketed into five bins.

## Data API

The best way to access the Numerai Crypto dataset is via the data API:

```python
from numerapi import CryptoAPI
napi = CryptoAPI()

[f for f in napi.list_datasets() if f.startswith("crypto/v2.0")]

[
 'crypto/v2.0/live_universe.parquet',
 'crypto/v2.0/train_targets.parquet',
]

# Download the training data
napi.download_dataset("crypto/v2.0/train_targets.parquet")
```

* `train_targets.parquet` contains the historical symbols and targets
* `live_universe.parquet` contains the latest token universe with no targets of the current round

## Community Data

The Numerai Council of Elders partnered with [YIEDL](https://yiedl.ai/) to bring the YIEDL crypto dataset to Numerai Crypto. This comprehensive collection encompasses over ten years of cryptocurrency data, featuring components such as price volume momentum (PVM), sentiment analysis, and on-chain metrics.

* Read the [Official Announcement](https://medium.com/numerai-council-of-elders/yiedl-and-the-numerai-council-of-elders-join-forces-to-enhance-numerai-crypto-b191f9024486)
* Run the [Example Notebook](https://github.com/councilofelders/notebooks/blob/main/yiedl_crypto_data/yiedl_crypto_data_for_numerai_example.ipynb)
