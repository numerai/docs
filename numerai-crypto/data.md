# Data

## Data Structure

The Numerai Crypto dataset is a tabular dataset that describes a token universe and their returns over time.

At a high level, each row represents a token at a specific point in time identified by its `symbol` and the `date`. The `date` represents the day that "market close" (23:59 UTC on a given day) data was used to generate the features - in the context of rounds and live data, this is the day before a round opens. The `target` is a measure of future returns (eg. after 30 days) relative to the `date`.

### Target

Numerai Crypto has one target, which is the returns of the token after 30 days. For each round, the 30 day returns for each token in the universe are ranked, gaussianized, then bucketed into five bins.

## Data API

The best way to access the Numerai Crypto dataset is via the data API:

```python
from numerapi import NumerAPI
napi = NumerAPI()

[f for f in napi.list_datasets() if f.startswith("crypto/v1.0")]

[
 'crypto/v1.0/live_universe.parquet',
 'crypto/v1.0/train_targets.parquet',
]

# Download the training data
napi.download_dataset("crypto/v1.0/train_targets.parquet")
```

- `train_targets.parquet` contains the historical symbols and targets
- `live_universe.parquet` contains the latest token universe with no targets of the current round
