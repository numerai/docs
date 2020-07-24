# Meta Model Contribution

## Motivation

Each user is incentivized to maximize their individual correlation score. But Numerai wants to maximize the meta model's correlation score, where the meta model is the stake weighted ensemble of all submissions.

Meta model contribution `mmc` is designed to bridge this gap. Whereas `correlation` rewards individual performance, `mmc` rewards contribution to the meta model's `correlation` or group performance. 

{% hint style="info" %}
If you are a manager of a basketball team, and you already have 4 Shaq O'Neals on your team, would you draft another Shaq as your 5th? Or would rather take a guard like Kobe? 
{% endhint %}

{% hint style="success" %}
In 2019, tree based models like [integration\_test](https://numer.ai/integration_test) have done well and become very popular. Knowing this, how would you design a model that would ensemble well with this group of models?
{% endhint %}

## Calculation

To calculate a user's \(U\) `mmc` for a given round we

* select a random 67% of all staking users \(with replacement\)
* calculate the stake weighted predictions of these users
* transform both the stake weighted predictions, and U's model to be uniformly distributed
* neutralize U's model with respect to the uniform stake weighted predictions
* calculate the covariance between U's model and the kazutsugi targets
* divide this value by 0.0841 \(this step is to bring the expected score up to the same magnitude as correlation\)
* the resultant value is an MMC score 
* repeat this whole process 20 times and keep the average MMC score

## Design Considerations

* Stake weight is necessary to make the system unattackable
* Sampling a random 67% each time is important to incentivize some redundancy.  

  A very large staker submitting similar predictions to yours would penalize you too much if we didn't do this.

## Discussion

Read more about the MMC calculation [here](https://forum.numer.ai/t/mmc2-announcement/93).  
Read more about MMC and profitability [here](https://forum.numer.ai/t/mmc-staking-change-corr-mmc/698).  
Read [this Medium post about MMC](https://medium.com/numerai/a-new-data-science-competition-where-being-different-pays-251c2aecc40a) and the value of originality.

