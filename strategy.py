from action import Action
import torch
from rl_model import RLModel

class Strategy():



    def actions(self,
                instruments,
                all_orders,
                portfolio,
                market_data):
        Action.cancel_order(all_orders)
        new_orders = self.model(instruments, portfolio, market_data)


        return  new_orders

    def model(self, instruments, portfolio, market_data):
        #Wrap RL model and feed data
        new_orders = []
        return new_orders

if __name__ == '__main__':
    print("torch version", torch.__version__)