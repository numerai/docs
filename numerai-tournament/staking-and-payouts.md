# Staking & Payouts

## Staking

You can stake [NMR](https://www.coinbase.com/price/numeraire) on your model to earn payouts based on performance.

<figure><img src="../.gitbook/assets/image (96).png" alt=""><figcaption></figcaption></figure>

Once staked, NMR will remain locked until you release it back to your wallet which takes 1 month. While pending release, the unstake amount will not count towards upcoming payouts.

<figure><img src="../.gitbook/assets/image (50).png" alt=""><figcaption></figcaption></figure>

You can optionally configure where your earnings go and the score multipliers used to compute your payouts.

<figure><img src="../.gitbook/assets/image (69).png" alt=""><figcaption></figcaption></figure>

## Payouts

Your payout is a primarily a function of your scores. If you have a positive score you will get a payout. If you have a negative score a portion of your stake will burn.

The maximum payout or burn per round is capped at ±5%

```python
payout = stake * clip(payout_factor * (corr * corr_mult + tc * tc_mult), -0.05, 0.05) 
```

`stake` is the your model's stake value at the `close` of the round. This is also referred to the stake value `at-risk` for a round. Your stake value `at-risk` for a round does not include any unstake amounts that are pending release, and is set to 0 if you have no valid submission for a round.

`payout_factor` is a dynamic value that scales inversely with total NMR staked across the tournament, or more precisely the total stake value `at-risk` across the tournament at the `close` of the round.

```python
payout_factor = min(1, 7200 / total_at_risk) 
```

<figure><img src="../.gitbook/assets/image (27).png" alt=""><figcaption></figcaption></figure>

`corr_mult` and `tc_mult` are configured by you to control your exposure to each score. Here are your options.

| corr multiplier options | tc multiplier options  |
| ----------------------- | ---------------------- |
| 1.0x                    | 0.0x, 0.5x, 1.0x, 2.0x |

