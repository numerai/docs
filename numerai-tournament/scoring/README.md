# Scoring

## Scores

There are two main scores used for payouts

* [Correlation](https://docs.numer.ai/tournament/correlation-corr) (`CORR`): Your prediction's correlation to the target
* [True contribution](https://docs.numer.ai/tournament/true-contribution-tc) (`TC`):  Your prediction's contribution to the hedge fund's returns&#x20;

We also have informational scores not used for payouts

* [Feature Neutral Correlation (FNC)](feature-neutral-correlation.md): Your prediction's correlation to the target after neutralizing against all features &#x20;

## Daily score updates

Within a single round, submissions will receive 20 score updates until the final score of the round is computed.&#x20;

For example, here is what the scoring schedule looks like for a hypothetical weekend round opening on Saturday 6th and closing on Monday 8th. The first day of scoring is on Friday 12th, with daily updates every Tuesday-Saturday, until the final score 4 weeks later on Thursday 8th of the next month.

<figure><img src="https://documents.lucid.app/documents/9e91ae48-1fb7-4603-bf30-8428d1a4fe1e/pages/0_0?a=20594&#x26;x=1874&#x26;y=34&#x26;w=1452&#x26;h=1180&#x26;store=1&#x26;accept=image%2F*&#x26;auth=LCA%20041ead69d99460102bf7ff0651835450958d6314c654fad6321e20ca012d975a-ts%3D1683569516" alt=""><figcaption></figcaption></figure>

The reason why scoring is done over these 20 days is because the main target is built on 20 days of returns ignoring the first 2 days after round close. This is commonly referred to as "20D2L", where "20D" means "20 days of returns" and "2L" means "ignoring the first two days". Each score update is computed using an expanding window of returns.

For example, the first day of scoring on Friday 12th uses a 1D2L target, which includes returns from Wednesday 10th only. The second day of scoring on Saturday 13th uses a 2D2L target which includes returns from Wednesday 10th through Thursday 11th. The final day of scoring 4 weeks later on Thursday 8th of next month uses a 20D2L target which includes returns starting from Wednesday 10th through Tuesday 6th of the next month.&#x20;

<figure><img src="https://documents.lucid.app/documents/9e91ae48-1fb7-4603-bf30-8428d1a4fe1e/pages/0_0?a=20588&#x26;x=1898&#x26;y=1331&#x26;w=1276&#x26;h=1100&#x26;store=1&#x26;accept=image%2F*&#x26;auth=LCA%20ca357e5e86017bddb4fd4a7f3e09ec7a62e4bc008858a2b65b0c9d4746587bad-ts%3D1683569516" alt=""><figcaption></figcaption></figure>

## The Leaderboard

Only the final scores for rounds count towards a model's live performance.

The 1 year average score is also called `reputation` and your model's rank on the leaderboard is primarily based on your model's 1 year average TC score. &#x20;

<figure><img src="../../.gitbook/assets/image (97) (1) (1).png" alt=""><figcaption><p><a href="https://numer.ai/leaderboard">numer.ai/leaderboard</a></p></figcaption></figure>

