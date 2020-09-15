from portfolio import Portfolio
from market_data import MarketData
from PnL import PnL
from trades import Trades
from order import Order


class Simulator():
    def __init__(self,
                 strategy,
                 instruments,
                 initial_positions,
                 initial_trades,
                 initial_orders,
                 start_time,
                 end_time):
        self.market_data = MarketData(instruments, start_time, end_time)
        self.instruments = instruments
        self.pnl = PnL()
        self.start_time = start_time
        self.end_time = end_time
        self.strategy = strategy
        self.time_stamp = start_time
        self.all_orders = initial_orders

        # initialize status
        self.portfolio = {start_time: Portfolio(instruments, initial_positions)}
        self.trades = initial_trades

    def run(self):
        while self.time_stamp < self.end_time:
            self.update_time_stamp()
            self.execution()
            self.actions()
            self.update_trades()
            self.update_orders()
            self.update_portfolio()
            self.update_pnl()
            self.update_margin()

    def update_time_stamp(self):
        self.time_stamp = self.market_data.get_next_time_stamp(self.time_stamp)

    def execution(self):
        

        return


    def actions(self):
        self.new_orders = self.strategy.actions(self.instruments,
                                                self.all_orders,
                                                self.portfolio,
                                                self.market_data)

    def update_trades(self):
        return

    def update_orders(self):
        return

    def update_portfolio(self):
        return

    def update_pnl(self):
        return

    def update_margin(self):
        return
