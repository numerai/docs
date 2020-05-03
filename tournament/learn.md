---
description: The official rules and getting started guide
---

# Tournament Overview

## Data

At the core of Numerai is a data science problem - the problem of predicting the stock market.

In the provided `training_data`, each `id` corresponds to a stock with a set of obfuscated `features`. The`target` represents future performance. Rows are grouped into `eras` that represent different points in time. 

Your goal is to train a machine learning model to predict the `target` given new `features`. 

{% hint style="info" %}
Read the [analysis and tips notebook](https://github.com/numerai/example-scripts/blob/master/analysis_and_tips.ipynb) for an in-depth exploration of the dataset.
{% endhint %}

![numerai\_training\_data.csv](../.gitbook/assets/ex_data.png)

## Modeling

Below is an example how to train a model on the `training_data` to make predictions on the `tournament_data`.

{% hint style="info" %}
Check out the [example-scripts](https://github.com/numerai/example-scripts) repo for more advanced examples.
{% endhint %}

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

## Submissions

Every Saturday at `18:00 UTC`, a new `round` begins and new `tournament_data` is released. Submit your predictions to Numerai to enter the tournament. 

The submission deadline is `Monday 14:30 UTC`. 

{% hint style="info" %}
Use our [tools and libraries](https://docs.numer.ai/tournament/tools) to connect with our GraphQL [API](https://api-tournament.numer.ai/). 
{% endhint %}

![predictions.csv](../.gitbook/assets/image%20%2835%29.png)

## Scoring

Your submission is scored on the `correlation` between your predictions and the true targets. The higher the correlation the better. 

{% tabs %}
{% tab title="scoring\_function.py" %}
```python
# method='first' breaks ties based on order in array
ranked_predictions = predictions.rank(pct=True, method="first")
correlation = np.corrcoef(labels, ranked_predictions)[0, 1]
```
{% endtab %}
{% endtabs %}

Your submission will also be scored on your metamodel contribution or `mmc`. 

See the [metamodel contribution](https://docs.numer.ai/tournament/metamodel-contribution) section for details.

## Staking and Payouts

You can `stake` on your submission to start earning `payouts`. You can either stake on `correlation` or `mmc` \(coming soon!\).

{% hint style="info" %}
Staking requires you to lock up [NMR](https://coinmarketcap.com/currencies/numeraire/) in an [Erasure](https://erasure.world/) smart contract agreement. This gives Numerai the ability to burn your stake if your model performs poorly. 
{% endhint %}

You `earn` or `burn` a percentage of your stake based on the score you are staking on. For example, if you stake `100 NMR` on `correlation` and your score was `+0.05`, then you will earn `5% of 100NMR = 5NMR`. The maximum you can earn or burn is `25%` of your stake each round.

```python
correlation_payout = (stake * correlation).clip(-0.25, 0.25)

mmc_payout = (2 * stake * mmc).clip(-0.25, 0.25)
```

See the [staking and payouts](https://docs.numer.ai/tournament/staking-and-payouts) section for details.

## Daily Updates

Each submission will receive daily updated scores starting from the first Thursday after the submission deadline to the Wednesday 4 weeks after. For example, if you made the blue submission on `Sun 7th`, you will receive your first score on `Thur 11th` and your final score on `Wed 7th` of the next month.

If you staked on your submission, you will also receive daily updates on your payouts. But only your final score and final payout will count. 

![submission and scoring calendar](https://documents.lucidchart.com/documents/d20914fb-a3d0-4bf5-a775-718fe5b41f17/pages/0_0?a=59169&x=-3266&y=-4681&w=1276&h=902&store=1&accept=image%2F*&auth=LCA%20016838a180a592a2c9146b00e03b2c9e7576491c-ts%3D1588381543)

## Reputation and Leaderboard

Your `rank` on the leaderboard is based on your `reputation`, which is a weighted average of your `correlation` scores over the past 20 rounds. 

See the [reputation](https://docs.numer.ai/tournament/reputation) section for details.

![](../.gitbook/assets/image%20%2822%29.png)

## Support

Need help? 

Find us on [RocketChat](https://community.numer.ai) for questions, support, and feedback!

