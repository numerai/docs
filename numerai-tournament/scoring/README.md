# Scoring

## Scores

There are two main scores currently used for payouts

* [Correlation](https://docs.numer.ai/tournament/correlation-corr) (`CORR`): Your prediction's correlation to the target
* [Meta Model Contribution](meta-model-contribution-mmc.md) (`MMC`): Your predictions contribution to the Meta Model

We also have informational scores not used for payouts

* [Feature Neutral Correlation (FNC)](feature-neutral-correlation.md): Your prediction's correlation to the target after neutralizing against all features
* Correlation with the Meta Model (CWMM): Your prediction's correlation to the Meta Model (stake weighted average of all predictions).
* Benchmark Model Contribution (BMC): Your prediction's correlation to the target after neutralizing against the stake-weighted Benchmark Models.

## Live Scoring

Within a single round, submissions will receive 20 score updates until the final score of the round is computed. Let's look at an example of a weekend round:

<figure><img src="../../.gitbook/assets/Numerai Engineering Master - General.png" alt=""><figcaption></figcaption></figure>

We score you against a target loosely based market returns of a stock. These market returns take 2 days to process, then we ignore the first 2 days of returns (known as **2 Lag** days) because they are noisy. Thus, 4 total business days elapse before we can start scoring. The final score is released 4 weeks later because we care about the stock returns over **20** (business) **Days.**

This is known as a "_**20D2L target**_" - _**20**_ _**D**_&#x61;ys of returns after _**2**_ _**L**_&#x61;g days:

<figure><img src="../../.gitbook/assets/Numerai Engineering Master - General (1).png" alt=""><figcaption></figcaption></figure>

So, the first day of scoring uses the 1D2L target from 2 days prior. Subsequent days of scoring use the 2D2L target, then 3D2L, etc. The final day of scoring is 4 weeks later, using the final 20D2L target. Here is the full breakdown:

<figure><img src="../../.gitbook/assets/Numerai Engineering Master - General (2).png" alt=""><figcaption></figcaption></figure>

Numerai also has **60D2L** scores, which follow the same logic as **20D2L** scores, but resolve after 60 business days. Any rounds paying out on **60D2L** scores, will lock up your stake for 12 weeks.

## The Leaderboards

Only the final scores for count towards a model's live performance. We rank you both on an account level and on a model level. The primary aggregate score is called your `reputation`.

Your model's `reputation` is just it's 1 year average score. This directly determines the rank of models on the model leaderboard.

Your account's `reputation` is determined by the Stake-Weighted-Average Score of your models. Each round, we multiply each of your model's scores by it's proportion of stake relative to your account and add them together. This means if you have a single model with no stake, your account score is the same as your `reputation` of your model.

<figure><img src="../../.gitbook/assets/Screenshot 2025-02-13 at 17.19.04.png" alt=""><figcaption><p><a href="https://numer.ai/leaderboard">numer.ai/leaderboard</a></p></figcaption></figure>

## Diagnostics

The diagnostics tool computes and charts your scores over the validation dataset.

<figure><img src="../../.gitbook/assets/image (5).png" alt=""><figcaption><p>An example diagnostics report</p></figcaption></figure>

If you uploaded your model via [Model Upload](../submissions/model-uploads.md), then Numerai will automatically run your model over the validation dataset to generate diagnostics. If you wish, you may also manually run diagnostics by heading over to [numer.ai/scores](https://numer.ai/scores) and clicking on the Run Diagnostics button:

<figure><img src="../../.gitbook/assets/Screenshot 2024-03-19 at 9.26.27 AM.png" alt=""><figcaption></figcaption></figure>

{% hint style="warning" %}
**Caution**: past performance is no guarantee of future performance. This is especially true in the domain of financial machine learning. Take care not to rely too heavily on validation metrics during your research process to avoid overfitting to the validation dataset. If you train on the validation dataset, then don't expect your in-sample validation metrics to generalize out-of-sample.
{% endhint %}
