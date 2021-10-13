---
description: 'If you are NOT a US person, you can ignore this.'
---

# US Taxes

## Background

Every year, the US government requires Numerai to issue a [1099-misc](https://www.irs.gov/forms-pubs/about-form-1099-misc) to every [US person](https://www.irs.gov/individuals/international-taxpayers/classification-of-taxpayers-for-us-tax-purposes) to whom we have paid least $600 in that year. In order to do so, we will need to send you a [W9](https://www.irs.gov/pub/irs-pdf/fw9.pdf) form in order to collect information like your [Taxpayer Identification Number](https://www.irs.gov/individuals/international-taxpayers/taxpayer-identification-numbers-tin) and your mailing address. 

## How do I know if I am a US person?

It is your sole responsibility to determine your tax classification. The IRS has great documentation on this subject [here](https://www.irs.gov/individuals/international-taxpayers/classification-of-taxpayers-for-us-tax-purposes). If in doubt, you should consult your own tax, legal and accounting advisors.  

## **What is considered a "Payout"?**

All tournament related earnings, bonuses, and bounties \(in any currency or token\), transferred from Numerai to your user wallet, is considered a "Payout". 

In the legacy staking and payout system \(before round 183\), each round is accounted for independently. Since a stake only lasted for the duration of a single round, the unburned portion of your stake was released back to your wallet immediately at the end of the round. Any extra payouts were also transferred immediately to your wallet at the end of each round. In this system, only the extra payouts beyond your returned stake is considered a "Payout". 

In the current staking and payout system \(after round 183\), staking is continuous and spans multiple rounds. At the end of each round, the unburned portion of your stake remains in your stake agreement, and any extra payouts are paid into your stake agreement instead of your wallet. "Payouts" only occur when you release NMR from your stake agreement into your wallet beyond what you have staked.

{% hint style="info" %}
In the current system, "Payouts" only occur when you release NMR from your stake agreement into your wallet beyond what you have staked.
{% endhint %}

Below is a simple example of how "Payouts" are calculated in the new system. This user started staking with 100 NMR and his stake starts to steadily grow every week. Later, he decides to take out 30 NMR and uses it to buy himself a new PS5 as a birthday gift. This is not considered a payout as he has not yet released more than his original stake amount of 100. Over the next few months, his stake continues to grow and he even gets awarded a bounty for helping to report a security issue on the website. The bounty payment is considered a "Payout" as it was sent to his wallet. By October, his stake value has grown to 350 NMR, but none of those earnings are considered payouts as they never hit his wallet. When Numerai Signals was released in October, he decided to release 95 NMR from his stake so he can use it to stake on Signals. This is considered a "Payout" as he has now released a total of 30 + 95 = 125 NMR which is 25 NMR more than his original 100 NMR stake. 

| Date | Transaction | Value | Payout |
| :--- | :--- | :--- | :--- |
| 2019-10-31 | Stake increase | 100 | 0 |
| 2020-02-20 | Stake release | 30 | 0 |
| 2020-06-01 | Bounty | 3 | 3 |
| 2020-10-12 | Stake release  | 95 | 25 |

Note: In this new system, Numerai does not always apply payouts / burns immediately at the end of each round. Instead, we "roll up" payouts and burns and only apply them on-chain when we have to in order to optimize gas usage. 

Note: In this new system, each stake's "Payouts" are computed independently. Stakes in the Tournament and Signals are considered separate stakes as they have separate agreements. 

Note: All dates and times refer to the "block\_timestamp" of the transaction, which is the time that this transaction was confirmed on chain. All dates and times are reported in UTC.

Note: The above method for computing "Payouts" is not up for debate.   

## **How is the USD value of a "Payout" determined?**

The USD value of each non-USD denominated transaction is computed by taking the most recent USD price of NMR at the time of the transaction. NMR prices are taken from CoinMarketCap.

Some legacy payouts were denominated in BTC/ETH. The USD value of those transactions were computed in the same way.  

## How do I know if I received more than $600 in "Payouts"?

For your convenience, Numerai will provide you with a historical transaction report with NMR prices and "Payouts" computed.

This report will be available for download at [https://numer.ai/account](https://numer.ai/account) or [https://signals.numer.ai/account](https://signals.numer.ai/account) \(both URLs point to the same/shared account settings page\).

Numerai will also send our email reminders to everyone who has made more than $600 in payouts to fill out the form.

## How do I fill out a W9? 

You can fill out the W9 form in [https://numer.ai/account](https://numer.ai/account) or [https://signals.numer.ai/account](https://signals.numer.ai/account) \(both URLs point to the same/shared account settings page\).

If your W9 information has not changed from previous years, you can simply sign the form to re-use last year's data. If it has changed, you can use the form to update it.

If you have multiple accounts, it is HIGHLY recommended that you merge your accounts before filling out the W9.

## **When should I fill out the W9? When will I get my 1099?**

The deadline for Numerai to send out 1099s is Jan 31. This means we need to collect your W9s by early January. 

Corrections, amendments and late W9s will be processed on a rolling basis. If you need to make any corrections, amendments or late W9 submissions, PLEASE contact us to let us know.

## **How will I get my 1099?**

We will email you a copy and snail mail you a physical copy.

Note: If you did not receive more than $600 in payouts, you will NOT receive a 1099 from Numerai even if you fill out a W9. 

## **How should I file my taxes?**

Numerai and its affiliates do not provide tax, legal or accounting advice. The above material and everything on the website has been prepared for informational purposes only, and is not intended to provide, and should not be relied on for, tax, legal or accounting advice. You should consult your own tax, legal and accounting advisors before engaging in any transaction.

## **Support**

We are here to help. If you have any questions please contact us on rocketchat in the [cryptotax](https://community.numer.ai/channel/cryptotax) channel or email us at support@numer.ai and we will try our best to assist you.

