# Submissions

While the underlying data used to create CryptoSignals can be very different (audited financials vs news articles vs images of parking lots), the CryptoSignals themselves all come in the same basic format - a list of token symbols each with an associated numerical value:

![An example crypto market signal](../.gitbook/assets/cryptosignals\_ex\_sub.png)

The list of token symbols in your submission are defined by the **Numerai Crypto token universe.** It covers roughly the top 300 largest tokens in the world and it is updated every day. In general, only a handful of low volume tokens will move in or out on a given day, but this is dependant on market volatility and (as we all know) crypto can be very volatile.

You can see the latest universe by downloading the live.parquet file.

The token universe is defined by the top 300 tokens by market cap, excluding:

* Stablecoins, wrapped tokens, liquid staking tokens (e.g. stETH, rpETH)
* Tokens less than two years old
* Tokens with less than $1,000,000 trading volume in the last 24 hours
* Lower market cap tokens for duplicate symbols
* After the above are removed, tokens that are either too stable or highly correlated:
  * Stable: Average 6 month daily returns less than 0.00001
  * Correlated: Removal of tokens with a correlation in daily returns >= 0.95 over the past 6 months, keeping the one with the highest market cap

When you submit a signal, you must include at least two columns:

* A `symbol`column - values must be valid symbols in the live universe.
* A `signal` column - values must be between 0 and 1 (exclusive).

Additionally, for a `live` submission to be valid:

* There must be at least 100 symbols from our universe with valid values (0 to 1).
* A symbol cannot appear more than once.

Please refer to the [Numerai Tournament Submissions docs](../numerai-tournament/submissions/) to understand the basics of how and when submission windows take place.

You can automate your submission workflow by using the API. The submissions API supports both Parquet and CSV file formats. Here is some example of how to upload a submission via NumerAPI:

```python
from numerapi import NumerAPI

# Authenticate
napi = NumerAPI("[your api public id]", "[your api secret key]")
napi.upload_predictions("[path to your submission]", tournament=12)
```

* You can use any of following
  * [Numerapi](https://github.com/uuazed/numerapi) (official Python client)
  * Raw [GraphQL API](https://api-tournament.numer.ai/) for other languages
* Our open-source cloud automation tool [Numerai Compute](https://docs.numer.ai/tournament/compute)
