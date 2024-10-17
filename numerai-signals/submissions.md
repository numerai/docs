---
description: Everything you need to know to make your first Signals submission.
---

# Submissions

## What is a Signal submission?

Underlying data used to create signals can be very different (audited financials vs news articles vs images of parking lots), but all Signals submissions must use the same basic format - a list of stock tickers each with an associated numerical value between 0 and 1:

![An example stock market signal](<../.gitbook/assets/group-42-2 (1).png>)

The list of stock tickers in your submission are defined by the **Numerai Signals stock market universe.** It covers roughly the top 5000 largest stocks in the world and it is updated every day. In general, only a couple low volume stocks will move in or out on a given day.

You can see the latest universe by downloading the [live.parquet file](data.md#files).

When you submit a signal, you must include at least two columns:

* A `cusip`, `sedol`, `bloomberg_ticker`, `composite_figi`, or `numerai_ticker` column - values must be valid tickers associated with the ticker type in the header.
* A `signal` column - values must be between 0 and 1 (exclusive).

Additionally, for a `live` submission to be valid:

* There must be at least 100 tickers from our universe with valid values (0 to 1).
* A ticker cannot appear in the current `live` time period more than once.

## When to submit

Please refer to the [Numerai Tournament Submissions docs](../numerai-tournament/submissions/) to understand the basics of how and when submission windows take place.

## How to automate

You can automate your submission workflow by using the API. Here is an example of how to make a submission once you've generated a CSV with your predictions:

```
from numerapi import SignalsAPI

# Authenticate
sapi = SignalsAPI("[your api public id]", "[your api secret key]")
sapi.upload_predictions("[path to your submission].csv")
```

* You can use any of following&#x20;
  * [Numerapi](https://github.com/uuazed/numerapi) (official Python client)
  * [RNumerai](https://github.com/OmniacsDAO/Rnumerai) (unofficial R client)
  * Raw [GraphQL API](https://api-tournament.numer.ai/) for other languages
* Our open-source cloud automation tool [Numerai Compute](https://docs.numer.ai/tournament/compute)
