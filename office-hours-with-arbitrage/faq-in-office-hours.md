---
description: The most popular recurring questions from Office Hours
---

# FAQ in Office Hours

### Hedge fund assets

**Can you explain what you think Numerai assets are \(market, investment type\), by taking into account what little we know, e.g. time over which they mature, etc?** 

Numerai has already disclosed that they trade global equities, Arbitrage said, noting that this information has been public for a while. Based on how the tournament data is structured, their evaluation period is long \(otherwise the models would need to be checked every second, which would require significant computing power beyond what most individuals have access to\). 

Richard explained that Numerai is a global equities hedge fund driven by the machine learning models of their data science community. They’ve never traded anything besides equity, and they’re, “long/short, market neutral, country neutral, sector neutral, currency neutral, factor neutral… just trying to find the edges that other people can’t find and that aren’t exposed to the risk factors that other funds are exposed to.”

**Since we know little about the assets or how predictions are utilized, why do you think there are historical limits on the hedge fund’s earning capacity?**

One of the limits for hedge funds is scale:

> “When you find an edge, trading on it collapses that edge because you’re making it more efficient. When you find an edge in finance, you are therefore finding something that is an inefficiency in the market and by trading on that inefficiency you are closing the profitability of it.” - Arbitrage

This presents a problem for hedge funds in finding a strategy that scales, which is absolutely true for Numerai as well.

I**s there a correlation between performance of the VIX \(**[**CBOE Volatility Index**](http://www.cboe.com/vix)**\) and Numerai’s burn rate?**

Richard explained that there was a significant market drawdown which began in February, and the VIX went up during that time, but in actuality it was hedge funds deleveraging risk \(occurring during a period of high VIX performance\) that had a more noticeable impact on Numerai data scientist model performance.

> “I think it’s a waste of time to think, ‘I’m going to put my stake up because the VIX is low and I think it will stay low.’ … Numerai is not a derivative of the VIX.” — Richard Craib

Arbitrage noted that, despite the large drops in the market, his recent models were performing better than he expected, crushing all of his prior models. For Richard, the fact that Arbitrage’s models were so drastically uncorrelated with market performance made perfect sense.

Richard explained that when Numerai provides backtest data to investors, that data can’t reflect any degree of correlation to something like the volatility index. He said, “If they come back and say, ‘this is 70% correlated with the VIX,’ we don’t get money from them. It has to be 0% correlated.” By design, Numerai has taken out these known factors to make it more difficult for anyone to find a correlation. Data scientists therefore can’t tie correlation to the fund’s performance. 

**Is Numerai’s influence on the market itself big enough to make a drop in correlation of our models on live data due to obvious signals from trained data already utilized?**

Phrased another way, this question is asking if Numerai is trading on the predictions and then squashing those signals’ ability to generate profit, to which Arbitrage confidently said “no” and included another question as part of his answer: _has Numerai ever revealed its yearly profit numbers or given any indication if the \[metamodel\] is working?_

Arbitrage said that he can answer both of these questions with one simple observation: all hedge funds that trade equities have to file a [form 13F](https://www.sec.gov/divisions/investment/13ffaq.htm) once they reach a certain threshold of assets under management \($100 million\). Numerai has not filed a 13F, so Arbitrage suggests that we can infer it’s not a large hedge fund and therefore is not moving the market.  
****

### Model evaluation

**What’s a good validation sharpe?**

[Michael P](https://numer.ai/master_key) answered this question, noting that validation sharpes are high values, with the Example Prediction model’s sharpe being around 1.5. Michael added the advice that the Example Prediction sharpe is “verification that you’re calculating things correctly, but you want to calculate your sharpe yourself on the cross validation and training set. You don’t want to rely on the validation sharpe to pick your model because the validation eras are too easy.”

Richard then brought up the Validation 2 data set Slyfox mentioned during [Office Hours \#2](https://medium.com/numerai/office-hours-with-arbitrage-2-a0686dc88417). Validation 2 is a data set the Numerai team are exploring which contains the previous year of live data, meant to be used as a more robust validation data set \(or additional training data as Arbitrage and Bor pointed out\).

**How much live data is needed to evaluate how overfit a model is? Is a month long enough? How confident could one be with 12 months of live vs 12 months of validation?**

> “One month is definitely not long enough.” — Arbitrage

Submissions to the Numerai tournament are making predictions on a month-long timeframe every week, essentially making the same prediction four times. This means anyone would need at least 12 weeks of performance history to evaluate a model. On top of that, if the model starts during a burn period, it tends to be auto-correlated, meaning it could experience four to eight weeks of continuous burn. “If you encounter that,” Arbitrage said, “you have to wait until it turns positive to see how everybody else does.”

Arbitrage said he hasn’t had the opportunity to experience entering the tournament during a burn period until recently, but he would want to know: if everybody is burning and so is his model, who recovers first? He said that if his model burns longer than the top performing users, it’s an indication that his model isn’t performant.”But that’s like, not scientific at all, just kind of a gut check.”

As for how confident one could be with 12 months of live data versus validation, Arbitrage said: “Not very- this is stocks, this is equities, we have no clue. Look at what happened with Covid-19, it’s a huge regime change right in the middle of all of this, and we have to hope that our models can survive regime changes.”

\*\*\*\*[**Themicon**](www.numer.ai/themicon)**:** I’ve been \[competing\] since 2016, and in the beginning I was changing my model every week and it did not work. I had no idea if it was me or the market or anything like that. I’ve started getting to the point where I think I have something and leave it for three or four months before I go back and look at it. I’d rather create more accounts and try other things on other accounts. I’d say four months at minimum.

Arbitrage echoed his advice to his students from back when the account limit was three: create three different accounts and over time kill the lowest performing one. Just delete it and try a new one. “If you have your own evolutionary process, similar to what Bor is doing but more manual, then you will always improve. It keeps you constantly innovating.” He added that now that the account limit is 10, maybe he would consider dropping the bottom three, but he’s unsure.

**Is live sharpe ratio versus validation sharpe ratio a good way to measure how overfit my model is?**

Arbitrage said that in general, yes, data scientists can use sharpe ratio to determine how overfit a model is but noted that the direct measure suggested in the question doesn’t work. A live sharpe ratio of 1 to a validation sharpe of 2 does not equal a 50% overfit, for example, because that could be the result of spurious correlation. “In general, comparing your in sample to out of sample will always give you an indication of whether you’re overfit but it’s not a direct measure.”

**If my model performs better or worse live compared to validation, how can I determine if it’s due to over/underfitting, market regimes, liking/disliking my model, or feature exposure?**

> "You can't." - Arbitrage

Arbitrage explained that because it’s live stock data, he doesn’t believe tournament participants can infer much about why models behave the way they do. The validation data is such a small subset of the larger data set: equities change by the minute and the tournament prediction time frame is a month long. This is why Arbitrage encourages his students to take a long view and to aim for something stable.

**What criterion should one consider when choosing their stake on MMC or correlation? More generally, does it make sense to still allow staking on correlation?**

Arbitrage believes it’s still too soon to compare staking on MMC to correlation. “I had some crazy high scores on correlation,” he said, “like 12% for three weeks in a row, and I don’t think I’ve ever seen a score that high on the MMC side.”

He’s in wait and see mode: “I’m going to wait and take a better look at it,” he said, adding “I would probably look at my MMC after a month, and if I had an indication that while all models are doing well, I’m also getting a high MMC, that would probably be your clue to look at burns: if everybody’s burning, how did your model do relative?”

In the past, Arbitrage said data scientists would look at where they were positioned in the burn group \(whether they saw some of the worst burns or closer to the middle\) and used that as a way to gauge variance relative to other models. His advice: have patience because results take time and to pick a stake and stick with it for a while.

**Can you create virtual eras to simulate a financial crash or economic boom or whatever? I’d like to know how my model fights against all odds.**

> “If only we could create such a thing.” — Arbitrage, full of sorrow

Arbitrage explained that he didn’t think it would be possible to create a synthetic data set because outside of Numerai, no one knows what the target or feature columns represent. Simulations of different economic conditions would have to be created by Numerai. “But honestly, I don’t really care. I want my model to be good on average. It seems like we all did pretty well during the recent selloff, and like we all recovered well, so it seems that on average we’re doing pretty good.”

He added that if you’d like Numerai to create something like this, suggesting it in their [Feedback channel](https://community.numer.ai/channel/feedback) is a good way to raise it to the team.







### External staking

**Will Numerai offer a route for non-participants to stake on participants’ models for a fee paid to them and to Numerai?**

“The purpose of the staking is to see if you believe in your model,” Richard said, “so if you’re staking someone else, and you’ve never seen any code and you don’t know data science, your stake is just based on some leaderboard information… It doesn’t give us very much information.”

He added that if someone is interested in NMR, they can hold NMR without being a data scientist, and if they’re not a data scientist, that’s what you can do. But regarding the tournament, Numerai wants the stakes to be meaningful and express information about the models without giving the model to them.

On top of that, Richard explained that there are legal risks in trying to have the token represent the cash flow of the hedge fund. Right now, NMR is an abstraction of user performance and there are many levels between that and the performance of the hedge fund. During those stages, Numerai performs ensembles, optimizations, trade implementations, and other transformations that aren’t part of the tournament modeling.

> “I see it more like we’re buying signals: we’re buying data from our users and they’re staking on the quality of their data, rather than we’re investing in their hedge fund.” -Richard Craib

**It would be a nice feature to stake on other users’ models. Do you plan such a feature?**

This will never happen because it’s too close to gambling to be within regulation.





### General data

**Does it make sense to use nonlinear dimensionality reduction methods in Numerai? If so, why and which are the most scalable?**

Arbitrage said that he doesn’t do any dimensionality reduction in his model, nor does he tell his students to do so. Because it’s a clean data set, so Arbitrage is of the mindset that Numerai is giving the data scientists data that’s ready to go, so why would he want to do anything to it? “Especially when the signal is so low,” he said, “any transformation you make risks blowing up the signal.”

Michael O agreed, adding that one way to see what trees are doing is to expand dimensionality, which seems to work better than any nonlinear dimensionality reduction. He concluded that if anything, expanding dimensionality would work better before reducing it.

**The data is encrypted — is it really homomorphic? Are some mathematical properties lost? Our models may be tricked! Is there anything to avoid?**

**Richard:** The homomorphic thing comes up so much, I think it’s a cool word. When we first launched … the homepage said ‘structure-preserving encryption’ in December 2015, but the Medium post said ‘using encryption techniques like homomorphic encryption’ and people really latched onto us using precisely homomorphic encryption schemes. Which I did try to do, and I had the data encrypted in this way, but it turned one megabyte of data into 16 gigabytes.

The data went from normal nice numbers like you have now to very high dimensional polynomials that you had to operate on.To any normal data scientist, or even expert data scientists, it looked so weird to have these strange polynomials that you have to operate on. So I decided not to launch with that, and instead went with a different kind of obfuscation. Encryption implies that there’s a key that if you had, you could unlock it, but the data is really just obfuscated.

The other important thing to note is that there are so many phases between the raw data and the obfuscated data. The raw data, you could understand, but in the middle, just the normalization stuff that we try to do to clean the data is taking away a lot of the structure of the original data. But it makes it more normal and makes eras look more alike than they would otherwise.

If we gave away our normalized data and didn’t even do the final obfuscation, I think people would still be really confused about what it was. Maybe if you were an expert who had the exact same data, you would be able to tell something.

**If models are mostly a random walk, what value do they provide?**

Arbitrage’s position is that data scientist performance should approximate a random walk because the models are predicting equities, meaning it’s unlikely to find a strategy that will stay above zero for very long. He mentioned one of Richard’s forum posts about autocorrelation and checking to see if performance is stationary or not.

“Hopefully,” Arbitrage said, “we’re doing a random walk and all of us, individually, are random and none of us are correlated. Because then the signal would be performant if you averaged across all of us.” Basically, each model hopefully has a period of high performance, and by averaging across all of the models and filtering out the noise, the resulting meta model should be performant.

The idea is that during the periods of high performance, a model was right at that time. By building a model on top of all of the performant periods of other models, the meta model carries the edge. Ideally, each individual wouldn’t have an edge, but then Numerai would be able to extract the edge from each model.

 **Would you recommend using the data from previous rounds for training and validation?**

Arbitrage pointed out that there is no data from previous rounds. The training data doesn’t change, and the validation data doesn’t change \([although more data was recently added](https://forum.numer.ai/t/validation-2-announcement/166)\). And while many people request having old tournament data converted into training data, “it would just cause us to overfit.”

He added that he doesn’t want more data, finding what is currently offered to be sufficient as long as it remains indicative of the market. He also recommends against using older tournament data as training data because anything you add will change your model, and [stationarity is important](https://forum.numer.ai/t/performance-stationarity/151/2).

**Do feature interactions make sense for feature engineering?**

Arbitrage pointed out that tree models take into account interactions and are also performant in the tournament, so feature interactions matter. “Would I want to create my own? I’ve tried that before, very early in the tournament, and it never worked out. But this was three years ago, I haven’t done it since.”

He thinks interactions make sense, but is unsure that, with the way the tournament data is constructed currently, it’s conducive to create your own features \(because tree models and neural nets do it on their own\).

**Should you Z score the features by eras before interaction? Could you use a neural net to find which new features to use?**

Arbitrage passed the mic to Bor for his insight after building a complex genetic algorithm for the tournament.

Bor runs his model once to generate a series of solutions and excludes the features that have the highest correlation. He repeats this several times then takes the average of all of those models \(similar to what tree models and neural nets do themselves\).

Ultimately, Arbitrage and Bor agree that some feature engineering makes sense, with Bor adding that his manual process is similar to what neural networks would be doing.

### General

**What are the differences between the various** [**Integration Test**](https://numer.ai/integration_test) **accounts?**

As Numerai engineer Jason explained to Arbitrage, the Integration Test accounts are the same example model but submitted on different days of the week to test the system.

**Jason:** Yeah that is true, that’s exactly what that is.

**Does Numerai pay more attention to models with higher stakes when building the meta-model?**

The Meta-Model is stake weighted so this does mean that more “attention” is placed on models with higher stakes. MMC2 provides a path for this to change, so this question may be amended at a future date.

**Does the meta-model perform so well that Numerai can afford to keep paying data scientists when they run out of their NMR reserves?**

Arbitrage explained that the whole purpose of the Numerai tournament is to increase the performance of the meta-model in such a way that Numerai pays the data scientists more - it's a positive feedback loop. If Numerai also reaches a significant amount of assets under management \(hypothetically $100b\), and takes a 1% management fee, Arbitrage is confident some of that revenue would find its way to the data scientists.

**When will Numerai change the current training and validation data sets and move on to the next tournament?**

Mr. Numerai himself Richard Craib stepped in to answer this question.

> **Richard:** We have been thinking about new data: new features and a new target. We talked recently about having a target that's feature neutral _in_ the target. That way you're not paid for any feature exposures. What you would have seen, if we had a feature neutral target, is that those first two months of Kazutsugi would have been kind of normal and people would have made money if they were neutral over that period. But then they wouldn't have made much money in the last month or so where things have gone _really_ well. That's kind of why we gave that feature neutral code away in the[ analysis and tips doc](https://github.com/numerai/example-scripts/blob/master/analysis_and_tips.ipynb). You can tweak it yourself, you can say, 'I want to be 50% neutral,' or, '60% neutral,' it's kind of like deciding how optimized you want your portfolio to be. The more neutral, the better to some extent from some perspective of sharpe. However, as many people have noted, there are diminishing returns. It looks like going beyond 50% neutral starts to cut into your profitability. 
>
> So when we thought about this feature neutral target, which we actually had ready, we decided not to release it and instead tried to make a Kazutsugi-style target without feature neutrality but with a few tweaks that make it a bit better, more performant, and more generalizable. One of the ideas we had is we don't want to make everybody retrain their models if there's only a minor difference in the target, and the other thing is that if we gave out the target, we want models trained on the new target to actually do better than would have even scored against the Kazutsugi target. In a sense, basically, can we make a new target that's strictly better and wouldn't hurt anybody? It feels like we have that, and we're a few days away from feeling like it's ready. It could be within the next few weeks that we put something out as a, "take a look at this," preview. Then everybody will have a chance to play with it to see that it really does help. But, we won't switch to payouts based on it for quite a while. Maybe at the end of June or something, we'll see.
>
> That's what we're thinking in terms of new targets. In terms of new features: we're not going to be adding new features any time in the next month or so, but I think maybe a couple new features by the end of the year but we wouldn't want to completely revamp the whole data set. We like what we have now and don't want anybody to think they'll never see Intelligence 9 again - whatever features we have now will stay ****there.

\*\*\*\*



