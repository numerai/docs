# Atomic Blockchain Staking

Atomic Blockchain Staking (ABS) is Numerai's new blockchain-native staking system. It is also referred to as "v3 staking". It locks NMR atomically per round, tracks each model's stake independently, and lets resolved stakes be claimed when a round resolves. ABS is currently only supported for [Numerai Crypto](https://app.gitbook.com/s/-LmGruQ_-ZYj9XMQUd5x/numerai-crypto "mention") with support for other tournaments coming soon.

You can interact with ABS on the [Dashboard](https://numer.ai/dashboard) > **V3 Stakes page:**, which allows you to connect to your wallet and manage your staking strategy:

<figure><img src="../.gitbook/assets/Screenshot 2026-06-18 at 10.37.43.png" alt=""><figcaption></figcaption></figure>

## Accessing the Wallet

When you click the "email me a code" button and enter the code sent to your email, you'll be presented with your wallet and, if you're a new user, an option to enable an allocation strategy:

<figure><img src="../.gitbook/assets/Screenshot 2026-06-18 at 10.43.33.png" alt=""><figcaption></figcaption></figure>

This wallet is assigned to your account and shared across tournaments. It shows you:

* The `email` address attached to this wallet.
* The Ethereum `wallet address` that holds your available NMR. If you send NMR to this address from another wallet, it should appear in the `available` balance value.
* The `available` balance is the actual amount of NMR owned by this wallet on chain.
* A section to `withdraw` NMR from your wallet to any other address.

## Allocation Strategies

Enabling your allocation strategy will generate a new on-chain contract owned by your wallet and operated by Numerai to automate your staking:

<figure><img src="../.gitbook/assets/Screenshot 2026-06-18 at 10.47.58.png" alt=""><figcaption></figcaption></figure>

The allocation strategy shows you a few things:

* The address of your deployed `contract`, which stores your staking configurations. You could send NMR directly to this address in order to replenish your idle balance.
* The address of Numerai's `operator` contract, which "invokes" your strategy. This is how we can automate your staking for you and it's explained later on.
* The `idle balance` available is not currently staked NMR, it's currently-unused NMR owned by this contract. This balance can be used to automatically stake your models next round or you can withdraw to your wallet.
* You can `deposit` NMR from your wallet into your allocation strategy or `withdraw` NMR from your idle balance into your wallet. Due to security, NMR withdrawn from your strategy must go directly to the owning wallet.

Once you have an allocation strategy, each model allows you to configure stake settings for it:

<figure><img src="../.gitbook/assets/Screenshot 2026-06-18 at 11.07.31.png" alt=""><figcaption></figcaption></figure>

This will display inputs for "per-round stake" and "mode":

<figure><img src="../.gitbook/assets/Screenshot 2026-06-18 at 11.09.40.png" alt=""><figcaption></figcaption></figure>

`Per round stake` defines the intended amount of NMR locked up as stake in each round. Be aware that a single round takes 1-3 months to resolve, so set your per-round carefully as to not lock up all of your NMR at once.

`Mode` defines how payouts should be handled. It supports 2 modes:

* **Fixed**: stakes the configured per-round amount and leaves extra payouts as idle balance in the allocation strategy. This basically acts like a maximum stake.
* **Compound**: accumulates resolved payouts into the next stake, going above your configured per-round stake. This basically acts as a minimum stake.

You can edit multiple models at once and, when you're ready save all of them at once:

<figure><img src="../.gitbook/assets/Screenshot 2026-06-18 at 11.23.50.png" alt=""><figcaption></figcaption></figure>

## Automation

Once an allocation strategy is enabled, configured, and funded, Numerai can “operate” your allocation strategy on your behalf by doing the following:

1. Numerai queries your submissions for an open round.
2. Numerai calls your allocation strategy to stake on these submissions. This stake remains locked in a separate staking contract until the round resolves.&#x20;
3. When a round resolves, Numerai generates "stake claims" based on the final payout and burn values, then posts a Merkle root hash on-chain so the staking contract can verify claims.
4. Claims are automatically processed for you when we invoke your allocation strategy. Numerai will `claim` and re-stake that NMR in the next open round.

## Payouts Settings

The payout settings for each tournament will migrate to the following:

| Tournament | New Clip | New Payout Factor | Multipliers      |
| ---------- | -------- | ----------------- | ---------------- |
| Crypto     | 1        | 1                 | 0.1xCORR + 1xMMC |
| Numerai    | 1        | 1                 | 5xCORR + 1xMMC   |
| Signals    | 1        | 1                 | 4xALPHA + 8xMPC  |

## Withdrawing NMR

When you are ready to withdraw idle NMR, first withdraw it from the allocation strategy to your new wallet. You can then use the new wallet controls to send NMR to an external Ethereum address.

## APIs and Manual Staking

You can manage your own stake manually via the API. API tokens that automate Atomic Blockchain Staking need the `web3_staking` scope.

The staking v3 API fields are intended for contract-aware automation:

* `v3StakeConfig` returns staking contract metadata for a tournament.
* `v3StakeRound` returns round status and round-level staking parameters.
* `v3StakeAuth` issues a staking authorization for an eligible selected submission.
* `v3StakeClaim` returns the claim proof for an authenticated model and staker after a round resolves.

At a high level, stake authorizations are tied to selected submissions while staking is open, and claims are model-scoped. If you automate beyond the website flow, keep your scripts aligned with the allocation strategy settings you own.

Once a tournament's Atomic Blockchain Staking flag is enabled, the legacy V2 staking mutations for that tournament are disabled. Use the Atomic Blockchain Staking flow and staking v3 API fields instead.

## Official Contracts

Crypto (tournament 12)

* [Staking Contract](https://etherscan.io/address/0x82fc3999151f2a7b0a643ee0156790b19e10cd91#code) - this is the base staking logic responsible for rounds and stake accounting.
* [Strategy Implementation](https://etherscan.io/address/0x5d6bb8387703d722fe045cf55cf32ad8568b51e8#code) - this is a clone-able implementation of the stake strategy contracts.
* [Strategy Factory](https://etherscan.io/address/0xEe080C969587dee61608EB6C250f283696B62BBB#code) - this is the factory that clones the stake strategies.
* [Batch Invoker](https://etherscan.io/address/0x586b44b0dd165b8c31ba5ad3560fd154c354cbce#code) - this invokes strategies in bulk to improve speed and cost.

## The Migration

The legacy off-chain continuous staking system is being replaced by Atomic Blockchain Staking. The  migration schedule is as follows:

| Tournament | First v3 staking round | Expected migration length |
| ---------- | ---------------------- | ------------------------- |
| Crypto     | June 18, 2026          | 24 business days          |
| Numerai    | June 25, 2026          | 24 business days          |
| Signals    | June 25, 2026          | 64 business days          |

Migrating from the current continuous staking protocol to the new Atomic Blockchain Staking protocol is complicated. So let’s break down what that will look like:

1. **The legacy off-chain staking system will be no longer accessible.** We will be turning off the ability to interact with continuous staking. You will no longer be able to increase or decrease your stake through the normal website page / APIs. Instead, we will replace the staking UI with a new web3-native staking page that can create and control an allocation strategy through a non-custodial wallet solution backed by Privy.
2. **Your Numerai Wallet will still be accessible, but will no longer be used for staking.** You can still access your [Numerai wallet page](https://numer.ai/wallet), but links to it will be removed and your wallet address will be hidden to prevent new users from accidentally sending to the old wallet. You can still send _**from**_ your wallet, but the available NMR in the wallet will no longer be used for staking.
3. **Your stake will begin migrating from your Numerai Wallet to the new stake contracts.** The current system keeps your staked NMR in your wallet and simply uses off-chain accounting to earmark that NMR as staked and unavailable. The new system will need to actually lock up that NMR on the blockchain, so we will execute on-chain transactions to move that NMR from your Numerai wallet into the new staking contracts.
4. **New rounds will now lock up a smaller portion of stake.** When an old “continuous staking” round resolves, we transfer 1/24th of your staked NMR into the new stake contract. This will sit as idle balance until next round, when we invoke your strategy lock up that NMR.
5. **You don’t need to do anything during the migration.** We will handle provisioning your wallets and allocation strategies. We will also handle the migration of your staked NMR from your Numerai Wallet into your allocation strategy.
