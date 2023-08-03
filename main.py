from AlgorithmImports import *


class CryingRedHorse(QCAlgorithm):

    def Initialize(self):
        self.SetStartDate(2010, 1, 1)
        self.SetEndDate(2020, 12, 31)
        self.SetCash(500)  # Starting with 500 in account

        # symbols of interest (top tech companies, including Tesla)
        self.symbols = [""]
        for symbol in self.symbols:
            self.AddEquity(symbol, Resolution.Minute)

        self.purchasePrices = {}  # Store the purchase price for each stock
        self.trailingStop = {}  # Store the highest price for each stock

    def OnData(self, data: Slice):
        for symbol in self.symbols:
            if symbol not in self.Portfolio or not self.Portfolio[symbol].Invested:
                if data.ContainsKey(symbol):
                    self.SetHoldings(symbol, 1.0 / len(self.symbols))
                    self.purchasePrices[symbol] = self.Securities[symbol].Close
                    self.trailingStop[symbol] = self.Securities[symbol].Close
            else:
                if data.ContainsKey(symbol):
                    currentPrice = self.Securities[symbol].Close
                    if currentPrice > self.trailingStop[symbol]:
                        self.trailingStop[symbol] = currentPrice

                    # calculate percentage change from the highest price
                    pctChange = (currentPrice - self.trailingStop[symbol]) / self.trailingStop[symbol]

                    # If the price has dipped by 10% from the highest price, sell the stock
                    if pctChange <= -0.5:
                        self.Liquidate(symbol)

    # Add cash at the end of each month
    def OnEndOfMonth(self):
        self.SetCash(self.Portfolio.Cash + 500)  # Add 500 Euros to the account
