---
description: Overview of all definitions and vocabulary used to speak about scoring
---

# Definitions

Described below are the vast majority of definitions for functions and statistical tools used to publish scores. Read the open-sourced code at [numerai-tools/scoring](https://github.com/numerai/numerai-tools/blob/master/numerai_tools/scoring.py). Install the package with:

```bash
> pip install numerai_tools
```

## Statistics

* tie-broken rank
  * [percentile rank](https://en.wikipedia.org/wiki/Percentile_rank) a series
  * break ties based on id / index
* tie-kept rank
  * [percentile rank ](https://en.wikipedia.org/wiki/Percentile_rank)a series
  * for each set of ties set their ranks to the average of that set's tie-broken ranks
* correlation
  * correlation coefficient between two series
* spearman correlation
  * [spearman correlation coefficient](https://en.wikipedia.org/wiki/Spearman's_rank_correlation_coefficient) between live target and predictions
  * different than tie-broken-rank correlation b/c spearman ranking keeps ties by assigning mean rank
* pearson correlation
  * [pearson correlation coefficient](https://en.wikipedia.org/wiki/Pearson_correlation_coefficient) between live target and predictions
  * different that other correlations b/c pearson does not use ranking
* tie-broken-rank correlation
  * correlation between live target and tie-broken ranked predictions (w/ sorted index, no nans)
  * NOTE: This is a pearson correlation, but rank the predictions, so it behaves more like a spearman. It is impossible to achieve 1.0 correlation because targets still have ties but predictions do not.
* variance normalize
  * given vector s, normalize its standard deviation to 1
* power x / pow x
  * given vector s, exponentiate each value of s to some power x, ignoring sign
* gaussianize
  * given vector s, make s unit norm by dividing standard deviation of s
* neutralization
  * given vector s, find the orthogonal component s' WRT a matrix of neutralizers N:
  * s' = s -(N dot (N\_inverse dot s))
* orthogonalize
  * similar to neutralize, but is faster for 2 centered column vectors
  * given vectors u and v, find the component of v that is orthogonal to u:
  * v - (u ⦻ ( dot(transpose(v), u) / dot(transpose(u), u) )
* numerai corr
  * given prediction vector s and target vector t find the correlation between s and t:
    * s\` = tie-kept rank, then gaussianize, then pow 1.5 vector s
    * t\` = pow 1.5 vector t
    * calculate the pearson correlation of s\` and t\`
* feature neutral corr
  * given prediction vector s, matrix of features to neutralize F, and target vector t, find the correlation of s with t after neutralizing to F:
    * s\` = tie-kept rank, then gaussianize s
    * s\`\` = neutralize s\` to F, then variance normalize
    * calculate numerai corr of s\`\` and t
* correlation contribution
  * given target vector t, meta model vector m, and prediction vector s, find how much s contributes to m’s correlation with t:
    * m\` = tie-kept rank then gaussianize m
    * s\` = tie-kept rank then gaussianize s
    * s\`\` = orthogonalize s\` with respect to m\`
  * get the covariance of s\`\` and t

### Factors & Features

* Factors
  * unencrypted (possibly cleaned/formatted/etc.) data from our data providers
  * signals not given to users, but are very well-known in finance
  * we always neutralize targets, portfolios, and the Meta Model to these
* Features
  * encrypted stock market signals given to users for use as machine learning features
  * a dataset is made of several variations of a smaller set of features
  * we usually penalize exposure to these, but are not always 100% neutral
* V3 Features
  * all features used in our v3 "supermassive" dataset
* V4 Medium Safe Features
  * there are 5 feature variations in the v4 dataset
  * only 2 of those variations are included in this subset

### Targets

* weekdays
  * Mon - Fri (20D = 20 Days = 4 weeks)
* returns lag
  * number of days skipped before starting returns calculations
  * (2L = 2 Lag = skip 2 weekdays)
* timeline XDYL
  * scores over X weekdays with Y days of returns lag
* neutralizers
  * factors/features to which the target is neutral
* bins=x
  * values for the target are binned into x distinct bins
* uniformity = x, y, z, …
  * x% of values in outer 2 bins (e.g. 0 and 1)
  * y% of values in next inner 2 bins (e.g. 0.25 and 0.75)
  * z% of values in next inner bin(s) (e.g. 0.5)
  * …
* target\_\[name]\_20
  * timeline: 20D2L
  * bins=5, uniformity=10%, 40%, 50%
  * neutralizers: Common Factors and/or Features
* target\_\[name]\_60
  * timeline: 60D2L
  * bins=5, uniformity=10%, 40%, 50%
  * neutralizers: Common Factors and/or Features

### Meta Models

Meta Models aggregate submissions into a single signal that Numerai uses to trade:

* Stake-Weighted Meta Model (SWMM)
  * A stake-weighted average of Numerai submissions
  * The Numerai Hedge Fund uses this for trading
* Benchmark Meta Model (BMM)
  * A stake-weighted average of Benchmark Models

### Scores

* data lag
  * number of days it takes our vendors to process returns data
  * scores start returns lag + data lag days after a round closes (usually 2+2=4 days)
* MMC - Meta Model Contribution
  * correlation contribution of a submission, SWMM, and target\_cyrus\_20
  * timeline: 20D2L (+ 2 days data lag)
* CORR20v2 - Correlation 20D2L v2
  * numerai corr of a submission against target\_cyrus\_20
  * timeline: 20D2L (+ 2 days data lag)
* CORJ60 - Correlation Jerome 60D2L
  * numerai corr of a submission against target\_jerome\_60
  * timeline: 60D2L (+ 2 days data lag)
* BMC - Benchmark Model Contribution
  * correlation contribution of a submission, BMM, and target\_cyrus\_20
  * timeline: 20D2L (+ 2 days data lag)
* FNCV3 - Feature Neutral Correlation V3
  * feature neutral corr of a submission, V3 Features, and target\_nomi\_20
  * timeline: 20D2L (+ 2 days data lag)
* CWMM - Corr w/ Meta Model
  * s\` = tie-kept rank, then gaussianize, then pow 1.5 a submission s
  * calculate pearson correlation between s\` and SWMM
  * timeline: 4 days data lag / not dependant on returns
* MCWNM - Max Corr w/ Numerai Models
  * Maximum pearson correlation of a submission with any other Tournament submission
  * only compared to other submissions made in the same round
  * timeline: 4 days data lag)/ not dependant on returns
* APCWNM - Average Pairwise Corr w/ Numerai Models
  * Average pearson correlation of a submission with each other Tournament submission
  * only compared to other submissions made in the same round
  * timeline: 4 days data lag / not dependant on returns
