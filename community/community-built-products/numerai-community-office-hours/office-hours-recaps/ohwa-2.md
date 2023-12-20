---
description: March 12, 2020 / Written by http://twitter.com/mandelliant
---

# OHwA S01E02

#### Office Hours with Arbitrage #2

Following the great Q\&A that came out of [his first office hours](https://medium.com/numerai/office-hours-with-arbitrage-1-aadc0ba4c53d), Arbitrage returned to answer more questions from the community about staking, finance, and [Numerai’s data science tournament](http://numer.ai/tournament) with special guest [Slyfox](https://numer.ai/slyfox) ([_Anson Chu_](https://twitter.com/ansonschu)_, CTO of Numerai_).

After a quick proof of credibility, Arbitrage dove into the questions from Slido.

![Pictured: proof of (school) work](https://cdn-images-1.medium.com/max/1600/1\*CKVV8SPnfpTEVXij-TI74Q.gif)

#### Questions from Slido

**Can you talk about the hyperparameter optimization you use, and the score you optimize for?**

Similar to Arbitrage’s three tips for performing well from [the first office hours](https://medium.com/numerai/office-hours-with-arbitrage-1-aadc0ba4c53d), he explained that he uses half of the training data and does a grid search for whichever model he’s using. Regarding score, Arbitrage checks to make sure his model doesn’t produce too strong of a signal as that likely means it’s overfit on the data.

> “In this close correlation environment, I want 4% — no higher than 4.5%.”

Though this has been the sweet spot for Arbitrage, he added, “your mileage may vary,” reiterating how important it is to avoid overfitting.

Once he feels confident a model is close to right, he trains on the entire training set to get exact parameters, noting that the parameters usually don’t change. Once he has that, he locks in the parameter space and adds in the validation data (132 eras at the time of recording). Arbitrage also noted that he has clones of his models that **don’t** look at validation, and is monitoring them to see how they perform long-term.

Arbitrage invited Slyfox to share his perspective:

![“I’m actually not qualified to answer this question.” — Slyfox](https://cdn-images-1.medium.com/max/1600/1\*Ygxztm8klrYt11YeVlhZnA.jpeg)

(Doing other fantastic work at Numerai, Mr. Fox doesn’t do much modeling.)

**I’d like to submit again on the past year data to save weeks of validation — even a little feedback, such as average rank, would be a great help. Is that nonsense?**

Arbitrage began by noting that the topic of historical performance frequently comes up during Numerai’s fireside chats ([like this one from ErasureCon 2019](https://www.youtube.com/watch?v=YojhLjLrG1M)).

> “You all have backtest data. It’s possible that you have some gaps where we could predict on something that doesn’t exist in the backtest but is former live data. It would be an out of sample validation. I don’t know how it would work in practice, but as long as it’s not in the backtest data, it **is** held out data and we could get some results on it. The problem is that those eras you’re looking at, in terms of average sample validation, are not like the current regime. If you fit to that, you’re going to get very bad results.”

![“This one I can answer!” — Slyfox](https://cdn-images-1.medium.com/max/1600/1\*8PrAdLMQRZ8NzVqHPr5G6g.jpeg)

Slyfox explained that this is something the team is actively exploring, citing again how frequently community members bring up their desire for historical data. Currently he’s investigating whether or not Numerai can release previously live data (live features and the targets) as something like a Validation 2 set specifically to give the data scientists feedback.

To Arbitrage’s point about previous data being part of a different regime, Slyfox said that’s exactly what they’re trying to figure out, adding, “I think it’s the future.”

Arbitrage wasn’t so sure:

> “The tendency to want to overfit to data; it’s **really** easy to fall into that trap. The way \[the tournament] is now, we’re so blind to everything that there is an element of luck. But with time, you do find some experience with the data like I found a range of correlation scores that works. If I had the opportunity to test my model \[against the Validation 2 set], I don’t think I would change anything. I don’t think it would benefit me and I’m not sure how it would benefit anyone else.”

Arbitrage mentioned that we’ve seen issues with overfitting in the tournament before, with some users hyper tuned on a specific set of eras and using multiple accounts to identify which eras are most like the current regime. “They’ll do well in the short term,” he said, “but if you were to lock those models in, they would be bottom performers.” Arbitrage expressed that he doesn’t want to keep modeling, preferring to model once, add that model to [Numerai Compute](https://docs.numer.ai/tournament/compute), and forget about it.

**Phorex (community member):** I never stop modelling.\
**Arbitrage:** More power to you.

Arbitrage went on to explain that the intention of the tournament is to have data scientists build models that generalize well, and that for Numerai, it’s more desirable for the models to be stable, with little change week to week. If the models were to change drastically, Numerai wouldn’t be able to rely on the backtests, adding, “It’s a risk.”

Slyfox agreed that the risk is present, but doesn’t want to discount the potential value in the availability of large sets of historic performance data over the long term, wondering how the tournament could benefit from this mechanism ten years (hypothetically) in the future.

> “Do we continue to hide that from you guys? Or do we give it out? I think it’s worth investigating.” — Slyfox

Slyfox then noted that as long as they keep a period that is truly out of sample, Numerai can evaluate a data scientist’s true out of sample performance which, from their perspective, is what matters most. Even if they do give out some of the live targets as Validation 2 data, Numerai would continue to retain a big chunk of the data as test data in order to maintain a good idea of how models are performing out of sample.

As Slyfox finished, Arbitrage noticed that Daily Scores were posted so he briefly paused to give everyone a chance to check their models.

![“Oh! We have a winner!” Arbitrage after a brief interlude to check Daily Scores](https://cdn-images-1.medium.com/max/1600/1\*2U79z6R4OWsoqGj71vddUg.gif)

**How extreme volatility in the global stock market is NOT translating directly into Numerai’s data scientists’ performance.**

“I talked to you guys about this in person,” Arbitrage said, “and I thought you were full of you-know-what.”

“This makes me have to eat crow.”

Arbitrage expected recent volatility in the global stock markets to have a dramatic impact on model performance, bringing up the idea of burn insurance he mentioned in [the first office hours](https://medium.com/numerai/office-hours-with-arbitrage-1-aadc0ba4c53d) but noting that he thinks it may be unnecessary based on the latest tournament results (at the time of recording).

In response, Slyfox said: “If this was back in the Bernie days, I think we would have problems, but the new Kazutsugi target, as [Richard](https://twitter.com/richardcraib) says, is much more stable and we are not that correlated with the overall markets — certainly not just the US \[market].” He then reiterated that the targets in the Numerai data are based on global markets, adding that they’re certainly not limited to longs only.

_Author’s note: Numerai names the targets in their data sets. The targets are Kazutsugi (current at the time of writing), preceded by Bernie, Charles, Elizabeth, Jordan, and Ken._

![Example Numerai data with the Kazutsugi target column at the far right.](https://cdn-images-1.medium.com/max/1600/1\*SuJW2eXvFLvNYRbUcCah7Q.png)

**How do users tune hyperparameters?**

[Michael P](https://numer.ai/master\_key) (Data Scientist at Numerai/coolguy) joined the video call to expand on the first question regarding tuning hyperparameters as a user, specifically what form of optimization to use and what score to optimize for.

Starting with what to optimize for, Michael said that for maximizing payouts, the data scientists are incentivized to optimize for mean correlation. He noted, however, that they do find it useful to optimize against something like a Sharpe ratio, taking the mean of a user’s error scores and dividing by the standard deviation of the era scores. This, he said, leads to much better consistency and lower risk (specifically out of sample).

Michael mentioned he would try to get boilerplate code for this optimization into the Numerai tournament [tips and tricks notebook](https://github.com/numerai/example-scripts/blob/master/analysis\_and\_tips.ipynb).

![From the tips and tricks notebook.](https://cdn-images-1.medium.com/max/1600/1\*L62AkvS4ACdtXI5YqfuW5g.png)

**Arbitrage to Michael: Now that you’ve had more time to look at the data and the users, have you noticed any interesting trends?**

Michael has been closely watching the meta-model contribution (MMC) scores, specifically to see how data scientists have changed their models [since Numerai made that announcement](https://docs.google.com/document/d/1z3WKnwvchbq67sw7JQ-Y46aJjwUFbHAnbdnjL6khxU8/edit?usp=sharing).

> “In the first week or two, people were changing their models to get away from these tree-based approaches, but lately it’s been converging on integration-test type models because MMC is encouraging that. I think there’s going to be a short term where it is more correct to go to these safer models, where everybody is doing good and MMC will discourage bad models. Once everyone converges on the easy approach, it will open up and start being more profitable to diverge from that and come up with more creative ideas.”

**Any thoughts about optimizing feature exposure methods?**

Arbitrage echoed his earlier point about being afraid of accidentally overfitting. “If you take Richard’s advice and treat the eras properly and not over sampling the data, you can control for that naturally.” Considering the [tournament leaderboard](https://numer.ai/tournament), Arbitrage noted that he hasn’t seen any model with lower than 8% exposure that’s also performing well.

Michael added that feature exposure is included because, in their research, the Numerai team has seen a strong correlation between low feature exposure and high performance on the leaderboard.

“But it’s not for free,” he said, “you can’t just post something with 0% feature exposure and expect it to perform, it all has to be going in the right direction. It suggests that the models are looking at something a lot deeper than just linear exposures. They’re more robust and don’t degrade as much over time.”

> “If you have two models that are close in performance but one has significantly lower feature exposure, you might want to consider using that one.”

Arbitrage pointed out that there are groups of features, and he would be interested to see how a meta-model based on an ensemble of multiple models, each trained a group of features, would perform. His suspicion is that it would overfit, but said he’s curious how it would perform.

Michael mentioned Numerai data scientist [Lack of Intelligence](https://numer.ai/lackofintelligence), who chose that name because they don’t use any of the intelligence features. He said that the features are grouped for a reason: they are related and not just randomly grouped. Arbitrage added that Richard told him it would be interesting to see users completely ignore a set of features, and if they still performed well, it would be very unique for the fact that it wasn’t looking at those features.

![Numerai data feature groups. Roll 2d10 to see which feature you overfit to.](https://cdn-images-1.medium.com/max/1600/1\*zGAz65FAJBLBUfhhcn7ddA.png)

**Arbitrage asks: how’s MMC coming along?**

**Slyfox:** “We’re still in the phase of analyzing how people are reacting to \[MMC] and doing internal research. We’re designing a payout structure for it, but we don’t want to rush it. The last few changes to the payout system stirred up backlash, so we want to do it right and we don’t mind taking it slow. We want to do the minimum amount of change, a 20% change for 80% of the effects.”

He gave the example of releasing the MMC scores without the payouts as a first step to get the data scientists thinking about MMC in the right way. “Similarly to multiple accounts,” he said, “where we loosened the rule before shipping the feature so we can get most of the benefit before we have to enact the change because we know every change is disruptive.”

“In short,” Slyfox concluded, “we’re definitely doing it but it’s not going to be soon.”

**Arbitrage asks: Michael mentioned an internal priority is moving multi-account to one account, any updates?**

Very proud of the name he came up with, Slyfox introduced ‘Single Account Multiple Models,” which Arbitrage dubbed, SAMM.

![Pictured: Numerai data scientist](https://cdn-images-1.medium.com/max/1600/1\*aRNr8nq8\_NVWMHFOKnc7aw.png)

Slyfox gave a shout out to Numerai team member [Patrick](https://twitter.com/pschork) who is taking the lead on this project, adding that it’s making good progress. From Slyfox’s perspective, there’s been an increase in new accounts created, which comes with the need to properly set up multi-factor authentication and IP verification (an admittedly cumbersome process). Slyfox and Patrick are both primarily focused on shipping SAMM so data scientists can easily manage multiple models “without going crazy,” as Slyfox said.

Michael added:

> “I kind of overlooked it at first but I think it’s a prerequisite for real MMC — the ability to experiment with different models without having to stake on them yet, but still getting MMC scores and seeing how correlated they are with the meta-model, is going to work in conjunction with MMC to create a better environment for iteration. That’s a big part of why it’s prioritized right now.”

**Arbitrage has a feature request for SAMM**

As someone managing six accounts already, Arbitrage expressed that he doesn’t have the time to create more. But, still wanting to take advantage of multiple accounts, suggested a feature to adjust the weight of different models within a SAMM account.

Arbitrage explained that a data scientist with two accounts could want to create a third account with the first model weighted 70% and the second model 30%, giving users a new vector for improving their performance without the need for starting accounts from scratch.

Slyfox had been down this road before, however, and had Richard’s counterpoint ready — would data scientists trust Numerai to blend their predictions correctly? Or would they not blend the predictions on their own before submitting a model to the competition?

“I think it would be a fun feature for the future,” he said, “but right now our focus is on the most basic case of making sure you all don’t have to keep logging out and back in.”

**Arbitrage asks: what’s the next step in the evolution of the data set?**

Arbitrage noted that there’s significantly more tournament data now, but the training data has remained the same, wondering, “when do you think that will flip?”

The next possible change to the tournament data sets Numerai is exploring internally is releasing more validation data- the Validation 2 data (historical live data) that Slyfox mentioned earlier in the discussion.

Alongside that, Slyfox said they continue to monitor the ever-growing test set to make sure it doesn’t push data scientists past memory limits. Following from that, one idea Slyfox mentioned is to explore different file formats such as HD5 or Parquet. Much of the Python tooling, like Pandas, already supports these file types and they’re faster to transfer and cheaper to compute.

If you’re passionate about finance, machine learning, or data science and you’re not competing in [the most challenging data science tournament in the world](https://numer.ai/tournament), take a minute to sign up.

Don’t miss the next Office Hours with Arbitrage: follow [Numerai on Twitter](http://twitter.com/numerai) or join the discussion on [Rocket.Chat](https://community.numer.ai/home) for the next time and date.

_Thank you to_ [_Arbitrage_](https://numer.ai/arbitrage) _for hosting Office Hours, and to Arbitrage,_ [_Slyfox_](https://numer.ai/slyfox)_, and_ [_Michael_](https://numer.ai/master\_key) _for collaborating on this post._
