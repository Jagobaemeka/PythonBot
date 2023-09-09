# PythonBot

Trading Bot: CryingRedHorse | Python, QuantConnect API

Initialization and Configuration:

Developed using the QuantConnect Algorithm Framework.
Configured to run over a decade from January 1, 2010, to December 31, 2020.
Initialized with a starting balance of €500.
Designed to trade a predefined list of symbols, with placeholders for top tech companies, including Tesla.
Trading Strategy:

Upon receiving new data, the bot checks if it currently holds any of the symbols in its portfolio.
If not already invested in a symbol, the bot allocates an equal portion of its funds to each symbol and records the purchase price and the highest price (trailing stop) for that symbol.
If already invested, the bot updates the trailing stop if the current price of the symbol is higher than the previously recorded highest price.
The bot calculates the percentage change from the highest price and liquidates the position if the current price dips by 10% or more from the highest recorded price for that symbol.
Monthly Cash Infusion:

At the end of each month, the bot adds an additional €500 to its account, simulating a regular investment strategy.
