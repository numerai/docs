---
description: From April 23, 2020 / interview with Patrick @Numerai
---

# OHwA S01E08

**Arbitrage:** Why don’t you start us out … I don’t think you’ve even introduced yourself in [the forum](https://forum.numer.ai) yet.

**Patrick:** Well I actually built out the forum. I haven’t done a formal introduction, but I’ve been planning to do a response to Anson’s [Humans of Numerai](https://forum.numer.ai/t/the-humans-of-numerai/54), and I’m not going to give away what I’m planning to post there. But anyway, I joined Numerai earlier in the year (I worked with Anson at Uber, actually). A lot of the stuff I work on is backend infrastructure: I built up the forum, the whole single sign-on aspect, and what I’m working on right now is rolling out the multiple account support.

That stuff has been happening under the covers for a while, and it’s kind of imminent- it’s going to be rolling out very soon. Some of our APIs, like [Omni Analytics](https://github.com/Omni-Analytics-Group/Rnumerai) and [UUA](https://github.com/uuazed/numerapi)’s already have API updates that are going to support the multiple account stuff. So things are happening, and if anyone has questions I’m happy to answer stuff like that.

**Arbitrage:** Very cool! So you get to answer some questions because I keep this list, this handy list that I’ve been using for a couple of weeks now. So you’re the next victim.

![He only checked it once to avoid overfitting](https://cdn-images-1.medium.com/max/1600/1\*MUp55VUVVqYaH8sX2pSwiA.gif)

**Arbitrage:** I’m going to guess that you heard about Numerai from Anson.

**Patrick:** Yes.

**Arbitrage:** So that was my question, “how did you first hear about Numerai?” Since we know the ‘who’ maybe tell us the ‘how’? Did he call you? Did you have coffee? Did you have a beer? What was the circumstance behind it?

**Patrick:** Anson and I were on the same team at Uber, in mapping, and he was really getting into crypto at this point. He was trying to buy some Ripple or something- I got into crypto a few years earlier and was part of the initial Ripple giveaway so I had some anyway and ended up giving him some Ripple. He gave me some … I think he had an Anson token that he was working on? Some little token that he had.

We connected over the crypto stuff and when he decided to join Numerai, that’s when I first heard about it. I stuck around at Uber for probably another year and a half after that, but we stayed in touch. Then he and I synced up and he gave me the pitch on where they were; Erasure had just launched so that kind of sparked my interest, and I joined earlier this year.

**Arbitrage:** Great! That’s awesome. So you live in San Francisco?

**Patrick:** No, I live in the East Bay in Berkeley, actually.

**Arbitrage:** Ah, but you’re still on the West Coast.

**Patrick:** Yeah.

**Arbitrage:** Were you working in the office before you all got sent home?

**Patrick:** Yup, I was.

**Arbitrage:** So we’re all under the same shared suffering. I wonder about the people who are used to working from home. Has this changed their habits much? I did a lot of working from home prior to this, and so I think I’ve adapted pretty well, but there are people who are not taking this well at all.

**Patrick:** Yeah it’s funny- I have a wife and two kids and we just got a puppy right before this. He’s having a good time with all of the attention. I don’t know what he’s going to do when we go back to work.

**Arbitrage:** A puppy? Well I’m not sure I wouldn’t want to deal with a puppy 24/7 — I like being able to leave for a little while so somebody else can deal with it. So you’re an engineer at the team, that’s what you do for a living. What do you do when you’re not working?

**Patrick:** I was really into martial arts, primarily Aikido and some Brazilian Jiu Jitsu, but the whole COVID thing is really hampering on that. My dojo does Zooms but it’s really not the same. Other than that, I like to build stuff. A lot of woodworking, concrete, repairs around the house- things like that.

**Arbitrage:** Gotcha. So what programming language do you use and why?

**Patrick:** Right now, I do a lot of [Elixir](https://elixir-lang.org/). JavaScript is another popular one, and Python. Those are probably the three main languages I spend most of my time in.

**Arbitrage:** Makes sense. Have you participated in the tournament yet at this point?

**Patrick:** Not really. I have my own little [Integration Test](https://numer.ai/integration\_test) that I use mostly for making sure all of the changes I’m making aren’t breaking things.

![“Thank you!” — Arbitrage to Patrick](https://cdn-images-1.medium.com/max/1600/1\*tqbxpq-pvy67rXJ\_z4wo6A.gif)

**Patrick:** I don’t have any serious models that I’m working on or anything like that.

**Arbitrage:** Alright, so who’s your favorite team member? I’m going to guess Anson.

**Patrick:** My favorite team member at Numerai? I would say probably [NJ](https://twitter.com/tasha\_jade).

![Gauntlet = thrown](https://cdn-images-1.medium.com/max/1600/1\*Um3PSMVA\_9JO5brKgOsN6A.gif)

**Arbitrage:** There we go. The race is on.

**Patrick:** She’s a boss.

**Arbitrage:** Anson has a vote, NJ has a vote … Finally we have some people picking, so that’s good… Normally I would ask Patrick what your number one feature request or improvement for the tournament would be, but since you’re working on one, maybe you can just tell us a guesstimate on a release date for SAMM \[single account multiple models]?

**Patrick:** The plan is to have a really light beta roll out with a couple of select folk, and then open it up to the rest of the tournament user-base. This is imminent, it’s probably going to start next week.There’s a couple loose ends that I’m tying up. Expect a forum post from me soon talking about what happens to accounts, how they get absorbed, if you have any USD in your wallet you’ll have to drain that before you absorb it, how NMR gets transferred when you absorb accounts, and how the API keys change for models and stuff. So expect a forum post from me very soon, and I expect the beta period to be pretty short.

**Arbitrage:** That’s great! Thanks for working on that — I’m pretty excited for it. Keno is saying show the puppy.

**Patrick:** Hold on.

**Arbitrage:** That’s right Keno, I’m watching the chat. And there were a ton of questions in Slido, too, so I’m pretty pumped for that. That’s my favorite segment of Office Hours: me trying to answer a question and then Richard telling me how it is. Or if I have no idea, I’ll just pawn it off to [Bor](https://numer.ai/bor1) or [Michael Oliver](https://numer.ai/mdo). The more people I interview, the more people I can pawn it off to, so that’s working out pretty well for me. But if you guys stop showing up, I’m in a heap of trouble. Oh well, I’ll figure it out. Here we go, I think it’s puppy time.

![“NJ is melting.” — Arbitrage](https://cdn-images-1.medium.com/max/1600/1\*L\_z81NO-alH1JN3ZoVUxFQ.gif)

**Patrick:** His name is Espresso.

**Arbitrage**: I see that. NJ.exe has stopped.

**NJ:** Patrick, he’s going in the spare office when we’re back, just saying.

**Arbitrage:** That’s awesome — thanks for sharing, Patrick. So there’s so many questions, I think I need to just hop in on this.

#### Questions from Slido

**From Keno: How would you neutralize a model, example XGBoost, against the meta model?**

Arbitrage explained that the challenge here is not knowing what the meta model actually is. He joked that because his model is so close to the meta model, he could sell his weekly predictions to people to help them neutralize to the meta model.

“I’m just kidding, but I really don’t have an answer for that because unless they give us some way to accurately neutralize against a set of predictions, we’re going to have to use proxies for the meta model.” Arbitrage said he could imagine a scenario where a data scientist wants to create the closest approximation to the meta model but without submitting it. Submitting the model wouldn’t work because, as it’s so closely correlated to the meta model (by design), the meta model contribution (MMC) score would be awful.

“The payoff for me,” he said, “for MMC or the regular tournament is about the same. I’m a little bummed about that, but I think overall it’s a tremendous boost to how this all works.” He went on to say that someone neutralizing against a model they’ve created which approximates the meta model could be useful, but he’s unsure how long something like that would take.

Arbitrage asked the audience if anyone has performed any analysis on the types of models that perform well, directing the question at Michael Oliver, who has done some experimenting in the past.

**Arbitrage:** Have you seen any groups of users that correlate with some of the stuff you’ve tested?

**Michael Oliver:** Not a ton, I haven’t looked too much into how other users are doing correlated with what I’m doing. There’s definitely a lot of models that are pretty close to each other and have high correlation with the meta model also. Probably variants of XGBoost and whatnot. The interesting thing that I posted in chat and seems to be true is that for linear models, their MMC and score tend to be pretty highly correlated, which is interesting. The couple of linear models I had protracting different regimes, their MMC and scores were very highly correlated, as were [Madmin](https://numer.ai/madmin) and [Madmax](https://numer.ai/madmax). For the team’s linear model, too, that’s also the case. That’s one of the more interesting things I’ve found. You can sort of tell who’s got a linear model by looking at that.

Arbitrage mentioned how in [the previous Office Hours,](https://medium.com/numerai/office-hours-with-arbitrage-7-c82eaae8c6e8) he said that there are basically three types of models: linear, tree-based, and neural nets, and the model in conjunction with how a data scientist subsets the features or eras have significant impact on a model’s performance. He imagines that the meta model is some combination of the three model types, although the proportions are unknown.

To clone the meta model, a data scientist would have to know the proportions of different model types that are contributing. With that information, a close approximation is likely possible by creating a weighting system in an averaged model that simulates the proportions of the different model types. “Without actually having the meta model to neutralize against,” Arbitrage said, “there’s no pure way. I believe Mike P has suggested we use Integration Test, but I think we can do better.”

**Madmin Drama: thoughts on the top model being engineered to cheat and not predict well, and the pragmatism of banning the top contributor to hedge fund performance?**

![No, MadMIN drama.](https://cdn-images-1.medium.com/max/1600/1\*BuSdxe0nk88nOLZDUEIH4Q.jpeg)

Arbitrage prefaced his answer by saying that he’s quit the Numerai tournament for months at a time in the past because he felt there was too much cheating going on. “When I play a sport, I try to follow the rules as they’re written, and I don’t try to invent ways to get around the rules.”

He looks at the situation with Madmin through the lens of whether or not that person is operating in the spirit of the competition or purposely trying to find a way to extract value. He also pointed out that the [Bot hunting channel](https://community.numer.ai/channel/bothunting) in the Numerai community has been around for a long time, with several users who actively search out people who are exploiting the tournament.

Arbitrage doesn’t like when users create models that don’t contribute to the hedge fund because ultimately, it hurts everyone, data scientists and Numerai alike.

> “If Numerai’s model does well, they can attract AUM \[assets under management]. If AUM increases, payouts will increase. If payouts increase, we’re more profitable. If we’re more profitable, then we’re happy. I want that positive feedback loop to have zero interference.”

A point of contention in this debate around what’s an acceptable submission is the idea that ‘[code is law](https://harvardmagazine.com/2000/01/code-is-law-html)’ which, basically, suggests that if something is possible within the constraints of a given piece of software, it is acceptable, and any unacceptable or ‘illegal’ behavior needs to be prevented in how the software is programmed.

_Author’s note: read about_ [_The DAO hack_](https://medium.com/@pullnews/understanding-the-dao-hack-for-journalists-2312dd43e993#.kw0ufw25q) _for more debate around how ‘code is law’ impacts the blockchain and cryptocurrency industries._

“While there are still humans involved,” Arbitrage said, “I have no problem with intervention from the team to set things straight. I think it’s called for and justified.” He added that the fact Madmin was the top contributor on both the traditional leaderboard and MMC leaderboard is very interesting. Arbitrage’s conclusion, after reading [Mike P’s forum post](https://forum.numer.ai/t/leaderboard-bonus-exploit-uncovered/200), was that Madmin is performant, so actually contributing to the hedge fund, but the person behind the model designed other accounts to neutralize the risk.

If a model is actually good, backtests will prove it. “I’ve always wondered if the team would attribute backtests to an individual user.” If a test showed conclusively that a particular model appeared performant but was actually terrible, it would be possible to send that user a message, prodding them to take action.

![](https://cdn-images-1.medium.com/max/1600/1\*sZxPcJC2yDngFYE\_ssZm2A.jpeg)

He argued that in some scenarios, it would be okay for the Numerai team to let data scientists know the results of their backtests. That way, if a model performs uncharacteristically well, the data scientist will know it’s an outlier and not likely to last.

**Tl;dr:** Intervention = good, cheating = bad

**Bor asks: What kind of risk management would fit well with staking NMR? Risk of ruin, and frequently take some NMR out of your stack, but what else?**

In a direct message, he told Bor that there are a lot of options so data scientists need to design their own system and stick to it. This is something Arbitrage discusses with his students: “They’ll come up to me and say, ‘I just got my student loan money, what stock should I invest in?’ and I want to lose my mind every time I hear that.”

He tells them that if they want to trade, deposit an amount into their brokerage account that they’re willing to lose.

> “Your first year of trading is your tuition. You’re probably going to lose all of it, but you’re going to learn a lot.” — Arbitrage

Risk management is a very personal thing, and Arbitrage stressed that if you design a system, you need to stick to it. One simple but fictitious example he shared using an investment portfolio is to sell a stock if it gains 20%, no matter what, and if you lose more than 7% cut your losses and get out. He added the caveat that this is a very simple system for risk management and isn’t very robust, which probably wouldn’t be effective for someone trading in a highly volatile asset class.

But in terms of NMR: if you stake on models, you have the total, aggregate risk across all of your accounts and your exposure is the amount of NMR staked on each model. “If you double that, maybe you should take some out. I don’t know, there’s no pure answer.” In the MMC environment, data scientists are searching for models that are **not** highly correlated, and “that will certainly factor in because now we can get into mean variance optimization. I don’t know if that will translate directly.”

Arbitrage’s personal style: “I just pick a fixed amount of NMR to skate and if it goes over that amount, then I’ll withdraw the excess as profit. If it dips below, I’ll ride it, maybe I’ll fund more if it reaches a 25% drawdown.” He added that it’s a personal perspective, but that considering the fiat value is important as well because your NMR exposure has a fiat equivalent. “We had a 6x run in fiat equivalency: your risk increased 6x on the fiat side… The best thing you can do is design a system and follow that system exactly. If you deviate from your own rules, you’re gambling. I don’t believe that gambling is a way to manage risk.”

**What criterion should one consider when choosing their stake on MMC or correlation? More generally, does it make sense to still allow staking on correlation?**

Arbitrage believes it’s still too soon to compare staking on MMC to correlation. “I had some crazy high scores on correlation,” he said, “like 12% for three weeks in a row, and I don’t think I’ve ever seen a score that high on the MMC side.”

He’s in wait and see mode: “I’m going to wait and take a better look at it,” he said, adding “I would probably look at my MMC after a month, and if I had an indication that while all models are doing well, I’m also getting a high MMC, that would probably be your clue to look at burns: if everybody’s burning, how did your model do relative?”

In the past, Arbitrage said data scientists would look at where they were positioned in the burn group (whether they saw some of the worst burns or closer to the middle) and used that as a way to gauge variance relative to other models. His advice: have patience because results take time and to pick a stake and stick with it for a while.

**What are the differences between the various Integration Test accounts?**

As Numerai engineer Jason explained to Arbitrage, the Integration Test accounts are the same example model but submitted on different days of the week to test the system.

**Arbitrage:** I don’t know if that’s still true. I don’t think Jason’s on… Jason? Jason?

![Speak of the devil](https://cdn-images-1.medium.com/max/1600/1\*RycGfEDwxG3IafTju1CCRw.gif)

**Jason**: Yeah, I’m here and yeah that is true, that’s exactly what that is.

**Arbitrage:** Oh! Jason’s here! Awesome. I’m going to pick on you next week, so you better come back.

**Jason:** Alright

_Author’s note: he did._

**Can you create virtual eras to simulate a financial crash or economic boom or whatever? I’d like to know how my model fights against all odds.**

> “If only we could create such a thing.” — Arbitrage, full of sorrow

Arbitrage explained that he didn’t think it would be possible to create a synthetic data set because outside of Numerai, no one knows what the target or feature columns represent. Simulations of different economic conditions would have to be created by Numerai. “But honestly, I don’t really care. I want my model to be good on average. It seems like we all did pretty well during the recent selloff, and like we all recovered well, so it seems that on average we’re doing pretty good.”

He added that if you’d like Numerai to create something like this, suggesting it in their [Feedback channel](https://community.numer.ai/channel/feedback) is a good way to raise it to the team.

**Would you recommend using the data from previous rounds for training and validation?**

Arbitrage pointed out that there is no data from previous rounds. The training data doesn’t change, and the validation data doesn’t change ([although more data was recently added](https://forum.numer.ai/t/validation-2-announcement/166)). And while many people request having old tournament data converted into training data, “it would just cause us to overfit.”

He added that he doesn’t want more data, finding what is currently offered to be sufficient as long as it remains indicative of the market. He also recommends against using older tournament data as training data because anything you add will change your model, and [stationarity is important](https://forum.numer.ai/t/performance-stationarity/151/2).

**What’s the mean correlation and standard deviation of the meta model on live eras? Does it have a fat left tail?**

**Arbitrage:** Oh Richard… Where’s Richard?

**Richard:** Does _what_ have a [fat tail](https://www.nytimes.com/2009/02/08/magazine/08wwln-safire-t.html)?

**Arbitrage:** The meta model. Does it have a fat tail?

**Richard:** I don’t know, I mean, it has a tail, I don’t think it’s fat. If you look on an era-basis, you can see there are some eras where things have gone wrong, but I wouldn’t say it’s catastrophic, it’s within the distribution normally.

**Arbitrage:** I would guess that it would follow the distribution of returns for equities. It would make sense that it would. If you’re trading on equities, I’d imagine that your return series is going to be similar. But, I’ll let your non-answer stand.

**Richard:** \[The data scientists] are not buying particular equities ever, you’re submitting predictions on the entire market, so it’s very much normal because of all of the different predictions.

**Do we know if the new MMC 2 will basically work the same as the current reputation bonus if MMC 2 bonuses are based on stake 100 days ago?**

For [MMC 2](https://forum.numer.ai/t/mmc2-announcement/93/2), there is no bonus, payouts are based on a model’s performance in a round.

**Richard:** Yeah, anything you make that looks back in time is going to have the same kind of problems we’ve seen with Madmin, so everything should be on a looking forward basis, and on your current stake.

**Arbitrage:** I think Zen’s pretty happy with those changes, based on those payout curves. I would be too, by the way. He’s smiling!

**Zen:** It looks really good, I’m ready to check the box.

**Arbitrage:** I’m a little jealous because I don’t have very high MMC which is that stability I like.

![Pictured: Arbitrage](https://cdn-images-1.medium.com/max/1600/1\*dhGPhL3IvraJX7\_bRWZgCw.jpeg)

**Arbitrage:** I think without the bonus is fine, especially with the 2x multiplier on performance. I think that’s a big incentive. I’ll be interested to see, without the rolling bonus approach, how the users will respond. Will we have MMC chasers?

> “We see this with mining in Bitcoin with Bitcoin Cash and all the other various iterations. At first, the miners switch to the more profitable blockchain. So I wonder if users will switch from XGBoost to neural nets week-to-week, to chase where the uniqueness lies. It’s my hunch that there are three different models, and I wonder if we’ll all jump back and forth among the three. Or we’ll stumble into different subsets of eras [like Bor is doing](https://medium.com/numerai/office-hours-with-arbitrage-5-421ea23f4eec), or we’ll come up with some blend therein. I think it will be very interesting.”

**Is optimizing sharpe the best way to reach a high MMC without resorting to hackish methods like Madmin?**

> “I don’t know, I have no idea because I don’t optimize sharpe.” -Arbitrage

**Richard:** What **do** you optimize?

**Arbitrage:** I optimize correlation, and that’s about all I’d like to say. I keep it simple.

**Richard:** You optimize your performance on the target.

**Arbitrage:** Yes. The objective function is achieved.

Arbitrage couldn’t answer the question himself because he doesn’t optimize for sharpe, so opened the floor to anyone who had experience with it. Michael Oliver previously experimented with optimizing for expected payout and then optimizing for sharpe and found the results to be very similar. Bor also tried optimizing the payout function in an older iteration of the tournament, and had similar results to Michael’s. Now, he’s optimizing sharpe minus feature exposure.

Arbitrage argued that because data scientists ultimately want performance through multiple eras and high MMC, optimizing for just one thing is probably not the best option. He doesn’t believe his models are particularly good, just very stable. “That gives me the opportunity to ride the top 100 all the time, instead of having sudden drops and rushes to the top.”

**It would be a nice feature to stake on other users’ models. Do you plan such a feature?**

This will never happen because it’s too close to gambling to be within regulation.

**Do feature interactions make sense for feature engineering?**

Arbitrage pointed out that tree models take into account interactions and are also performant in the tournament, so feature interactions matter. “Would I want to create my own? I’ve tried that before, very early in the tournament, and it never worked out. But this was three years ago, I haven’t done it since.”

He thinks interactions make sense, but is unsure that, with the way the tournament data is constructed currently, it’s conducive to create your own features (because tree models and neural nets do it on their own).

**Should you Z score the features by eras before interaction? Could you use a neural net to find which new features to use?**

Arbitrage passed the mic to Bor for his insight after building a complex genetic algorithm for the tournament.

Bor runs his model once to generate a series of solutions and excludes the features that have the highest correlation. He repeats this several times then takes the average of all of those models (similar to what tree models and neural nets do themselves).

Ultimately, Arbitrage and Bor agree that some feature engineering makes sense, with Bor adding that his manual process is similar to what neural networks would be doing.

**It would be nice to submit a model and get an immediate MMC backtest result.**

In the past, fast access to feedback data hasn’t been beneficial for the tournament because competitors could easily make small changes over several submissions to try to reverse engineer what the most impactful features or eras might be.

Richard mentioned that one thing they’ve considered doing is adding new metrics after uploading predictions beyond validation sharpe, such as correlation after Numerai neutralizes the model with the example predictions. “If that has correlation that’s positive with the target,” Richard said, “that’s a pretty strong sign that you have some MMC.”

Richard added that they wouldn’t be giving data scientists backtests over the test set, but some information on the validation sets could help them decide whether or not to target MMC with a model.

**Do Richard and Slyfox have their own models in the tournament? If so, what are their names?**

**Richard:** I don’t, I never really have put one in. It’s maybe because I’m lazy, and I actually do want to get some in. Maybe convince Anson to do it, make sure they’re all hooked up to [Compute](https://docs.numer.ai/tournament/compute), or just run automatically. But there is actually a model that’s one of ours (which I was going to mention in the [era boosting post I wrote](https://forum.numer.ai/t/era-boosted-models/189)). This model, [Sugaku](https://numer.ai/sugaku), is a Numerai employee’s model that uses some of the era boosting ideas. It’s not only \[era boosting] so I didn’t want to bring it up as an example of that, but it does use some of the ideas and it’s had a very consistent score.

**Arbitrage:** I’ll tell you that you might like your Sugaku, but my student’s ranked higher at 68 to your 73.

**Joakim:** Sugaku means ‘smart’ in Japanese, by the way.

**Arbitrage:** That’s cool — did not know that.

**Does it make sense to optimize some of your models for correlation and others for MMC or is correlation something we should forget already?**

Arbitrage summarized his position from earlier: at the moment, it seems like a better strategy to diversify and split your models between both options. Ultimately you want a model that’s performant over time but also has high MMC. “The answer to that,” he said, “is to build a performant model across all eras and is relatively stable, and then you can have a little bit more faith in the model that will do well.”

**I understand what the p, 1-p attack is, but it’s not clear to me why the analytics of Madmin’s model have shown the model itself to not be particularly interesting, just a linear combination of a few features. Isn’t that the highest performing model?**

Put another way: how is the Madmin model ranked so highly on the leaderboard if it’s not doing anything noteworthy? Arbitrage suggested that if the model is just a linear combination of a few features, it’s possible the creator found or stumbled onto the strongest features that are working right now under the current regime.

**Richard:** It’s not a good model, it’s not like you should try to use only a few features. It’ll give you a high variance model, and if you have two such high variance models, then one of them will do well and one will do badly. It’s not really a good thing to do long term.

If you’re passionate about finance, machine learning, or data science and you’re not competing in [the most challenging data science tournament in the world](https://numer.ai/tournament), what are you waiting for?

Don’t miss the next Office Hours with Arbitrage : follow [Numerai on Twitter](http://twitter.com/numerai) or join the discussion on [Rocket.Chat](https://community.numer.ai/home) for the next time and date. And remember to stick around until the end for the exclusive conversation that doesn’t make it to publication.

_Thank you to_ [_Richard_](https://twitter.com/richardcraib?lang=en)_, Jason, and_ [_Michael Oliver_](https://numer.ai/mdo) _for fielding questions during this Office Hours, to_ [_Arbitrage_](https://numer.ai/arbitrage) _for hosting, and to_ [_Patrick_](https://twitter.com/pschork) _for stepping up to be interviewed at the last minute._
