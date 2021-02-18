---
description: 'From September 17, 2020 / Michael Oliver round two'
---

# OHwA S03E02

For the second episode of Season Three, longtime competitor and now Numerai team member [Michael Oliver](https://numer.ai/mdo) returned to talk about [Target Nomi](https://forum.numer.ai/t/new-target-nomi-release/959), the latest iteration of the Numerai tournament.

![Kazutsugi vs Nomi](../../../.gitbook/assets/target-nomi.png)

The full interview and discussion with Michael Oliver on Target Nomi will be published on YouTube.

### Questions from Slido

**When new Corr + MMC leaderboard?**

Michael Oliver: Soon!

**All else being equal, are models trained on the new target always better than those trained on the current targets? Does blending old and new models make sense?**

Michael Oliver said that there's no guarantee that every model will perform better on the Nomi targets, but his testing seems to indicate that's the case.

You could blend results from a model trained on each, but Michael Oliver doesn't think there's a compelling reason to do so.

**How will you test on live data that the predictions made on the new target are more useful? Some people will train on the old target, some on the new one?**

Michael Oliver explained that because the targets represent the same underlying signal, the introduction of Nomi predictions should blend nicely together with the Kazutsugi predictions and gradually move the meta-model performance in the right direction as users switch over. 

**Are significant differences between validation mean and feature-neutral mean representative of the quality of the model? If so, is there a minimum ratio to aim for?**

Put another way - if there's a small difference between the two, is that a good thing or a bad thing? Or if it's good to be close, what should users aim for?

Michael Oliver said it's a question of how much risk a user is willing to take on. "If your validation mean is much higher than your feature-neutral mean, that means you have a lot of feature exposure," he said, "which means you have a lot of feature risk and your model is pretty linear."

He concluded with, "whether or not that's good is an empirical question. I wouldn't do it."

[Richard](https://twitter.com/richardcraib) added that one way of thinking about feature-neutral mean is as the score you get when taking on **no** risk. "That's clearly better than returns that come from risks," he said. 

> "Your feature-neutral score is always going to tell you how rich your model is in actual alpha." - Richard

**Has Numerai seen a significant jump in average participant validation metrics after the release of the new diagnostic section?**

> "Yeah." - Richard Craib

Richard explained that because the new diagnostics make the average user more aware of what they're doing so they can improve themselves, the meta-model performance since March has continued to improve. 

**What kind of improvements in our predictions do you think the new target will lead to? E.g. better at predicting extremes / overall Spearman / etc?**

Michael Oliver explained that Nomi targets have a different distribution so the extreme values \(0, 1\) are only going to be 5% of the targets per era \(previously they were each 20%\). He said that 0.25's and 0.75's will each be 20%, and that 0's would be 50%. In terms of correlation, the models seem to perform almost identically but with lower volatility for your score on the new targets. 

**When feature neutralization tutorial** [**on Twitch**](https://www.twitch.tv/prof_jtaylor)**?** 

Arbitrage is working through some technical challenges, but hopes to have one soon.

**Did the change from three to ten models help \[improve the meta model\]?**

Richard said that they're not entirely sure because multiple changes are happening at the same time, but he does think it's all helping. 

**Why don’t convolutional neural nets and LTSM neural networks work very well with Numerai data?**

Michael Oliver said that every algorithm you could use has an inductive bias, and just because you can fit one to a data set, doesn't mean it's a good algorithm for generalizing. "If you're using convolutional neural networks," he said, "you should be thinking, 'why do I think there's some kind of invariant structure along the dimensions I'm convolving?'"

He explained that in processing an image, it makes sense that a given feature would work on several locations within that image. The Numerai data set, on the other hand, is a set of features in no particular order. "What dimension would you convolve over?" Michael Oliver asked. "And for LTSMs; it is a time series problem to some degree, but you know the correspondences so making an LTSM work seems fraught at best."

**Isn’t it disingenuous for Michael Oliver to post a little tweak to`sklearn.model_selection.TimeSeriesSplit` in the forum and claim he has open sourced his model?** 

Michael Oliver provided the exact code he used to create the model and included the same parameters that he does a search over. "There's no benefit for anyone else to have more than that." 

Richard added that the important thing is explaining how the solution was found.

_If you’re passionate about finance, machine learning, or data science and you’re not competing in_[ _the most challenging data science tournament in the world_](https://numer.ai/tournament)_, what are you waiting for?  
  
Don’t miss the next Office Hours with Arbitrage : follow_[ _Numerai on Twitter_](http://twitter.com/numerai) _or join the discussion on_[ _Rocket.Chat_](https://community.numer.ai/home) _for the next time and date.   
  
Thank you to_ [_Michael Oliver_](https://numer.ai/mdo) _for talking about Nomi, to_ [_Richard_ ](https://twitter.com/richardcraib)_for joining and contributing to answers,_ _and to_ [_Arbitrage_](https://numer.ai/arbitrage) _for hosting._











