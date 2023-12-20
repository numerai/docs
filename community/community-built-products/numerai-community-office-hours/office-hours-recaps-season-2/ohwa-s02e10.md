---
description: From August 13, 2020 / Suraj interview
---

# OHwA S02E10

For this episode, Arbitrage interviewed data scientist [Suraj P](https://numer.ai/surajp), who recently published a [guide to participating in the Numerai tournament](https://medium.com/@parmarsuraj99/a-guide-to-the-hardest-data-science-tournament-on-the-planet-748f46e83690).

![Great turnout for episode 10](<../../../../.gitbook/assets/everybody (1).png>)

Check out Suraj's interview on YouTube:

{% embed url="https://youtu.be/cYY-omNU0G4" %}

### Questions from Slido

**Which one is less wrong: `import torch stf` or `import tensorFlow as torch`?**

Resident neural net wizard [JRB](https://numer.ai/jrb) said both are pretty much equally wrong, a more optimal method would be `import jax.numpy as np`.

**When** [**Sorios**](https://numer.ai/sorios)**?**

One of the most mysterious users on the leaderboard, Sorios is often requested as a guest. Arbitrage reached out on [Rocket.Chat](https://community.numer.ai) to remind Sorios that the answer to [their Slido question](ohwa-s02e06.md#questions-from-slido) will be revealed once they attend an Office Hours.

**Considering that we are in a different regime (compared to the last time this question was asked), are you and/or the team happy with how MMC has turned out thus far?**

Arbitrage explained that he's staked six of his ten models on MMC + Corr, and he's mostly happy with that decision. "Only one model is hurting me, but overall I think it's been good," he said. MMC performance is highly dependent on how everyone else is doing, making it more unpredictable, but Arbitrage is going to stick with it.

From the team, [Mike P](https://numer.ai/master\_key) said that they're happy with how many people are using MMC. He added that he's overall really happy with MMC, but doesn't think the community will be as enthusiastic as he is because it's _very_ difficult to consistently perform well on MMC. "I think there's always going to be an air of confusion around 'why is it down?' and that bothers me a bit," Mike said, "But other than that, I'm happy with all of the usage and how it's working out."

**What kind of leaderboard do we want/need once reputation bonuses phase out?**

[Keno](https://numer.ai/wander) noted that with staked vs unstaked, and whether or not a model is staking on MMC, there are several different leaderboards which make it difficult to gauge a model's performance. Arbitrage's opinion is that, once the reputation bonuses phase out, there should only be one leaderboard that clearly shows a model's relative performance.

> "None of this sorted-by, or stake-weighted, no... If they set up a leaderboard based on correlation, we're going to chase correlation. I think the team should come up with an absolute measure of performance in the tournament that blends the metrics together and that's your leaderboard." - Arbitrage

**Why can't we stake on our account instead of individual models? Then it would be easier to change the percent of stake allocated to each model.**

[Slyfox](https://twitter.com/ansonschu) said that he likes the idea, but that we're a little far away from something like that happening. He explained that if a user wants a blend of their models, it would probably be better for them to blend the models first before submitting and then just staking on that.

Ultimately, Slyfox doesn't want Numerai to be responsible for blending or not blending user submissions correctly. He did note that he likes the idea of auto-balancing among different models and he wants to work on that, but it's not on the short-term product road map. "We have some low-hanging fruit to improve on first, like making the profile page better or making the diagnostic validation metrics better. We're probably going to work on those first."

**Do you foresee people going to use Numerai as their main source of income?**

Arbitrage definitely sees a future where that's possible for someone who _chooses_ to put in the time and effort to make their models a source of income. He added that once you have a profitable model, if you set up [Numerai Compute](https://docs.numer.ai/tournament/compute) you don't even have to worry about running your models every weekend.

**Slyfox:** I actually joined Numerai to make something so that I can not work and have an income eventually. My goal is to eventually become a user so I can fully automate and have a little piece of programming that makes money for me. We'll get there.

**Are Numerai employees allowed to actively participate in the tournament? Or are they only allowed to submit models created before hiring?**

[Mike P](https://numer.ai/master\_key) said that Numerai previously had a rule prohibiting team members from participating because of the potential to take reputation bonuses away from other users. With the rep bonus phasing out, it's less clear how employees being in the tournament effect other users; as Mike said, "there's no real victim in letting the employees actively participate," noting also that this is something they're discussing internally.

[Slyfox](https://twitter.com/ansonschu) added that if there were any data the Numerai team had access to which would result in better model performance, the first thing they would do is release that data to the tournament participants. As Slyfox explained, Numerai makes money when the meta-model predictions are accurate, so the incentives are aligned between the team and the data scientists. "There's nothing that we are trying to win from you," he said.

**How does Numerai analyze the ratio of rolling MMC rep? Is a model with rep 0.02 / MMC 0.02 more desirable than rep 0.04 / MMC 0.02 since the signal is more purely MMC?**

Eventually Mike P explained that the Corr + MMC rep is close to what would be an ideal model for Numerai. "It has this cool trade-off," Mike said, "where as you get a more unique model, it allows you to get higher MMC but it also makes it harder to get consistent correlation because you're deviating from what everyone thinks is the right model." The result is that it helps models stay balanced.

**Should I be afraid that when my model works well during this current regime, it no longer does when the regime changes?**

There's no way to tell until the regime changes.

> "Each regime should be completely different than the last because that's what a regime change is." - Arbitrage

Arbitrage added that if you're doing good cross-validation, your models will tend to do well regardless of regime. He said to "try to find your \[performance] in a band that's consistent across many eras."

**How do I filter out bad and good models early? What gives the least chance of overfitting?**

Arbitrage defines a bad model as one that's extremely volatile on the out of sample eras that you're judging. If you have too much drawdown or variation week to week, that may not be a good model. "It's really tough to say. You have ten slots \[for models], use them and try to gauge as time goes on... if the volatility is also really high on the live data, the model is probably not very good."

**Where is the new talent in the leaderboard? Which models will dominate the leaderboard in the near and far future?**

Arbitrage noted that one of his most recent models, [Arbitrage 3](https://numer.ai/arbitrage3), shot up on the leaderboard to around rank 70, adding that if any models have top 100 potential, around 20 weeks of performance on the live data is where that will begin to show.

Arbitrage suspects that in the near future, models that handle burn periods well will be the most performant (or the least non-performant): his era-boosting models are doing relatively well, but linear models (like [HB](https://numer.ai/hb) potentially) were getting hit hard.

**When do you interview yourself for Office Hours with Arbitrage? I would love to hear your top 3 tips.**

Arbitrage would love to, so stay tuned. There's also another Data Science Happy Hour in the works, and [NJ](https://twitter.com/tasha\_jade) will be a special guest on an upcoming episode.

_If you’re passionate about finance, machine learning, or data science and you’re not competing in_[ _the most challenging data science tournament in the world_](https://numer.ai/tournament)\_, what are you waiting for?

Don’t miss the next Office Hours with Arbitrage : follow\_[ _Numerai on Twitter_](http://twitter.com/numerai) _or join the discussion on_[ _Rocket.Chat_](https://community.numer.ai/home) \_for the next time and date.

Thank you to\_ [_JRB_](https://numer.ai/jrb)_,_ [_Mike P_](https://twitter.com/easymikep)_, and_ [_Slyfox_](https://twitter.com/ansonschu) _for contributing to answers during this Office Hours, to_ [_Suraj_](https://numer.ai/surajp) _for being interviewed and writing an awesome_ [_guide to the tournament_](https://medium.com/@parmarsuraj99/a-guide-to-the-hardest-data-science-tournament-on-the-planet-748f46e83690)_,_ _and to_ [_Arbitrage_](https://numer.ai/arbitrage) _for hosting._
