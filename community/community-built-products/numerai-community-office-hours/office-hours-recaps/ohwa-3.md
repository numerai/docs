---
description: March 19, 2020 / Interview with Michael Oliver
---

# OHwA S01E03

**The one where Arbitrage interviews Michael Oliver** _/ Written by_ [_http://twitter.com/mandelliant_](http://twitter.com/mandelliant)\_\_

Arbitrage welcomed [Numerai tournament](https://numer.ai/tournament) data scientist [Michael Oliver](https://twitter.com/the\_moliver) to Office Hours, showing off the questions he prepared in advance.

![“It’s nothing big, just random stuff.” — Arbitrage](https://cdn-images-1.medium.com/max/1600/1\*i7Wc0Q2OYD5hh34DZtm8Cg.gif)

As part of Office Hours, Arbitrage introduced a new segment where he interviews other Numerai users, and Michael had the honor of being the first. After the short introduction, Arbitrage dove right into the questions.

**Arbitrage:** How did you first hear about Numerai?

**Michael:** It was a while back, I think 2016, I read an article and thought, “hey that sounds like a good idea and kind of fun.” I procrastinated working on my thesis by spending way too much time building models for the data back then.

**Arbitrage:** I resemble that comment.

**Michael:** \*Laughs\* Yeah, I found out about \[Numerai] and played with it for a while, but it was taking up too much of my time. I made like, $6, so I kind of forgot about it — this was before NMR existed. I thought, “I should get my $6,” and found out I had a bunch of NMR, and that sucked me back in.

**Arbitrage:** And here we are, right? I quit for a while then heard about the token coming out and saw I was supposed to get like, 1200 NMR, and thought that’s pretty cool.

**Michael:** Yeah, and I didn’t find out about \[NMR] until like, a year after it came out… This happened before I really understood anything about cryptocurrencies, so it forced me to learn about that stuff.

**Arbitrage:** I’ve heard that too, from other users.

**Michael:** Yeah I had to learn about how to use cryptocurrencies and move them around and such.

**Arbitrage:** What are the names of your three primary accounts?

**Michael:** There’s [Niam](https://numer.ai/niam), [NMRO](https://numer.ai/nmro), and [MDO](https://numer.ai/mdo) (which is my original account).

**Arbitrage:** Are you up to ten accounts yet?

**Michael:** No, you still need email addresses and I didn’t want to make ten email addresses.

**Arbitrage:** If you have gmail, you can just add, “+test1, +test2”

**Michael:** Oh yeah, I forgot about that! I’ve been working on some things that I want to test, but couldn’t figure out how to do it.

**Arbitrage:** You kind of answered my next question, “When did you start participating?” And that was around 2016 — do you remember what month?

**Michael:** \*Looking up his account\* [MDO woke on July 11, 2016.](https://numer.ai/mdo)

**Arbitrage:** What’s MDO’s rank?

**Michael:** Well, it fell a lot today …

**Arbitrage:** Yeah, we’ll talk about that.

**Michael:** Niam is my best account and he fell a lot today too.

**Arbitrage:** Yeah it was a bloodbath.

**Michael:** He just got back into the top 25 staked accounts, but fell un-staked to 60th.

**Arbitrage:** You mentioned you live in the Seattle area — would you mind telling folks what you do for a living?

**Michael:** I’m a computational neuroscientist; I work at the Allen Institute for Brain Science, which is a non-profit research institute, and my actual job title there is scientist. I analyze data that they collect — they collect a lot of data from mice — and the data I work with is mostly from the visual cortex. I try to build models to figure out what are the functional properties of neurons in the visual cortex that we record. Basically trying to build models from the stimuli of the pixels and the stimuli of the screen you show \[the mice] to the responses we record and trying to figure out what it all means.

![Same.](https://cdn-images-1.medium.com/max/1600/1\*X5fJuqDnt7nvFa\_d8x3UKA.gif)

**Arbitrage:** I don’t even know what to say — that’s amazing.

**Michael:** It’s basically building neural networks to understand real neural networks.

**Arbitrage:** I mean, if it’s a dendron, if that’s what we’re using, then it should work, right?

**Michael:** I hesitate to draw too many direct analogies, because when you get into this world of building complicated, function-approximators to model complicated functions, there are many different neural architectures that can approximate the same function reasonably well. Trying to figure out what is relevant and what is not is a tricky thing. The model selection problem in science is a tricky one. One of the nice things about things like finance and whatnot is that no one cares -

**Arbitrage:** \*Laughs\* Hey….

**Michael:** I mean, especially in this competition, we have all of these features and we don’t even know what they mean. So it’s like, “Interpretation? What? Ah, who cares.”

**Arbitrage:** That’s that I tell my students all the time: “Who cares? I don’t know what it is either.”

_Author’s note: in_ [_Office Hours with Arbitrage #1_](https://docs.numer.ai/office-hours-with-arbitrage/office-hours-recaps/ohwa-1)_, he mentioned using the Numerai tournament with the students in his Financial Machine Learning course._

**Arbitrage:** What programming language do you use and why?

**Michael**: I use [Python](https://www.python.org/). I spent a lot of time in Matlab in grad school, because that’s what was best to use back then, but I was there for the takeover of Python in scientific computing. What really brought me to Python was the GPU libraries like Theano originally (which sadly no longer exists). Most recently I’ve been using [PyTorch](https://pytorch.org/) a lot, which is fantastic. Doing neural network stuff, you basically have to use GPUs if you want to finish anything in a reasonable amount of time. The GPU libraries for Python are basically the best there are in any language, just in terms of the depth of the ecosystem.

Automatic differentiation in these things is amazing because you can write your crazy class functions — which are irrelevant for \[the Numerai] tournament because you can write a function to optimize Sharpe, and you don’t have to pick out the gradients because it will do it for you… Things are so much nicer now than when I was doing neural network stuff in Matlab where you had to do the gradients for all of your functions by hand to make sure they’re right. This is tricky because things will work even when they’re not right.

I believe there are papers in the neural network literature that were inspired by people realizing their buggy code still worked. One paper showed that some arbitrary linear transform of the gradient will work just as well as the actual gradient for training a neural network. That’s kind of weird and interesting.

**Arbitrage:** Yeah, I’m teaching machine learning in my finance class, and it’s completely out of domain. I showed them what a binary classifier would represent: if a 1 is a dog, and a 0 is a cat, and you show it a fish, it’s going to determine if it’s a cat or a dog. And so I think we still have that kind of problem at a very base level with what we’re doing with machine learning.

**Michael:** As a biological vision and semi-computer vision person, it’s been kind of surprising to see how well a lot of these artificial vision systems are working and it’s showing us that the problem is actually a bit easier than we might have thought. What these things are doing are really good texture classifications. They’re really good at understanding complex combinations of features and textures, but whole-object understanding is still a ways off. That’s why they can be fooled fairly easily: if you paint a car with a leopard pattern, it will classify it as a leopard with very high probability because it’s looking for these higher order features but doesn’t have any object understanding.

It’s a problem because if you have the right combination of features, like a goldfish but it has some features a cat might have, \[a neural network] might think it’s a cat because it has the cat features \[the network] is looking for.

**Arbitrage:** Yeah, it may not be confident, but it’s going to tell you if it’s one or the other.

**Michael:** It might even be confident! It might just be an adversarial fish.

**Arbitrage:** What are your top 3 tips for users new to the tournament?

**Michael:**

1. **Use eras for cross-validation**, that’s definitely something that’s easy to overlook.
2. **Read the documentation of** [**scikit-learn**](https://scikit-learn.org/stable/) so you actually know what the functions you’re using are actually doing. For example, the \`time series cross-validation\` routine can take a \`groups\` argument, but it doesn’t use it, it completely ignores it. So if you feed the data in and use a time series cross-validation, it will not split things into eras even if you fed it a list of groups. It says this in the documentation, but even if you read that you might assume it works because it takes the argument in.

![](https://cdn-images-1.medium.com/max/1600/1\*nr3\_bH5QZMu4OFkF0Sc6iw.png)

_Read more about using scikit-learn in the ‘_[_Working with Numerai data and SKLearn_](https://github.com/numerai/example-scripts/blob/master/Working\_with\_Numerai\_data\_and\_SKLearn.ipynb)_” notebook._

1. **It takes a long time to validate a model.** Models will be better for a while and work for a while, but I have spent a lot of time changing models based on a couple weeks’ performance which I’m not sure was the best use of my time. A model might be overall better, but can perform worse for a few weeks. You have to shoot for the long game, and it can be hard to do.

It can be hard to validate your model within the data set we have because it’s not a lot of data.If you divide it up by era, it’s really 132 eras you can use for training and it’s not a ton.

**Arbitrage:** Who’s your favorite team member?

**Michael:** Who’s my favorite team member? You mean out of the Numerati people?

**Arbitrage:** Sure, we’ll call them the Numerati.

**Michael:** Well….

**Arbitrage:** \*_Laughing_\* Look how cautious he’s being!

**Michael:** At [ErasureCon](https://www.youtube.com/watch?v=zeGx7gVgK0o\&list=PLz3D6SeXhT3tHxfgCT5i3XqSmcHAv6BLo) where I met you, I also met [Mike](https://numer.ai/master\_key) who joined the team, and you guys are the ones I spent the most time with and I like both of you. I really like [Richard’s](https://twitter.com/richardcraib) interactions, I always find them interesting.

**Arbitrage:** You have to pick one!_“_

![There can be only one” — Arbitrage](https://cdn-images-1.medium.com/max/1600/1\*Y63cTWb4cltpKrI4TCkShQ.jpeg)

**Michael:** I have to pick one?! It’s tricky — I wish Ralph interacted more because every time I have a conversation with him or hear him talk about something, I feel like I learned something. He knows a lot more about a lot of things than I do, so I feel like I always learn from Ralph.

**Arbitrage:** Alright, alright, I’ll let you non-answer, I’ll let you off the hook.

**Michael:** Yeah that was kind of a non-answer. It’s hard to pick! And of course there’s Anson ([Slyfox](https://numer.ai/slyfox)) who’s always so helpful with everything.

**Arbitrage:** \*_Laughing_\* How many beers did you drink at [ErasureCon](https://www.youtube.com/watch?v=zeGx7gVgK0o\&list=PLz3D6SeXhT3tHxfgCT5i3XqSmcHAv6BLo)?

**Michael:** \*_Also laughing_\* I kind of stopped counting.

**Arbitrage:** Alright, maybe you can help me with this next one: how many beers did **I** drink at [ErasureCon](https://www.youtube.com/watch?v=zeGx7gVgK0o\&list=PLz3D6SeXhT3tHxfgCT5i3XqSmcHAv6BLo)?

**Michael:** It was comparable.

**Arbitrage:** What’s the number one feature request or improvement you have for the tournament?

**Michael:** I know a lot of the improvements I want to happen are in the pipeline, such as multiple accounts and better graphing and data visualization on the website. Now, based on a conversation I had with Mike P the other day, I’m interested in their new data pipeline. It’s apparently going to be really cool when they tell us about it, which makes me wonder if they added pandemic features or something. I feel like something interesting is coming.

The reputation system still hasn’t been switched over (at the time of recording), I think it was supposed to go live on March 4th or something. But I’d rather have it done right than have to fix it.

If you’re passionate about finance, machine learning, or data science and you’re not competing in [the most challenging data science tournament in the world](https://numer.ai/tournament), what are you waiting for?

Don’t miss the next Office Hours with Arbitrage — you never know who might join. Follow [Numerai on Twitter](http://twitter.com/numerai) or join the discussion on Rocket.Chat for the next time and date.

![Pictured: happy data scientists](https://cdn-images-1.medium.com/max/1600/1\*cN6GC2Of9VLDne5e2Jjtrw.png)

_Thank you to_ [_Arbitrage_](https://numer.ai/arbitrage) _for hosting Office Hours, and to_ [_Michael Oliver_](https://numer.ai/mdo) _for the Q\&A. Shout out to_ [_NJ_](https://twitter.com/tasha\_jade) _for joining the call._
