# Signals Overview

Numerai Signals allows anybody to upload stock market signals and find out how original they are vs all other signals on Numerai. Signals can be staked with the NMR cryptocurrency to earn rewards. The best most orignal signals are used in Numerai's hedge fund.

## How Numerai Signals Works

1. Sign up to [Numerai Signals](https://signals.numer.ai). Accounts are shared with the main Numerai tournament, and you can just use your email/password from there if you've already made an account with Numerai.
2. Upload signals on stocks in our universe \(it's roughly the biggest 5000 stocks in the world, see [example signals for full universe](https://numerai-signals-public-data.s3-us-west-2.amazonaws.com/example_predictions/latest.csv)\).
3. Prove you believe in your signals by staking them with cryptocurrency.
4. Earn or lose money based on how original and good your signals are according to Numerai.

## Signals

Stock market signals are data feeds about stocks that can be used by hedge funds like Numerai to improve performance. A count of the number of tweets mentioning ticker symbols in the Russell 3000 universe every day could be a signal. By itself, it might not be very predictive but taken together with other signals, it might improve predictive accuracy. Other examples of signals include signals produced from quant models such as those created on Quantopian, raw high quality data about stocks such as P/E ratios, executive compensation data, signals based on public filings or earnings calls, etc.

Format your signals as a CSV, with tickers on one column and signals, expressed between 0 and 1, on the other. Your CSV upload must contain at least 100 predictions to be considered a valid submission. If you have access to SEDOLs or CUSIP ids for your stocks, you can use those as ids as well.

![](../.gitbook/assets/screen-shot-2020-06-04-at-11.39.52-am.png)

An example CSV is [here](https://numerai-quant-public-data.s3-us-west-2.amazonaws.com/example_predictions/latest.csv). This CSV includes an up to date universe that is generated daily.

## Creating Signals

Unlike Numerai which provides clean training data to build your model, Numerai Signals provides no data. This is because Numerai Signals is a tool for people who have already built their own models or already have access to data they believe might produce good signals. However, there is a lot of free or low cost data available on the internet and a number of tools such as Quantopian, QauntConnect and Alpaca that provide data or make it easy to turn data into signals.

Quantopian has a hosted IDE, with tightly integrated data sources and backtesting engine. Unfortunately, it’s tricky to export orders from that IDE. One strategy:

1. Publish your algorithm for live trading
2. Copy the live trading ID in the URL \(ie, ...live\_algorithms/\[your\_ID\]\)
3. Go to their research notebook \(Research &gt; Notebooks\)
4. Run this command:

```text
bt = get_live_results(‘[your_ID]’)
bt = bt.pyfolio_positions.to_string()
print(bt)
```

Quantopian descriptions on the kinds of models they like give some good insights as to what would make a good signal on Numerai Signals as well. Quantopian's Risk Model and AlphaLens Tearsheets are a great way to analyze the quality of a signal (what they call a "factor"). See [https://www.quantopian.com/tutorials/alphalens#lesson1](https://www.quantopian.com/tutorials/alphalens#lesson1) and [https://www.quantopian.com/risk-model](https://www.quantopian.com/risk-model)

Alpaca has a freely available set of scripting tools, including data, with a broker backend to place trades once designed. TK [Alpaca built a tool to export from Alpaca to Erasure](https://github.com/alpacahq/alpaca-erasure).

Users also have a thread on the forums discussing potential data sources. [Check it out](https://forum.numer.ai/t/free-or-cheap-data-for-erasure-numerai-quant/350), and add what works for you.

## Universe

The stock universe is updated daily, but in general only a couple, low volume stocks will move in/out on a given day. You can see today's universe by downloading the [latest example predictions](https://numerai-signals-public-data.s3-us-west-2.amazonaws.com/example_predictions/latest.csv).

You can view the historical universe by downloading old example predictions files directly from s3, with urls like the following: [https://numerai-quant-public-data.s3-us-west-2.amazonaws.com/example\_predictions/20200519.csv](https://numerai-quant-public-data.s3-us-west-2.amazonaws.com/example_predictions/20200519.csv)

## Neutralization

The way Numerai assesses the originality of an uploaded signal is by neutralizing it to all other signals Numerai already has. All signals uploaded to Signals are neutralized by Numerai before being scored. If Numerai, already has 12 month momentum as a signal, the neutralization ensures Signals users aren't rewarded for uploading that same signal again. The goal of Numerai Signals is to capture original new data for Numerai. The predictive value of common signals is diminished by neutralization but the predictive value of highly original signals will be unchanged or even improved by neutralization.

TK Example of neutralization picture, mathematics and code

## Submissions

Every Saturday at `18:00 UTC`, a new `round` begins. Submit your predictions to Numerai Signals to enter the tournament.

The submission deadline for each round is `Monday 14:30 UTC`. Late submissions will not be eligible for payouts.

TK
{% hint style="info" %}
Use our [tools and libraries](https://docs.numer.ai/tournament/tools) to connect with our GraphQL [API](https://api-tournament.numer.ai/).
{% endhint %}

## Targets

Numerai Signals is looking for signals we don't already have and also signals we can implement in live trading in our hedge fund. To achieve each of these two goals we score all signals based on their correlation to a custom target which is (1) neutralized to the signals we already have and (2) ignores the first two days of returns.

## ***One Week Neutralized Return Targets***

Numerai Signals rewards users based on their signal's correlation to custom target created by Numerai. This target is created by neutralizing subsequent 6 day returns (ignoring the first 2 days) to all the signals Numerai already has. Since Signals users are not provided any of the data that Numerai uses to create the target, the target is a blackbox. The targets are in effect a Numerai customized "specific return" aka "residual return" where major risk factors and features such as country risk, sector risk, size, value etc are neutralized out of the return.

All this neutralization means that signals with very high correlation with subsequent stock returns (information coefficient) may score very badly on Numerai Signals and signals with weak correlation with subsequent returns might score well. This highlights the key unique aspect of Signals: Numerai Signals is not about predicting stock returns, it's about providing original data we don't yet have that's specifically helpful to Numerai.

## ***Two Day Lag***

A common problem with many signals is that they are impossible to implement because the signal works only on short time horizons. For example, a signal that can predict the subsequent one hour return of a stock might not be useful if it would take a hedge fund one day to build up a sizeable position in the stock. The signals that are most implementable by Numerai are signals which have predictive power for a long time after we receive them (known as "low alpha decay" signals).

So Numerai Signals only rewards signals based on their weekly performance after subtracting off the first two days of return. When weekly submissions close on `Mondays at 14:30 UTC`, we want the signals submitted to be correlated with returns from Tuesday's close to the following Monday's close so all our targets are constructed based on these 2 day lagged returns. High frequency signals that are only predictive on sub 2 day time horizons are unlikely to perfom well in the current version of Numerai Signals.

## Scoring

Numerai Signals scores uploaded signals by first ranking the signal between \[0,1] and then neutralizing the ranked signal to all the same signals that the target is neutral to and then computing the Spearman correlation of the neutralizated signal with the target. Every signal uploaded is first neutralized to all the other signals that Numerai already has then Numerai computes the correlation of this neutralized signal with the target. By pre-neutralizing all uploaded signals, Numerai aligns them with the targets which improves their perfromance against the target. Because Numerai doesn't provide the data that the targets are neutralized to, this neutralization of your signal effectively optimizes it for best performance on the target. For example, if your signal is not neutralized to country risks, Numerai Signals will do that neutralization for you before scoring you so you can focus on the signal and not the risk neutralization.

If you only have signals on a subset of the universe (eg only signals on US stocks), you can still submit to Signals and still perform well. However, for each stock in the universe where you have missing signals, Numerai will automatically fill those in with 0.5 values after the signal is ranked.

TK code and pictures for ranking > filling missing values > neutralization.

## Evaluation

Because scoring on Numerai Signals is a blackbox, we've built a tool to help users analyze whether their signals are likely to be useful to Numerai based on historical data. Whenever users upload their latest signals, they can also choose to upload over a historical test period (TK 2014-2020). Over this historical period, Numerai neutralizes their signal and scores them vs our custom neutralized target variable and displays the user's scores over the entire period and diagnostics. These diagnostics serve as a guide for users to estimate whether their signal is original enough and strong enough to be worth staking on Numerai Signals.

Using this historical evaluation tool repeatedly will quickly lead to overfitting. It should instead be used as a final check of an otherwise robust scientific signal creation process. The focus of a good Signal's user should be on using novel datasets and modelling techniques to create signals, not on overfitting to the test period.

## Meta Model Contribution

Just like Numerai, Numerai Signals also has payouts for Meta Model Contribution (MMC). Whereas the target variable is neutralized to all the signals Numerai has, MMC is how your model would perfom when neutralized by signals Numerai has *and all other Numerai Signals users' signals*. On Numerai Signals, MMC is computed by computing a special signal called the Signals' Meta Model which is defined as the stake weighted average of all the (ranked and neutralized) signals on Numerai Signals. The MMC of a signal is the correlation of the signal to the target after being neutralized to the Signals' Meta Model.

TK code for computing MMC

Having large and consistent MMC on Signals is doubly impressive because it means your signal has an edge over all Numerai's data and the combination of all other signals on Numerai Signals as well.

Numerai Signals' MMC is separate from the MMC on Numerai. None of the submissions to Numerai are considered in the calculation only the submissions to Numerai Signals are used in the calculation.

See the [metamodel contribution](https://docs.numer.ai/tournament/metamodel-contribution) section for details on how we compute MMC on Numerai.

## Staking and Payouts

You need to `stake` your submission to start earning `payouts`. You can either stake on `correlation` or `corr plus mmc`.

{% hint style="info" %}
Staking requires you to lock up the [NMR cryptocurrency] (https://coinmarketcap.com/currencies/numeraire/) for a week. This gives Numerai the ability to burn your stake if your model performs poorly.
{% endhint %}

You `earn` or `burn` a percentage of your stake based on the score of your submissions. For example, if you stake `100 NMR` on `correlation` and your score was `+0.05`, then you will earn `5% of 100NMR = 5NMR`. The maximum you can earn or burn is `25%` of your stake each round.

```python
corr_payout = stake * clip(corr, -0.25, 0.25)

mmc_payout = stake * clip(corr + mmc, -0.25, 0.25)
```

See Numerai's [staking and payouts](https://docs.numer.ai/tournament/staking-and-payouts) section for further details.

## Daily Updates

Each submission will receive daily updated scores starting from the first Thursday after the submission deadline to the Wednesday one week after (TK correct?). For example, if you made the blue submission on `Sun 7th`, you will receive your first score on `Thur 11th` and your final score on `Wed 7th` of the next month.

If you staked on your submission, you will also receive daily updates on your payouts. But only your final score and final payout will count.

![submission and scoring calendar](https://documents.lucidchart.com/documents/d20914fb-a3d0-4bf5-a775-718fe5b41f17/pages/0_0?a=59169&x=-3266&y=-4681&w=1276&h=902&store=1&accept=image%2F*&auth=LCA%20016838a180a592a2c9146b00e03b2c9e7576491c-ts%3D1588381543)

## Reputation and Leaderboard

Your `rank` on the leaderboard is based on your `reputation`, which is a weighted average of your `correlation` scores over the past 20 rounds.

See the [reputation](https://docs.numer.ai/tournament/reputation) section for details.

![](../.gitbook/assets/image%20%2822%29.png)

## Support

Need help?

Find us on [RocketChat](https://community.numer.ai) for questions, support, and feedback!
