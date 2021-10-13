---
description: >-
  This FAQ is based on the community conversations during Office Hours with
  Arbitrage and is not necessarily verified by Numerai. For the Numerai FAQ, see
  [docs.numer.ai/tournament/faq].
---

# FAQ in Office Hours

## Hedge fund assets

**Can you explain what you think Numerai assets are (market, investment type), by taking into account what little we know, e.g. time over which they mature, etc? (**[**Episode 4**](https://docs.numer.ai/office-hours-with-arbitrage/office-hours-recaps/ohwa-4)**)**

Numerai has previously disclosed that they trade global equities. It has been discussed that the fund is long/short, market neutral, country neutral, sector neutral, currency neutral, factor neutral.

Richard explained that Numerai is a global equities hedge fund driven by the machine learning models of their data science community. They’ve never traded anything besides equity, and they’re, “long/short, market neutral, country neutral, sector neutral, currency neutral, factor neutral… just trying to find the edges that other people can’t find and that aren’t exposed to the risk factors that other funds are exposed to.”

[**Read more**](https://docs.numer.ai/office-hours-with-arbitrage/office-hours-recaps/ohwa-4)

**Since we know little about the assets or how predictions are utilized, why do you think there are historical limits on the hedge fund’s earning capacity? (**[**Episode 1**](https://docs.numer.ai/office-hours-with-arbitrage/office-hours-recaps/ohwa-1)**)**

One of the limits for hedge funds is scale:

> “When you find an edge, trading on it collapses that edge because you’re making it more efficient. When you find an edge in finance, you are therefore finding something that is an inefficiency in the market and by trading on that inefficiency you are closing the profitability of it.” - Arbitrage

This presents a problem for hedge funds in finding a strategy that scales, which is absolutely true for Numerai as well.

[\
**Read more**](https://docs.numer.ai/office-hours-with-arbitrage/office-hours-recaps/ohwa-1)

I**s there a correlation between performance of the VIX (**[**CBOE Volatility Index**](http://www.cboe.com/vix)**) and Numerai’s burn rate? (**[**Episode 4**](office-hours-recaps/ohwa-4.md)**)**

By design, Numerai has taken out these known factors to make it more difficult for anyone to find a correlation. Data scientists therefore can’t tie correlation to the fund’s performance.

[**Read more**](office-hours-recaps/ohwa-4.md)\*\*\*\*

**Is Numerai’s influence on the market itself big enough to make a drop in correlation of our models on live data due to obvious signals from trained data already utilized? (**[**Episode 6**](office-hours-recaps/ohwa-6.md)**)**

Arbitrage said that he can answer both of these questions with one simple observation: all hedge funds that trade equities have to file a [form 13F](https://www.sec.gov/divisions/investment/13ffaq.htm) once they reach a certain threshold of assets under management ($100 million). Numerai has not filed a 13F, so Arbitrage suggests that we can infer it’s not a large hedge fund and therefore is not moving the market.

\*\*\*\*[**Read more**](office-hours-recaps/ohwa-6.md)\*\*\*\*

## Model evaluation

**What’s a good validation sharpe? (**[**Episode 4**](office-hours-recaps/ohwa-4.md)**)**

[Michael P](https://numer.ai/master_key) answered this question, noting that validation sharpes are high values, with the Example Prediction model’s sharpe being around 1.5. Michael added the advice that the Example Prediction sharpe is “verification that you’re calculating things correctly, but you want to calculate your sharpe yourself on the cross validation and training set. You don’t want to rely on the validation sharpe to pick your model because the validation eras are too easy.”

[**Read more**](office-hours-recaps/ohwa-4.md)\*\*\*\*

**How much live data is needed to evaluate how overfit a model is? Is a month long enough? How confident could one be with 12 months of live vs 12 months of validation? (**[**Episode 6**](office-hours-recaps/ohwa-6.md)**)**

> “One month is definitely not long enough.” — Arbitrage

Submissions to the Numerai tournament are making predictions on a month-long time-frame every week, essentially making the same prediction four times.

[**Read more**](office-hours-recaps/ohwa-6.md)\*\*\*\*

**Is live sharpe ratio versus validation sharpe ratio a good way to measure how overfit my model is? (**[**Episode 6**](office-hours-recaps/ohwa-6.md)**)**

Arbitrage said that in general, yes, data scientists can use sharpe ratio to determine how overfit a model is but noted that the direct measure suggested in the question doesn’t work. A live sharpe ratio of 1 to a validation sharpe of 2 does not equal a 50% overfit, for example, because that could be the result of spurious correlation.

[**Read more**](office-hours-recaps/ohwa-6.md)\*\*\*\*

**If my model performs better or worse live compared to validation, how can I determine if it’s due to over/underfitting, market regimes, liking/disliking my model, or feature exposure? (**[**Episode 6**](office-hours-recaps/ohwa-6.md)**)**

> "You can't." - Arbitrage

Arbitrage explained that because it’s live stock data, he doesn’t believe tournament participants can infer much about why models behave the way they do.

[**Read more**](office-hours-recaps/ohwa-6.md)\*\*\*\*

**What criterion should one consider when choosing their stake on MMC or correlation? More generally, does it make sense to still allow staking on correlation? (**[**Episode 8**](office-hours-recaps/ohwa-s01e08.md)**)**

Arbitrage believes it’s still too soon to compare staking on MMC to correlation.

He’s in wait and see mode: “I’m going to wait and take a better look at it,” he said, adding “I would probably look at my MMC after a month, and if I had an indication that while all models are doing well, I’m also getting a high MMC; if everybody’s burning, how did your model do relative to everyone else?”

[**Read more**](office-hours-recaps/ohwa-s01e08.md)\*\*\*\*

**Can you create virtual eras to simulate a financial crash or economic boom or whatever? I’d like to know how my model fights against all odds. (**[**Episode 8**](office-hours-recaps/ohwa-s01e08.md)**)**

> “If only we could create such a thing.” — Arbitrage, full of sorrow

Arbitrage explained that he didn’t think it would be possible to create a synthetic data set because outside of Numerai, no one knows what the target or feature columns represent.

[**Read more**](office-hours-recaps/ohwa-s01e08.md)\*\*\*\*

## External staking

**Will Numerai offer a route for non-participants to stake on participants’ models for a fee paid to them and to Numerai? (**[**Episode 5**](office-hours-recaps/ohwa-5.md)**)**

“The purpose of the staking is to see if you believe in your model,” Richard said, “so if you’re staking someone else, and you’ve never seen any code and you don’t know data science, your stake is just based on some leaderboard information… It doesn’t give us very much information.”

He added that if someone is interested in NMR, they can hold NMR without being a data scientist, and if they’re not a data scientist, that’s what you can do. But regarding the tournament, Numerai wants the stakes to be meaningful and express information about the models without giving the model to them.

On top of that, Richard explained that there are legal risks in trying to have the token represent the cash flow of the hedge fund. Right now, NMR is an abstraction of user performance and there are many levels between that and the performance of the hedge fund. During those stages, Numerai performs ensembles, optimizations, trade implementations, and other transformations that aren’t part of the tournament modeling.

[**Read more**](office-hours-recaps/ohwa-5.md)\*\*\*\*

**It would be a nice feature to stake on other users’ models. Do you plan such a feature? (**[**Episode 8**](office-hours-recaps/ohwa-s01e08.md)**)**

Please see above.

[**Read more**](office-hours-recaps/ohwa-s01e08.md)\*\*\*\*

## General data

**Does it make sense to use nonlinear dimensionality reduction methods in Numerai? If so, why and which are the most scalable? (**[**Episode 4**](office-hours-recaps/ohwa-4.md)**)**

Michael Oliver said that one way to see what [trees](https://en.wikipedia.org/wiki/Decision_tree_learning) are doing is to expand dimensionality, which seems to work better than any nonlinear dimensionality reduction. He concluded that if anything, expanding dimensionality would work better before reducing it.

[Read more](office-hours-recaps/ohwa-4.md)

**The data is encrypted — is it really homomorphic? Are some mathematical properties lost? Our models may be tricked! Is there anything to avoid? (**[**Episode 5**](office-hours-recaps/ohwa-5.md)**)**

**Richard:** "The homomorphic thing comes up so much, I think it’s a cool word. Encryption implies that there’s a key that if you had, you could unlock it, but the data is really just obfuscated. "

[**Read more**](office-hours-recaps/ohwa-5.md)\*\*\*\*

**If models are mostly a random walk, what value do they provide? (**[**Episode 7**](office-hours-recaps/ohwa-7.md)**)**

Arbitrage’s position is that data scientist performance should approximate a random walk because the models are predicting equities, meaning it’s unlikely to find a strategy that will stay above zero for very long. Numerai relies on many different predictions to build a performant meta-model. He mentioned one of Richard’s [forum posts about autocorrelation](https://forum.numer.ai/t/learning-two-uncorrelated-models/400) and checking to see if performance is stationary or not.

[**Read more**](office-hours-recaps/ohwa-7.md)\*\*\*\*

**Would you recommend using the data from previous rounds for training and validation? (**[**Episode 8**](office-hours-recaps/ohwa-s01e08.md)**)**

Arbitrage pointed out that there is no data from previous rounds. The training data doesn’t change, and the validation data doesn’t change ([although more data was recently added](https://forum.numer.ai/t/validation-2-announcement/166)). And while many people request having old tournament data converted into training data, “it would just cause us to overfit.”

[**Read more**](office-hours-recaps/ohwa-s01e08.md)\*\*\*\*

**Do feature interactions make sense for feature engineering? (**[**Episode 8**](office-hours-recaps/ohwa-s01e08.md)**)**

Arbitrage pointed out that tree models take into account interactions and are also performant in the tournament, so feature interactions matter.

[**Read more**](office-hours-recaps/ohwa-s01e08.md)

## General

**What are the differences between the various** [**Integration Test**](https://numer.ai/integration_test) **accounts? (**[**Episode 8**](office-hours-recaps/ohwa-s01e08.md)**)**

The Integration Test accounts are the same example model but submitted on different days of the week to test the system.

[**Read more**](office-hours-recaps/ohwa-s01e08.md)\*\*\*\*

**Does Numerai pay more attention to models with higher stakes when building the meta-model? (**[**Episode 11**](office-hours-recaps/ohwa-s01e11.md)**)**

The Meta-Model is stake weighted so this does mean that more “attention” is placed on models with higher stakes. MMC2 provides a path for this to change, so this question may be amended at a future date.

[**Read more**](office-hours-recaps/ohwa-s01e11.md)\*\*\*\*

**Does the meta-model perform so well that Numerai can afford to keep paying data scientists when they run out of their NMR reserves? (**[**Episode 11**](office-hours-recaps/ohwa-s01e11.md)**)**

Arbitrage explained that the whole purpose of the Numerai tournament is to increase the performance of the meta-model in such a way that Numerai pays the data scientists more - it's a positive feedback loop.

[**Read more**](office-hours-recaps/ohwa-s01e11.md)\*\*\*\*

**When will Numerai change the current training and validation data sets and move on to the next tournament? (**[**Episode 11**](office-hours-recaps/ohwa-s01e11.md)**)**

Mr. Numerai himself Richard Craib stepped in to answer this question.

> **Richard:** We have been thinking about new data: new features and a new target. One of the ideas we had is we don't want to make everybody retrain their models if there's only a minor difference in the target, and the other thing is that if we gave out the target, we want models trained on the new target to actually do better than would have even scored against the Kazutsugi target. In a sense, basically, can we make a new target that's strictly better and wouldn't hurt anybody? That's what we're thinking in terms of new targets. In terms of new features: we're not going to be adding new features any time in the next month or so, but I think maybe a couple new features by the end of the year but we wouldn't want to completely revamp the whole data set. We like what we have now and don't want anybody to think they'll never see Intelligence 9 again - whatever features we have now will stay _\*\*_there.

\*\*\*\*[**Read more**](office-hours-recaps/ohwa-s01e11.md)\*\*\*\*

\*\*\*\*
