# Scoring

## Scores

There are two main scores currently used for payouts

* [Correlation](https://docs.numer.ai/tournament/correlation-corr) (`CORR`): Your prediction's correlation to the target
* [True contribution](https://docs.numer.ai/tournament/true-contribution-tc) (`TC`):  Your prediction's contribution to the hedge fund's returns&#x20;

On Jan 2, 2024 the payout metric will change to [Meta Model Contribution](meta-model-contribution-mmc-and-bmc.md) (`MMC`): Your predictions correlation to the target after neutralizing to the Meta Model.&#x20;

We also have informational scores not used for payouts

* [Feature Neutral Correlation (FNC)](feature-neutral-correlation.md): Your prediction's correlation to the target after neutralizing against all features &#x20;
* Correlation with the Meta Model (CWMM): Your prediction's correlation to the Meta Model (stake weighted average of all predictions).
* Benchmark Model Contribution (BMC): Your prediction's correlation to the target after neutralizing against the stake-weighted Benchmark Models.

## Live Scoring

Within a single round, submissions will receive 20 score updates until the final score of the round is computed.&#x20;

For example, here is what the scoring schedule looks like for a hypothetical weekend round opening on Saturday 6th and closing on Monday 8th. The first day of scoring is on Friday 12th, with daily updates every Tuesday-Saturday, until the final score 4 weeks later on Thursday 8th of the next month.

<figure><img src="https://documents.lucid.app/documents/9e91ae48-1fb7-4603-bf30-8428d1a4fe1e/pages/0_0?a=20594&#x26;x=1874&#x26;y=34&#x26;w=1452&#x26;h=1180&#x26;store=1&#x26;accept=image%2F*&#x26;auth=LCA%20041ead69d99460102bf7ff0651835450958d6314c654fad6321e20ca012d975a-ts%3D1683569516" alt=""><figcaption></figcaption></figure>

The reason why scoring is done over these 20 days is because the main target is built on 20 days of returns ignoring the first 2 days after round close. This is commonly referred to as "20D2L", where "20D" means "20 days of returns" and "2L" means "ignoring the first two days". Each score update is computed using an expanding window of returns.

For example, the first day of scoring on Friday 12th uses a 1D2L target, which includes returns from Wednesday 10th only. The second day of scoring on Saturday 13th uses a 2D2L target which includes returns from Wednesday 10th through Thursday 11th. The final day of scoring 4 weeks later on Thursday 8th of next month uses a 20D2L target which includes returns starting from Wednesday 10th through Tuesday 6th of the next month.&#x20;

<figure><img src="https://documents.lucid.app/documents/9e91ae48-1fb7-4603-bf30-8428d1a4fe1e/pages/0_0?a=20588&#x26;x=1898&#x26;y=1331&#x26;w=1276&#x26;h=1100&#x26;store=1&#x26;accept=image%2F*&#x26;auth=LCA%20ca357e5e86017bddb4fd4a7f3e09ec7a62e4bc008858a2b65b0c9d4746587bad-ts%3D1683569516" alt=""><figcaption></figcaption></figure>

## The Leaderboard

Only the final scores for rounds count towards a model's live performance.

The 1 year average score is also called `reputation` and your model's rank on the leaderboard is primarily based on your model's 1 year average TC score. This will change to MMC on Jan 2, 2024.

<figure><img src="../../.gitbook/assets/image (46).png" alt=""><figcaption><p><a href="https://numer.ai/leaderboard">numer.ai/leaderboard</a></p></figcaption></figure>

## Diagnostics (Validation Scoring)

Diagnostics is a tool to help you compute and visualize your scores over the validation dataset.

<figure><img src="../../.gitbook/assets/image (5).png" alt=""><figcaption><p>An example diagnostics report</p></figcaption></figure>

If you uploaded your model via [Model Upload](../submissions/model-uploads.md), then Numerai will automatically run your model over the validation dataset to generate diagnostics.

If you wish, you may also manually run diagnostics by heading over to [numer.ai/scores](https://numer.ai/scores) and clicking on the Run Diagnostics button.  &#x20;

&#x20; &#x20;

<figure><img src="../../.gitbook/assets/image (22).png" alt=""><figcaption></figcaption></figure>

To note, all of the scoring code we use to generate diagnostics is also available in our [example scripts repository](https://github.com/numerai/example-scripts) if you wish to replicate this locally.&#x20;

A word of caution: past performance is no guarantee of future performance. This is especially true in the domain of financial machine learning. Take care not to rely too heavily on validation metrics during your research process to avoid overfitting to the validation dataset. If you train on the validation dataset, then don't expect your in-sample validation metrics to generalize out-of-sample.
