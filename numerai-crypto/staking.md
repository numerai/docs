# Staking

You can optionally `stake` [NMR](https://www.coinbase.com/price/numeraire) on your model to earn or burn based on your `MMC` scores. Staking means locking up NMR in your Numerai Wallet on the [Ethereum](https://ethereum.org/en/whitepaper/) blockchain. For the duration of the stake, Numerai is given the permission to add payouts to or burn from the NMR locked up.

You can manage your stake on the website. When you increase your stake, NMR is transferred from your wallet to the staking contract. When you decrease your stake, NMR is transferred from the staking contract back into your wallet after a \~4 week delay. You can also change your stake type, which determines which scores you want to stake on.

![](https://docs.numer.ai/~gitbook/image?url=https:%2F%2Fgblobscdn.gitbook.com%2Fassets%252F-LmGruQ_-ZYj9XMQUd5x%252F-MTwWeGztnW6NaH6Sd_A%252F-MTxK8xvV36McXIClWAt%252Fimage.png%3Falt=media%26token=aea91c60-7079-439b-bbd6-f64e9d8c26d7\&width=768\&dpr=4\&quality=100\&sign=c26f0dc43daabd09b8834fe5fa0d22f7e105ca7c1b17f4fb0c4b1aa5c8ff0b2e)

{% hint style="info" %}
It is important to note that the opportunity to stake your signal is not an offer by Numerai to participate in an investment contract, a security, a swap based on the return of any financial assets, an interest in Numerai’s hedge fund, or in Numerai itself or any fees we earn. Numerai's hedge fund has no relation whatsoever to Numerai Crypto, it does not trade cryptocurrencies, and does it does not use the Numerai Crypto Meta Model. Payouts will be made at our discretion, based on a blackbox target that may not be disclosed to users. Fundamentally, Numerai Crypto is a service offered by Numerai that allows users to assess the value of their CryptoSignals, using NMR staking as a way to validate “real” signals. Users with different expectations should not stake.

**Please read our** [**Terms of Service**](https://numer.ai/terms) **for further information.**
{% endhint %}

## Payouts

Payouts are a function of your stake value and scores. The higher your stake value and the higher your scores, the more you will earn. If you have a negative score, then a portion of your stake will be burned. Payouts are limited to ±5% of the stake value per round.

```python
payout = stake_value * payout_factor * mmc
```

The `stake_value` is the value of your stake as of the `close` of the round, minus and pending releases, and 0 if you have no submission.

The `payout_factor` reduces logarithmically as the total NMR staked grows over the `stake_cap_threshold.`See the values of `stake_cap_threshold` [here](../numerai-tournament/staking.md#the-payout-factor).
