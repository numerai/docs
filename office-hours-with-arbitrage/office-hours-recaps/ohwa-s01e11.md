---
description: "May 14, 2020 / Interview with Dr. Rudi Kuhn \U0001F1FF\U0001F1E6"
---

# OHwA S01E11

As the last of the stragglers logged onto the call, Arbitrage pointed out that the day's daily scores were his first opportunity to check how his models trained with Validation 2 performed compared to those only trained on Validation 1. "I was slightly more performant on those models," he said, "compared to my main models which are only trained on Validation 1 and the training data."

Before tackling the questions from Slido, Arbitrage gave another shout out to [Patrick](https://twitter.com/pschork) for his work on [multi-model accounts](https://forum.numer.ai/t/announcing-general-availability-of-multi-model-account-support-for-all-users/399). Thanks to Patrick's work, one account for the Numerai [tournament](../../) can support up to ten different models and easily manage your allocated stake. After enabling the multi-model feature on your account page, you can easily absorb any previous models you've created into your primary account or generate new ones.

For episode 11, Dr. Rudi Kuhn aka [Themicon](https://numer.ai/themicon), who graciously agreed to sit in the hot seat.

### The one where Arbitrage interviews Themicon

**Arbitrage:** You joined the tournament in August 2016, but how did you find out about Numerai?

**Themicon:** I was looking for a really hard data science or machine learning program. I needed to find something similar to the work I do, so all of the toy models and things like that were just not doing it for me. So I was looking for something really hard, then I came across the Numerai tournament by a Medium post \(I think\). I thought, "hey this is really interesting, let's see if I can use something I learn from Numerai in my day job."

**Arbitrage:** So let's change the order a little bit since you brought it up - what do you do for a living?

**Themicon:** I'm an astrophysicist.

![&#x1F92F;](../../.gitbook/assets/explode.gif)

**Arbitrage:** This group is amazing! Let me get this straight: we have a user who works for NASA JPL, another user who does pandemic modeling, and now we have an astrophysicist and this astrophysicist says that Numerai is hard enough to simulate some of the things he's doing. I just wanted to make sure I have that straight because every time I ask people what they do I'm blown away. So please, carry on! You're an astrophysicist ... 

**Themicon:** Yeah, I work on the largest telescope in the southern hemisphere, the [Southern African Large Telescope](https://www.salt.ac.za/telescope/). I'm one of the astronomers that get to use that telescope and send the data to the rest of the world. In my research, I'm an exoplanet astronomer so I look for planets around other stars.

**Arbitrage:** What?! That's amazing! 🤯🤯🤯

**Themicon:** Part of my PhD thesis was looking for planets around these stars but the signals are _extremely_ low - there's a lot of noise and things in it. I was trying to find techniques to use machine learning to identify the signatures I was looking for.

**Arbitrage:** Wow.

**Themicon:** With Numerai, the data set looked very similar to the kinds of things that I was doing: you're looking for _really_ tiny signals in a really noisy data set. It was the perfect thing to do.

**Arbitrage:** You just got creeped - somebody found you and posted you in chat.

**Themicon:** Yeah that's [my profile](https://www.salt.ac.za/news/meet-the-team-dr-rudi-kuhn/).

![Astrophysicist. Alien hunter. Numerai data scientist.](../../.gitbook/assets/rudi.jpg)

**Arbitrage:** I'm going to have to open that up, but I'm also going to let you continue talking about these exoplanets. So basically you look for aliens.

**Themicon:** Basically yeah.

**Arbitrage:** Does that explain your profile picture? 

![Aliens exist \(probably\)](../../.gitbook/assets/themicon.jpg)

**Themicon:** Yes it does.

**Arbitrage:** Ahhhh I was going to ask about that! So you got started in August 2016 because it was roughly similar to what you do, which is look for exoplanets \(just want to be clear on that\), because forming portfolios on blind data approximates that - which is just amazing! And you live in South Africa?

**Themicon:** Yup! In Cape Town.

**Arbitrage:** Alright - I know there's a couple people in the audience who are super pumped to hear that. So wait, what time is it there right now?

**Themicon:** It's just after 10:00 in the evening.

**Arbitrage:** Okay that's not too bad. Thank you for coming on, I'll try not to keep you too late. There was some rumor about drinking while this is going on, which I thought was a terrible idea, but, well, I defer...

**Themicon:** Well... I've run out of quarantine alcohol. We're not allowed to buy alcohol in South Africa during quarantine. So yeah, we've run out.

**Arbitrage:** Have you read that alcohol sales in the United States are up record-breaking amounts?

**Themicon:** Yeah, I can't wait for the day that I can go into a store and buy a beer.

**Arbitrage:** That's wild. So what programming language do you use and why?

**Themicon:** Python. I started off with, when I was a kid, programming in [Turbo Pascal](https://wiki.freepascal.org/Turbo_Pascal), then I moved on to Fortran, there was some C in there, and then in undergraduate I moved onto Python and haven't looked back since 2004 or something like that.

**Arbitrage:** This has come up a few times. I would say the majority of people are using Python, but there's still quite a bit of other languages being used. But yeah, Python has the most tools, I think. Like I've said before, it's like a Swiss army knife - you can do just about everything. It may not be the best scalpel, but it'll get the job done. Can you tell us your top three tips for the tournament? I'm going to take notes because I have a feeling I'm going to learn something today.

**Themicon:** Well, all of us who have been around from 2016-2017 are of kind of the same mind. First, take a **lot** of notes and really document what you're doing. That's something I didn't do in the beginning, and that really bit me. Second one is, if you have a model you think is good on your data, on your machine, leave it. Don't let the live data mislead you into where you think your model is going. That's chasing your own tail and it's not worth it. Move on to a different model and work on that one. And the third one ... have a great time. 

**Arbitrage:** Yeah, have fun with it.

**Themicon:** I've learned so much from the people in [Rocket.Chat](https://community.numer.ai/) or [the forum](https://forum.numer.ai/) and things like that - I think really spend time reading the posts and trying to understand them.

**Arbitrage:** That's really good, I think that's important so I'm glad you brought it up. Definitely have fun. I think sometimes that gets forgotten. And it's like I tell my students: look at the source code of [scikit learn](https://scikit-learn.org/stable/index.html) because even the comments there are valuable. Take advice from other people like from Medium posts and whatnot; I mean the quality of the posts in Rocket.Chat is amazing, I don't even understand some of the stuff.

**Themicon:** Yeah, there's a couple of posts in the forum recently that just blew my mind, like wow. I did not even imagine things like that were real and people do them all the time. Definitely read those and try to get your head around them and if you learn something, you learn something. And if you didn't, you didn't.

**Arbitrage:** So 1. Take notes; 2. Be patient; and 3. Have fun. That's great! I think that's awesome. I'll buy into that. Here comes a really big question, and this is going to be fought over, I'm sure: who's your favorite team member?

**T**h**emicon:** Well it has to be either [Richard](https://twitter.com/richardcraib) or [NJ](https://twitter.com/tasha_jade) - Cape Town for the win!

![Table Bay Harbour in Cape Town](../../.gitbook/assets/table-bay-harbour-3541607_960_720.jpg)

**Arbitrage:** You gotta pick one.

**Themicon:** Well since NJ has her camera on, I'll go for NJ.

**Arbitrage:** There we go! I think we're tied: [Slyfox](https://twitter.com/ansonschu) and NJ have the same number of votes. So we're back at parity. I've got three for NJ and three for Anson. Chat wants to know: are there infinite parallel universes?

**Themicon:** That's one of those questions where you can't prove what you're trying to answer, so their might be? But I can't prove it.

**Arbitrage:** Do you have a feature request or improvement that you'd like to see for the tournament?

**Themicon:** You just mentioned an easy way to compare all of your different models to one another, that's one of the things that was really bugging me, seeing how every single model stacks up against the others. Having ten tabs open and trying to flip between them was driving me nuts. I could do a script, but I haven't had the time to get all the information from the API and build it myself.

**Arbitrage:** Yeah I'm with you, I recently thought about building my own dashboard to track the payments side, but it was too big of a project. It lives in Excel now, but I should would love it to update automatically. Do you have ten models now or are you still developing?

**Themicon:** I've got ten at the moment. I have them clustered similar to the way you do it in three different ways: three of them do similar things, another three do similar things but with slight changes, three more do another thing, and then there's one where I went for [MMC](https://forum.numer.ai/t/metamodel-contribution-live/449).

### Questions from Slido

**From** [**Keno**](https://numer.ai/wander)**: Would you, or anyone, like to see in a community-run dashboard that is not already shown on the Numerai site?**

Arbitrage suggested the ability to compare one to _n_ other models would be a valuable feature and then opened the floor to Keno to talk about his idea.

Keno explained that tournament data scientists are missing some information he believes to be very valuable, like a daily or weekly measure of performance as a group \(or individually\) against external benchmarks, how much the average staked model has at stake, or the average amount of burn. "I have like, maybe twenty data points I want to track," Keno said, "but I don't have a lot of time these days. I thought we could have a chart or a couple of charts that everyone works on together."

Arbitrage pointed out that the biggest risk in asking a group of data junkies what kind of data they want to see is that the response will be endless. Keno said it would be open source, so anyone could add any metrics they want, and he hopes to have the first chart built within a few weeks.

**Does Numerai pay more attention to models with higher stakes when building the meta-model?**

Arbitrage pointed out that it's stake-weighted, so technically, yes they do pay more attention to models with higher stakes.

**What is your opinion on the recent discussion surrounding the MMC metric?**

Arbitrage doesn't have an opinion yet, he's still watching and waiting for more performance data. 

There are two things Arbitrage is looking at:

1. How are his models doing on the new Validation 2 data?
2. How many people are going to change their models to chase MMC?

His hypothesis is that as people switch their models for MMC, his correlation with the meta-model will drop and his MMC will rise. If Arbitrage sees correlation drop for his [primary model](https://numer.ai/arbitrage) \(which has always had greater than 95% correlation with the meta-model\), that would be a strong indicator that some number of tournament participants are changing their models for MMC.

Arbitrage mentioned a [forum post](https://forum.numer.ai/t/mmc-payout-details-and-analysis/220) by [Mike P](https://numer.ai/master_key) where he said MMC was more profitable than correlation for the top tournament participants and asked if Mike has done any further analysis since that post.

**Mike P:** Very briefly. The correlation scores of everyone's models have been so high over the last five weeks, so MMC doesn't look as good as compared to when I did that analysis a month ago. But if you're doing good and you think you're going to keep doing good so you stake on correlation, that tells us something as well. It tells us you think these models are so good it's going to be hard to find something that's unique to compete with them. What you can do to look at your profitability is look at your MMC reputation versus your correlation reputation and if your MMC rep is about half or better than your correlation rep, then that's kind of an indicator that you might want to be staking on MMC.

**Does the meta-model perform so well that Numerai can afford to keep paying data scientists when they run out of their NMR reserves?**

Arbitrage explained that the whole purpose of the Numerai tournament is to increase the performance of the meta-model in such a way that Numerai pays the data scientists more - it's a positive feedback loop. If Numerai also reaches a significant amount of assets under management \(hypothetically $100b\), and takes a 1% management fee, Arbitrage is confident some of that revenue would find its way to the data scientists. 

**Do you \(or does anyone\) think that these high correlations represent some sort of 'back to basics' behaviors from traders and investors as a reaction to Covid shock?**

Arbitrage believes that the high correlation was a byproduct of increased volatility making quant models more profitable. He thinks that the correlation is coming from high performing signals during times of high market volatility. Even though the training data is neutralized against volatility \(and a host of other factors\), Arbitrage suspects that somehow most models are picking up on similar signals.

**What happened at the start of Kazutsugi? Were eras 168-171 outliers?**

> "When I look at my own performance from back then it's like, 'whoa what happened? Was I just really bad?' I didn't change anything, thankfully, but I was sure scared." - Arbitrage

![We don&apos;t talk about the beginning of Kazutsugi](../../.gitbook/assets/cupcake.jpg)

Mike P mentioned that they use that period as a benchmark for how predictions would hold up during a period of really low performance. Ultimately, though, he doesn't believe there was any one specific cause for why eras 168-171 were so difficult, chalking it up to market behavior that had never been present in the test data up until that point. He did add that it seems like it correlates with the beginning of Kazutsugi, but that's completely coincidental.

**When will Numerai change the current training and validation data sets and move on to the next tournament?**

Mr. Numerai himself Richard Craib stepped in to answer this question.

> **Richard:** We have been thinking about new data: new features and a new target. We talked recently about having a target that's feature neutral _in_ the target. That way you're not paid for any feature exposures. What you would have seen, if we had a feature neutral target, is that those first two months of Kazutsugi would have been kind of normal and people would have made money if they were neutral over that period. But then they wouldn't have made much money in the last month or so where things have gone _really_ well. That's kind of why we gave that feature neutral code away in the[ analysis and tips doc](https://github.com/numerai/example-scripts/blob/master/analysis_and_tips.ipynb). You can tweak it yourself, you can say, 'I want to be 50% neutral,' or, '60% neutral,' it's kind of like deciding how optimized you want your portfolio to be. The more neutral, the better to some extent from some perspective of sharpe. However, as many people have noted, there are diminishing returns. It looks like going beyond 50% neutral starts to cut into your profitability. 
>
> So when we thought about this feature neutral target, which we actually had ready, we decided not to release it and instead tried to make a Kazutsugi-style target without feature neutrality but with a few tweaks that make it a bit better, more performant, and more generalizable. One of the ideas we had is we don't want to make everybody retrain their models if there's only a minor difference in the target, and the other thing is that if we gave out the target, we want models trained on the new target to actually do better than would have even scored against the Kazutsugi target. In a sense, basically, can we make a new target that's strictly better and wouldn't hurt anybody? It feels like we have that, and we're a few days away from feeling like it's ready. It could be within the next few weeks that we put something out as a, "take a look at this," preview. Then everybody will have a chance to play with it to see that it really does help. But, we won't switch to payouts based on it for quite a while. Maybe at the end of June or something, we'll see.
>
> That's what we're thinking in terms of new targets. In terms of new features: we're not going to be adding new features any time in the next month or so, but I think maybe a couple new features by the end of the year but we wouldn't want to completely revamp the whole data set. We like what we have now and don't want anybody to think they'll never see Intelligence 9 again - whatever features we have now will stay ****there.

**The bonus goes away \(luckily\), but will it come back in a different form? If so, how would you distribute this NMR and what would you reward?**

Arbitrage is a fan of the bonus because prior to Kazutsugi, data scientists were paid on average 0 \(with payouts and burns roughly cancelling out\)- the only path to profitability was through the bonuses. "But," Arbitrage noted, "it seems Kazutsugi is a net-positive for the bonus." He also pointed out that getting rid of the bonus removes an exploit vector.

One potential way to bring back the bonus would be to reward model stability. Arbitrage isn't sure what the best implementation would look like \(he's suggested one possibility [in the past](https://docs.numer.ai/office-hours-with-arbitrage/office-hours-recaps/ohwa-s01e10)\), but it's complex. He opened the floor for the team to respond.

**Richard:** The principle is always that if we ever make the Numerai tournament easier than the stock market, then there is an attack. It always is going to be very hard. That's why we put it on the home page: "this is the hardest data science tournament on the planet." It's not really supposed to be a way to earn interest on your NMR by submitting something dumb. Imagine if all stakes earned 5% interest every year. Suddenly being long and short the same model generates 5% interest and that's bad. You'd have to always have the p/1-p going long the same model that you're short; you shouldn't be able to make money doing that. That's the only way to keep it high-integrity which is much, much better for everyone in the long term.

**From chat: Any best practices in identifying current regimes and mapping them to past eras to train on?**

> "I would **very** strongly caution you from even trying to do that." - Arbitrage

Arbitrage explained that even if you could do that, the regime may change before you have a chance to capitalize on the fact that you've mapped regimes to eras. You're also much more likely to overfit by trying to do that. He mentioned that [Bor](https://numer.ai/bor1) has a novel way of mapping easy and hard eras and recommended reading through [his forum post](https://forum.numer.ai/t/stories-of-validation/70) to learn more about that. 

As for best practices, Arbitrage said the best thing is to just not do it.

**To build models for MMC, wouldn't it also be useful to know how our models correlate to other users' models instead of just correlation with the meta-model?**

Yes, that information would be useful because you would want to know how many other people are doing something similar to what your doing and you're all fighting for the same pool of MMC. "That's why I argued very early on that there is still a benefit to people staking on the same thing because that's independent validation of the methodology," Arbitrage said. 

If you're in a huge cluster of models and you're not at the top of the cluster in terms of performance, you might want to consider switching things up.

**Some supposedly simple linear models are still at the top of both of the leaderboards. Does this mean that Numerai needs a better metric to determine model usefulness?**

No, it just means that the linear models have found a feature set that's performant. Arbitrage explained that for however these users have sliced their data, their models have found features that produce a good result.

"But it won't last forever! 🙃"

**What incentives does Numerai have to pay uses who stake thousands of NMR? This has nothing to do with model confidence but more to do with one's personal finance.**

Arbitrage mentioned that Slyfox talked about this [not long ago](https://docs.numer.ai/office-hours-with-arbitrage/office-hours-recaps/ohwa-7): basically the scale of payouts is relative to the individual. Keno, for example, has more NMR at risk than Arbitrage, as that's his risk tolerance. Arbitrage explained that if you entered the tournament today with $30,000 worth of NMR compared to three months ago, your dollar-value for entry is the same but your NMR value is vastly different. That's just market timing, and Arbitrage doesn't think there's anything to be done about that. Some people have more wealth and a higher risk tolerance. 

_If you’re passionate about finance, machine learning, or data science and you’re not competing in_ [_the most challenging data science tournament in the world_](https://numer.ai/tournament)_, what are you waiting for?_

_Don’t miss the next Office Hours with Arbitrage : follow_ [_Numerai on Twitter_](http://twitter.com/numerai) _or join the discussion on_ [_Rocket.Chat_](https://community.numer.ai/home) _for the next time and date. And remember to stick around until the end for the exclusive conversation that doesn’t make it to publication._

_Thank you to_ [_Richard_](www.twitter.com/richardcraib)_, and_ [_Mike P_](https://twitter.com/EasyMikeP) _for fielding questions during this Office Hours, to_ [_Arbitrage_](https://numer.ai/arbitrage) _for hosting, and to_ [_Rudi / Themicon_](www.numer.ai/themicon) _for being interviewed._

