---
description: April 16, 2020 / Interview with ZEN
---

# OHwA S01E07

#### Office Hours with Arbitrage #7

Kicking off number seven, Arbitrage welcomed data scientist [Zen](https://numer.ai/nasdaqjockey) to his first ever Office Hours.

![The usual suspects](https://cdn-images-1.medium.com/max/1600/1\*5mFEJCqAr7UEpumvkmUhKg.jpeg)

**Arbitrage:** So I’m going to just open right with you because I imagine we’re going to have so much to talk about afterwards, I’d hate to run out of time.

**Zen:** Okay. How long is this?

**Arbitrage:** I run an hour, I stop right on time.

#### The one where Arbitrage interviews Zen and goes over his one-hour limit

**Arbitrage:** Zen is one of our older users. Not in age, but in account age.

**Zen:** Both!

**Arbitrage:** You say both, but I can’t tell. You could have an AI running your Zoom right now — we don’t know. So you have three accounts, which one do you consider to be your number one account?

**Zen**: Oh well obviously [Nasdaq Jockey](https://numer.ai/nasdaqjockey).

**Arbitrage:** How did that name come to be?

**Zen:** I’ve had that handle for a long time on Yahoo (I trade stocks). I just made it up. The second model is [Evolvz](https://numer.ai/evolvz). That one started out with genetic algorithms, so that’s why I named it \[that]. And actually, the first model I ever put up was [ZBrain](https://numer.ai/zbrain).

**Arbitrage:** Ah well then technically ZBrain would be your OG handle for this tournament.

**Zen:** Oh yeah, that’s right, that was back in 2016.

**Arbitrage:** How did you find out about Numerai?

**Zen:** A friend of mine read a Medium article and said, ‘hey maybe you should go look at this.’ So I did and then hopped on.

**Arbitrage:** You just said you joined in 2016, do you know the start date of your first account?

**Zen:** Yeah it was December 12.

**Arbitrage:** In 2016?

**Zen:** 2016.

**Arbitrage:** Okay so a little after the first wave, but still early on. And we’ve established now that you live in New York, or at least the New York area.

**Zen:** New Jersey.

![True New Jersey priorities](https://cdn-images-1.medium.com/max/1600/1\*e\_ifPfiMrZaybfi0KEu\_xA.jpeg)

**Arbitrage:** New Jersey, yeah like I said New York area basically. What do you do for a living?

**Zen:** I’m a software engineer by trade, but I’ve had a pretty long career and ended up working mostly in defense. Eventually I became a manager, then a senior manager, took a few buyouts here and there. I’ve kind of come full circle: now I work for a company and I lead the AI department. I do a lot of hands on work too.

**Arbitrage:** What programming language do you use and why?

**Zen:** I use Python. I’m self taught, started a few years ago. I actually used Python maybe ten years ago for various little things when it was easier to use something that already existed. But I’ve used just about every language on the planet. Right now everything I do for Numerai is in Python.

**Arbitrage:** I’ve generally found that to be true. [Except Bor who likes to cut his wild streak and run his own way.](https://medium.com/numerai/office-hours-with-arbitrage-5-421ea23f4eec) But I imagine he’s going to switch to Python, he talked a lot about the simplicity.

**Zen:** Bor is \[running] R?

**Bor:** I’m using [Clojure](https://clojure.org/).

**Zen:** Very cool. I’m a Python lover, actually. I’ve used just about every language, but Python is great for just getting things done quickly. Maybe not speed, but some things are still good.

**Arbitrage:** Python wasn’t really fast until, what, 2015?

**Zen:** Yeah, absolutely. In the beginning it was very slow.

**Arbitrage:** In your opinion, do you think that was a Moore’s law contribution? Or do you think we just got better at compiling this stuff?

**Zen:** I think they got a lot better, and with that they’ve done on the backend … I read a little bit about it, but I think they’ve done quite a lot of work to make the core libraries run really fast. It depends what you do and how you do things now.

**Arbitrage:** Oh for sure. I saw [a tweet](https://twitter.com/gvanrossum/status/1249001227972558848) by Guido \[van Rossum] and he was saying that people who are used to old-style Python should just ignore everything data science is doing. It seems like the data science community has almost “forked” Python for our own use. One of the questions that I have to ask, because you’re the legendary Nasdaq Jockey: can you tell us your top three tips for the tournament?

**Zen:** Ha, well, let me think about that. I think the biggest problem most people have is they over-train still, even though they think they’re not.They’re training too much on the initial \[data set], and if they’re using the Validation data they’re screwing themselves.

**Zen:** I don’t use the Validation data, and I try very hard not to over-train. I do a lot of things to make sure I don’t.

**Arbitrage:** Alright, so that’s one tip.

**Zen:** Consistency across the validation eras is important. There’s a couple of them that are really tough to get on, and that’s what Nasdaq Jockey does. It might not be so great at some of the eras in the validation data, but it’s really good on a couple of the tough ones. I’m looking forward to that new \[[Validation 2](https://medium.com/numerai/office-hours-with-arbitrage-4-2c5da71ef40)] data because now I’m interested in seeing how I’m going to have to change what I do to tune to the new Validation data set.

**Arbitrage:** I’m going to ask you more about that in a second, but I’m still waiting on tip #3.

**Zen:** One of the things that screwed me up in the beginning was that I didn’t keep good records of when I made changes of things. It takes so long to know how your model is doing. Just keep good records and go back and make small tweaks, not trying to make gigantic changes all the time (like changing states or models). I haven’t changed Nasdaq Jockey in a long time. With ZBrain I’ve been fooling around, but \[Nasdaq Jockey] I haven’t changed in a long time.

**Arbitrage:** Yeah, I haven’t changed anything with my Arbitrage account in maybe 18 months, beyond getting it adjusted for the different features. It’s done pretty well. Going back, you said of the new Validation data that you’re going to change a lot of stuff. But if your model’s doing well now, why would you change anything?

**Zen:** Well I’m probably not going to change anything with Nasdaq Jockey, but I have seven other Nasdaq Jockeys that I started three or four weeks ago.

**Arbitrage:** That was another question, if you’re up to ten accounts now.

**Zen:** Yeah, I have the three initial ones, and I just made about a month ago seven more. And they’re totally different. A whole different idea. I think they’re looking pretty good, actually.

**Arbitrage:** Yeah, these have been some pretty easy eras lately, so I’m waiting with bated breath to see how this all turns out.

**Zen:** Yeah, exactly.

**Arbitrage:** One of the questions I like to ask people: who is your favorite team member?

**Zen:** It’s gotta be [Anson](https://twitter.com/ansonschu).

![This is the second vote for Slyfox, Numerai CTO](https://cdn-images-1.medium.com/max/1600/1\*9xqKgvKPSBRlBJrSb9e\_Iw.gif)

**Zen:** \*Laughing\* I don’t really have a favorite.

**Arbitrage:** But you finally picked one!

**Zen:** He’s the only one I talk to.

**Slyfox:** Yesss.

**Arbitrage:** There ya go, Slyfox.

**Zen:** I was in Pittsburgh and saw a bar called ‘Sly Fox.’

**Slyfox:** You should share the picture if you still have it.

**Arbitrage:** We should have the East Coast meetup at the bar.

![Sly Fox Taphouse in Pittsburgh](https://cdn-images-1.medium.com/max/1600/1\*Iaivi01ezcnS0zz4OOCmpw.jpeg)

**Zen:** I don’t go to Pittsburgh very often.

**Arbitrage:** Let’s hope we’ll be able to go to Pittsburgh, let alone worry about going very often… What is your number one feature request or improvement you’d like to see for the tournament?

**Zen:** I don’t have a big rig or anything, I have an Alienware that I bought five years ago and I do everything on that. I wish the files were smaller. Not the number of records, I think that’s fine, it’s just that there’s so much waste. You can reduce that file size and make it 25% of what it is and still have all of the same features and data. I don’t know if \[Numerai’s] looked at that, it just seems pretty wasteful. It’s time consuming and a pain in the ass.

**Arbitrage:** That’s good, and I think that’s something Slyfox has talked about in the past as something they’d like to iterate on. It comes out of the box ‘float64’ and it could easily be reduced from there.

**Zen:** I mean really, there’s five targets, you can use zero through four if you want. Then right there off the bat you’ll get a tremendous \[improvement]. You can even make it a binary file if you want — I’m old school.

**Slyfox:** Yeah for sure. It’s something we’re looking into. File size is also something that makes everything we do slower, internally. So yeah, we’re definitely looking into it. Good recommendation.

**Zen:** Otherwise, I think the whole [layout of the tournament](https://numer.ai/) with the leaderboard and MMC; it’s all good, it’s just very convoluted right now. It’s hard to tell what we’re going to end up with. You’re setting an objective function for the company — that’s the way I look at it.

It’s like, their objective is to get the best models so that they can create a good metamodel. So they’re tweaking all of our rewards so we give them what they want. I think it’s working, at least it seems to be working. It’s hard to tell. I didn’t like [the answer the other day](https://medium.com/numerai/office-hours-with-arbitrage-6-f0171c6d4c81) when \[Richard] said that he’s okay when people want to stake on the example model. I don’t know, that kind of seemed odd to me.

**Arbitrage:** I was kind of irked by that too, but if you take a huge step back and think about it, the way it was answered made sense.

**Zen:** I know it makes sense.

**Arbitrage:** It is in the sense that it’s a zero-effort way to climb the leaderboard. I don’t like that because I want people to struggle as much as I did and so I want the path to be as difficult and onerous as possible so they don’t inadvertently surpass me, but I digress.

![Learning data science](https://cdn-images-1.medium.com/max/1600/1\*Tnoo\_hN9H7ymZWOqTZJWxw.jpeg)

**Zen:** I understand. I mean, it’s a competition, so you’ve got to have your own secret sauce so you can beat the other guys, but there’s a certain amount of collaboration we’re all doing (to a certain level).

**Arbitrage:** Agreed. I know this is your first Office Hours, but there’s this section of the process in this Zoom series where we talk about some stuff, but don’t really say anything at all. And I think that’s the collaboration you might be referring to. So you said you’re up to ten models, eight total variations of Nasdaq Jockey — why didn’t you go for ZBrain or Evolvz and try something with those?

**Zen:** Actually, at this point, they’re all similar. Well, the first three \[Nasdaq Jockey, Evolvz, ZBrain] are similar, but the new seven are very different. Just because they’re the same name doesn’t mean they’re the same model. I keep track of everything that’s going on, but [Nasdaq Jockey 1](https://numer.ai/nasdaqjockey1) has _nothing_ to do with Nasdaq Jockey. Totally different. One through seven are all different.

**Arbitrage:** Interesting. For me, I actually do use the numbers, they mean something.

**Zen:** I wish I had started out like that, and just used Google accounts like that. I can’t wait for single sign-in.

**Arbitrage:** Yeah, SAMM \[**S**ingle **A**ccount **M**ultiple **M**odels] — we’re all anxiously awaiting that. That’ll definitely be good. So, you have pretty good confidence in your models: are you staking evenly across them, or do you still favor Nasdaq Jockey?

**Zen:** About every three months I look at the performance and I weight the staking to the best model. I have more on Nasdaq Jockey, less on Evolvz, and even less on ZBrain.

**Arbitrage:** Yeah personally I look at the approach I took to arriving at that model. If I think it has the best justification from a design standpoint — I came at it with a scientific approach and came to a conclusion that makes sense — I can believe in that a little more than something I cobbled together by chance.

**Zen:** I just look at the stripped-down performance, not the bonuses, just how well did it really perform on the live data. That’s number 1 for me on staking. I don’t have the other seven staked yet, I have to transfer some NMR there.

**Arbitrage:** Yeah, I’m waiting to see a little bit before I stake on some of the new ones. In the end, I probably will, but I doubt I’ll stake very large.

**From chat: Do we get to rename accounts with the new merger?**

**Slyfox (in chat):** Eventually yes. The username is pretty embedded in a few places (leaderboard, profile page, internal code) etc so it will take a bit of time, but eventually yes.

**Slyfox (in meatspace):** Another question I’m thinking about is, “what can we build to help you guys track your changes better?” Keno had a lot of good suggestions here, and ideas for somehow letting you label your models in time. If you guys have any ideas how we can make that easier, that’s something we can also build. At the simplest level, letting you change your name might help.

**Arbitrage:** Yeah, I don’t know. I’m kind of a fan of stickiness. My account is Arbitrage and has been since June of 2016. I don’t want to change that, I want it to stay nice and stable. I guess I’m old school in that sense. You change your profile picture, but your username to me is a fixed thing. It’s tied to the blockchain too, in a way.

**Slyfox:** It used to be tied to the blockchain. Right now, it is not. The new set of staking contracts are only tied to your Ethereum address.

**Arbitrage:** Well Zen, or Nasdaq Jockey… I’m going to call you Nasdaq Jockey because that’s who I want to beat. Thank you for coming in today and answering some of my questions.

**Zen:** Hey, no problem.

**Arbitrage:** It was really helpful. There is a theme, I’ve noticed, with a lot of the people talking about avoiding overfitting, make sure you average across the eras, and also take good notes. That was [Bor’s number one suggestion](https://medium.com/numerai/office-hours-with-arbitrage-5-421ea23f4eec): good note taking. You can see that that’s consistent across users at the top of the leaderboard. I’m really excited about the questions today, because this first one, I’ve thought about for a while.

#### Questions from Slido

**Pretend I’m a five year old: explain exactly how MMC2 works (asking for a friend).**

> “I’m not sure I’m going to do a good job, but I’m gonna give it hell.” — Arbitrage

Banking on the fact that most people have played some team sport by age five, Arbitrage set up the following analogy: If you play a team sport, not everybody can be the pitcher (in baseball). Sometimes the team needs an outfielder, an infielder, pitcher, catcher, people who are really good at handling left-handed pitchers, etc. In the end, it takes all of the varied skill sets coming together to achieve victory for the team.

Extrapolating that example to the Numerai tournament: if all of the data scientists competing were pitchers, then the meta model would be terrible. But if we had a bunch of unique skillsets and played as a team, then we can win.

[NJ](https://twitter.com/tasha\_jade) shared that Michael P used a similar explanation at Numerai HQ in the past (although Numerai engineer Jason didn’t quite agree).

Michael P’s controversial example opted for a basketball team with four Shaquille O’Neals (one of the most dominant players ever but with a specific skill set) and posed the question: would that team be better off with a fifth Shaq or literally any other player with a different skill set (even if that player isn’t as talented). Slyfox and Arbitrage were quick to side with Jason and draft Shaq #5.

!["Data science is not a singular act, but a habit. You are what you repeatedly do.” — Shaq Craib](https://cdn-images-1.medium.com/max/1600/1\*VI3pOE7BdZhWTnUE2iwWDA.jpeg)

_Author’s note: Michael P’s basketball reputation dropped to -0.0547_

Slyfox tried his hand at an explanation, also choosing a basketball analogy in the form of the plus-minus score. When someone evaluates an athlete’s performance, they can look at their individual stats (like points scored, plays made, etc). But, you can also statistically measure how well the team does when that player is on the court compared to when they’re on the bench. If you play fantasy sports, this kind of scoring is already popular. “To me, MMC is just plus-minus,” Slyfox said. “Does the team perform better with you in it or not?”

“But what if you **are** the team?” Arbitrage asked.

![Slyfox was not ready for that](https://cdn-images-1.medium.com/max/1600/1\*nSxlefwP9lJCu-FeeS0COA.gif)

“In the case of my model,” Arbitrage explained, “I submit predictions on Saturday afternoon. And then the meta model is built after that. So if the meta model converges on the solution that I’ve already uploaded, I don’t get an MMC bonus.”

**Michael P:** Yeah.

**Arbitrage:** Yeah.

**Slyfox:** Well, you’re not helping.

**Arbitrage:** But I came first — you guys took my solution and now you’re not paying me for it.

**Slyfox:** We don’t want to give people too much advantage for just being first. I think that’s one of the problems we had with originality (if you’ve been here for long enough).

**Arbitrage:** Well wait a sec — it’s unlikely that I could predict with very high certainty the exact solution of the meta model. It’s the sum of hundreds and hundreds of other models. But the fact that I did, and my model existed in the top 20 for two and a half months suggests that it’s good and it validates the meta model itself. Yet I’m not getting any MMC for it because of the way that it’s designed.

**Slyfox:** When we’re designing this payout, we still want to reward you for being good, but we’re not going to reward you because you didn’t add anything to the team.

**Arbitrage:** I am the team. That’s what I’m saying: I’m the team, I came first, and you just stumbled into my solution.

**Slyfox:** The timing of it doesn’t really matter, but yeah.

**Arbitrage:** I’m just playing a little semantic game, but I’m sure I’m not the only one who encounters this problem. Just something to think about. I won’t be playing MMC because I have no incentive to, but I feel like if I am providing you the signal first, and then you stumble into my solution as the optimal one, well I think I should get something for that. Especially if other people are getting a larger piece of the proverbial pie just because they’re different. If I’m the only one complaining about it, well clearly you’re going to ignore me, but I bring it up because it’s an interesting problem that I’m thinking about.

**Michael P:** Say that you’re the meta model. Now, when other people are playing MMC, in order to have positive rewards they have to be pulling the meta model in a better direction: they have to be better than the meta model. You can’t get good MMC just for being unique if you’re doing worse than the meta model. To get long term expected benefits from it, your model has to be better than the meta model.

If you do have the meta model, if you have the best possible model, and the meta model is better than what anyone else could come up with, then no one will be making money on MMC anyway and everyone would just play the main tournament. MMC was designed to remove those inefficiencies and accelerate the progress towards the best meta model. So if you truly have the best model and the MMC was the best, no one would be playing MMC.

**Arbitrage:** Just a note since this gets summarized and put on the web: I’m not claiming that I have the best model, it’s apparent that I don’t because I’m not number one now and I’ve only been number one for a couple of days. Just wanted to make sure I clarified that a bit.

**You said that you use Validation for training after having applied cross validation properly. Are you planning to use the Validation 2 data for training also?**

Arbitrage felt that his model is performing well at the moment, expressing that he mostly hopes Validation 2 doesn’t change his data pipeline, forcing him to go through his code and remove the new data.

Arbitrage doesn’t plan to change anything with his current models — at least at first. Using his remaining account slots, he’s going to train new models on the Validation 2 data and track their performance long-term. “I’m not changing my main models at all,” he said, “they’re really good and they’ve been good for a long time. And I am the meta model.”

**Regarding payouts: when do you (or anyone) think they will stabilize? How far are we from a fair payout system?**

> “When do I think it will stabilize? Never.” — Arbitrage

Because the tournament deals with stock market data, Arbitrage doesn’t believe that it will ever truly “stabilize,” adding that “the second we think we arrive at a fair solution, everybody’s all in, some kind of regime change will occur and blow up our models and we’re going to have some kind of risk we didn’t account for and it will have to change.”

The more relevant question, in Arbitrage’s opinion, is around reaching a fair payout system. “I think we’re still a ways off.” He explained that even though the lift in the NMR market was awesome, if you started staking right before the increase you also saw a 1:1 increase in risk. Because “fair” is relative to the person observing the system, Arbitrage said it’s possible to design a payout system that’s fair to a subset of users, but not for everybody. “I don’t know any possible way to satisfy everybody.”

Keno explained that his question is mostly focused on situations where models are seeing negative reputation and negative MMC but still generating high payouts. To Keno, this suggests the incentives may not be optimally aligned to help Numerai because it looks like models are getting paid despite poor performance.

Arbitrage pointed out that, during his tenure with the Numerai contest, the [current payout system](https://docs.numer.ai/tournament/learn#staking-and-payouts) is the best that he’s seen so far. He noted that occasionally, there are models that have negative performance but still seem to be paid, speculating that it’s a quirky function of a model being highly performant the majority of the time with short periods of negative performance. “Just because it was wrong one time doesn’t mean it’s bad for the fund.”

Keno referenced the leaderboard, explaining how a model in the 79th spot had a payout of over 400 NMR, while his two models in the top ten received around 50 NMR each. He said, “I’m thinking, ‘What am I doing wrong? Are my models _that_ much worse?’ If they are, then the leaderboard is wrong and it doesn’t reflect reality. That’s my main concern.” Without payouts being directly tied to performance, data scientists lose incentive to increase their stakes.

“I think it has a lot to do with scale,” Arbitrage responded, “it’s almost a wealth effect.” He explained how someone willing to put $200,000 at stake in the tournament is willing to take on a level of risk that many of the participants can’t relate to. “I would never risk that much. That’s trading houses … I would just buy a house.” But, because risk is relative, “this is capitalism so it all works out in the end. There’s a lot of compensation for those high stakers, but that’s exactly how it’s supposed to be.”

Arbitrage believes that the “answer” to that question, or at least what he thinks Richard might say, is that if you want to receive bigger payouts, you need to do better and if you think you’re going to be in the top, increase your stake.

Bor asked Keno if he won’t just catch up to the accounts who are receiving larger payouts, noting that Keno’s stake is growing relatively faster. Keno said that unfortunately, he’ll never catch up based solely on payouts because all of the models are growing exponentially, and the others are already higher on the curve.

Keno said, “It’s a systems problem called ‘[success to the successful](https://www.systems-thinking.org/theWay/sss/ss.htm).’” He used the example of governments taxing the wealthy and providing relief to those in need, concluding that by not engaging in any kind of redistribution, Numerai is okay with models receiving high payouts only because of a large stake and not because of how much the model actually contributes to the meta model or how well it performs.

Slyfox thanked Keno for the question, saying that it’s something they at Numerai think about often but don’t really talk about. He shared his philosophy regarding fairness:

> I think there are two ways to think about ‘fairness.’ One is in the human sense in that each human is an individual and they need to be respected. This is kind of like how governments work: you need to have strong systems for identity in order to implement fair systems that are fair per person. In crypto, and a lot of the systems we study when we’re trying to design what Numerai wants to be in the long term, it’s fair per NMR. It’s like that because it’s really, really hard to implement sybil-resistant schemes on-chain. Instead of trying to say, ‘this is one human and there’s a maximum amount of stake this human can make,’ we have to make every payout as a percentage of stakes. We’re going to pay you regardless if you’re a human, you’re a dog, you’re an AI, or just some script that exists on the blockchain. We have to respect that NMR as the base unit of our payouts. -Slyfox

“Obviously, we’re not there yet,” Slyfox said, “I don’t think there are autonomous AI agents competing on Numerai yet.” He sees the tournament as a group of humans working together trying to make the system work. Ultimately, he explained, the long term solution needs to be something that’s completely decentralized and has as few rules as possible. “When I think about stability and what we’re asymptotically going to move towards, the simplest and most fair is: you do well, you get paid, you don’t do well, you get burned in a perfectly symmetric way.”

At its core, Numerai’s [payout system](https://docs.numer.ai/tournament/learn#staking-and-payouts) still functions this way. The bonuses and compounding stake are additional payout avenues that Numerai uses to reward data scientists beyond what Slyfox believes is the absolute, fair, symmetric payout. These extra payments are necessary, at least for now, because the tournament targets are not yet in a place where the data scientists can reasonably expect consistent payouts.

“The experience of having to go through multiple burn weeks, as we saw in the last few years, is really bad,” Slyfox said. He explained that were Numerai to just stick to their guns and only have perfect, symmetric payout, many of the data scientists might not still be participating, adding that a lot of new users would likely quit if the first six weeks are nothing but getting burned.

> “They’re not going to think, ‘oh this is an elegant, symmetric system,’ no, they’re going to think, ‘this sucks.’” — Slyfox

Ultimately, what Numerai is trying to accomplish with all of the bonuses is giving the tournament data scientists more money in a way that doesn’t break the symmetry, and that in the extreme long-term they want to end up with just a symmetric payout. Slyfox explained that when the team thinks about MMC or new tournament targets, they’re designed to be more consistent and stationary so that the payouts are more consistent. The result will hopefully be the best users who do really well in the tournament can expect more consistent payouts, making the bonuses unnecessary.

**Is there any study available on how many of the Numerai models are overfit based on live performance?**

> “I’ve read that [Quantopian paper](https://joi.pm-research.com/content/25/3/69), by the way: 99.9% of the backtests are overfit (Wiecki et al., 2016).” — Arbitrage

As a benchmark, Arbitrage suggested that any model that’s been active for over 20 weeks and still has negative reputation is clearly overfit. Taking MMC into consideration: if a model has negative or near-zero reputation and zero or negative MMC, it’s clearly overfit. He added anything slightly above that is probably just luck.

While no formal study exists, Arbitrage has thought about what a proper study would look like, adding that it would be a little too niche for him as he’s not sure where he would publish it.

**Slyfox:** Publish it in [the forum](https://forum.numer.ai/), Arbitrage, for fame and glory.

**Arbitrage:** I’ll let someone else get that fame and glory, I need publications in finance journals.

**For a beginner, how does MMC change what I should be looking to aim for with my model? Am I now looking to be unique?**

MMC means that models should be both unique **and** performant. Having a high correlation model is still good for the fund and data scientists can earn money on it — bonuses aren’t the only way to make money (they just help). Arbitrage said that specifically targeting MMC might not be an optimal strategy, instead suggesting to combine performance with uniqueness as an option. “But right now, I wouldn’t advise anybody new to go down that path, at least not with your main model,” he concluded.

**MMC2 neutralizes our forecast against the meta model: in a world where the meta model is perfect, we should expect MMC2 to always be negative. Is that desirable?**

Arbitrage explained that if MMC always offered perfect predictions, the data scientists would be out of business. Numerai would have no need for their submissions because they’re not beating the meta model. “We need to be better than the meta model,” Arbitrage said, “and we need to have performance. In that sense, we need to add something to it and make everything better overall.”

He reiterated that he doesn’t think a world exists where the meta model is perfect since it’s dealing with stocks: there will always be regime changes, currency risks, fraud, and multiple other reasons why the stock market will never be perfectly solved.

“I’m quite happy never having perfect predictions. We’ll always be able to add signal, and no matter how many changes the team makes to the tournament, we’ll always be able to do something.”

**What’s the best way to introduce Validation 2 into our validation pipeline?**

> “I don’t know, I have to see it first. I want to see how it’s structured in the data.” — Arbitrage

Arbitrage hasn’t planned out how he’s going to handle Validation 2 data yet, but did mention that he’ll probably add two iterations of his Arbitrage model with that data. “I don’t really plan on doing anything — I’m not going to change any of my models, and I really hope I don’t have to change any of my code in [Compute](https://docs.numer.ai/tournament/compute). That’s my number one feature request: whatever change is done, do not change the number so if it’s column 3 through 313, leave that alone please.”

![Benevolent Slyfox is benevolent](https://cdn-images-1.medium.com/max/1600/1\*lST7bcCgE6648hfPilp\_ag.gif)

**If models are mostly a random walk, what value do they provide?**

Arbitrage’s position is that data scientist performance should approximate a [random walk](https://www.tandfonline.com/doi/abs/10.2469/faj.v21.n5.55) because the models are predicting equities, meaning it’s unlikely to find a strategy that will stay above zero for very long. He mentioned one of [Richard’s forum posts](https://forum.numer.ai/t/performance-stationarity/151) about autocorrelation and checking to see if performance is stationary or not.

“Hopefully,” Arbitrage said, “we’re doing a random walk and all of us, individually, are random and none of us are correlated. Because then the signal would be performant if you averaged across all of us.” Basically, each model hopefully has a period of high performance, and by averaging across all of the models and filtering out the noise, the resulting meta model should be performant.

The idea is that during the periods of high performance, a model was right at that time. By building a model on top of all of the performant periods of other models, the meta model carries the edge. Ideally, each individual wouldn’t have an edge, but then Numerai would be able to extract the edge from each model.

**What are your ideas around a fair payout system?**

> “Homo-economicus: we’re all rational agents of the economy.” — Arbitrage

“The only reason we do something is to increase our wealth, or expend wealth to increase utility.” Instead of fairness, Arbitrage instead opted to evaluate the payout system in terms of wealth-maximization. Fair would be compensation based on effort: particularly in the early days, tournament competitors can struggle with the amount of time put into creating a model compared to the rewards. Now, though, Arbitrage expends hardly any effort because he has battle-tested models, and [Numerai Compute](https://docs.numer.ai/tournament/compute) automates the weekly contribution process, so he continues to earn based on work done in the past.

“As long as my effort is being rewarded,” he said, “and I feel that I’m being compensated for the time that I’m investing, I think it’s worth doing. When that time comes that I think I’m putting in more effort than I’m being rewarded for, then I’ll exit.”

**Slyfox**: To me there’s two games going on. There’s the tournament, which is just a game of data science, then there’s the hedge fund trying to make money in the markets. The hedge fund’s performance depends on more than just the tournament: it depends on the amount of capital we have and whether or not we can execute on that. It makes sense for those to be somewhat decoupled, and if you want to play the second game (and you’re also an accredited investor) you can talk to us about that. **Not advertising**, but you could ask us for more information.

With the questions from Slido completed, Arbitrage carried the conversation beyond his usual one-hour limit for the first time, chatting with Slyfox and the audience.

If you’re passionate about finance, machine learning, or data science and you’re not competing in [the most challenging data science tournament in the world](https://numer.ai/tournament), what are you waiting for?

Don’t miss the next Office Hours with Arbitrage : follow [Numerai on Twitter](http://twitter.com/numerai) or join the discussion on [Rocket.Chat](https://community.numer.ai/home) for the next time and date. And remember to stick around until the end for the exclusive conversation that doesn’t make it to publication.

_Thank you to_ [_Slyfox_](https://twitter.com/ansonschu)_, and_ _Michael P_ _for fielding questions during this Office Hours, to_ [_Arbitrage_](https://numer.ai/arbitrage) _for hosting, and to_ [_Zen / Nasdaq Jockey_](https://numer.ai/nasdaqjockey) _for being interviewed._
