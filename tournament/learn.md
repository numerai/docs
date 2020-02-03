# Tournament Overview

## Introduction <a id="rounds"></a>

Numerai is a data science tournament that powers the Numerai hedge fund. Watch the [meta-model video](https://www.youtube.com/watch?v=dhJnt0N497c) to understand how it works at a high level.

The long term vision of Numerai is to manage all the money in the world with a decentralized network of autonomous AI agents. Read our [master plan](https://medium.com/numerai/numerais-master-plan-1a00f133dba9) to learn more.

This document is a brief overview of the tournament structure and rules. If you are new, start here!

## Data <a id="rounds"></a>

To make good predictions, you need good data. But production grade financial data is not easy to find. Hedge funds spend millions buying and managing this data, so they keep it secret.

Numerai provides this production grade financial data for free. Our data is [obfuscated](https://medium.com/numerai/encrypted-data-for-efficient-markets-fffbe9743ba8) to keep the actual assets and features secret while preserving underlying structure.

This is what our `training_data` looks like. Each `id` represents an asset with some abstract`features` and each `era` is a unit period of time in history. The `target` is an abstract measure of performance.

![](../.gitbook/assets/ex_data.png)

## Modeling <a id="rounds"></a>

Your task is to train a model to make predictions on the out-of-sample `tournament_data`. This dataset includes `validation` and `test` hold out sets, as well as `live` features of current stock market.

Here is a basic example model.

```python
import pandas as pd
from xgboost import XGBRegressor

# training data contains features and targets
training_data = pd.read_csv("numerai_training_data.csv").set_index("id")

# tournament data contains features only
tournament_data = pd.read_csv("numerai_tournament_data.csv").set_index("id")
feature_names = [f for f in training_data.columns if "feature" in f]

# train a model to make predictions on tournament data
model = XGBRegressor(max_depth=5, learning_rate=0.01, \
                     n_estimators=2000, colsample_bytree=0.1)
model.fit(training_data[feature_names], training_data["target"])

# submit predictions to numer.ai
predictions = model.predict(tournament_data[feature_names])
predictions.to_csv("predictions.csv")
```

To help you get started, we have also written two detailed walkthroughs of the problem in [Python](https://github.com/numerai/example-scripts/blob/master/analysis_and_tips.ipynb) and [R](https://github.com/numerai/example-scripts/blob/master/example_model.r). These guides cover key concepts such as feature importance, cross validation, consistency, overfitting, and how to use `eras`. Whether you are a novice or master level data scientist, we highly recommend that you go through these guides!

If you want to learn more about why we have setup the problem this way, check out the book [Advances in Financial Machine Learning](https://www.amazon.com/Advances-Financial-Machine-Learning-Marcos/dp/1119482089) by [Marcos Lopez de Prado](https://www.linkedin.com/in/lopezdeprado/), who is our scientific advisor.

## Submissions

Every weekend, new `tournament_data` is released and a new round begins. To participate in the round, run the new `tournament_data` through your model and submit your predictions back to Numerai.

Submission files look like this. The `id` column must match the one in `tournament_data` exactly. The `prediction` can be any number between 0 and 1 \(exclusive\).

![](../.gitbook/assets/image%20%2830%29.png)

You can upload your submission at any time before the next round opens. However, only submissions made before `Monday 14:30 UTC` are considered on-time. Late submissions will not count towards your score and will not be eligible for payouts or bonuses.

![](../.gitbook/assets/image%20%285%29.png)

You can upload your submission to our [website](https://numer.ai/) or[ api](https://api-tournament.numer.ai). You can also use the [Python](https://github.com/uuazed/numerapi) and [R](https://github.com/Omni-Analytics-Group/Rnumerai) client libraries to do this programatically.

For advanced users, check out [Numerai Compute](https://docs.numer.ai/tournament/compute) - a framework to help you automate your submission workflow.

## Scoring

Numerai measures performance based on the `rank_correlation` between your predictions and the true targets.

{% tabs %}
{% tab title="scoring\_function.py" %}

```python
# method='first' breaks ties based on order in array
ranked_predictions = predictions.rank(pct=True, method="first")
correlation = np.corrcoef(labels, ranked_predictions)[0, 1]
```

{% endtab %}
{% endtabs %}

Each day \(for 4 weeks\) the submission gets an updated correlation score showing how well it has done so far.

If you upload new submissions each week, you will get overlapping scores of multiple submissions as shown below. Notice that there are no scores on Sundays or Mondays. These gaps correspond to the weekends when markets are closed.

![ submissions and scoring calendar](https://lh5.googleusercontent.com/MYmSmSF8vKx3OYn6llB0c5EarVXOaNF6pdHysbCmaKfxQsYcR86QZ6PrB5X9sJOMXwKW8cKW5WJLSs3euODA7JoKT9akwIn-o48nBYWWZciCz2SazrjGlGghLqliSZR4GzuVWVVc)

Here is how the example model performed over 10 weeks. Each colored line represents the correlation of a different submission. Notice how they are staggered.

![](../.gitbook/assets/image%20%288%29.png)

We combine these overlapping scores into a single continuous score by taking the daily marginal change in `correlation` score of each submission, and averaging it across all overlapping submissions. We call this `average_daily_correlation`, and is the primary score that all payouts and bonuses are based.

Here is a graph of the daily marginal changes in `correlation`shown above in colored dots and the `average_daily_correlation` in solid black.

![](../.gitbook/assets/image%20%286%29.png)

## Staking <a id="staking"></a>

You can `stake` on your model to start earning daily payouts.

Staking requires you to lock up [NMR](https://coinmarketcap.com/currencies/numeraire/) in an [Erasure](https://github.com/erasureprotocol/erasure-protocol) smart contract agreement. This gives Numerai the ability to grief \(aka burn\) your stake if your performance is poor. This also known as having "skin in the game".

![payout band of ±0.2](../.gitbook/assets/image%20%281%29.png)

Your daily payout is a function of your `stake_value` and `average_daily_correlation`. For example, if your `stake_value` is 100 NMR, and your `average_daily_correlation` is 0.1, your payout will be +50% and so you will earn 50 NMR. If instead your `average_daily_correlation` is -0.1, then your payout will be -50% and so you will lose 50 NMR.

Payouts occur every day scores are updated, and the payout curve is applied to each `average_daily_correlation` score independently. All payouts are rolled into your stake balance, but they don't effect your `stake_value` used for payout calculation until the following Thursday. For example, the payouts computed from the 11th to 17th use the initial `stake_value` of `100` but from the 18th forward until the next command, payouts will use `150` as the `stake_value`.

![](https://documents.lucidchart.com/documents/d20914fb-a3d0-4bf5-a775-718fe5b41f17/pages/0_0?a=58892&x=2877&y=-2127&w=1385&h=451&store=1&accept=image%2F*&auth=LCA%2035723e092586a7fbc486a6bb994f540144f5e3ac-ts%3D1571771371)

You can create and manage your stake on the [website](http://numer.ai) or directly [on the Ethereum blockchain](https://github.com/numerai/tournament-contracts). Below is an example of staking on the website.

![](../.gitbook/assets/image%20%2832%29.png)

You can increase your stake at any time and it will apply next Thursday. Decreasing works similarly except it always takes an additional 4 weeks.

At the beginning of each Thursday, up to `100K NMR` in stakes will be selected and eligible for payouts. If the total amount staked exceeds this, then all stakes will be selected pro rata.

If you don't already have NMR, you can acquire it on the open market. The easiest way is through [ETH](https://coinmarketcap.com/currencies/ethereum/) on [Uniswap](https://uniswap.exchange/swap) or through [BTC](https://coinmarketcap.com/currencies/bitcoin/) on [Changelly](https://changelly.com/), [Upbit](https://upbit.com/exchange?code=CRIX.UPBIT.BTC-NMR), [Bittrex](https://bittrex.com/Market/Index?MarketName=BTC-NMR), [Poloniex](https://poloniex.com/exchange#btc_nmr), and [HitBTC](https://hitbtc.com/NMR-to-BTC).

## Leaderboard

Maintaining a high `average_daily_correlation` over time earns you a place on the leaderboard and a large daily bonus.

![](../.gitbook/assets/image%20%2811%29.png)

Your `rank` on the leaderboard depends on your `reputation`, which is the sum of your `average_daily_correlation`over the past 100 days.

Any days with a missing `average_daily_correlation` score will be filled with a `-0.005`. We call this adjusted score `average_daily_correlation_penalized` and will use this to compute your reputation instead. This means that new users start with `reputation` of `-0.5`. This also means that if you have been submitting weekly, you would need to miss 4 submissions in a row to be penalized.

Your bonus is a function of your `rank` amongst all staked models \(otherwise known as `staked_rank`\) and your `stake_value` at the beginning of the 100 day window. For example, if your `stake_value` was 100 NMR at the beginning of the window and your `staked_rank` is 1, then you will get a 5 NMR bonus.

Like payouts, bonuses are paid into your stake balance. The max bonus paid out per day is `250 NMR` across all models. If the total bonus amount exceeds this, then all bonuses will be paid pro rata.

| Staked Rank | Daily Bonus |
| :---------- | :---------- |
| Top 1       | 5%          |
| Top 10      | 4%          |
| Top 25      | 3%          |
| Top 100     | 2%          |
| Top 300     | 0.5%        |

We reserve the right to refund your stake and void all earnings and burns if we believe that you are actively abusing or exploiting the payout rules.

## Support

Need help with anything?

Find us on [RocketChat](https://community.numer.ai) for questions, support, and feedback!
