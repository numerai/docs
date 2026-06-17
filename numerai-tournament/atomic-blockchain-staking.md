# Atomic Blockchain Staking

Atomic Blockchain Staking is Numerai's new blockchain-native staking system. It is also referred to as staking v3 in API and contract names. It locks NMR atomically per round, tracks each model's stake independently, and lets resolved stakes be claimed when a round resolves.

You can interact with Atomic Blockchain Staking manually through the contracts and API, or automate staking with an account allocation strategy. Most users should use the Dashboard > **V3 Stakes** page, which manages the Privy embedded wallet and allocation strategy flow.

## Staking Flow

Atomic Blockchain Staking is managed from your Dashboard:

1. Go to [Dashboard](https://numer.ai/dashboard) > **V3 Stakes**.
2. Use the Privy embedded wallet shown on the page. This wallet is the account wallet used for atomic staking actions.
3. Enable your account allocation strategy. The allocation strategy is a user-owned smart contract that holds your staking policy and idle strategy NMR.
4. Deposit NMR from your Privy embedded wallet into the allocation strategy.
5. Configure each model's per-round stake and payout mode.
6. Save the model settings.
7. Monitor **Stake Activity** and **Wallet Activity** on the V3 Stakes page.

Numerai's staking operator invokes your allocation strategy according to your saved per-model settings. You are not required to interact with the blockchain directly when you use the allocation strategy flow.

## Per-Round Stake Settings

Each model has a per-round stake setting. This is the NMR amount the allocation strategy will try to stake for that model when a new eligible round opens.

Atomic Blockchain Staking supports two automated modes:

* **Compound**: rolls resolved releasable value forward above your configured per-round stake. Your configured per-round stake acts as the minimum.
* **Fixed**: stakes the configured per-round amount and leaves extra resolved value idle in the allocation strategy. This is the website label for the constant, or take-profit, strategy mode.

In either mode, the allocation strategy can only stake according to the model settings you save.

## Claims and Payouts

When a round resolves, Numerai generates model-scoped stake claims based on the final payout and burn values, then posts a Merkle root on-chain so the staking contract can verify claims.

Atomic Blockchain Staking removes continuous-stake overlap leverage and the legacy per-round clip. Payouts and burns are applied to the NMR staked for each model and round. If you use stake automation, resolved stakes can be claimed and restaked in one transaction; burns can be netted against future same-model payouts while you continue staking.

## Reducing Stake

To reduce future exposure, lower the model's per-round stake and withdraw any idle strategy NMR back to your Privy embedded wallet. NMR already staked in an active round remains locked until that round settles.

The legacy V2 stake release process does not apply to Atomic Blockchain Staking.

## Migration

The legacy off-chain continuous staking system is being replaced by Atomic Blockchain Staking. Once a tournament is migrated, legacy continuous staking pages and API mutations for increasing or decreasing stake are no longer used for that tournament.

During migration, Numerai handles provisioning Privy embedded wallets and allocation strategies, then migrates staked NMR from the Numerai Wallet into allocation strategies and staking contracts over the tournament's overlap period.

The announced migration schedule is:

| Tournament | Migration starts | Expected migration length |
| ---------- | ---------------- | ------------------------- |
| Crypto     | June 16, 2026    | 24 business days          |
| Signals    | June 23, 2026    | 64 business days          |
| Numerai    | June 23, 2026    | 24 business days          |

The Numerai Wallet remains accessible for wallet history and non-staking transfers, but it is no longer the place to manage new stakes after a tournament migrates.

## API and Automation

API tokens that automate Atomic Blockchain Staking need the `web3_staking` scope.

The staking v3 API fields are intended for contract-aware automation:

* `v3StakeConfig` returns staking contract metadata for a tournament.
* `v3StakeRound` returns round status and round-level staking parameters.
* `v3StakeAuth` issues a staking authorization for an eligible selected submission.
* `v3StakeClaim` returns the claim proof for an authenticated model and staker after a round resolves.

At a high level, stake authorizations are tied to selected submissions while staking is open, and claims are model-scoped. If you automate beyond the website flow, keep your scripts aligned with the allocation strategy settings you own.

Once a tournament's Atomic Blockchain Staking flag is enabled, the legacy V2 staking mutations for that tournament are disabled. Use the Atomic Blockchain Staking flow and staking v3 API fields instead.

## Withdrawing NMR

When you are ready to withdraw idle NMR, first withdraw it from the allocation strategy to your Privy embedded wallet from the V3 Stakes page. You can then use the embedded wallet controls to send NMR to an external Ethereum address. Active round stake remains locked until settlement.

## Official Contracts

* Staking Contract: [https://etherscan.io/address/0x82fc3999151f2a7b0a643ee0156790b19e10cd91#code](https://etherscan.io/address/0x82fc3999151f2a7b0a643ee0156790b19e10cd91#code)
* Strategy Implementation: [https://etherscan.io/address/0x5d6bb8387703d722fe045cf55cf32ad8568b51e8#code](https://etherscan.io/address/0x5d6bb8387703d722fe045cf55cf32ad8568b51e8#code)
* Strategy Factory: [https://etherscan.io/address/0xEe080C969587dee61608EB6C250f283696B62BBB#code](https://etherscan.io/address/0xEe080C969587dee61608EB6C250f283696B62BBB#code)
* Batch Invoker: [https://etherscan.io/address/0x586b44b0dd165b8c31ba5ad3560fd154c354cbce#code](https://etherscan.io/address/0x586b44b0dd165b8c31ba5ad3560fd154c354cbce#code)
