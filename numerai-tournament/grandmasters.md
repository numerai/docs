# Grandmasters

Grandmasters is a prestige system for Numerai participants. In Grandmasters, users are awarded for their stake-weighted model performance over the calendar year.

At the start of each calendar year, a new season begins. After 20 qualifying submissions a data scientist’s account will be assigned a provisional title for that season based on average year-to-date stake-weighted account score rankings. This title can change based on performance throughout the year.

At the end of the season when the last round has been resolved and rankings finalized, titles will be awarded.

## Canon Scores

The term 'Canon scores' refers to the standardized metrics used to unify different scoring versions into a single, consistent performance measure.

In the context of the Numerai tournament, Canonical Scores (or “Canon Scores”) are particularly relevant. For example, the CORR score, which is a payout metric, has undergone updates. Initially, the payout score was 'CORR20' until round 484. It evolved into 'CORR20v2' starting from round 485. The 'Canon CORR' score accounts for these changes by combining them into a unified score — it is 'CORR20' for rounds up to and including 484 and 'CORR20v2' for rounds thereafter.

The 'TC' score has remained consistent throughout the tournament's history, meaning 'Canon TC' and 'TC' are equivalent.

For the 2022 and 2023 seasons, scores are based on Canon TC and Canon CORR. However, the scoring criteria for future seasons may be revised.

## Stake-weighted Average (SWA) Scores

### Understanding Stake-weighted Scores

In the Grandmasters rankings, a participant's performance is not only measured by the raw score of their models but also by how confident they are in their models, as demonstrated by their stakes. This is encapsulated in the 'stake-weighted average score', a metric that balances model accuracy with the stake amount to produce a comprehensive performance measure.

For the 2022 and 2023 seasons, participants' rankings were determined by their stake-weighted average scores derived from the Canon CORR and Canon TC metrics.

### Season Scoring

Your season score is the average of your stake-weighted average scores for all rounds included in the season. It's important to note that for any round where you do not submit a model or place a stake, your score for that round will be considered zero, potentially impacting your overall seasonal average.

### Example

Consider if you made submissions with two staked models and one unstaked model in a round:

* &#x20;Model A with a score of 0.01 and a stake of 10 NMR
* &#x20;Model B with a score of 0.02 and a stake of 5 NMR
* &#x20;Model C with a score of 0.03 and no stake

The stake-weighted average score for this round would be:

```
SWA score = ((0.01 * 10) + (0.02 * 5)) / (10 + 5) = 0.0167
```

Note that Model C is not included in the calculation because it is not staked.

## Rankings and Tiers

Participants in the Numerai tournament are recognized with titles that reflect their performance. At the conclusion of each season, once the final round is resolved, these titles are awarded based on the following tier system:

**Grandmasters** place first

**Masters** place in the top 10

**Experts** place in the top 100

**Researchers** place in the top third

**Contributors** place in the middle third

**Apprentices** place in the bottom third

**Novices** have not yet made 20 qualified submissions

Each participant can earn multiple titles, as titles are assigned based on independent scoring categories. For example, a participant may achieve the "Expert" title in one score of the tournament while being a "Researcher" in another.

## Qualification

Qualification for a Grandmasters season is based on active and consistent participation. You need to achieve **20 Qualified Rounds** to ensure placement in the season. A round is considered a **Qualified Round** when:

1. Your account has on-time submission(s) for the round
2. There is >= 1 NMR total at-risk across your models on-time submissions

For example if you maintain 1 NMR on a single model and make on-time submissions for 20 rounds (about 1 month), you will officially qualify for a season. Once you've met these criteria, you'll be considered for the season's ranking, where your performance will earn you a title. &#x20;

### Earning Your Place in the Season

* **Minimum Stake Threshold**: The cumulative at-risk stake across all your models must be at least 1 NMR for a round to count towards your 20 qualifying rounds. This threshold ensures that all qualifying participants are genuinely invested in the tournament's outcomes.
* **Qualified Round**: To qualify for a round, you must make on-time submissions with staked models that in total meet the minimum stake threshold.
* **Distinct Rounds**: To qualify for the season, you must make qualified submissions in 20 separate rounds throughout the season. These rounds can occur at any point during the season but must be unique; multiple submissions in the same round do not count toward this total.

Qualification for a Grandmasters season is based on active and consistent participation. Here’s what you need to know to ensure your spot:

### What's Next After Qualification

Once you've met these criteria, you'll be considered for the season's ranking, where your performance will earn you a title.

## Earned Titles

<figure><img src="https://lh7-us.googleusercontent.com/YmPbxNj7AsjPfPg6W-4Z7qifrG0BOoFqy-iXb0jjunPGWyeiwvb1O8Z0ekG_y-cLDuJrdiCyQKxz7ssOTFjqgQneW8Ek7l9EFHrC58qlUzGPdw-_asyB3ndm_sLkmaDJ4blJWV5RQqDqKq3T8gxY9I0" alt=""><figcaption></figcaption></figure>

Once you've earned a title, it will be displayed to celebrate your accomplishment:

* **Profile Highlight**: Your highest earned title will be visually represented by a colored border around your profile picture on the leaderboards. Each title corresponds to a specific color, making your achievements instantly recognizable.
* **Account Profile**: The title will also be featured on your account profile.
* **Detailed Insights**: Hover over your title to view a tooltip that provides detailed information about all the titles you've earned.
* **Discord Integration**: After earning a title and integrating your account with Discord, your highest earned title will be showcased on your Discord profile as a role.

## Discord Integration

Users can now integrate their Numerai accounts with their Discord account to receive roles that correspond to their Grandmasters titles.&#x20;

To connect your Discord account:

1. Navigate to your account profile and click the “Edit account profile”
2. Click the “Connect Discord account” button
3. You’ll be redirect to the Discord authorization page
4. Authorize the Numerai Discord bot, named ‘The Craibinator’, to link your account.

<img src="https://lh7-us.googleusercontent.com/_WDG-6YMi5LLgz3bjkKj3R0bYRCE3T6toeA8eskjgJJJgM-boH3xzfw_sMXpUpdCnVC7xDRhyvEiqpaeeF3EaLshmyXJOAVtuh7tBemQji5yhRot6lojzLu0II9abSINiaL1gxpyApaAMRZuzBb-Uco" alt="" data-size="original">

Once authorized, your Grandmasters titles will automatically appear as roles in your Discord account. Additionally, your Discord profile will be visible on your Numerai profile page, enhancing your presence in the community.

