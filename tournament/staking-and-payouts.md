# Staking and Payouts

## Motivation

How do we design a payout system that incentive aligned and resistant against [sybil attacks](https://en.wikipedia.org/wiki/Sybil_attack)?

The answer is staking.

Numerai wants accurate predictions and is willing to reward it. How much you can earn/burn is a function of your performance and stake. This is also known as having [skin in the game](https://www.amazon.com/dp/B075HYVP7C/).

Staking also gives Numerai a sybil resistant way to allocate payouts. Since payouts are a percentage of your stake value, you cannot game the payout system by simply creating duplicate accounts.

You can start participating in Numerai without staking to learn more about the tournament and about your model\(s\)' performance. When you feel confident in your model\(s\), you can attach some stake to it. The minimum stake value is 0.01 NMR. 

## Managing your stake

You can manage your stake on the Numerai website by clicking 'Manage Stake'. Use this modal to increase or decrease your stake amount, or opt into or out of `mmc`.

![](../.gitbook/assets/image%20%2859%29.png)

Increasing your stake will take NMR from your wallet and put it into the stake. Decreasing will take NMR from the stake and back into your wallet.

Changes to your stake do not apply immediately, instead they apply on the `effective_date` as shown on the right.

* Opting into or out of `mmc` applies next `Thursday`
* Increases apply next `Thursday`
* Decreases impact your `stake amount`next Thursday,  but the funds are only released after next `Thursday + 4 weeks`

/par

Please note that [feature neutral correlation](https://docs.numer.ai/tournament/feature-neutral-correlation) \(`fnc`\) cannot be staked on.

## Payouts

The payout for each round is based on your `stake_value` as of the first Thursday after the submission deadline. Payouts are rolled back into your stake value at the beginning of the next round on Thursday.

For example, if your `stake_value` on round N is `100`, and your `correlation = 0.05` then your payout will be `+ 5NMR`, which will be applied to your stake value in round N+4.

If you have opted into `mmc`, then you are paid for both `correlation` and `mmc`.  `correlation` is always a 1x multiple, but `mmc` could be 0.0x, 0.5x, 1.0x, or 2.0x.

 For example if you have `mmc+corr` selected, and your round scores are `correlation = 0.05` and `mmc = 0.01`, your payout will be `0.06 * stake_value NMR.`

 If instead you have `corr + 2x mmc` selected, for the same round, your payout would be `0.07 * stake_value NMR.`

Note that 2x MMC could be risky!  Be certain of your model's live MMC performance before selecting this option! 

Payouts are capped at plus or minus `25%` per round.

{% hint style="warning" %}
Decreasing your stake will lower your `stake_value` in the immediate next round, even though the decrease will only happen 4 weeks later.
{% endhint %}

{% hint style="info" %}
If you decide to cancel your decrease request, your stake value will go back up to the original value in the immediate next round.
{% endhint %}

Track your payouts with the community-built [Numerai Payouts](https://docs.numer.ai/help/payouts-app) app.

## Compounding

Since there is a new round every week and each round lasts 4 weeks, stake values compound with a 4-week delay.

For example, the stake value of week 6 is based on the previous stake value of week 5 \(110 NMR\) + the payout from week 2 \(-5 NMR\) = 105 NMR.

![](../.gitbook/assets/image%20%2862%29.png)

## Abuse

We reserve the right to refund your stake and void all earnings and burns if we believe that you are actively abusing or exploiting the payout rules.

We will rarely ever exercise this right, as our payout systems are designed to be attack resistant, and we want users to try new ideas without fear of punishment.

If we do detect abuse, we will inform the community about it and explain the actions we take against it. Here is [one example](https://forum.numer.ai/t/leaderboard-bonus-exploit-uncovered/200/8).

