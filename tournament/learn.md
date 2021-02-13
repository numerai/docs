---
description: The official rules and getting started guide to the Numerai Tournament
---

# Numerai Tournament Overview

The Numerai Tournament is where you build machine learning models on abstract financial data to predict the stock market. Your models can be staked with the NMR cryptocurrency to earn rewards based on performance. 

The staked models of Numerai are combined to form the Meta Model which controls the capital of the Numerai hedge fund across the global stock market. 

Watch this short film to learn how it all fits together:

{% embed url="https://www.youtube.com/watch?v=dhJnt0N497c" %}

## Summary 

1. Sign up at [https://numer.ai/](https://numer.ai/)
2. Download the dataset with training data and example scripts.
3. Build your model and submit your predictions back to Numerai.
4. Stake NMR on your models to earn/burn based on performance.
5. Automate your weekly submissions and grow your stake over time.

## Data

At the core of the Numerai Tournament is the dataset. It is made of high quality financial data that has been cleaned, regularized, and obfuscated.  

![](../.gitbook/assets/ex_data.png)

Each `id` corresponds to a stock at a specific time `era`. The `features` describe known attributes of the stock at the time. The `target` represents an abstract measure of future performance. 

## Modeling

Your objective is to build a model to predict the target given features that correspond to the stock market at the current time. 

Here is a basic example using XGBoost in Python. We train the model using the historical training data, and make predictions on the live tournament data. 

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

A new `round` begins every `Saturday at 18:00 UTC` and new tournament data is released. To participate in the tournament, you must submit your latest predictions every week by the deadline on `Monday 14:30 UTC`.

You can download the new data and submit your predictions using the website, via our [GraphQL API](https://api-tournament.numer.ai/) directly or using the [Python](https://github.com/uuazed/numerapi) or [R](https://github.com/Omni-Analytics-Group/Rnumerai) api-client. You can also automate your entire submission workflow with [Numerai Compute](https://github.com/numerai/numerai-cli).  

![](../.gitbook/assets/image%20%2868%29.png)

## Scoring

You are primarily scored on the `corr` or correlation between your predictions and the true targets. The higher the correlation the better.

{% tabs %}
{% tab title="scoring\_function.py" %}
```python
# method='first' breaks ties based on order in array
ranked_predictions = predictions.rank(pct=True, method="first")
correlation = np.corrcoef(labels, ranked_predictions)[0, 1]
```
{% endtab %}
{% endtabs %}

You are also scored on your [meta model contribution](https://docs.numer.ai/tournament/metamodel-contribution) \(`mmc`\) and [feature neutral correlation](https://docs.numer.ai/tournament/feature-neutral-correlation) \(`fnc`\).

Your model's performance is displayed on its public model profile. Here is an example of a model's performance over 20 rounds.

![](../.gitbook/assets/image%20%2866%29.png)

Upon each submission, we will show you diagnostic metrics to help you understand the performance characteristics of your model.

![](../.gitbook/assets/image%20%2871%29.png)

## Staking & Payouts

You can optionally `stake` [NMR](https://www.coinbase.com/price/numeraire) on your model to earn or burn based on your live `corr` and `mmc` scores. For the duration of the stake, you will earn a percentage of your stake if you have positive scores, and burn if you have negative scores.

You cannot stake on your `fnc` scores.

Here is an example of how you would manage a stake on the website. [INTEGRATION\_TEST](https://numer.ai/integration_test) is our official example model. 

![](../.gitbook/assets/image%20%2861%29.png)

See [Staking and Payouts](https://docs.numer.ai/tournament/staking-and-payouts) for details.

## Leaderboard

The leaderboard can be sorted by the reputation of model's `corr`, `mmc`, and `fnc`. [Reputation](https://docs.numer.ai/tournament/reputation) is the weighted average of a given metric over the past 20 rounds.

Keep an eye on the leaderboard to see how your models compare to all other models in terms of performance and returns from staking.

![](../.gitbook/assets/image%20%2869%29.png)

## Support

We are here to help.

Find us on [RocketChat](https://community.numer.ai) for questions, support, and feedback!

