#region imports
from AlgorithmImports import *
#endregion
"""
from: Derek Melchin's version 1 Dec 2020
Based on 'In & Out' strategy by Peter Guenther 4 Oct 2020
expanded/inspired by Tentor Testivis, Dan Whitnable (Quantopian), Vladimir, and Thomas Chang.

https://www.quantopian.com/posts/new-strategy-in-and-out
https://www.quantconnect.com/forum/discussion/9597/the-in-amp-out-strategy-continued-from-quantopian/p1
"""

# Import packages
import numpy as np
import pandas as pd
import scipy as sc


class ExpToFro2(QCAlgorithm):

    def Initialize(self):

        self.SetStartDate(2015, 1, 1)  # Set Start Date
        self.SetEndDate(2018, 10, 1)  # Set Start Date
        self.SetCash(100000000)  # Set Strategy Cash
        res = Resolution.Second
        
        # Feed-in constants
        self.INI_WAIT_DAYS = 5  # out for 3 trading weeks
        
        # Holdings
        ### 'Exit' holdings and weights
        self.BND1 = self.AddEquity('TMF', res).Symbol #TLT; TMF for 3xlev
        self.BND2 = self.AddEquity('TYD', res).Symbol #IEF; TYD for 3xlev
        self.HLD_OUT = {self.BND1: .5, self.BND2: .5}
        ### 'Entry' holdings and weights (static stock selection strategy)
        self.STKS = self.AddEquity('TQQQ', res).Symbol #SPY or QQQ; TQQQ for 3xlev
        self.HLD_IN = {self.STKS: 1}

        # Market and list of signals based on ETFs
        self.MRKT = self.AddEquity('SPY', res).Symbol  # market
        self.PRDC = self.AddEquity('XLI', res).Symbol  # production (industrials)
        self.METL = self.AddEquity('DBB', res).Symbol  # input prices (metals)
        self.NRES = self.AddEquity('IGE', res).Symbol  # input prices (natural res)
        self.DEBT = self.AddEquity('SHY', res).Symbol  # cost of debt (bond yield)
        self.USDX = self.AddEquity('UUP', res).Symbol  # safe haven (USD)
        self.GOLD = self.AddEquity('GLD', res).Symbol  # gold
        self.SLVA = self.AddEquity('SLV', res).Symbol  # vs silver
        self.UTIL = self.AddEquity('XLU', res).Symbol  # utilities
        self.INDU = self.PRDC  # vs industrials
        self.SHCU = self.AddEquity('FXF', res).Symbol  # safe haven currency (CHF)
        self.RICU = self.AddEquity('FXA', res).Symbol  # vs risk currency (AUD)

        self.FORPAIRS = [self.GOLD, self.SLVA, self.UTIL, self.SHCU, self.RICU]
        self.SIGNALS = [self.PRDC, self.METL, self.NRES, self.DEBT, self.USDX]
        self.pairlist = ['G_S', 'U_I', 'C_A']

        # Initialize variables
        ## 'In'/'out' indicator
        self.be_in = 999 #initially, set to an arbitrary value different from 1 (in) and 0 (out)
        ## Day count variables
        self.dcount = 0  # count of total days since start
        self.outday = 0  # dcount when self.be_in=0
        ## Flexi wait days
        self.WDadjvar = self.INI_WAIT_DAYS
        np.random.seed(1)
        # 1000 random integers between 0 and 50
        x = np.random.randint(0, 3056, 10340)
        # Positive Correlation with some noise
        y = x + np.random.normal(0, 23, 10340)
        self.corr = np.corrcoef(x, y)
        
        self.Schedule.On(
            self.DateRules.EveryDay(),
            self.TimeRules.AfterMarketOpen('SPY', 5),
            self.rebalance_when_out_of_the_market
        )


        self.Schedule.On(
            self.DateRules.WeekEnd(),
            self.TimeRules.AfterMarketOpen('SPY', 360),
            self.rebalance_when_in_the_market
        )
        
        # Setup daily consolidation
        symbols = self.SIGNALS + [self.MRKT] + self.FORPAIRS
        for symbol in symbols:
            self.consolidator = TradeBarConsolidator(timedelta(days=1))
            self.consolidator.DataConsolidated += self.consolidation_handler
            self.SubscriptionManager.AddConsolidator(symbol, self.consolidator)
        
        # Warm up history
        self.lookback = 252
        self.history = self.History(symbols, self.lookback, Resolution.Hour)
        if self.history.empty or 'close' not in self.history.columns:
            return
        self.history = self.history['close'].unstack(level=0).dropna()
        self.update_history_shift()
        
    def consolidation_handler(self, sender, consolidated):
        self.history.loc[consolidated.EndTime, consolidated.Symbol] = consolidated.Close
        self.history = self.history.iloc[-self.lookback:]
        self.update_history_shift()
        
    def update_history_shift(self):
        self.history_shift = self.history.rolling(11, center=True).mean().shift(60)

    def rebalance_when_out_of_the_market(self):
        # Returns sample to detect extreme observations
        returns_sample = (self.history / self.history_shift - 1)
        # Reverse code USDX: sort largest changes to bottom
        returns_sample[self.USDX] = returns_sample[self.USDX] * (-1)
        # For pairs, take returns differential, reverse coded
        returns_sample['G_S'] = -(returns_sample[self.GOLD] - returns_sample[self.SLVA])
        returns_sample['U_I'] = -(returns_sample[self.UTIL] - returns_sample[self.INDU])
        returns_sample['C_A'] = -(returns_sample[self.SHCU] - returns_sample[self.RICU])    

        # Extreme observations; statist. significance = 1%
        pctl_b = np.nanpercentile(returns_sample, 1, axis=0)
        extreme_b = returns_sample.iloc[-1] < pctl_b

        # Determine waitdays empirically via safe haven excess returns, 50% decay
        self.WDadjvar = int(
            max(0.50 * self.WDadjvar,
                self.INI_WAIT_DAYS * max(1,
                     np.where((returns_sample[self.GOLD].iloc[-1]>0) & (returns_sample[self.SLVA].iloc[-1]<0) & (returns_sample[self.SLVA].iloc[-2]>0), self.INI_WAIT_DAYS, 1),
                     np.where((returns_sample[self.UTIL].iloc[-1]>0) & (returns_sample[self.INDU].iloc[-1]<0) & (returns_sample[self.INDU].iloc[-2]>0), self.INI_WAIT_DAYS, 1),
                     np.where((returns_sample[self.SHCU].iloc[-1]>0) & (returns_sample[self.RICU].iloc[-1]<0) & (returns_sample[self.RICU].iloc[-2]>0), self.INI_WAIT_DAYS, 1)
                     ))
    )
        adjwaitdays = min(60, self.WDadjvar)

        # self.Debug('{}'.format(self.WDadjvar))

        # Determine whether 'in' or 'out' of the market
        if (extreme_b[self.SIGNALS + self.pairlist]).any():
            self.be_in = False
            self.outday = self.dcount
        if self.dcount >= self.outday + adjwaitdays:
            self.be_in = True
        self.dcount += 1

        #self.be_in = True # for testing; sets the algo to being always in

        # Swap to 'out' assets if applicable
        if not self.be_in:
            # Only trade when changing from in to out
            self.trade({**dict.fromkeys(self.HLD_IN, 0), **self.HLD_OUT})

        self.Plot("In Out", "in_market", int(self.be_in))
        self.Plot("In Out", "num_out_signals", extreme_b[self.SIGNALS + self.pairlist].sum())
        self.Plot("Wait Days", "waitdays", adjwaitdays)


    def rebalance_when_in_the_market(self):
        # Swap to 'in' assets if applicable
        if self.be_in:
            # Only trade when changing from out to in
            self.trade({**self.HLD_IN, **dict.fromkeys(self.HLD_OUT, 0)})
            
    def trade(self, weight_by_sec):
        buys = []
        for sec, weight in weight_by_sec.items():
            # Check that we have data in the algorithm to process a trade
            if not self.CurrentSlice.ContainsKey(sec) or self.CurrentSlice[sec] is None:
                continue
            
            cond1 = weight == 0 and self.Portfolio[sec].IsLong
            cond2 = weight > 0 and not self.Portfolio[sec].Invested
            if cond1 or cond2:
                quantity = self.CalculateOrderQuantity(sec, weight)
                if quantity > 0:
                    buys.append((sec, quantity))
                elif quantity < 0:
                    self.Order(sec, quantity)
                else:
                    self.Order(sec, quantity/3)
                    self.Order('FXA', -quantity/5)

        for sec, quantity in buys:
            self.Order(sec, quantity)
