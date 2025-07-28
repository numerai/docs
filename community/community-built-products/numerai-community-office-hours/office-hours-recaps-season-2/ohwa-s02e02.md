---
description: From June 11, 2020 / Jason interview pt. II
---

# OHwA S02E02

Before diving in, Arbitrage and Keno discussed Keno's new model, [Inki](https://numer.ai/inki), that he's using to test staking on MMC and the timing of when stakes pay out. Keno concluded that if you increase a stake by Sunday, the added value will be reflected the following Thursday but won't be available for withdrawal for four subsequent weeks.

After welcoming new and returning guests of Office Hours, Arbitrage tackled the questions from Slido before bringing back the hair master Jason P to talk about the newly launched Numerai Signals beta.

### Questions from Slido

**Abr - what is your golf handicap?**

> "I'm actually not very good at golf." - Arbitrage

His golf group gives him 20 strokes to start ("And I don't think that's enough," he said). His score is over 100, but his goal is to break 100 this summer.

**Are linear models useful for Numerai? Didn't they mention that they neutralize user predictions before using them? Why not score us on those?**

Linear models are useful for the Numerai tournament and can be quite performant. However, they run the risk of being inconsistent week over week.

Numerai's neutralization process is a black box to the user base. [Michael Oliver](https://numer.ai/mdo) (graciously volunteered by [Slyfox](https://twitter.com/ansonschu)) explained that neutralization takes place on a per-era basis but fitting a model does not, so the neutralization process won't necessarily remove everything from a linear model. Linear models, he said, can be useful, but anecdotally the most successful models they've seen have been other varieties.

Against advice not to, Arbitrage speculated that some of the factors being picked up by the linear models are things like momentum, which happens to work well as a signal generator, and the market just left a high-momentum period where everything went up.

**From chat: frisbee golf is the real golf**

!["No"](../../../../.gitbook/assets/uncomfortable.png)

**Is the apprentice now the master?**

This question is referring to [Arbitrage's student](https://numer.ai/lawrence\_michael) who is a participant in the tournament. At the time of recording, their model was #10 on the leaderboard (_Author's note: at the time of writing, they had climbed to #8)._

Arbitrage said that he gave his students a possible method for devising a model for the tournament, and he thinks this student took his advice. He tells all of his students to divide the eras into subsets and train different models for each subset and then average across.

**Is the rep score of the top 100 models currently unusually high? Or are these fairly normal levels?**

Yes - they are unusually high and no, these are not normal levels.

Arbitrage thinks that, in a "perfect" tournament, half of the models would have a positive rep, the other half would be negative. There have been times, however, when nearly everyone on the leaderboard were all positive or negative.

**What is the rationale of linear models in Numerai? What makes them so special during these times?**

What makes linear models special is that they're picking up on some linear relationship. As Arbitrage explained, some coefficient has shown to be predictive, but he doesn't know why linear models have been particularly good at picking up on that recently.

**It's pretty embarrassing to earn NMR for a Correlation stake with negative MMC. Am I getting paid to make the meta-model worse?**

**Slyfox:** I think the answer is 'yes', you are. But it's also important that there's a game here you can play where doing well pays you, regardless of how you're impacting the meta-model. That's why MMC right now is not optimal.

**JRB:** Yeah MMC has a competitive element to it where Correlation does not.

**Arbitrage:** Correlation is independent of how you perform against other people, whereas MMC depends wholly on who your competition is. I'm also curious what [Sorios](https://numer.ai/sorios)' effect is. If you have a stake that big that's 10% of the entire staking pool and you have a model with high correlation, you're going to see positive MMC if it's stake-weighted.

**Slyfox:** The way that we calculate MMC gets rid if the big staker effect, if you read [Mike's formulation of it](https://forum.numer.ai/t/mmc2-announcement/93).

**Arb - are you going to do a video tutorial of the Numerai Classic tournament?**

Arbitrage has several video tutorials in the pipeline, but is working on finalizing his setup to make production a smooth process.

**Some models are earning insanely high MMC with scores that don't follow the correlation score but blast beyond it. Good for the hedge fund or too early to tell?**

Bor mentioned that with a lot of the linear models that have done well in the tournament, the MMC and correlation tend to follow each other. But lately he's seen models with extremely high MMC and low correlation. His follow-up question is, can we focus too much on MMC where it doesn't become useful anymore?

Slyfox's position is that more MMC is just straight up good.

![](../../../../.gitbook/assets/more.jpg)

Arbitrage asked if that's only the case with models with positive correlation. Slyfox explained that Numerai needs the models with high correlation as well because they need them to work alongside the high MMC models.

**Arbitrage:** Did you expect models to blow out the MMC score such as we've seen the last week?

**Slyfox:** I didn't do as much analysis as Mike P, but we talked about it earlier on. We expected the MMCs to be much higher. We started measuring MMC before we showed it on the website, and we knew that once we launched it the scores were going to go higher. We're not sure what to expect, but it's looking pretty good.

At this point, the remaining questions were focused on Numerai Signals. Before opening up the floor for questions, Arbitrage introduced someone who needs no introduction, Senior Developer Jason P who has been focused primarily on Signals for some time now.

### The second one where Arbitrage interviews Jason

Jason joined the Office Hours call mostly because of how much he likes Arbitrage but also to talk about Numerai Signals, the replacement for Erasure Quant, Numerai's other tournament. Unlike the Numerai Classic tournament, Quant required users to bring their own data to generate signals and was focused on individual equities, rather than encrypted data on the entire market.

Erasure Quant was written in such a way that it was incompatible with the Numerai data set and was based on the [Russel 3000](https://www.ftserussell.com/products/indices/russell-us) index, which Numerai doesn't really trade off. It made sense to bring the Quant data under the Numerai umbrella in some way and at that point it made sense to enable account sharing and wallet sharing (when staking is available).

![](../../../../.gitbook/assets/signals.png)

**Will there be limits on Numerai Signals rewards and burns?** **Not having clarity or estimates makes it hard to justify the time to submit again.**

Jason explained that they haven't settled on a final payouts scheme for Numerai Signals yet. He wants it to payout exactly like Quant did, which means 50 NMR per day based on the leaderboard, which is currently about the top 20 positions (though they may adjust that). It's not a long term solution, Jason said, but as a first pass it's not bad.

For now, Numerai Signals is still in beta, and Jason said will most likely remain in beta when payments launch because they'll almost certainly want to change and fine-tune how they work.

**If a stock is dropped from the Numerai Signals universe, you would just liquidate your position in that stock, right?**

Though they aren't trading based on Signals yet, Jason said that most likely what would happen when stocks drop out of the universe is that Numerai would rebalance their positions.

The concern is that if a Signals participant is long a stock for two weeks and it drops out of the universe two days later, the score is dead and the user is stuck with those dead numbers for the duration of their prediction set.

Jason explained that's why they always do daily returns. Everything on Signals is from one day's close to the next. There's special logic for handling situations where stocks drop out of the universe - they actually still live in the universe for an extra day.

**Any advice on how/where to score or model all 5000+ tickers in the Numerai Signals universe?** **Especially international markets.**

[Joakim](https://numer.ai/joakim\_arvidsson) expressed concern that aggregating all of the data he needs requires multiple (expensive) sources and was hoping someone might have suggestions to either reduce the computing overhead, amount of data pipeline he needs to oversee, or find alternative data sources.

Jason explained that the philosophy behind Signals is that Numerai wants people submitting predictions for things they're confident in, as opposed to building confidence in something for the sake of submitting it. "We don't need everyone to submit all 5,000 signals," Jason said (though there is currently a required minimum of 100 accepted tickers).

Arbitrage noted that, even though you might not be able to model all 5,000 tickers within Numerai Signals, if you can pick a market and build a robust model for that specific niche, it can be very strong.

**How do you know the universe of stocks for Numerai Signals?**

When you download the daily example file, it will show you the entire universe of tickers within Signals.

_The Erasure Quant revamp, called Numerai Signals, is in beta as of June 4, 2020. Check out_ [_Numerai Signals_](https://signals.numer.ai/tournament)_, read the_ [_Signals docs_](https://docs.numer.ai/numerai-signals/signals-overview)_, or join the conversation on_ [_Rocket.Chat_](https://community.numer.ai/channel/signals)_._

_If you’re passionate about finance, machine learning, or data science and you’re not competing in_[ _the most challenging data science tournament in the world_](https://numer.ai/tournament)\_, what are you waiting for?

Don’t miss the next Office Hours with Arbitrage : follow\_[ _Numerai on Twitter_](http://twitter.com/numerai) _or join the discussion on_[ _Rocket.Chat_](https://community.numer.ai/home) \_for the next time and date.

_Thank you to [_Joakim_](https://numer.ai/joakim\_arvidsson)_, [_Jason_](https://numer.ai/rockorun)_, and_ [_Michael Oliver_](http://numer.ai/mdo) _for contributing to answers during this Office Hours, to Jason P for agreeing to be interviewed (again), and to_ [_Arbitrage_](https://numer.ai/arbitrage) _for hosting._
