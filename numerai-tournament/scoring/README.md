# Scoring

## Scores

There are two main scores used for payouts

* [Correlation](https://docs.numer.ai/tournament/correlation-corr) (`CORR`): Your prediction's correlation to the target
* [True contribution](https://docs.numer.ai/tournament/true-contribution-tc) (`TC`):  Your prediction's contribution to the hedge fund's returns&#x20;

We also have informational scores not used for payouts

* [Feature Neutral Correlation (FNC)](feature-neutral-correlation.md): Your prediction's correlation to the target after neutralizing against all features &#x20;

## Daily score updates

Within a single round, submissions will receive 20 score updates until the final score of the round is computed.&#x20;

The reason why scoring is done over these 20 days is because the main target is built on 20 day returns. Each point on this chart represents an estimate of your final score based on returns of an expanding window of days.&#x20;

For example the 1st score is based on a 1 day return target all the way up to and the 20th score being based on a 20 day return target. But since scoring is officially done based on the 20 day return target, only the final 20th score is counted as the official score for the round.

## The Leaderboard

Only the final scores for rounds count towards a model's live performance.

The 1 year average score is also called `reputation` and your model's rank on the leaderboard is primarily based on your model's 1 year average TC score.&#x20;

<figure><img src="../../.gitbook/assets/image (97) (1) (1).png" alt=""><figcaption><p><a href="https://numer.ai/leaderboard">numer.ai/leaderboard</a></p></figcaption></figure>

