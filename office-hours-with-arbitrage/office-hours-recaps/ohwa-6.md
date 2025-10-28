---
description: 'April 9, 2020'
---

# OHwA S01E06

**Changes to the tournament**

Before diving into the questions from Slido, Arbitrage started off by talking about the recent change to the tournament’s [reputation calculations](https://docs.google.com/document/d/1o3-J8qFyo7aQQZ8BIja0Lmw7Gr81sPVYazq6v41-ENI/edit) that resulted in models being reranked \(including historical ranking\). For Arbitrage, this put him in the top 25 for a period of about two months — a net positive for his reputation. He asked the audience, “What was your impression of the change?”



![Feelings were mixed: &#x1F44D;/&#x1F44E;](https://cdn-images-1.medium.com/max/1600/1*xaVwZiYdF3FIq02KI1ryXA.gif)

[Joakim](https://numer.ai/joakim_arvidsson) mentioned that his model is still young and dropped several ranks under the new system. “I think it has a lot to do with whether or not you already have four or more weeks in a row of submissions, then you weren’t averaged across like we used to be,” Arbitrage said. “That would increase your volatility because it was based on less than four rounds.”

The new reputation score is based on a weighted average of a model’s performance in 20 rounds. “I had a really good ramp-up from October through March, so for me I’m losing all of my good rounds every week. So my rank is going to decline as those rounds fall off. So I’m watching that with bated breath, if you will.”

Arbitrage also pointed out that several tournament participants noticed that, on the same day as Office Hours, the tournament hit the 250 NMR per day payout cap.

_Author’s note: since recording this episode, Numerai introduced_ [_new updates to the payout system_](https://forum.numer.ai/t/mmc-payout-details-and-analysis/220)_._

Data scientist [Keno](https://numer.ai/wander) expressed that it might be cause for concern among participants; someone could, for example, create multiple accounts with the same model as a way to earn more rewards without actually creating multiple models, taking up positions on the leaderboard in the process.

Arbitrage noted that this is a concern, although this behavior has yet to manifest. “It’s always been a risk,” he said, “but I don’t think anyone’s using \[that method\] because of diversification benefits.”

He then explained [McNemar’s test](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3716987/), a way to score two models against each other to see if they’re the same model or not. The test produces a statistical analysis that says if the two models are similar. “I’ve proposed that as a way to sniff out if somebody is running clones of something, and also to prevent people from submitting the example predictions.”

![Not quite &#x2026;](https://cdn-images-1.medium.com/max/1600/1*0c40viHwPzvmvB-hkU6N-A.jpeg)

Keno pointed out that, historically, once the tournament data scientists “solve” the payout structure, the Numerai team is quick to update the payout calculations. He said, “Trying to earn NMR, from my observations of others, works for a little bit but then they figure it out and say, ‘these people are gaming us,’ so they change the \[payouts\] … you kind of have to think ‘what am I going to do with this competition — am I going to always try to game them? Or do I just submit a model that makes sense?’”

“Yeah, you’re right Keno,” Arbitrage said, “and they’ve shown in the past that they’re willing to make big moves to prevent attacks.” Arbitrage then pointed out that the tournament rules also [clearly state](https://docs.numer.ai/tournament/learn): “We reserve the right to refund your stake and void all earnings and burns if we believe that you are actively abusing or exploiting the payout rules.”

Returning to the topic of the new payout calculations, Arbitrage explained a quick analysis he performed on his own payouts. Now that the submission correlation is the payout percentage, his average correlation is 0.81%, noting he skews a little positive and that this calculation doesn’t take into consideration bonus payouts. “I was concerned that it would be skewed negative, because in the past, that was the case: the data indicated we were more likely to burn than to earn.”

Arbitrage thanked [Michael Oliver](https://numer.ai/mdo) for joining, telling him, “Now that I’ve interviewed you, I’m going to refer to you as my Panel of Experienced Users, along with Bor.” He asked Michael if he’s done any data exploration on the new payouts system.

![That gang&#x2019;s all here](https://cdn-images-1.medium.com/max/1600/1*aJ3U8JFkMOcWV0ydbzUsnw.png)

Though he hasn’t done any exploring yet, Michael said he noticed that there’s going to be less day-to-day volatility because the smoothing window has more of a Gaussian shape, but it’s actually narrower because of the change from 100 days weighted equally to not being weighted equally. “You could expect that without the noise of the day-to-day fluctuation, you can expect to move up and down a little faster than before.” He added that the [tournament docs](https://docs.numer.ai/tournament/learn) have already been updated to reflect the new reputation scoring.

“Also, I think the downside will be more persistent,” Arbitrage said, “if it’s sticky on top it’ll be sticky at the bottom.” He explained that his model is hovering around 89th place on the leaderboard and isn’t gaining higher positions despite high performance. As mentioned in previous Office Hours, Arbitrage includes validation data in his training set so he experiences higher volatility in past tournaments. He wasn’t surprised that his model is sticking in the midrange on the leaderboard, saying “I kind of expected this.”

Arbitrage then shared that with expanded access to accounts \(10 instead of 3\), he’s testing cloned models but without including validation data in the training sets to see what the impact is on model performance, noting that it will be months before he can determine if that worked or not.

![&#x1F3B5; So I keep on waiting, waiting on my scores to change. &#x1F3B5;&#x200A;&#x2014;&#x200A;Arbitrage](https://cdn-images-1.medium.com/max/1600/1*ldAcoD0bPGe_jTiN1eMJzQ.jpeg)

Michael asked Arbitrage why he thought excluding the Validation data might improve his model performance, as that would effectively be just excluding one year’s worth of data. Arbitrage countered that the excluded year could be very similar to five other years or extremely unlike a year from a more challenging period, either of which would weaken the signals from the more significant eras. “That’s my hunch,” he said.

To that point, Michael explained that testing that hypothesis would entail excluding random eras, random years, or random blocks of eras to see which approach would have the most positive impact on performance. “I haven’t done it,” Michael said, “but I’ve often wondered if excluding some of these early eras from so long ago might be a good idea.”

> “Recency matters…

… especially when you’re trying to capture regime changes,” Arbitrage said. This is one of the reasons why he was so excited about the prospect of using the Validation data as training data: it’s more recent, so likely more relevant. When he added the validation data, Arbitrage considered dropping some of the earliest eras, but ultimately decided that was a risk. His approach is that Numerai is giving participants the data for a reason and they’re not trying to be misleading, “and that’s served me well in the past… I have found that the validation data as additional training data has increased volatility of my performance. Yeah I could punch higher, but I would get punished harder, too.”

Arbitrage explained that when he didn’t include Validation data in his training, his model performance was smoother, but it didn’t help him climb the leaderboard as much. “I haven’t figured out which is more profitable,” he said, “The upside is I did really well in the beginning of the year, but we don’t have enough time with Kazutsugi to really know how it’s going to play out.”

Arbitrage then asked another OG Numerai data scientist [Themicon](https://numer.ai/themicon) for their take on the latest changes, who shared that they experienced results nearly identical to Arbitrages. Themicon explained that including Validation data in their training set resulted in huge fluctuations in their score: “when everyone else was doing well, I was doing _really_ well; when everyone else was doing bad, I was doing _really_ bad.”

“I don’t remember who I was talking to, or when,” Arbitrage said, “but somebody just pointed out that if you do really well and include Validation data, it just means that the current live era is similar to Validation.” Arbitrage suspects that this will also apply to meta-model contribution \(MMC\) such that if one person trains with Validation and others don’t, the models that don’t include Validation will become performant \(though it’s still too early to tell if this is the case at the time of this Office Hours\).

**Joakim:** MMC is going to be a more difficult tournament, I reckon.

**Arbitrage:** I think so. If it’s a side pot, it’ll be fun, but I don’t know about targeting MMC. If I switch my model to MMC and other people do as well, if we stumble into the same solution then our share of MMC is going to decline. So you need to choose between stability and chasing MMC. I think it’s going to be very difficult to be performant **and** have high MMC over time. But I’m very interested to see how it all plays out. Especially with all of these crazy genetic algorithms that Bor is running.

**Joakim:** It might be more valuable for Numerai, though.

**Arbitrage:** When you think about it from a hedge fund perspective, it absolutely is more valuable for them to get 1,000 completely different but performant models, then to get clusters of 3 different types of models that are performant because then they’re really just creating a metamodel on 3 different models.

This, Arbitrage said, he believed was unavoidable: because of the nature of the data, tournament participants will likely converge around the most performant strategies. But, as he discussed with Richard Craib, if a data scientist treats the features differently, drops certain features or subsets of features, only trains on certain eras, or uses different blending techniques, this is where MMC becomes a powerful anchor point. There’s probably enough variation in the data to capture MMC, but Arbitrage isn’t convinced that there is enough diversification of modeling techniques to achieve the same thing.

In the chat, Michael Oliver posted a link to [a linear model with almost perfect correlation to MMC](https://numer.ai/krat):

![Model: https://numer.ai/krat](https://cdn-images-1.medium.com/max/1600/1*Hr3RbHXeW2pf26tWmlYPVg.png)

**Michael Oliver:** It’s a linear model trained on a subset of eras in an automatically determined way. Since MMC came out, I’ve been really curious as to how MMC and the model performance line up. I don’t know what to completely make of it. It’s basically half of a mixture of linear regression models, so it tries to find the eras that best go with two linear regressions. Sort of a regime within the data. The fact that MMC and performance look so similar, I don’t know what to make of it, it’s just really interesting.

**Arbitrage:** Your correlation with the metamodel is similar to what I’ve seen with neural nets. Is it just a linear regression? You probably won’t tell me more than that, will you …

**Michael Oliver**: It’s a mix of linear regressions: it automatically parses out eras to two different linear regressions, so it’s basically about 60% of the eras.

Arbitrage pointed out that some of his students have come up with ensembles of basic linear models. Their early indication is that performance will be above average, adding that 19 of his students have completed their production models and have created tournament accounts \(some of them even asking if they’re allowed to continue tinkering with their models even though the assignment was finished\).

#### Questions from Slido

**How much live data is needed to evaluate how overfit a model is? Is a month long enough? How confident could one be with 12 months of live vs 12 months of validation?**

> “One month is definitely not long enough.” — Arbitrage

Submissions to the Numerai tournament are making predictions on a month-long timeframe every week, essentially making the same prediction four times. This means anyone would need at least 12 weeks of performance history to evaluate a model. On top of that, if the model starts during a burn period, it tends to be auto-correlated, meaning it could experience four to eight weeks of continuous burn. “If you encounter that,” Arbitrage said, “you have to wait until it turns positive to see how everybody else does.”

Arbitrage said he hasn’t had the opportunity to experience entering the tournament during a burn period until recently, but he would want to know: if everybody is burning and so is his model, who recovers first? He said that if his model burns longer than the top performing users, it’s an indication that his model isn’t performant.”But that’s like, not scientific at all, just kind of a gut check.”

As for how confident one could be with 12 months of live data versus validation, Arbitrage said: “Not very- this is stocks, this is equities, we have no clue. Look at what happened with Covid-19, it’s a huge regime change right in the middle of all of this, and we have to hope that our models can survive regime changes.”

**Themicon:** I’ve been \[competing\] since 2016, and in the beginning I was changing my model every week and it did not work. I had no idea if it was me or the market or anything like that. I’ve started getting to the point where I think I have something and leave it for three or four months before I go back and look at it. I’d rather create more accounts and try other things on other accounts. I’d say four months at minimum.

Arbitrage echoed his advice to his students from back when the account limit was three: create three **different** accounts and over time kill the lowest performing one. Just delete it and try a new one. “If you have your own evolutionary process, similar to what Bor is doing but more manual, then you will always improve. It keeps you constantly innovating.” He added that now that the account limit is 10, maybe he would consider dropping the bottom three, but he’s unsure.

At the time of the Office Hours, Arbitrage was experiencing a flippening: his model [Leverage](https://numer.ai/leverage) was higher than his model [Arbitrage](https://numer.ai/arbitrage).

_Author’s note: In the time since recording this Office Hours, Arbitrage surpassed Leverage and balance has been restored._

Arbitrage never expected this to happen because his namesake model has always performed well, but now he’s thinking it needs a closer look and might warrant some tinkering. “But if Arbitrage fell to the bottom, I’d kill it,” he said mercilessly.

“Like I tell my students with trading, there are no sacred cows. You have to be willing to drop something that’s not working.” — Arbitrage

The conclusion: A longer time frame and manual evolutionary process help lead to improvement over time.

**Is Numerai’s influence on the market itself big enough to make a drop in correlation of our models on live data due to obvious signals from trained data already utilized?**

Phrased another way, this question is asking if Numerai is trading on the predictions and then squashing those signals’ ability to generate profit, to which Arbitrage confidently said “no” and included another question as part of his answer: **has Numerai ever revealed its yearly profit numbers or given any indication if the \[metamodel\] is working?**

Arbitrage said that he can answer both of these questions with one simple observation: all hedge funds that trade equities have to file a [form 13F](https://www.sec.gov/divisions/investment/13ffaq.htm) once they reach a certain threshold of assets under management \($100 million\). Numerai has not filed a 13F, so Arbitrage suggests that we can infer it’s not a large hedge fund and therefore is not moving the market.

**Was Round 202 considered a difficult round?**

> “Yes.”

Arbitrage believed that this round took place when most assets were seeing high correlation: gold, bitcoin, equities in every major market, and bonds all sold off and the only asset that saw any positive performance was treasuries \(which barely moved because yield was already practically zero\). “When correlations are 1,” he said, “everything blows up.”

**Themicon:** Any other eras that correlate with 202?

**Arbitrage:** I would suggest in the middle of the training data — there appear to be some difficult eras.

Arbitrage said that the difficult eras seem to be rare, and that he suspects there are models in the tournament that fit to those high volatility periods and intentionally leaving off the “easier” eras. This leads to doing well when everyone else is burning, but rarely doing well after that. “Now that the data is balanced,” he said, “it doesn’t make sense to purposefully fit to the difficult eras.” He also noted that tournament participants should expect to see eras where performance doesn’t match their perception of the market, e.g. high burn despite no clear signals of volatility in the market.

**Joakim:** You mentioned eras 60–90 were difficult, do you know roughly what years they represent?

**Arbitrage:** I don’t — they’ve never officially told us when the time period starts. We can only guess, I’ve just noticed that the middle third of the eras seem to be rather difficult. I wouldn’t even know how to extrapolate that back to an actual time series, and I’m not sure that it really matters.

Even though Numerai data is delivered chronologically, Arbitrage pointed out that data scientists know so little about it to begin with so he’d be very cautious about trying to align the time series with any actual news or events, because that could introduce bias \(which is one of Arbitrage’s least favorite things\).

**Joakim:** I’m mostly just curious.

**Arbitrage:** Oh me too! Every time I see Richard I’m asking him every possible question I can and he always laughs at me and thinks I’m an idiot for even bothering to try, but so be it.

![&quot;Lol&#x201D;&#x200A;&#x2014;&#x200A;Richard Craib](https://cdn-images-1.medium.com/max/1600/1*WIwpYldq7J1WS5pdgpUUQw.jpeg)

Michael Oliver indicated in the chat that he has a counterpart model which performed well during era 202, prompting Arbitrage to wonder if Michael averaged the performance of his primary model with the one that performed during the high volatility period, what would the resulting score look like.

Michael has considered that approach, but hasn’t come around to trying it yet. He explained that his counterpart model is trained on the disjoint set of eras from his other model, so they’re not quite mirror images of each other, but an attempt at capturing two different regimes. The counterpart model does perform well when everyone else is doing badly, but that rarely happens so the model overall isn’t particularly good.

A model diversification strategy like MIchael’s counterpart models may have been worthwhile in the past, but Arbitrage doesn’t see the value in something like that as the tournament currently stands because ultimately, sustained positive performance is preferable to short gains.Michael then added that he doesn’t stake on this models, but finds them as interesting data points to track performance over time.

**Arbitrage asks the Panel of Experienced Users: are you going to spread your stakes out across ten models or are you going to stick with what you know?**

**Themicon:** I think it’s too early to say at the moment. I’ve added four more accounts with ideas that I had a long time ago that I want to try out, and I’ll leave them for the next four months and see how they do. Depending on how they do I might \[spread my stake around\], but at the moment I’m just sticking to my original three because I know they work in different regimes.

**Arbitrage:** The one thing to consider is that if you are planning on staking eventually, every day that you wait, you have to wait another 100 days to earn reputation. That’s what I’m struggling with: I staked early for three accounts and staked again right in the middle of a burn sequence so I haven’t broke even yet. Let’s extrapolate out: 20 weeks in, all of your models are in the top 300, are you staking evenly on them or are you sticking with what you know?

**Michael Oliver:** I’m definitely sticking with what works for my biggest stakes and gradually increasing stakes on things with increased confidence. If some model is looking better overall, I might switch it to one of the higher stake accounts.

**Arbitrage:** I guess you could switch your stakes just by changing your submission files — I didn’t even think about that. That would blend out your reputation series too. That’s interesting, I have to think about that some more. I gotta stop talking out loud and giving out my ideas.

**What are your plans to improve your models’ performance? Not asking for secret sauce, but would be interested in the direction of your and others’ thoughts.**

Arbitrage said his plan is to essentially keep killing his worst performing models. He also considers volatility to be one of his parameters, so if he has a performant model but one that keeps swinging on the leaderboard, he would consider killing it just because of how volatile it is. “To me, that’s not very good.”

Ultimately, Arbitrage pointed out that iterating on tournament models takes a significant amount of time so his strategy is focused more on steady growth as opposed to big incremental gains. One example he gave was having three models in the top 50 for a cumulative period of nine months. As to how he’ll achieve that, Arbitrage said he “can’t think of any way other than to kill the worst performing one in some kind of death match among my own ten models.”  


![Are you not entertained?](https://cdn-images-1.medium.com/max/1600/1*S0htcUiRBAeHCNluG9x9Ww.jpeg)

**Themicon:** Yeah, I think I’m going to do what you’ve been discussing. It’s such a long game. Keep the things that are working, and kill off the things that aren’t working after four months. That’s why I haven’t filled up my accounts yet. I have three that are working, four more with ideas, and I’ll see how those go before I start adding more.

**SSH \(in chat\):** Keeping 90% in one major stake and around 10% in the other two.

**Richard asks in chat: How many of you plan to stake on MMC?**

**Arbitrage:** I’m in “wait and see” mode, not going to say yes or no to that.

**Michael Oliver:** They’re going to change to MMC2 first, which we haven’t seen yet, so I have to see that first.

**Richard:** I was looking at MMC2 and it does look a little bit more stable, from what I was seeing. I only looked at a few users, but it does seem to me that whereas you’re at the mercy of the market with the normal tournament, like you’re **going** to burn if there’s a burn period, that doesn’t seem to be the case with MMC. Part of me has concerns that we might get to a place, maybe a year from now, where 80% of the stakes are on MMC.

**Arbitrage:** Why is that a concern, though?

**Richard:** Well, it’s not a concern, it would just be strange. The tournament changes its whole character: it’s not about modeling the data, it’s also about kind of knowing what others are trying to do.

**Arbitrage:** Oh yeah, that would be a concern. Like what I was saying about how I chase MMC along with others and we stumble onto the same solution so our share of MMC goes down because we’re correlated together.

**Richard:** You guys said earlier that you think it’s quite volatile; it doesn’t seem as volatile as the normal returns. If you look at the black line and the blue line on the Submissions page, usually the blue line is a little bit more compressed than the black line. So it seems to me to be a little less volatile. Often, if someone has 80% of weeks up on the normal tournament, and their MMC is up 90% of weeks, so it seems like it might be quite compelling for a lot of people.

**Arbitrage:** Yeah, but I just don’t know that I can stake on both because my MMC is correlated so strongly with my tournament performance. When my model does good I get high MMC and when I burn I get negative MMC. For me, it doesn’t offer a diversification, but maybe MMC2 does. I don’t know, it’ll be interesting to see. Any way I can reduce my risk, and if that’s betting on a side pot, that’s beneficial to me. That’s what I’m waiting to see.

**Slightly off topic but: what do you \(or others\) think will kill the project? And why do you think there’s no real competition out there?**

Off the bat, Arbitrage noted that a significant change to the global equities markets which invalidated **all** of the Numerai data would kill the project. A scenario where capital controls prevented investing in foreign markets, for example, would kill the model as it’s based on foreign equity trading. Arbitrage also pointed out the legal risks involved working within such heavily regulated industries, such as if cryptocurrency can no longer be used as a compensation mechanism. “That kind of screws things up pretty bad.”

After Keno asked about competition as a threat to the tournament, Arbitrage added one more potential killer: what if one day Richard gets a call from a massive financial services company and they buy Numerai for $10 billion, then shut it down.

**Arbitrage:** Richard’s laughing, what do you have to say Richard?

**Richard:** Well, that’s why I have more than half the shares and control the board of the company.  


![Richard to people trying to buy Numerai](https://cdn-images-1.medium.com/max/1600/1*OLsdWV--sM52oU4QbkmpEQ.gif)

Richard explained that he doesn’t mind investing in his own company and his own token because he specifically doesn’t want some kind of hostile takeover to happen.

**Arbitrage:** If somebody called you and said, “hey, we’re going to give you $10 billion to buy your project,” that’s going to be a tough call to turn down.

**Richard:** Nope 🙅‍♂️

**Slyfox**: It’s not about the money, it’s about the vision!

**Arbitrage:** Everyone has a number, I refuse to believe there isn’t a number that you would take to shut this thing down. Or rather, you would take not knowing they were going to shut it down.

**Richard:** Well that’s why everything is open source, so even if someone did buy it and shut it down \(which is impossible because we wouldn’t sell it\) but even if they did, someone would just rebuild it with the code we left behind.

**Arbitrage:** That’s true, with Erasure being open source the way it is, I can see that.

**Is live sharpe ratio versus validation sharpe ratio a good way to measure how overfit my model is?**

Arbitrage said that in general, yes, data scientists can use sharpe ratio to determine how overfit a model is but noted that the direct measure suggested in the question doesn’t work. A live sharpe ratio of 1 to a validation sharpe of 2 does not equal a 50% overfit, for example, because that could be the result of spurious correlation. “In general, comparing your in sample to out of sample will always give you an indication of whether you’re overfit but it’s not a direct measure.”

**If my model performs better or worse live compared to validation, how can I determine if it’s due to over/underfitting, market regimes, liking/disliking my model, or feature exposure?**

> “You can’t.”

Arbitrage explained that because it’s live stock data, he doesn’t believe tournament participants can infer much about why models behave the way they do. The validation data is such a small subset of the larger data set: equities change by the minute and the tournament prediction time frame is a month long. This is why Arbitrage encourages his students to take a long view and to aim for something stable.

**When is SAMM \(single account multiple models\) coming out? Can we consolidate to a single email yet?**

[**Slyfox**](https://twitter.com/ansonschu)**:** Yeah, it’s coming soon! We’re working on it right now. We’re slowly making those changes to our API and putting on the final touches so sign on and account creation make sense on the front end. It’s taking time to make it look good and useable, but it’s coming and it’s definitely a priority, so any feature requests?

Arbitrage took the opportunity to bring up a hot topic in [RocketChat](https://community.numer.ai/): the ability to withdraw from stakes on Wednesday nights — Thursday morning \(to send a reputation bonus directly to a user’s wallet or to pare down their stake\). Arbitrage is an advocate and stamped it as his \#1, highest priority feature request. Essentially, Arbitrage is asking for a window where his stake is not active after receiving a payout where he can choose to roll it forward or take his profit off the top.

Slyfox agreed that the idea makes sense and noted that it’s been discussed internally. He said he would look into it, noting that in terms of timeline if they move forward with this, it would likely be grouped with the introduction to MMC2.

**Another “Feature” request: it’s been about three months since the last Fireside Chat.**

Arbitrage said that Office Hours with Arbitrage is not a substitution for a Fireside Chat and wanted to know when the next one would be.

“I feel like we’re scheduled to have one next week,” said [NJ](https://twitter.com/tasha_jade) who was fortunately on the call.

_Author’s note: Richard and Anson host quarterly Numerai Fireside Chats where they answer questions from the Numerai tournament community covering topics like recent changes, feature requests, modeling tips, and what to look out for in the coming months. They did, in fact, have a Fireside Chat the following week. Stay tuned for a recap from that call._

If you’re passionate about finance, machine learning, or data science and you’re not competing in [the most challenging data science tournament in the world](https://numer.ai/tournament), what are you waiting for?

Don’t miss the next Office Hours with Arbitrage : follow [Numerai on Twitter](http://twitter.com/numerai) or join the discussion on [RocketChat](https://community.numer.ai/home) for the next time and date.

_Thank you to_ [_Keno_](https://numer.ai/wander)_,_ [_Michael Oliver_](https://twitter.com/the_moliver)_,_ [_Slyfox_](https://twitter.com/ansonschu)_, and_ [_NJ_](https://twitter.com/tasha_jade?) _for fielding questions during this Office Hours, to_ [_Arbitrage_](https://numer.ai/arbitrage) _for hosting, and to_ [_Richard Craib_](https://twitter.com/richardcraib) _for being utterly unwilling to sell Numerai._

