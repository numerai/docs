---
description: Supercharge your models with novel datasets and automate your submissions with QuantConnect.
---

# QuantConnect Integration

QuantConnect was founded in 2012 to serve quants everywhere with the best possible algorithmic trading technology. Seeking to disrupt a notoriously closed-source industry, QuantConnect takes a radically open-source approach to algorithmic trading. The QuantConnect Cloud Platform enables more than 50,000 quants on a monthly basis to backtest, research, and trade various asset classes, including Equities, Options, Futures, Crypto, Forex, and CFDs.

Numerai Signals lets you use any dataset to generate your trading signals. By using QuantConnect, you can leverage [their rich library of alternative data](https://www.quantconnect.com/datasets) or your own [custom datasets](https://www.quantconnect.com/docs/v2/writing-algorithms/importing-data/key-concepts) to generate unique trading signals. The QuantConnect team ensures the data is processed correctly and delivered on time. Their API provides simple and helpful methods to select universes of assets, define trading logic, and schedule submissions to Numerai Signals. When you deploy a live algorithm on QuantConnect, their team of engineers monitors the live trading infrastructure so that you can simply automate your Numerai Signals submissions and focus on other research.

## Requirements

To run live algorithms on QuantConnect's co-located servers, you must be in an [organization](https://www.quantconnect.com/docs/v2/cloud-platform/organizations) with an idle [live trading node](https://www.quantconnect.com/docs/v2/cloud-platform/organizations/resources#04-Live-Trading-Nodes). The minimum cost to start live trading is $8/month for a seat in a Quant Researcher organization and $24/month for a live trading node.

## Connecting to Numerai Signals

To export signals to Numerai from your algorithm on QuantConnect, add a Numerai signal export provider during [initialization](https://www.quantconnect.com/docs/v2/writing-algorithms/initialization).

```python
self.SignalExport.AddSignalExportProviders(NumeraiSignalExport(publicId, secretId, modelId, fileName))
```

The `NumeraiSignalExport` constructor accepts the following arguments:



| Argument | Data Type | Description | Default Value |
|---|---|---|---|
| `publicId`  | `string` | Your Numerai API key. |   |
| `secretId`  | `string` | Your Numerai API secret. |   |
| `modelId`   | `string` | The Id of the Numerai model. |   |
| `fileName`  | `string` | The name for the signal file. If you use a file name that already exists, the new file overwrites the old one. | "predictions.csv" |


## Universe Selection

The Numerai Signals stock market universe covers roughly the top 5,000 largest stocks in the world, but the QuantConnect Cloud Platform currently only supports live trading of US Equities. The universe available on QuantConnect that's the closest match to the Numerai Signals universe is the CRSP US Total Market Index, which represents approximately 100% of the investable US Equity market regularly traded on the New York Stock Exchange and Nasdaq. This Index doesn't contain all of the stocks in the Numerai Signals universe, but you don't need to submit signals for all the stocks in the Numerai Signals universe.

To get the constituents of the CRSP US Total Market Index, add an ETF constituents universe for the Vanguard Total Stock Market ETF, VTI.

```python
self.etf_symbol = self.AddEquity("VTI").Symbol 
self.AddUniverse(self.Universe.ETF(self.etf_symbol))
```

When the universe constituents change, we notify your algorithm through the `OnSecuritiesChanged` event handler. If you add a `securities` list to your class, you can define the `OnSecuritiesChanged` event handler to maintain the list so you can use it later in your algorithm.

```python
def OnSecuritiesChanged(self, changes: SecurityChanges) -> None:
    for security in changes.RemovedSecurities:
        if security in self.securities:
            self.securities.remove(security)
            
    self.securities.extend([security for security in changes.AddedSecurities if security.Symbol != self.etf_symbol])
```

## Portfolio Construction

When you submit signals to Numerai Signals, abide by the following rules:

- All signals must be between 0 and 1 (exclusive)
- You must submit at least 10 different signals per submission
- At least 1 signal value must be unique from the rest of the securities in the universe

To create signals, create `PortfolioTarget` objects. 

```python
targets = [PortfolioTarget(symbol, weight) for symbol, weight in weight_by_symbol.items()]
```

If you use the [Algorithm Framework](https://www.quantconnect.com/docs/v2/writing-algorithms/algorithm-framework/overview) design, we have many [pre-built Portfolio Construction models](https://www.quantconnect.com/docs/v2/writing-algorithms/algorithm-framework/portfolio-construction/supported-models) you can use to create your signals. The Equal Weighting model won’t work since it gives each security the same signal. In most cases, we recommend you use the Insight Weighting model, which weighs the assets according to the strength of the signal you create.

You don’t need to actually place any trades in your algorithm, but it may be helpful to visualize your algorithm activity. You just need to send signals to Numerai. To send the signals to Numerai, call the `SetTargetPortfolio` method. The method returns a boolean that represents whether the targets were successfully sent to Numerai.

```python
success = self.SignalExport.SetTargetPortfolio(targets)
```

## Scheduling Signals

Every Tuesday, Wednesday, Thursday, Friday, and Saturday of the week, a new round is open for you to submit signals. Saturday rounds open at 18:00 UTC, and the submission window is open until Monday 14:30 UTC. Weekday rounds open at 13:00 UTC, and the submission window is open for 1 hour. For more information about the competition rounds, see [Rounds](https://docs.numer.ai/numerai-signals/signals-overview#rounds).

To schedule your submissions, you can use a [Scheduled Event](https://www.quantconnect.com/docs/v2/writing-algorithms/scheduled-events).

```python
self.Schedule.On(
    self.DateRules.EveryDay(self.etf_symbol),
    self.TimeRules.At(13, 0, TimeZones.Utc), 
    self.submit_signals)
```

In the preceding example, the `submit_signals` method will automatically run at 13:00 UTC every trading day. 


## Deploying Live Algorithms

Follow these steps to deploy a live algorithm on QuantConnect that submits signals to Numerai Signals:

1. [Create a new project](https://www.quantconnect.com/docs/v2/cloud-platform/projects/getting-started#03-Create-Projects).

2. In the [Initialize method](https://www.quantconnect.com/docs/v2/writing-algorithms/initialization), add a US Equity universe.

```python
self.etf_symbol = self.AddEquity("VTI").Symbol
self.AddUniverse(self.Universe.ETF(self.etf_symbol))
```

3. In the Initialize method, add the Numerai Signal export provider.

```python
self.SignalExport.AddSignalExportProviders(NumeraiSignalExport(publicId, secretId, modelId, fileName))
```

4. In the Initialize method, add a Scheduled Event to submit signals for each round.

```python
self.Schedule.On(
    self.DateRules.EveryDay(self.etf_symbol),
    self.TimeRules.At(13, 0, TimeZones.Utc), 
    self.submit_signals)
```

5. Add a class member to track the securities in the universe.

```python
securities = []
```

6. Define the `OnSecuritiesChanged` event handler to update the `securities` list as the universe changes.

```python
def OnSecuritiesChanged(self, changes: SecurityChanges) -> None:
    for security in changes.RemovedSecurities:
        if security in self.securities:
            self.securities.remove(security)
            
    self.securities.extend([security for security in changes.AddedSecurities if security.Symbol != self.etf_symbol])
```

7. Define the Scheduled Event to create and send targets.

```python
def submit_signals(self):
    # Select the subset of ETF constituents we can trade
    symbols = [security.Symbol for security in self.securities if security.HasData]
    if len(symbols) == 0:
        return

    # Get historical data
    # close_prices = self.History(symbols, 22, Resolution.Daily).close.unstack(0)
    
    # Create portfolio targets
    # weight_by_symbol = {} # Add your logic here
    targets = [PortfolioTarget(symbol, weight) for symbol, weight in weight_by_symbol.items()]

    # (Optional) Place trades
    self.SetHoldings(targets)

    # Send signals to Numerai
    success = self.SignalExport.SetTargetPortfolio(targets)
    if not success:
        self.Debug(f"Couldn't send targets at {self.Time}")
```

For more information about requesting historical stock prices and alternative data, see [History Requests](https://www.quantconnect.com/docs/v2/writing-algorithms/historical-data/history-requests).

8. At the top of the web IDE, click the **Backtest** icon. 

QuantConnect doesn’t send targets to Numerai during backtests, but running a backtest is a quick way to test if the algorithm has coding errors before deploying live.

9. Deploy the algorithm to live trading.

If you don’t want to place real-money trades in your algorithm, [deploy with the paper trading brokerage](https://www.quantconnect.com/docs/v2/cloud-platform/live-trading/brokerages/quantconnect-paper-trading#14-Deploy-Live-Algorithms). If you want to trade and submit signals to Numerai in the same algorithm, see the **Deploy Live Algorithms** documentation for one of [QuantConnect’s supported brokerages](https://www.quantconnect.com/docs/v2/cloud-platform/live-trading/brokerages).

## Next Steps

To start using QuantConnect to automate your Numerai Signals submissions, review the [Numerai Signals Overview documentation](https://docs.numer.ai/numerai-signals/signals-overview) and [create a QuantConnect account](https://www.quantconnect.com/signup).

## Demonstration Algorithm

For a full example algorithm that submits signals to Numerai Signals, see the [NumeraiSignalExportDemonstrationAlgorithm](https://github.com/QuantConnect/Lean/blob/master/Algorithm.Python/NumeraiSignalExportDemonstrationAlgorithm.py) in the LEAN GitHub repository.