# Signals FAQ

_\[under construction\]_

#### FAQ from classic Numerai users starting Signals

1. What is a Symbol? A stock symbol is an arrangement of characters—usually letters—representing publicly-traded securities on an exchange.
2. What is a stock universe?
   1. A set of stock symbols that share a common feature. Numerai wants predictions for these symbols in a round. 
   2. Symbols in the latest [Signals Universe](https://numerai-signals-public-data.s3-us-west-2.amazonaws.com/universe/latest.csv). 
   3. Historical universe in [historical targets](https://numerai-signals-public-data.s3-us-west-2.amazonaws.com/signals_train_val_bbg.csv) file
3. Differences between Numerai main tournament and Signals?
   1. **Data**. For Signals, users have to come up with their own features. However they can use historical targets provided in [historical targets](https://numerai-signals-public-data.s3-us-west-2.amazonaws.com/signals_train_val_bbg.csv) file to train the models and evaluate on validation data.
   2. Signals has one week round resolve duration compared to 4 weeks in the main tournament.
4. Similarities between Numerai main tournament and Signals?
   1. Signals has three data splits, Training, validation and live with targets.
   2. A diagnostics dashboard for performance on validation data
   3. Metrics are very similar i.e., correlation and neutralization.

#### General FAQ

1. Where can I find stock price data and data in general? Check out [this discussion at the forum](https://forum.numer.ai/t/free-or-cheap-data-and-tools-for-numerai-signals/350/8) 
2. How do I know if my IP is protected? Numerai does not view the source code that builds your predictions; Numerai only receives the predictions themselves. Reverse-engineering such a complex system is impossible. 
3. Do I have to stake NMR in order to participate? You can submit your prediction file and receive performance without staking. Stake NMR on the live portion of your signal to earn or lose NMR based on your performance relative to Numerai's custom targets. 
4.  Why should I submit a good trading system to you if I could just trade on my own? [Learn more in this Medium post](https://medium.com/numerai/building-the-last-hedge-fund-introducing-numerai-signals-12de26dfa69c). 
5. Can you tell me if \[insert diagnostic output here\] is good enough? Since you do not need to stake Numeraire in order to participate, we recommend that you submit your predictions and find out over time. This is often called ‘paper trading’ and constant timely submissions will give you more feedback than any out-of-sample estimation could.  
6. Do I need to know how to code in order to participate? While example models and exploratory notebooks are available to aid in idea development, new coders are encouraged to try Numerai Classic rather than Signals. Signals does require a high-level of coding / scripting knowledge to be successful.  

