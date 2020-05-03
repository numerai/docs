# Staking and Payouts

## Motivation

How do we design a payout system that is open, fair, and resistant against [sybil attacks](https://en.wikipedia.org/wiki/Sybil_attack)? 

The answer is staking.

Staking allows Numerai to trust the predictions submitted by users because Numerai knows that it can burn the user's stake if the predictions are junk. In other words, users have "skin in the game".

Staking also gives Numerai a fair way to allocate payouts. Since payouts are a percentage of your stake value, you cannot cheat the payout system by simply creating duplicate accounts.

{% hint style="success" %}
What would the internet look like if every interaction was staked? Read more at [erasure.world](https://erasure.world/)
{% endhint %}

## Managing your stake

You can increase or decrease your stake on the Numerai website by opening the staking modal. 

Increasing your stake will take NMR from your wallet and put it into the stake. Decreasing will take NMR from the stake and back into your wallet.

Changes to your stake do not apply immediately, instead they apply on the `effective_date` as shown on the right.

* Increases apply to the next `Thursday`
* Decreases apply to the next `Thursday + 4 weeks`

![the staking modal](../.gitbook/assets/image%20%2824%29.png)

## Payouts

The payout for each round is based on your `stake_value` as of the first Thursday after the submission deadline. Payouts are rolled back into your stake value at the end of each round on Wednesday. 

For example, if your `stake_value` on round N is `100`, and your `correlation = 0.05`, then your payout will be `+ 5NMR`, which will be applied to your stake value in round N+4.  

{% hint style="warning" %}
Decreasing your stake will lower your `stake_value` in the immediate next round, even though the decrease will only happen 4 weeks later.
{% endhint %}

## Abuse

We reserve the right to refund your stake and void all earnings and burns if we believe that you are actively abusing or exploiting the payout rules.

We will rarely ever exercise this right, as our payout systems are designed to be attack resistant, and we want users to try new ideas without fear of punishment.

If we do detect abuse, we will inform the community about it and explain the actions we take against it. Here is [one example](https://forum.numer.ai/t/leaderboard-bonus-exploit-uncovered/200/8). 

