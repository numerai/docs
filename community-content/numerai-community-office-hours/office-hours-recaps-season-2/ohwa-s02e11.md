---
description: From August 20, 2020 / Carlo Lepelaars interview
---

# OHwA S02E11

On episode 11, Arbitrage interviewed Carlo Lepelaars who recently wrote a [guide to competing in the Numerai tournament](https://app.wandb.ai/carlolepelaars/numerai\_tutorial/reports/Build-the-World-s-Open-Hedge-Fund-by-Modeling-the-Stock-Market--VmlldzoxODU0NTQ).

![Carlo in the hot seat on Arbitrage's right](../../../.gitbook/assets/Carlo.png)

Check out the full interview with Carlo [on YouTube](https://www.youtube.com/channel/UCQt3RVSKsDpFgYIm1A-nWbA).

{% embed url="https://youtu.be/5j6Nf1s:tTU" %}

### Questions from Slido

**When** [**Sorios**](https://numer.ai/sorios)**?**

Another request from the community for Sorios to join Office Hours. Sorios, if you're reading, slide into Arbitrage's DMs, he would love to have you as a guest.

**Carlo - would you please share some insights on how you choose and decide between abstraction and elaboration while writing?**

Carlo admitted that one of his biggest challenges while writing is wanting to include as many small details as possible, but he knows that wouldn't make for coherent posts.

> "What I do is write everything down and truncate it from there." - Carlo

**What if the team use all previous submissions and their metrics to model the relationship between submission stats and live performance and to suggest improvements?**

[Michael Oliver](https://numer.ai/mdo) said that it's technically possible, but the team is definitely not going to give tournament participants any metrics from Numerai's backtesting. Doing so would run the risk of inadvertently leaking information about the test data. He added that they are working on adding new submission metrics based on the validation data, and these should be available soon, saying "obviously these will only be valid if you're not training on your validation data."

Michael Oliver concluded by saying that he doesn't think data scientists need to train on the validation set and it's probably better used for hypervalidation of different parameters or techniques.

Arbitrage added that any suggestions for improvement from Numerai would also introduce bias and would lead to models being overfit to the data.

**Which is the metric (or combination of several) that we should optimize for?**

"There is no one metric to rule them all," Arbitrage said, "you should consider several." Arbitrage suggested that given accounts can have up to ten models, try optimizing different models for different metrics. He said different people are going to have different techniques and different metrics they optimize for, adding "don't just chase high correlation- I think that's risky."

**Can the team elaborate on how predictions are combined? Have you gone from simple averaging to stacking or some sort of IPW?**

Without divulging too much, Michael Oliver said that they're not doing anything particularly complicated when combining predictions, adding that it's still stake-weighted.

**How can I start staking? Any video tutorials?**

🎥 Coming soon 🎥

Arbitrage is working on video tutorials and is close to publishing the first, so stay tuned. Some will be short videos covering the basics, others will be longer tackling different aspects of the [tips and tricks](https://github.com/numerai/example-scripts/blob/master/analysis\_and\_tips.ipynb) notebook.

_If you’re passionate about finance, machine learning, or data science and you’re not competing in_[ _the most challenging data science tournament in the world_](https://numer.ai/tournament)\_, what are you waiting for?

Don’t miss the next Office Hours with Arbitrage : follow\_[ _Numerai on Twitter_](http://twitter.com/numerai) _or join the discussion on_[ _Rocket.Chat_](https://community.numer.ai/home) \_for the next time and date.

_Thank you to [_Michael Oliver_](https://numer.ai/mdo) _for contributing to answers during this Office Hours, to Carlo for being interviewed and writing an awesome_ [_guide to the tournament_](https://app.wandb.ai/carlolepelaars/numerai\_tutorial/reports/Build-the-World-s-Open-Hedge-Fund-by-Modeling-the-Stock-Market--VmlldzoxODU0NTQ)_, _and to_ [_Arbitrage_](https://numer.ai/arbitrage) _for hosting._

\*\*\*\*
