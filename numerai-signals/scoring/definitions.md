# Definitions

Please refer to the [main definitions docs](../../numerai-tournament/scoring/definitions.md) to understand the basic functions referenced below.

### Targets

* target\_raw\_return\_20/60
  * timeline: 20D2L / 60D2L
  * bins=5, uniformity=10%, 40%, 50%
  * neutralizers: none
* target\_factor\_neutral\_20/60
  * timeline: 20D2L / 60D2L
  * bins=5, uniformity=10%, 40%, 50%
  * neutralizers: Standard Factors
* target\_factor\_feat\_neutral\_20/60
  * timeline: 20D2L / 60D2L
  * bins=5, uniformity=10%, 40%, 50%
  * neutralizers: Standard Factors and other features not listed
* target\_chili\_60
  * timeline: 60D2L
  * bins=5, uniformity=10%, 40%, 50%
  * neutralizers: everything and the proprietary Numerai risk model
  * other adjustments: ADV-weighted and per-level exposure constraints

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

### Meta Portfolio

* neutral weights
  * applying neutralizers matrix and sample weights vector to a submission
* Stake-Weighted Portfolio (SWP)
  * Stake-weighted average of all neutral weights in Signals

### Scores

* submissions are cleaned before used in scoring:
  * drop invalid tickers
  * tie-kept rank the submission
  * fill nans with 0.5
* ALPHA
  * dot product neutral weights with target\_chili\_60
  * timeline: 60 score days w/ 2 days returns lag (+ 2 days data lag)
* MPC - Meta Portfolio Contribution
  * Gradient of the SWP multiplied by the target\_chili\_60 with respect to stakes
  * timeline: 60 score days w/ 2 days returns lag (+ 2 days data lag)
* MMC - Meta Model Contribution
  * correlation contribution of a submission, SNWMMmin10, and target\_factor\_neutral\_20
  * timeline: 20 score days w/ 2 days returns lag (+ 2 days data lag)
* CORRV4 - Correlation v4
  * numerai corr of a submission and target\_factor\_feat\_neutral\_20
  * timeline: 20 score days w/ 2 days returns lag (+ 2 days data lag)
* ICV2 - Information Coefficient V2
  * numerai corr between binned returns and submission
  * timeline: 20 score days w/ 2 days returns lag (+ 2 days data lag)
* RIC - Residual Information Coefficient
  * numerai corr between target\_factor\_neutral\_20 and submission
  * timeline: 20 score days w/ 2 days returns lag (+ 2 days data lag)
* FNCV4 - Feature Neutral Correlation v4
  * submission is tie-kept-ranked then gaussianized then neutralized
  * tie-broken-rank correlation between target\_factor\_feat\_neutral\_20 and submission
  * neutralizers: Standard Factors and V4 Medium Safe Features
  * timeline: 20 score days w/ 2 days returns lag (+ 2 days data lag)
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
