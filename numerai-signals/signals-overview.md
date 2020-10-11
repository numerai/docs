# Numerai Signals Overview

[Numerai Signals](https://signals.numer.ai) lets you upload stock market signals and find out how original they are compared to all other signals on Numerai. Signals can be staked with the NMR cryptocurrency to earn rewards. The best most orignal signals are used in Numerai's hedge fund.

Numerai Signals is a part of the Numerai master plan to build the world's last hedge fund. Read the &lt;medium post&gt; to learn more about how it all fits together.

## Summary

1. Sign up to [Numerai Signals](https://signals.numer.ai) or sign in with your existing Numerai tournament account.
2. Upload your signal on Numerai's stock universe to receive performance, risk, and profitability diagnostics over the historical portion of your signal.
3. Stake NMR on the live portion of your signal to earn or lose NMR based on your performance relative to Numerai's custom targets.
4. Automate the weekly upload of your signal by connecting directly to our API and grow the value of your stake over time.

## What are stock market signals?

Stock market signals are feeds of numerical data about stocks used by quantitative hedge funds like Numerai to construct portfolios. 

![An example stock market signal](../.gitbook/assets/group-42-2.png)

Examples of stock market signals include:

* [Fundamental signals](https://www.investopedia.com/terms/f/fundamentalanalysis.asp)  \([P/E ratio](https://www.investopedia.com/terms/p/price-earningsratio.asp), [dividend yield](https://www.investopedia.com/terms/d/dividendyield.asp), [analyst ratings](https://www.investopedia.com/terms/r/rating.asp#:~:text=A%20rating%20is%20conducted%20by,this%20action%20for%20the%20stock.)\)
* [Technical signals](https://www.investopedia.com/terms/t/technicalindicator.asp) \([MACD](https://www.investopedia.com/terms/m/macd.asp), [RSI](https://www.investopedia.com/terms/r/rsi.asp), [MFI](https://www.investopedia.com/terms/m/mfi.asp)\)
* [Alternative data signals](https://en.wikipedia.org/wiki/Alternative_data_%28finance%29) \([credit card transactions](https://secondmeasure.com/), [satellite images](https://www.theatlantic.com/magazine/archive/2019/05/stock-value-satellite-images-investing/586009/), [social media sentiment](https://www.swaggystocks.com/dashboard/wallstreetbets/realtime)\)
* [Blended signals](https://www.investopedia.com/terms/m/multifactor-model.asp) \([Barra risk factors](https://www.investopedia.com/terms/b/barra-risk-factor-analysis.asp#:~:text=The%20Barra%20Risk%20Factor%20Analysis%20is%20a%20multi%2Dfactor%20model,turnover%20and%20senior%20debt%20rating.), [Fama French factors](https://www.investopedia.com/terms/f/famaandfrenchthreefactormodel.asp)\)

While the underlying data used to generate these signals can be very different \(audited financials vs images of parking lots\), the signals themselves all come in the same basic format - a list of stock tickers each with an associated numerical value.

## Signal Creation

### Data and Tools

To create your own signal, you will first need to acquire some stock market data.

{% hint style="info" %}
Data scientist with no stock market data? Participate in the [Numerai Tournament](https://numer.ai/) instead. 
{% endhint %}

If you do not already have access to stock market data, there are a number of free or cheap data providers on the internet such as [Yahoo Finance](https://finance.yahoo.com/), [Quandl](https://www.quandl.com/), and [Koyfin](https://www.koyfin.com/). 

There are also platforms that make it easy to create signals such as [Quantopian](https://www.quantopian.com/), [QuantConnect](https://www.quantconnect.com/), and [Alpaca](https://alpaca.markets/). In particular, [Risk Model](https://www.quantopian.com/risk-model) and [AlphaLens Tearsheets](https://www.quantopian.com/tutorials/alphalens#lesson1) are great ways to analyze the quality of a signal. 

Check out this [forum thread](https://forum.numer.ai/t/free-or-cheap-data-for-erasure-numerai-quant/350) for a list of sources popular data sources, platforms, and tools used by our community. 

{% hint style="success" %}
Finding unique and differentiated datasets is key to creating original signals.
{% endhint %}

### Universe

The Numerai Signals stock market universe covers roughly the top 5000 largest stocks in the world. 

The universe is updated every week, but in general only a couple low volume stocks will move in or out on a given week. 

You can see the latest universe by downloading the latest universe file:

{% embed url="https://numerai-signals-public-data.s3-us-west-2.amazonaws.com/universe/latest.csv" %}

### Submissions

When you submit a signal to Numerai Signals, you must include at least two columns:

* A `cusip`, `sedol`, or `bloomberg_ticker` column - values must be valid tickers associated with the ticker type in the header.     
* A `signal` column - values must be between 0 and 1 \(exclusive\).

Submissions with only two columns are assumed to correspond to the current `live` time period, which means the ticker values must be unique.

You may also to upload your signal over a historical `validation` time period to receive diagnostics metrics on your performance, risk, and potential earnings. The `validation` time period spans `374` weeks from `20130104` to `20200228`. 

Submissions that include the `validation` time period must include two extra columns: 

* A `friday_date` column - values must be Fridays as week periods begin on Friday in Numerai Signals.  
* A `data_type` column - values can only be `live` or `validation`. Rows with `data_type` of `live` must contain the date of the most recent Friday. 

![An example submission with bloomberg\_ticker](../.gitbook/assets/submission_screenshot.png)



### Diagnostics

Once your submission has been accepted, it will be queued for diagnostics. This usually takes 10-15 minutes depending on the number of weeks and tickers that span your submission.

![An example diagnostics report](../.gitbook/assets/screen-shot-2020-10-10-at-4.19.28-pm.png)

These diagnostics serve as a guide for you to estimate whether your signal is good enough to be worth staking on. It is important to note that signals with strong diagnostics over the historical `validation` period may not score well in any current or future `live` periods.

{% hint style="danger" %}
Using this historical evaluation tool repeatedly will quickly lead to overfitting. Treat diagnostics only as a final check in your signal creation process. 
{% endhint %}

All of the historical targets used to calculate diagnostics are available here:

{% embed url="https://numerai-signals-public-data.s3-us-west-2.amazonaws.com/signals\_train\_val\_bbg.csv" %}

### API and Automation

You can automate your submission workflow by connecting directly to our GraphQL API

{% embed url="https://api-tournament.numer.ai/" %}

Or using our official Python client library 

{% embed url="https://github.com/uuazed/numerapi\#usage-example---numerai-signals" %}

## Signal Evaluation

### Neutralization

Numerai has a variety of existing signals. Our existing signals include Barra factors \(like size, value, momemtum, etc\) country and sector risk factors, and custom stock features. 

{% hint style="info" %}
**Definition**: A signal or target is considered "neutralized" after Numerai transforms it to have zero correlation with any of Numerai's existing signals such as Barra factors, country, sector factors and other custom stock features.
{% endhint %}

Every signal uploaded to Numerai Signals is neutralized before being scored. The point of the neutralization is to isolate the original or orthogonal component of the signal that is not already present in known signals.

![A visualization of neutralization against a single known signal](../.gitbook/assets/image%20%2853%29.png)

{% hint style="warning" %}
If you submit a simple linear combination of a few well-known signals, there will be little to no orthogonal component after neutralization. 
{% endhint %}

The targets used to evaluate signals are also neutralized. The targets are in effect Numerai's custom "specific return" or "residual return".

The data that is used to perform neutralization is not provided, which means the process is a "black box". However, you can use the historical diagnostics of your signal to estimate the impact neutralization will have on your signal in the future although it’s important to note that signals with strong scores over the historical period may not score well in any current or future round.

The code that is used to implement neutralization is open source. You can learn more about the neutralization process in this example notebook:

{% embed url="https://github.com/numerai/example-scripts/blob/master/SignalsScoringExample.ipynb" %}

Or check out this forum post to understand broader implications of feature exposure and neutralization.  

{% embed url="https://forum.numer.ai/t/model-diagnostics-feature-exposure/899" %}

Signals with very high correlation with subsequent stock returns may score very badly on Numerai Signals and signals with weak correlation with subsequent returns might score well. 

In other words, “good” signals with strong predictive value when considered alone may score poorly on Numerai Signals. This highlights the key unique aspect of Signals: Numerai Signals is not about predicting stock returns, it is about finding original signals that Numerai doesn't already have.

### **Six Day Neutralized Return Targets**

Signals are evaluated against a custom target created by Numerai. This target is based on 6 day neutralized subsequent returns \(ignoring the first 2 days\) starting from Friday close.

The reason why signals are evaluated on a 6 day horizon \(minus the first 2 days\) is because signals that only work on short time horizons are impossible for large hedge funds to implement. For example, even if a signal can accurately predict the 1 hour return of stocks, it is not very useful if it takes a hedge fund 24 hours to fully trade into that position. Signals that are most useful to large hedge funds have predictive power over a long time horizon which is also known as having "low alpha decay".      

For more information on the exact market days that make up the 6 days of subsequent returns, see the following section on dates and deadlines. 

### Scoring

Before scoring, signals are first ranked between \[0, 1\] and then neutralized. Finally the score is computed by taking the Spearman correlation between the neutralized signal and the target. This score is simply referred to as `corr` throughout this doc and the website.

By neutralizing your signal before scoring, Numerai aligns it with the target which improves its performance against the target. Since the target is also neutralized, the neutralization step effectively optimizes your signal for best performance without Numerai having to give out the data used for neutralization.

For example, if your signal is not neutralized to country risks, Numerai Signals will neutralize your signal against country risks before scoring so you can focus on creating an original signal without having to worry about country risk neutralization.

If you only have signals on a subset of the universe \(eg only signals on US stocks\), you can still submit to Signals and still perform well. For each stock in the universe where you have missing signals, Numerai will automatically fill those in with the median value after the signal is ranked.

### Meta Model Contribution

If `corr` is a measure of how well your signal correlates to a target that is neutralized to all signals known to Numerai, Meta Model Contribution \(MMC\) is a measure of how well your signal correlates to a target that is neutralized to all signals known to Numerai _and all other staked signals on Numerai Signals._ This score is simply referred to as `mmc` throughout this doc and the website.

The `mmc` of a signal is computed by first constructing a special signal called the Signals' Meta Model,  which is defined as the stake weighted average of all the \(ranked and neutralized\) signals on Numerai Signals for a given round. The `mmc` of a signal is the correlation of the signal to the target after being neutralized to the Signals' Meta Model.

{% hint style="success" %}
High and consistent MMC on Signals is doubly impressive because it means your signal has an edge over all of Numerai's data and the combination of all other signals on Numerai Signals as well.
{% endhint %}

MMC is a concept that is taken from the main Numerai Tournament and the scoring system is very similar. See the  [metamodel contribution](https://docs.numer.ai/tournament/metamodel-contribution) section in the Numerai Tournament docs for details on how we compute MMC on Numerai.

Note the computation of Numerai Signals' MMC is completely separate from that of the Numerai Tournament. Specifically, only submissions to Numerai Signals are used to construct the Signals' Meta Model.

## Staking and Payouts

You can `stake` your submission if you want the opportunity to earn `payouts`. You can either stake on `corr` or `corr_plus_mmc`.

{% hint style="info" %}
Staking requires you to lock up the [NMR cryptocurrency](https://www.coinbase.com/price/numeraire). This gives Numerai the ability to burn your stake if your signal performs poorly.
{% endhint %}

Once staked, you will `earn` or `burn` a percentage of your stake based on the score of your submissions. 

```python
corr_payout = stake * clip(2 * corr, -0.25, 0.25)

corr_plus_mmc_payout = stake * clip(2 * corr + mmc, -0.25, 0.25)
```

For example, if you stake `100 NMR` on `corr` and your score was `+0.05`, then you will earn `2 * 5% of 100NMR = 10NMR`. If you staked on `corr_plus_mmc` and your `mmc` was `+0.03` then you will earn `(2 * 5% + 3%) of 100NMR = 13NMR`.

The maximum you can earn or burn is `25%` of your stake each round. Payouts are automatically rolled into your stake. 

{% hint style="danger" %}
It is important to note that the opportunity to stake your signal **is not** an offer by Numerai to participate in an investment contract, a security, a swap based on the return of any financial assets, an interest in Numerai’s hedge fund, or in Numerai itself or any fees we earn. Payouts will be made at our discretion, based on a blackbox target that will not be disclosed to users.  Fundamentally, Numerai Signals is a service offered by Numerai that allows users to assess the value of their signals, using NMR staking as a way to validate “real” signals. In return, Numerai uses the staked signals and related data in the Numerai hedge fund. Users with different expectations should not stake signals.

**Please read our** [**Terms of Service**](https://numer.ai/terms) **for further information.**
{% endhint %}

To create a stake, click the "manage stake" button on the website and create a "change request" to "increase" your stake. Here you can select whether you want to stake on `corr` or `corr_plus_mmc`. If at any time you wish to reduce your stake, you can also create a "change request" to "decrease" your stake.  

![](../.gitbook/assets/image%20%2850%29.png)

Please note that change requests do not apply immediately. Always double check the "effective date" shown on the website before applying changes.

## Dates and Deadlines

### Data Date vs Effective Date

There are two types of dates in Numerai Signals 

* `data_date` - dates corresponding to the underlying stock market data. All `data_dates` refer to the market close of that date and do not include a time. For example, values in the `friday_date` column of submissions are of type `data_date`.
* `effective_date`- dates corresponding to actions or events that take place on Numerai Signals and may include a time which is always specified in UTC. There is usually a delay between the `data_date` and the `effective_date` because of time zones and the time it takes for stock market data to be processed. Unless otherwise specified, all dates mentioned in the website and this doc are of type `effective_date`. 

### Rounds

All actions and events and their corresponding dates and times are grouped into numbered `rounds` to make them easier to talk about.

Every `Saturday at 18:00 UTC` a new `round` begins. The submission window \(blue\) is open until the submission deadline of `Monday at 14:30 UTC`. Stakes are locked in during a processed known as "stake selection" on the following Friday. Preliminary scores and pending payouts are reported over the span of 4 days \(green\) on Friday, Saturday, Tuesday and Wednesday. The score and payout reported on Wednesday is taken as the final score and payout for the round.

![Example effective dates for a single round](https://documents.app.lucidchart.com/documents/9e91ae48-1fb7-4603-bf30-8428d1a4fe1e/pages/0_0?a=1995&x=302&y=125&w=1276&h=770&store=1&accept=image%2F*&auth=LCA%207753c57aaa6418ec9384eec80145adfc6731f248-ts%3D1602207875)

The universe of the `round` is a defined by the market as of the `data_date` of the prior Friday. The 6 day returns are constructed using the `data_date` of the following Monday, Tuesday, Wednesday, Thursday, Friday and the subsequent Monday. As mentioned above, the first two days are ignored. Weekends are skipped \(grey\) as the markets are closed. 

![Example data dates for a single round](https://documents.app.lucidchart.com/documents/9e91ae48-1fb7-4603-bf30-8428d1a4fe1e/pages/0_0?a=2075&x=321&y=945&w=1276&h=770&store=1&accept=image%2F*&auth=LCA%2016eb13929c60220c4fb03784d58c0b244f884a0b-ts%3D1602207875)

## Reputation and Leaderboard

The `reputation` of your signal is a weighted average of your signal's `corr` over the past 20 rounds. Similarly, the `mmc_reputation` of your signal is a weighted average of your signals' `mmc` over the past 20 rounds.

![](../.gitbook/assets/image%20%2847%29.png)

## Support

Need help?

Find us on [RocketChat](https://community.numer.ai) for questions, support, and feedback!

