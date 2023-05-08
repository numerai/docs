---
description: From September 24, 2020 / Discussing Nomi with Michael Oliver
---

# OHwA S03E03

For episode three, [Michael Oliver](https://numer.ai/mdo) returned to discuss some of the initial results from [the tournament's new target, Nomi](https://forum.numer.ai/t/new-target-nomi-release/959/3?u=jrb).

![Michael Oliver pt III](../../../.gitbook/assets/mdo.png)

The full video of Michael Oliver's Nomi discussion will be uploaded to [YouTube](https://youtube.com/numerai).

### Questions from Slido

**Will the payout structure change once the Nomi targets are used as the live targets? If so, how?**

Michael Oliver explained that currently the team has no plans to change the payout structure. He teased that the team has some payout-related projects in the pipeline, but said ultimately the structure isn't likely to change.

**Why do you force a probability distribution? Why not have five (or more) bins and let the targets fall where they may?**

This is done partially to keep the signal as stationary as possible. The bins, especially the tail bins, would have to be unlimited width. "It's tricky to get bins that would work across time, for every era" Michael Oliver said, "so we're forcing the bins to be the same size across eras."

**Is the method used to generate target Kazutsugi the same as that used for Nomi? If so, how can we compare head to head?**

It's the same method, just with a different target distribution.

**When live metrics?**

"Right now we're keeping that data at part of our test set, so if we were to give you metrics on that, it would be leaking data," Michael Oliver explained, "so this is not really something that's in the works right now."

**What is the derivation of Nomi? Is it Chef Nomi?**

> "Google all of the previous target names and you'll see a pattern." - Michael Oliver

**Are there reasons why the validation data can’t walk forward in time as we move forward each week? I think it would help users formulate new hypotheses as we move through time instead of training and validating on the same data each week over and over.**

Having a stable test set makes it much easier for the Numerai team to do research on model performance and effectiveness. Michael Oliver said that if there were to be any changes, they would likely be something similar to a test set of secret data for users to get performance metrics on.

Michael Oliver added that giving us new data each week would incentivize users to retrain their models every week, "and it would be kind of a mess, I think."

**If a Nomi-trained model is better than a Kazutsugi-trained model at predicting Kazutsugi targets, but worse at predicting Nomi targets, what might be the reason(s)?**

"If the target has more signal in it," Michael Oliver said, "it'll predict better on a more regularized target." He explained that Kazutsugi is an easier target, and a model that's trained with more signal will find more signal and predict better on an easier target.

**Why do you try to change the Kazutsugi to Nomi? Is it based on the investment strategy of Numerai?**

As Michael Oliver explained earlier in the episode and in the [Nomi announcement](https://forum.numer.ai/t/new-target-nomi-release/959/3?u=jrb), the new target is designed to improve the fund's investment performance. "We care about the extremes of your predictions," he said, "so having a target that better captures those extremes is useful."

**In my neural net model, target Nomi still doesn’t work, the performance even goes down. Is this target only valid for tree models?**

Michael Oliver explained that one of the reasons tree-based models are so popular is because they work out of the box. Neural nets require a lot of additional tuning in order to train properly. "There's no good out of the box neural networks that are going to work all the time," Michael Oliver said.

**When more slots?**

Michael Oliver said that the 10 model slot limit hasn't been discussed internally that he's aware of, and he and Arbitrage encouraged discussing this topic in the upcoming fireside chat.

**When the final files with the Nomi target are available on the API, will the target\_kazutsugi column remain there or will it be completely gone?**

Michael Oliver said he imagines they will remove the target\_kazutsugi column from the set and are considering renaming the column to just **target** rather than **target\_nomi.**

**So today’s results showed that my Nomi-trained model performed strictly worse.**

Arbitrage empathizes because his day one results also were lower than his Kazutsugi-trained models, but he said that one day's results alone are far from a trend and was looking forward to seeing how things looked with a week's worth of data.

Michael Oliver added that the only real way to compare performance is to have the exact same model but trained on each set of data because the overall trend was going down for most users.

_If you’re passionate about finance, machine learning, or data science and you’re not competing in_[ _the most challenging data science tournament in the world_](https://numer.ai/tournament)\_, what are you waiting for?

Don’t miss the next Office Hours with Arbitrage : follow\_[ _Numerai on Twitter_](http://twitter.com/numerai) _or join the discussion on_[ _Rocket.Chat_](https://community.numer.ai/home) \_for the next time and date.

Thank you to\_ [_Michael Oliver_](https://numer.ai/mdo) _for talking about Nomi (again), to_ [_Wigglemuse_](https://numer.ai/wigglemuse) _and_ [_Joakim_](https://numer.ai/joakim\_arvidsson) _for contributing to this week's discussion,_ _and to_ [_Arbitrage_](https://numer.ai/arbitrage) _for hosting._

\*\*\*\*
