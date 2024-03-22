# Staking

## Introduction

When you are ready and confident in your model's performance, you may optionally stake it with [NMR](https://www.coinbase.com/price/numeraire) - Numerai's cryptocurrency. "Staking" on a model or submission means locking up NMR during the scoring period of submissions.

By staking on Numerai, for the duration of staked submissions, you give Numerai permission to payout or burn the NMR at stake. After a staked submission finishes [scoring](scoring/), positive scores are rewarded with more NMR, while negative scores cause staked NMR to be _burned_. This serves two functions:

1. "Skin in the game" allows Numerai to trust the quality of staked predictions.   &#x20;
2. Payouts and burns continuously improve the weights of the [_SWMM_](scoring/definitions.md#meta-models).&#x20;

{% hint style="info" %}
It is important to note that the opportunity to stake is not an offer by Numerai to participate in an investment contract, a security, a swap based on the return of any financial assets, an interest in Numerai’s hedge fund, or in Numerai itself or any fees we earn. Users with different expectations should not stake.

**Please read our** [**Terms of Service**](https://numer.ai/terms) **for further information.**
{% endhint %}

## Numeraire (NMR)

NMR is the cryptocurrency that powers staking and payouts on Numerai.

* You can read more about NMR on Github: [https://github.com/erasureprotocol/NMR](https://github.com/erasureprotocol/NMR)
* You can see token statistics here: [https://numer.ai/nmr](https://numer.ai/nmr)

To stake NMR on your model you must first acquire NMR, then deposit it into your [Numerai wallet](https://numer.ai/wallet). When you are ready, you can withdraw it to a given eth address.

## Depositing NMR

We recommend two places for buying NMR&#x20;

* [Coinbase](https://www.coinbase.com/price/numeraire) - a safe and easy place to buy NMR with USD, GBP, EUR or Bitcoin. A good place to start if you are new to crypto. Availability depends on your region.
* [Uniswap](https://app.uniswap.org/#/swap?outputCurrency=0x1776e1f26f98b1a5df9cd347953a26dd3cb46671) - a decentralized exchange you can use to swap Ethereum based tokens like ETH or USDC for NMR. Requires you to bring your own wallet like MetaMask. Great for DeFi enthusiasts.

Once you own some NMR, copy your adress from the [Wallet Page](https://numer.ai/wallet):

<figure><img src="../.gitbook/assets/image (15).png" alt=""><figcaption><p>numer.ai/wallet</p></figcaption></figure>

## Increasing Stake

Head over to [numer.ai/staking](https://numer.ai/staking), and click on the "manage stake" button next to the model on which you would like to stake:&#x20;

<figure><img src="../.gitbook/assets/Screenshot 2024-03-22 at 1.56.52 PM.png" alt=""><figcaption><p>If you're on a smaller screen, you may need to scroll to find this button.</p></figcaption></figure>

This will open the Stake Modal. You can use this to stake NMR from your wallet on your model:

<div align="center">

<figure><img src="../.gitbook/assets/image (107).png" alt=""><figcaption></figcaption></figure>

</div>

## Releasing Stake

Staked NMR will remain locked until you release it back to your wallet, which takes 1 month. Specifically, the NMR will be released at the resolution of your last active round at the time of the request. While pending release, the unstaked amount may still be subject to burns but will not count towards upcoming payouts.

<figure><img src="../.gitbook/assets/image (36).png" alt=""><figcaption></figcaption></figure>

## Payouts

Your payout is a primarily a function of your scores. If you have a positive score you will get a payout. If you have a negative score a portion of your stake will burn.

The maximum payout or burn per round is capped at ±5% and uses the following formula:

```
payout = stake * clip(payout_factor * (corr * 0.5 + mmc * 2), -0.05, 0.05) 
```

`stake` is your model's stake value at the `close` of the round. This is also referred to as the stake value `at-risk` for a round. Your stake value `at-risk` for a round does not include any unstaked amounts that are pending release, and is set to 0 if you have no valid submission for a round.

`payout_factor` is a dynamic value that scales inversely with total NMR staked based on the `staking_threshold`.&#x20;

```python
payout_factor = min(1, stake_threshold / total_at_risk) 
```

| Tournament | Stake Threshold |
| ---------- | --------------- |
| Numerai    | 72000           |
| Signals    | 36000           |

<figure><img src="../.gitbook/assets/image (35).png" alt=""><figcaption></figcaption></figure>

## Withdrawing NMR

When you are ready to withdraw NMR from your Numerai Wallet visit the [Wallet Page](https://numer.ai/wallet), specify an amound, and copy your destination address into the relevant text box:

<figure><img src="../.gitbook/assets/Screenshot 2024-03-13 at 4.42.37 PM.png" alt="" width="375"><figcaption></figcaption></figure>

Finally, click "Next" and wait for the page to show a confirmation. It may take a few moments to complete the transaction, so please be patient.

## Tax Reporting

We usually release tax reports for the previous year in mid-January. You can find these by hovering over the account icon in the top right > click "Settings" > "TAXES & REPORTS" section.&#x20;
