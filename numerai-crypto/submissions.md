# Submissions

While the underlying data used to create CryptoSignals can be very different (audited financials vs news articles vs images of parking lots), the CryptoSignals themselves all come in the same basic format - a list of token symbols each with an associated numerical value:

<figure><img src="../.gitbook/assets/example-prediction (1).png" alt="" width="375"><figcaption></figcaption></figure>

The list of token symbols in your submission are defined by the **Numerai Crypto token universe.** It covers roughly the top 300 largest tokens in the world and it is updated every day. In general, only a handful of low volume tokens will move in or out on a given day, but this is dependant on market volatility and (as we all know) crypto can be very volatile.

You can see the latest universe by downloading the live.parquet file.

The token universe is defined by reviewing all tokens then we:

1. always keep BTC, ETH, and NMR in the universe
2. remove symbols tagged as stablecoin, wrapped, or liquid staking (e.g. stETH, rpETH)
3. remove symbols with less than 30 data points and < 2 years old
4. remove symbols with 0 latest market cap
5. remove symbols with < $500,000 in 24h trading volume
6. remove symbol duplicates with lower latest market cap
7. remove symbols with volume below min\_latest\_volume
8. remove symbols with low (less than 0.00001) absolute mean return
9. remove symbols highly correlated (>= 0.95) with higher market cap tokens
10. return the top 500 tokens by market cap

When you submit a signal, you must include at least two columns:

* A `symbol`column - values must be valid symbols in the live universe.
* A `signal` column - values must be between 0 and 1 (exclusive).

Additionally, for a `live` submission to be valid:

* There must be at least 100 symbols from our universe with valid values (0 to 1).
* A symbol cannot appear more than once.

Please refer to the [Numerai Tournament Submissions docs](../numerai-tournament/submissions/) to understand the basics of how and when submission windows take place.

You can automate your submission workflow by using the API. The submissions API supports both Parquet and CSV file formats. Here is some example of how to upload a submission via NumerAPI:

```python
from numerapi import CryptoAPI
napi = CryptoAPI("[your api public id]", "[your api secret key]")
napi.upload_predictions("[path to your submission]", model_id="your-model-id")
```

* You can use any of following
  * [Numerapi](https://github.com/uuazed/numerapi) (official Python client)
  * Raw [GraphQL API](https://api-tournament.numer.ai/) for other languages
* Our open-source cloud automation tool [Numerai Compute](https://docs.numer.ai/tournament/compute)
