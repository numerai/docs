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

To stake NMR on your model you must first acquire NMR, then use the [Atomic Blockchain Staking](atomic-blockchain-staking.md) flow to fund your Privy embedded wallet, enable your allocation strategy, and configure per-model stake settings.

## Getting NMR

We recommend two places for buying NMR&#x20;

* [Coinbase](https://www.coinbase.com/price/numeraire) - a safe and easy place to buy NMR with USD, GBP, EUR or Bitcoin. A good place to start if you are new to crypto. Availability depends on your region.
* [Uniswap](https://app.uniswap.org/#/swap?outputCurrency=0x1776e1f26f98b1a5df9cd347953a26dd3cb46671) - a decentralized exchange you can use to swap Ethereum based tokens like ETH or USDC for NMR. Requires you to bring your own wallet like MetaMask. Great for DeFi enthusiasts.

Once you own NMR, send it to the Privy embedded wallet address shown on the [V3 Stakes](https://numer.ai/dashboard/v3-stakes) page.

## Atomic Blockchain Staking

Current staking setup and stake management are handled through the standalone [Atomic Blockchain Staking](atomic-blockchain-staking.md) flow. Use that page for:

* enabling and funding your allocation strategy.
* configuring each model's per-round stake.
* choosing Compound or Fixed mode.
* understanding atomic per-round locks, claims, and migration.
* reducing future stake exposure.
* withdrawing idle strategy NMR.
* using the staking v3 API fields for automation.

## Legacy Continuous Staking Payouts

Your payout is primarily a function of your scores. If you have a positive score you will get a payout. If you have a negative score a portion of your stake will burn.

The formula below describes the legacy continuous staking payout function. Atomic Blockchain Staking removes continuous-stake overlap leverage and the legacy per-round clip; see [Atomic Blockchain Staking](atomic-blockchain-staking.md#claims-and-payouts).

The maximum payout or burn per round is capped at +/-5% and uses the following formula:

```
score = corr20 * corr_multiplier + mmc20 * mmc_multiplier
payout = stake * clip(payout_factor * (score), -0.05, 0.05) 
```

* `corr20` and `mmc20` are the 20-day [CORR](scoring/correlation-corr.md) and [MMC](scoring/meta-model-contribution-mmc.md) scores respectively. These are multiplied by their relevant multipliers, which don't change often and can be checked on a round-by-round basis (see the latest round [here](https://numer.ai/round/latest)).
* `stake` is your model's stake value at the `close` of the round. This is also referred to as the stake value `at-risk` for a round. Your stake value `at-risk` for a round does not include idle strategy NMR, and is set to 0 if you have no valid submission for a round.

#### The Payout Factor

The `payout_factor` is a dynamic value that scales inversely with total NMR staked based on the `staking_threshold`.&#x20;

```python
payout_factor = min(1, stake_threshold / total_at_risk) 
```

| Tournament | Stake Threshold |
| ---------- | --------------- |
| Numerai    | 72000           |
| Signals    | 36000           |
| Crypto     | 10000           |

Here is an example of what the Numerai payout factor looks as stake grows:

<figure><img src="../.gitbook/assets/image (35).png" alt=""><figcaption></figcaption></figure>

## Withdrawing NMR

For Atomic Blockchain Staking, see [Withdrawing NMR](atomic-blockchain-staking.md#withdrawing-nmr). Active round stake remains locked until settlement.

## Tax Reporting

We usually release tax reports for the previous year in mid-January. You can find these by hovering over the account icon in the top right > click "Settings" > "TAXES & REPORTS" section.&#x20;
