# Definitions

Please refer to the [main definitions docs](../../numerai-tournament/scoring/definitions.md) to understand the basic functions referenced below.

### Targets

* target
  * timeline: 20D2L
  * bins=5, uniformity=10%, 40%, 50%

### Meta Models

* Numerai Crypto submissions are cleaned first by:
  * join on the token universe
  * drop nan and duplicate symbols
  * tie-kept-rank each submission
  * fill nans in each submission with 0.5
* Numerai Crypto Naive-Weighted Meta Model w/ minimum 1 NMR stake (CNWMMmin1)
  * Average of cleaned Crypto submissions with at least 1 NMR stake

### Scores

* submissions are cleaned before used in scoring:
  * drop invalid symbols
  * tie-kept rank the submission
  * fill nans with 0.5
* MMC - Meta Model Contribution
  * correlation contribution of a submission, CNWMMmin1, and target
  * timeline: 20D2L (+ 2 days data lag)
* CORR - Correlation
  * numerai corr of a submission and target
  * 20 score days w/ 2 days returns lag (+ 2 days data lag)
