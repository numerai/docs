---
description: The official rules and getting started guide to the Numerai Signals Tournament
---

# Numerai Signals Overview

[Numerai Signals](https://signals.numer.ai) lets you upload stock market signals and find out how original they are compared to all other signals on Numerai. Signals can be staked with the NMR cryptocurrency to earn rewards. The best most original signals are used in Numerai's hedge fund.

Numerai Signals is a part of the Numerai master plan to build the world's last hedge fund. Read the [Medium Post](https://medium.com/numerai/building-the-last-hedge-fund-introducing-numerai-signals-12de26dfa69c) and watch [the short film](https://youtu.be/GWeC2PK4yXQ) to learn more about how it all fits together.

## Summary

1. Sign up to [Numerai Signals](https://signals.numer.ai) or sign in with your existing Numerai tournament account.
2. Upload your signal on Numerai's stock universe to receive performance, risk, and profitability diagnostics over the historical portion of your signal.
3. Stake NMR on the live portion of your signal to earn or lose NMR based on your performance relative to Numerai's custom targets.
4. Automate the daily upload of your signal by connecting directly to our API or use [numerai-cli](https://github.com/numerai/numerai-cli)\
   &#x20;and grow the value of your stake over time.

## What are stock market signals?

Stock market signals are feeds of numerical data about stocks used by quantitative hedge funds like Numerai to construct portfolios.

![An example stock market signal](<../.gitbook/assets/group-42-2 (1).png>)

Examples of stock market signals include:

* [Fundamental signals](https://www.investopedia.com/terms/f/fundamentalanalysis.asp) ([P/E ratio](https://www.investopedia.com/terms/p/price-earningsratio.asp), [dividend yield](https://www.investopedia.com/terms/d/dividendyield.asp), [analyst ratings](https://www.investopedia.com/terms/r/rating.asp))
* [Technical signals](https://www.investopedia.com/terms/t/technicalindicator.asp) ([MACD](https://www.investopedia.com/terms/m/macd.asp), [RSI](https://www.investopedia.com/terms/r/rsi.asp), [MFI](https://www.investopedia.com/terms/m/mfi.asp))
* [Alternative data signals](https://en.wikipedia.org/wiki/Alternative\_data\_\(finance\)) ([credit card transactions](https://secondmeasure.com/), [satellite images](https://www.theatlantic.com/magazine/archive/2019/05/stock-value-satellite-images-investing/586009/), [social media sentiment](https://www.swaggystocks.com/dashboard/wallstreetbets/realtime))
* [Blended signals](https://www.investopedia.com/terms/m/multifactor-model.asp) ([Barra risk factors](https://www.investopedia.com/terms/b/barra-risk-factor-analysis.asp), [Fama French factors](https://www.investopedia.com/terms/f/famaandfrenchthreefactormodel.asp))

While the underlying data used to generate these signals can be very different (audited financials vs images of parking lots), the signals themselves all come in the same basic format - a list of stock tickers each with an associated numerical value.

## Signal Creation

### Data and Tools

To create your own signal you can start with the given features in the V1 dataset, but will need to acquire stock market data to make constructive submissions.

{% hint style="info" %}
Data scientist with no stock market data? Participate in the [Numerai Tournament](https://numer.ai/) instead.
{% endhint %}

If you do not already have access to stock market data, there are a number of free or cheap data providers on the internet such as [Yahoo Finance](https://finance.yahoo.com/), [Quandl](https://www.quandl.com/), and [Koyfin](https://www.koyfin.com/).

There are also platforms that make it easy to create signals such as [QuantConnect](https://www.quantconnect.com/), and [Alpaca](https://alpaca.markets/).

Check out this [forum thread](https://forum.numer.ai/t/free-or-cheap-data-for-erasure-numerai-quant/350) for a list of sources popular data sources, platforms, and tools used by our community.

{% hint style="success" %}
Finding unique and differentiated datasets is key to creating original signals.
{% endhint %}

### Universe

The Numerai Signals stock market universe covers roughly the top 5000 largest stocks in the world.

The universe is updated every day, but in general only a couple low volume stocks will move in or out on a given day.

You can see the latest universe by downloading the [live.parquet file](signals-data.md#files).

### Submissions

When you submit a signal to Numerai Signals, you must include at least two columns:

* A `cusip`, `sedol`, `bloomberg_ticker`, `composite_figi`, or `numerai_ticker` column - values must be valid tickers associated with the ticker type in the header.
* A `signal` column - values must be between 0 and 1 (exclusive).

Additionally, for a submission to be valid:

* There must be at least 100 rows with predictions for tickers in the Signals stock market universe for the current `live` time period.
* A ticker cannot appear in the current `live` time period more than once.

Submissions with only two columns are assumed to correspond to the current `live` time period.

Refer to the [Submissions](signals-overview.md#submissions) docs to understand how and when submission windows take place.

### Diagnostics & Validation Predictions

You may also use the diagnostics tool (click the beaker next to your model on the [scores](https://signals.numer.ai/scores) page) to upload your signal over a historical `validation` time period and receive diagnostics metrics on your performance, risk, and potential earnings. The `validation` time period spans from `20130104` to the latest `validation` date.

Uploads over the `validation` time period must include one extra column:

* A `date` column - historic data is weekly and the diagnostics tool assumes your predictions for a given week are made using market close data of the latest Friday

<figure><img src="../.gitbook/assets/signals_validation_example_preds.png" alt=""><figcaption></figcaption></figure>

Once your upload is validated, diagnostics will start running. This usually takes 5-10 minutes depending on the number of weeks and tickers that span your submission.

<figure><img src="../.gitbook/assets/Screenshot 2023-08-18 at 1.53.00 PM.png" alt=""><figcaption></figcaption></figure>

These diagnostics serve as a guide for you to estimate whether your signal is good enough to be worth staking on. It is important to note that signals with strong diagnostics over the historical `validation` period may not score well in any current or future `live` periods.

{% hint style="warning" %}
Using this historical evaluation tool repeatedly will quickly lead to overfitting. Treat diagnostics only as a final check in your signal creation process.
{% endhint %}

### API and Automation

{% hint style="info" %}
You must submit your latest signal to Numerai every day
{% endhint %}

You can automate your submission workflow by using:

* The API:
  * [Numerapi](https://github.com/uuazed/numerapi) (official Python client)
  * [RNumerai](https://github.com/OmniacsDAO/Rnumerai) (unofficial R client)
  * Raw [GraphQL API](https://api-tournament.numer.ai/) for other languages
* Our open-source cloud automation tool [Numerai Compute](https://docs.numer.ai/tournament/compute)

## Signal Evaluation

### Neutralization

Numerai has a variety of existing signals. Our existing signals include Barra factors (like size, value, momentum, etc) country and sector risk factors, and custom stock features.

{% hint style="info" %}
**Definition**: A signal or target is considered "neutralized" after Numerai transforms it to have zero correlation with any of Numerai's existing signals such as Barra factors, country, sector factors and other custom stock features.
{% endhint %}

Every signal uploaded to Numerai Signals is neutralized before being scored. The point of the neutralization is to isolate the original or orthogonal component of the signal that is not already present in known signals.

![A visualization of neutralization against a single known signal](<../.gitbook/assets/image (53) (1).png>)

{% hint style="info" %}
If you submit a simple linear combination of a few well-known signals, there will be little to no orthogonal component after neutralization.
{% endhint %}

The targets used to evaluate signals (`target_20d_factor_feat_neutral`) are also neutralized. The targets are in effect Numerai's custom "specific return" or "residual return".

The data that is used to perform neutralization is not provided, which means the process is a "blackbox". However, you can use the historical diagnostics of your signal to estimate the impact neutralization will have on your signal in the future although it’s important to note that signals with strong scores over the historical period may not score well in any current or future round.

The code that is used to implement neutralization is open source. You can learn more about the neutralization process in this example notebook:

{% embed url="https://github.com/numerai/notebooks/blob/master/signals_scoring_example.ipynb" %}

Or check out this forum post to understand broader implications of feature exposure and neutralization.

{% embed url="https://forum.numer.ai/t/model-diagnostics-feature-exposure/899" %}

Signals with very high correlation with subsequent stock returns may score very badly on Numerai Signals and signals with weak correlation with subsequent returns might score well.

In other words, “good” signals with strong predictive value when considered alone may score poorly on Numerai Signals. This highlights the key unique aspect of Signals: Numerai Signals is not about predicting stock returns, it is about finding original signals that Numerai doesn't already have.

### **20 Day Neutralized Return Targets**

Signals are evaluated against a custom blackbox target created by Numerai. This target is based on 22 day neutralized subsequent returns (ignoring the first 2 days), for a total of 20 days worth of returns.

The reason why signals are evaluated on 20 days of returns is because signals that only work on short time horizons are impossible for large hedge funds to implement. For example, even if a signal can accurately predict the 1 hour return of stocks, it is not very useful if it takes a hedge fund 24 hours to fully trade into that position. Signals that are most useful to large hedge funds have predictive power over a long time horizon which is also known as having "low alpha decay".

For more information on the exact market days that make up the 6 days of subsequent neutralized returns, see the following section on dates and deadlines.

### Scoring

Before scoring, signals are first ranked between \[0, 1] and then neutralized. Finally the score is computed by taking the [Numerai Correlation](https://docs.numer.ai/tournament/correlation-corr#calculation) between the neutralized signal and the target (`target_factor_feat_neutral_20`). This score is referred to as `FNCV4` throughout this doc and the website.

By neutralizing your signal before scoring, Numerai aligns it with the target which improves its performance against the target. Since the target is also neutralized, the neutralization step effectively optimizes your signal for best performance without Numerai having to give out the data used for neutralization.

For example, if your signal is not neutralized to country risks, Numerai Signals will neutralize your signal against country risks before scoring so you can focus on creating an original signal without having to worry about country risk neutralization.

If you only have signals on a subset of the universe (eg only signals on US stocks), you can still submit to Signals and still perform well. For each stock in the universe where you have missing signals, Numerai will automatically fill those in with the median value after the signal is ranked.

## Staking <a href="#staking" id="staking"></a>

You can optionally `stake` [NMR](https://www.coinbase.com/price/numeraire) on your model to earn or burn based on your `FNCV4` and/or `TC` scores.

Staking means locking up NMR in a [smart contract](https://github.com/numerai/tournament-contracts) on the [Ethereum](https://ethereum.org/en/whitepaper/) blockchain. For the duration of the stake, Numerai is given the permission to add payouts to or burn from the NMR locked up.

You can manage your stake on the website. When you increase your stake, NMR is transferred from your wallet to the staking contract. When you decrease your stake, NMR is transferred from the staking contract back into your wallet after a \~4 week delay. You can also change your stake type, which determines which scores (`FNCV4` and/or `TC`) you want to stake on.

![](https://gblobscdn.gitbook.com/assets%2F-LmGruQ\_-ZYj9XMQUd5x%2F-MTwWeGztnW6NaH6Sd\_A%2F-MTxK8xvV36McXIClWAt%2Fimage.png?alt=media\&token=aea91c60-7079-439b-bbd6-f64e9d8c26d7)

{% hint style="info" %}
It is important to note that the opportunity to stake your signal is not an offer by Numerai to participate in an investment contract, a security, a swap based on the return of any financial assets, an interest in Numerai’s hedge fund, or in Numerai itself or any fees we earn. Payouts will be made at our discretion, based on a blackbox target that will not be disclosed to users. Fundamentally, Numerai Signals is a service offered by Numerai that allows users to assess the value of their signals, using NMR staking as a way to validate “real” signals. In return, Numerai uses the staked signals and related data in the Numerai hedge fund. Users with different expectations should not stake signals.

**Please read our** [**Terms of Service**](https://numer.ai/terms) **for further information.**
{% endhint %}

## Payouts

### Payout function

Payouts are a function of your stake value and scores. The higher your stake value and the higher your scores, the more you will earn. If you have a negative score, then a portion of your stake will be burned. Payouts are limited to ±5% of the stake value per round.

```python
payout = stake_value * payout_factor * (fncv4 * fncv4_multiplier + tc * tc_multiplier)
```

The `stake_value` is the value of your stake as of the `close` of the round, minus and pending releases, and 0 if you have no submission.

The `stake_cap_threshold` is a number that determines when the `payout_factor` begins to decay.  At the time of this writing, the Signals `stake_cap_threshold` is 24K. The `stake_cap_threshold` can change per round at Numerai's discretion.

The `payout_factor` is a number that scales with the total NMR staked across all models in the tournament. When the total NMR staked across all models exceeds the `stake_cap_threshold`, the `payout_factor` is reduced.

<figure><img src="../.gitbook/assets/image (13).png" alt=""><figcaption></figcaption></figure>

The `fncv4_multiplier` and `tc_multiplier` are configured by you to control your exposure to each score. You are given the following multiplier options.

|                              |                              |
| ---------------------------- | ---------------------------- |
| FNCV4 **multiplier options** | TC **multiplier options**    |
| 1.0x, 1.5x, 2.0x             | 0.0x, 0.5x, 1.0x, 2.0x, 3.0x |

{% hint style="info" %}
The payout factor curve and available multiplier options may and will be updated by Numerai in the future alongside major tournament releases.
{% endhint %}

Here are some example payout calculations.&#x20;

| stake value | payout factor | FNCV4 | FNCV4 multiplier | TC    | TC multiplier | payout   |
| ----------- | ------------- | ----- | ---------------- | ----- | ------------- | -------- |
| 100 NMR     | 0.8           | 0.02  | 2.0x             | 0.002 | 2.0x          | 3.52 NMR |
| 100 NMR     | 0.8           | 0.02  | 2.0x             | 0.002 | 0.0x          | 3.2 NMR  |

## Grandmasters Rankings and Tiers

Signals Grandmasters is identical to Numerai, but has slightly different tier qualifications:

**Grandmasters** place first

**Masters** place in the top 10

**Experts** place in the top 25%

**Researchers** place in the top 50%

**Contributors** place in the top 75%

**Apprentices** place in the bottom 25%

**Novices** have not yet made 20 qualified submissions



## Grandmasters Canon Scores

In the context of the Signals tournament, Canonical Scores (or “Canon Scores”) are particularly relevant. For example, the FNC score, which is a payout metric, has undergone updates. Initially, the payout score was 'CORR20' until round 498. It evolved into 'FNCv4' starting from round 499. The 'Canon FNC' score accounts for these changes by combining them into a unified score — it is 'CORR20' for rounds up to and including 498 and 'FNCv4' for rounds thereafter.

The 'TC' score has remained consistent throughout the tournament's history, meaning 'Canon TC' and 'TC' are equivalent.

\


## Support

We are here to help.

Find us on [Discord](https://discord.gg/numerai) for questions, support, and feedback!
