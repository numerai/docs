# Definitions

Please refer to the [main definitions docs](../../numerai-tournament/scoring/definitions.md) to understand the basic functions referenced below.

### Targets

* target\_20d
  * timeline: 20D2L
  * bins=5, uniformity=10%, 40%, 50%
  * neutralizers: Standard Factors and other factors not listed
* target\_20d\_factor\_neutral
  * timeline: 20D2L
  * bins=5, uniformity=10%, 40%, 50%
  * neutralizers: Standard Factors and other factors not listed
* target\_20d\_factor\_feat\_neutral
  * timeline: 20D2L
  * bins=5, uniformity=10%, 40%, 50%
  * neutralizers: Standard Factors and other features not listed

### Meta Models

* Signals submissions are cleaned first by:
  * tie-kept-rank each submission
  * fill nans in each submission with 0.5
  * tie-kept-rank each submission
  * gaussianize each submission
* Signals Stake-Weighted Meta Model w/ minimum stake (SSWMM)
  * Stake-weighted average of cleaned Signals submissions
* Signals Naive-Weighted Meta Model w/ minimum stake (SNWMM)
  * Average of cleaned Signals submissions
* Signals Naive-Weighted Meta Model w/ minimum 10 NMR stake (SNWMMmin10)
  * Average of cleaned Signals submissions with at least 10 NMR stake

### Scores

* submissions are cleaned before used in scoring:
  * drop invalid tickers
  * tie-kept rank the submission
  * fill nans with 0.5
* MMC - Meta Model Contribution
  * correlation contribution of a submission, SNWMMmin10, and target\_20d\_factor\_neutral
  * timeline: 20D2L (+ 2 days data lag)
* CORRV4 - Correlation v4
  * numerai corr of a submission and target\_20d\_factor\_feat\_neutral
  * 20 score days w/ 2 days returns lag (+ 2 days data lag)
* ICV2 - Information Coefficient V2
  * spearman correlation between binned returns and submission
  * 20 score days w/ 2 days returns lag (+ 2 days data lag)
* RIC - Residual Information Coefficient
  * spearman correlation between target\_20d\_factor\_neutral and submission
  * 20 score days w/ 2 days returns lag (+ 2 days data lag)
* FNCV4 - Feature Neutral Correlation v4
  * submission is tie-kept-ranked then gaussianized then neutralized
  * tie-broken-rank correlation between target\_20d\_factor\_feat\_neutral and submission
  * neutralizers: Standard Factors and V4 Medium Safe Features
  * 20 score days w/ 2 days returns lag (+ 2 days data lag)
* CWSNMM - Corr w/ Signals Naive Meta Model
  * s\` = tie-kept rank, then gaussianize, then pow 1.5 a submission s
  * calculate pearson correlation between s\` and SNWMM
  * timeline: 4 days data lag / not dependant on returns
* MCWSM - Max Corr w/ Signals Models
  * Maximum pearson correlation of a submission with any other Signals submission&#x20;
  * only compared to other submissions made in the same round
  * timeline: 4 days data lag / not dependant on returns
* APCWSM - Average Pairwise Corr w/ Signals Models
  * Average pearson correlation of a submission with each other Signals submission
  * only compared to other submissions made in the same round
  * timeline: 4 days data lag / not dependant on returns
