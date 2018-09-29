This is a FAQ for common questions about Numerai.  If you see any mistakes or have any answers to add, please edit this page.

Numeraire(NMR) is a cryptocurrency rewarded to data scientists who compete in a tournament to develop algorithms to predict and profit off of market trends. It is currently tradeable on Bittrex.com.

## The Tournament
- **How many tournaments are there ?**
<br/>
  There are currently 5 tournaments.  
- **How long is each round of the tournament ?**
<br/>
  1 week.
- **When are round earnings paid out ?**
<br/>
  Weekly, 31 days after the start of the round.  
- **Does everybody get the same data ?**
<br/>
  Yes, the dataset download link is the same for everybody.  Everyone gets the same data.
- **How much USD or NMR is awarded ?**
<br/>
  Check out the [https://numer.ai/rounds](https://numer.ai/rounds) to see the prize pools for current round and tournaments.
- **How are the weekly payouts determined ?**
<br/>
  See the Payouts section of the [Tutorial](https://numer.ai/learn).  
- **Does Numerai consider my best submission or only my latest submission?**
<br/>
  Numerai uses only the latest submission.
- **Which of my submissions are considered for payout ?**
<br/>
  Only the last submission made by an account in a given round is considered for earnings.
- **Why did you change the payouts from X to Y ?**
<br/>
  The payout structure has changed and will probably continue to change and evolve in response to model performance and the tournament rules, which in turn are an interplay in between users behavior, and said tournament rules.

## Account
- **How do I withdraw earnings ?**  
![WithdrawNMRUSD](../img/withdrawWallet.jpg)  
 When logged in, see the "WITHDRAW/DEPOSIT" link at the bottom of your user wallet panel.
 <br/>

- **How do I get an ether wallet to withdraw earnings into?  How do I sell ether ?**
<br/>
There are many ways to do this.  The easiest is [Coinbase](https://www.coinbase.com).  Set up a free account there.  You can withdraw your Numerai ether earnings into your Coinbase account and sell the ether for USD and transfer to a bank account.
- **How fast are USD or NMR withdraws from my account ?**
<br/>
Expect less than 1 minute for the transaction to first appear on your account.  How quickly the funds become available to sell from your account depends both on the service you're using as your wallet, as well as the [current load on the eth blockchain](https://ethgasstation.info).  Typically it's less than 15 minutes.

## Numeraire
- **What is Numeraire ?**
<br/>
Numeraire (NMR) is Numerai's crypto currency.  Learn more [here](https://medium.com/numerai/a-new-cryptocurrency-for-coordinating-artificial-intelligence-on-numerai-9251a131419a).
NMR is an [ERC20](https://github.com/ethereum/EIPs/issues/20) Ethereum token.  The contract is [here](https://github.com/numerai/contract). Amounts of Numeraire are represented on the website using `Ꞥ`, the unicode character [U+A7A4](http://graphemica.com/%EA%9E%A4).
- **Where can I get some NMR ?**
<br/>
Bittrex, Shapeshift, Airswap, 0x, Upbit, DDEX, Paradex
- **Is there a telegram ?**
<br/>
Yes [https://t.me/joinchat/FluX1UoXVyd08zhrgwZLqQ](https://t.me/joinchat/FluX1UoXVyd08zhrgwZLqQ)
- **What is the current supply of NMR ?, How much is under Numerai's control ?**
<br/>
NMR supply and distribution changes often, for the latest numbers [please consult the contract on the blockchain](https://etherscan.io/address/0x1776e1f26f98b1a5df9cd347953a26dd3cb46671#readContract).

    The following table summarizes publicly available information as of August 13th 2018 :

    | Total Supply                     |   | 6,362,843 |
    |----------------------------------|---|-----------|
    | Mintable                         |   | 1,554,219 |
    | Weekly Disbursement              |   | 96,154    |
    | Total Minted                     |   | 6,433,454 |
    | Locked                           |   | 3,000,000 |
    | Burned (Minted -supply)          |   | (70,611)  |
    | Numerai (known wallet)           |   | 316,467   |
    | Under control (mintable+locked+Numerai Wallet)                    |   | 4,870,686 |





## Data
- **What are the features and ids in the dataset ?**
<br/>
The features and ids of the dataset are intentionally obfuscated to remove human bias from the data science.
- **Why isn't the data for past rounds included in the training data of subsequent rounds ?**
<br/>
There is a trade off between the length of the test data (used in our backtest) which gives us a lot of information to build the meta model and the length of the training data which gives users more information. Particularly, we like that our test set Sharpe is calculated on a large set of data. If we turned the test data into training data, we wouldn't have much to go on unless the staking tournament was working perfectly and users got extremely good at estimating p and communicating it through stakes. This is subject to change in the future.

## Company
- **How well is Numerai's fund doing ?**
<br/>
Numerai doesn't discuss this publicly.
- **Can I invest in Numerai ?**
<br/>
Numerai One, our Hedge Fund is intended for institutional investors with a $1 million minimum investment.
- **I am an institutional investor, how do I invest ?**
<br/>
Please email: contact@numer.ai

## Reputation
- **What is this reputation that I hear about ?**
Reputation is the number of benchmark beat in the past 20 rounds across all tournaments
<br/>
- **Is there a bonus associated with reputation ?**
<br/>
Retroactive bonus: 1 time bonus of 1 NMR for every benchmark beat before April 20 when you verify your phone number.
<br/>
Verification bonus: 1 time bonus of 0.1 NMR for verifying your phone number
<br/>
Reputation bonus: ongoing bonus of 0.1 NMR for every benchmark beat (if you have verified your phone number)

- **How does phone number verification work ?**
<br/>
Head over to the account to start phone verification process
<br/>
A single phone number can only be verified against one account
<br/>
You can remove your phone number and verify another if you wish, but you will only be paid the verification bonus once.
<br/>
Your phone number will not be used for anything apart from verification.

## Other
- **Is there an API ?**
<br/>
Use the open-source [Numerapi](https://github.com/uuazed/numerapi), note that this is an external project.
- **Any tips for first time competitors who are getting into machine learning ?**
<br/>
The download of our data includes [these](https://github.com/numerai/example_scripts) example scripts in Python and R.  Try starting with those.  Also, [this](https://medium.com/jim-fleming/notes-on-the-numerai-ml-competition-14e3d42c19f3#.lzl5g090h) blog post might be helpful.
- **Where can I go for more information ?**
<br/>
There are [community ](https://community.numer.ai/) as well as a [Telegram ](https://t.me/NMR_Official) as well as a number of [blog posts](https://medium.com/numerai).

## Old but valid news
- **Does Numerai still use bitcoin ?**
<br/>
No.  All USD earnings are paid out in ether.
- **Is Numeraire fully released ?**
<br/>
Yes.  The initial distribution of NMR has been given to data scientists on the website, and data scientists can continue to win NMR in the weekly tournament.  The [NMR contract](https://etherscan.io/address/0x1776e1f26f98b1a5df9cd347953a26dd3cb46671) has been released on the Ethereum blockchain.  
- **Can I withdraw NMR ?**
Yes, you can withdraw your NMR from the Numerai website, and deposit it into any wallet that supports ERC20 tokens.
- **Will there be a Numeraire ICO (Initial Coin Offering) ?**
<br/>
No.  The initial distribution of NMR has already been given out to all of Numerai's data scientists based on their historic performance in the tournament.  Data scientists will earn NMR each week, just like they earn USD.
- **What is `-ln(0.5)` used in the [whitepaper](https://numer.ai/whitepaper.pdf) ?**
<br/>
`-ln(0.5) = 0.6931471805599453...`  This is the logloss you'd expect to get from making completely random guesses.  A logloss lower than this is better than random guessing.

<br />
<br />
