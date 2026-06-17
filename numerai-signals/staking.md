---
description: How to earn (or burn) NMR with your Signals model
---

# Staking

If your signal has sufficiently low [churn and turnover](scoring/#what-is-churn-and-turnover), you may optionally `stake` [NMR](https://www.coinbase.com/price/numeraire) on your model to earn or burn based on your scores. Staking means locking up your NMR during the scoring period and giving Numerai permission to add payouts to or burn from the NMR at stake.

Use the [Atomic Blockchain Staking documentation](../numerai-tournament/atomic-blockchain-staking.md) for the current staking flow, including the Privy embedded wallet, allocation strategy setup, strategy deposits and withdrawals, per-model stake settings, Compound mode, Fixed mode, and API automation.

{% hint style="info" %}
It is important to note that the opportunity to stake your signal is not an offer by Numerai to participate in an investment contract, a security, a swap based on the return of any financial assets, an interest in Numerai’s hedge fund, or in Numerai itself or any fees we earn. Payouts will be made at our discretion, based on a blackbox target that will not be disclosed to users. Fundamentally, Numerai Signals is a service offered by Numerai that allows users to assess the value of their signals, using NMR staking as a way to validate “real” signals. In return, Numerai uses the staked signals and related data in the Numerai hedge fund. Users with different expectations should not stake signals.

**Please read our** [**Terms of Service**](https://numer.ai/terms) **for further information.**
{% endhint %}

## Payouts

Payouts are a function of your stake value and scores. Please review the [main staking documentation](../numerai-tournament/staking.md) to understand how payouts work generally.

The legacy continuous staking Signals payout function is:

```python
payout = stake * clip(payout_factor * (alpha * 0.3 + mpc * 0.8), -0.017, 0.017)  
```

See the [main staking documentation](../numerai-tournament/staking.md#the-payout-factor) for legacy payout factor details and stake threshold values. See [Atomic Blockchain Staking](../numerai-tournament/atomic-blockchain-staking.md#claims-and-payouts) for the current atomic staking claim and payout flow.
