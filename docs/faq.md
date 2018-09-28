This is a FAQ for common questions about Numerai.  If you see any mistakes or have any answers to add, please edit this page.

Numeraire(NMR) is a cryptocurrency rewarded to data scientists who compete in a tournament to develop algorithms to predict and profit off of market trends. It is currently tradeable on Bittrex.com.

## The Tournament
- **How many tournaments are there ?**
<br/>
  &nbsp;&nbsp;&nbsp;There are currently 5 tournaments.
- **How long is each round of the tournament ?**
<br/>
  &nbsp;&nbsp;&nbsp;1 week.
- **When are round earnings paid out ?**
<br/>
  &nbsp;&nbsp;&nbsp;Weekly, 4 weeks after the start of the round.  
- **Does everybody get the same data ?**
<br/>
  &nbsp;&nbsp;&nbsp;Yes, the dataset download link is the same for everybody.  Everyone gets the same data.
- **How much USD or NMR is awarded ?**
<br/>
  &nbsp;&nbsp;&nbsp;Check out the https://numer.ai/rounds to see the prize pools for current round.
- **How are the weekly payouts determined ?**
<br/>
  &nbsp;&nbsp;&nbsp;See the Payouts section of the [Tutorial](https://numer.ai/learn).  
- **Does Numerai consider my best submission or only my latest submission?**
<br/>
  &nbsp;&nbsp;&nbsp;Numerai uses only the latest submission.
- **Which of my submissions are considered for payout ?**
<br/>
  &nbsp;&nbsp;&nbsp;Only the last submission made by an account in a given round is considered for earnings.

## Account
- How do I withdraw earnings?
  - When logged in, see the "Earnings" button at the bottom of your user information control panel.
- How do I get an ether wallet to withdraw earnings into?  How do I sell ether?
  - There are many ways to do this.  The easiest is [Coinbase](https://www.coinbase.com).  Set up a free account there.  You can withdraw your Numerai ether earnings into your Coinbase account and sell the ether for USD and transfer to a bank account.
- How fast are USD or NMR withdraws from my account?
  - Expect less than 1 minute for the transaction to first appear on your account.  How quickly the funds become available to sell from your account depends both on the service you're using as your wallet, as well as the [current load on the blockchain](https://blockchain.info/charts/avg-confirmation-time?timespan=30days).  Typically it's less than 15 minutes.

## Numeraire
- What is Numeraire?
  - Numeraire (NMR) is Numerai's crypto currency.  Learn more [here](https://medium.com/numerai/a-new-cryptocurrency-for-coordinating-artificial-intelligence-on-numerai-9251a131419a).
  - NMR is an [ERC20](https://github.com/ethereum/EIPs/issues/20) Ethereum token.  The contract is [here](https://github.com/numerai/contract). Amounts of Numeraire are represented on the website using `Ꞥ`, the unicode character [U+A7A4](http://graphemica.com/%EA%9E%A4).
- Where can I get some NMR?
  - Bittrex, Shapeshift, Airswap, 0x, Upbit, DDEX, Paradex
- Is there a telegram?
  - Yes (https://t.me/joinchat/FluX1UoXVyd08zhrgwZLqQ)[https://t.me/joinchat/FluX1UoXVyd08zhrgwZLqQ]

## Data
- What are the features and ids in the dataset?
  - The featurs and ids of the dataset is intentionally obfuscated to remove human bias from the data science.
- Why isn't the data for past rounds included in the training data of subsequent rounds?
  - There is a trade off between the length of the test data (used in our backtest) which gives us a lot of information to build the meta model and the length of the training data which gives users more information. Particularly, we like that our test set Sharpe is calculated on a large set of data. If we turned the test data into training data, we wouldn't have much to go on unless the staking tournament was working perfectly and users got extremely good at estimating p and communicating it through stakes. This is subject to change in the future.

## Company
- How well is Numerai's fund doing?
  - Numerai doesn't discuss this publicly.
- Can I invest in Numerai?
  - Numerai One.  $1 million minimum.  Intended for institutional investors.
- I am an institutional investor, how do I invest?
  - Please email contact@numer.ai

## Reputation
- What is this reputation that I hear about?
  - Reputation is the # of benchmark beat in the past 20 rounds across all tournaments
- Is there a bonus associated with reputation?
  - Retroactive bonus: 1 time bonus of 1 NMR for every benchmark beat before April 20 when you verify your phone number.
  - Verification bonus: 1 time bonus of 0.1 NMR for verifying your phone number
  - Reputation bonus: ongoing bonus of 0.1 NMR for every benchmark beat (if you have verified your phone number)
- How does phone number verification work?
  - Head over to the account to start phone verification process
  - A single phone number can only be verified against one account
  - You can remove your phone number and verify another if you wish, but you will only be paid the verification bonus once.
  - Your phone number will not be used for anything apart from verification.

## Other
- Is there an API?
  - Use the open-source [Python client](https://github.com/atreichel/NumerAPI)
- Any tips for first time competitors who are getting into machine learning?
  - The download of our data includes [these](https://github.com/numerai/example_scripts) example scripts in Python and R.  Try starting with those.  Also, [this](https://medium.com/jim-fleming/notes-on-the-numerai-ml-competition-14e3d42c19f3#.lzl5g090h) blog post might be helpful.
- Where can I go for more information?
  - There are [forums](https://forum.numer.ai/) as well as a [slack team](https://slack.numer.ai/) as well as a number of [blog posts](https://medium.com/numerai).

## Old but valid news
- Does Numerai still use bitcoin?
  - No.  All USD earnings are paid out in ether.
- Is Numeraire fully released?
  - Yes.  The initial distribution of NMR has been given to data scientists on the website, and data scientists can continue to win NMR in the weekly tournament.  The [NMR contract](https://etherscan.io/address/0x1776e1f26f98b1a5df9cd347953a26dd3cb46671) has been released on the Ethereum blockchain.  
- Can I withdraw NMR?  
  - Yes, you can withdraw your NMR from the Numerai website, and deposit it into any wallet that supports ERC20 tokens.
- Will there be a Numeraire ICO (Initial Coin Offering)?
  - No.  The initial distribution of NMR has already been given out to all of Numerai's data scientists based on their historic performance in the tournament.  Data scientists will earn NMR each week, just like they earn USD.
- What is `-ln(0.5)` used in the [whitepaper](https://numer.ai/whitepaper.pdf)?
  - `-ln(0.5) = 0.6931471805599453...`  This is the logloss you'd expect to get from making completely random guesses.  A logloss lower than this is better than random guessing.
