---
description: 'From August 6, 2020 / Wigglemuse interview'
---

# OHwA S02E09

For this, the ninth episode of season two, Arbitrage interviewed longtime tournament participant and [Rocket.Chat](https://community.numer.ai) all-start [Wigglemuse](https://numer.ai/wigglemuse).

![Wigglemuse gets the center square, the Square of Honor](../../.gitbook/assets/wigglemuse.png)

The full interview with Wigglemuse will be published on YouTube.

### Questions from Slido

**When** [**NJ**](https://twitter.com/tasha_jade)**?**

Thanks to the overwhelming crowd response, NJ agreed to come on Office Hours as a guest on August 27th, "assuming nothing groundbreaking with the tournament happens between now and then," she said.

**Arbitrage:** Does that mean there's something coming?? 

**NJ:** No.

**Arbitrage:** I tried 🤷♂ 

**Assuming a reasonably fit model, how much extra performance can one expect from training on validation? Is it even worth it?**

Arbitrage used his [Arbitrage 2](https://numer.ai/arbitrage2) as an example, which only saw the first 120 eras and performs relatively well on the live data. The question is asking if Arbitrage were to take that model with the same parameters, settings, and configurations but add the remaining eras, will it perform better?

Arbitrage explained that he and [Themicon](https://numer.ai/themicon) do something very similar. They look at eras 1 - 132 and noticed that they have a small amount of additional variance compared to similar models trained on eras 1 - 120 \(although Themicon noted that during the ongoing round at the time of recording, his model trained on validation was outperforming those that were not\).

Ultimately, whether or not training a model on the additional data will improve that model's performance is dependent on the current regime.

**How have the new accounts been performing? Does it look like more experimentation is happening or is it just the same, more or less?**

Since [accounts were expanded to support up to ten models](https://forum.numer.ai/t/announcing-general-availability-of-multi-model-account-support-for-all-users/399), [Michael Oliver](https://numer.ai/mdo) noted that generally tournament health has improved and there's slightly more variance among models.

**Michael Oliver:** There are some weird models that people submit. I'm not even sure that they're training these models; they're just transforms of the data. I clearly don't think that's a good idea... As Mike P is always telling people, just because something is unique, doesn't mean it's good. We want different **and** good. There are infinite ways to be different and bad, and so we don't want those models. Stake weighting still seems to be working quite well, there's been a good feedback loop.

When asked about the changes to the meta-model the team has mentioned, Michael Oliver explained that they implemented a change, but it wasn't nearly as drastic as they originally anticipated.

**What's a good value for feature exposure?** 

Arbitrage the person shared that [Arbitrage the model](https://numer.ai/arbitrage) has a feature exposure of 0.923 \(_Author's note: for comparison, my model is rank 623 at the time of writing and has a feature exposure of 0.0754\)._ Michael Oliver shared some of his feature exposures: [MDO](https://numer.ai/mdo) = 0.0855, [NMRO](https://numer.ai/nmro) = 0.0823, [NIAM](https://numer.ai/niam) = 0.076.

Michael Oliver said that if your feature exposure is too high, you'll have more variance, and if it's too low your model will have too low of a mean. He added that if you're interested in feature exposure, look at the distribution of your scores and find your maximum feature exposure. "Each feature exposure is a risk," Michael Oliver said, "and if you still have some very high risks, that might get covered up by other ones you're low on."

**Will a shift come soon?**

Assuming a shift refers to a burn period, Arbitrage said that he believes that at the time of this episode, it was already beginning. This was anecdotally based on his performance trending downward over the previous 20 weeks and suddenly changing, suggesting that a regime change took place.

**Are the scores we see on the tournament website a day older than we realized? Are Wednesday's scores from Monday's market close?**

Numerai software engineer Jason confirmed that Wednesday's finish is Monday's close, and Thursday is Monday close through Tuesday close.

_If you’re passionate about finance, machine learning, or data science and you’re not competing in_[ _the most challenging data science tournament in the world_](https://numer.ai/tournament)_, what are you waiting for?  
  
Don’t miss the next Office Hours with Arbitrage : follow_[ _Numerai on Twitter_](http://twitter.com/numerai) _or join the discussion on_[ _Rocket.Chat_](https://community.numer.ai/home) _for the next time and date.  
  
Thank you to_ [_Michael Oliver_](https://numer.ai/mdo)_,_ [_Themicon_](https://numer.ai/themicon)_, and_ [_Wigglemuse_](https://numer.ai/wigglemuse) _for contributing to answers during this Office Hours, to Wigglemuse for being interviewed and his presence in_ [_Rocket.Chat_](https://community.numer.ai)_,_ _and to_ [_Arbitrage_](https://numer.ai/arbitrage) _for hosting._



