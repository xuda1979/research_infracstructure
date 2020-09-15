from simulator import Simulator

class Training():
    def __init__(self,
                 instruments,
                 strategy,
                 initial_positions,
                 initial_trades,
                 initial_orders,
                 training_start_time,
                 training_end_time,
                 validation_start_time,
                 validation_end_time):
        self.training_simulator = Simulator( strategy,
                                             instruments,
                                             initial_positions,
                                             initial_trades,
                                             initial_orders,
                                             training_start_time,
                                             training_end_time)

        self.validation_simulator = Simulator( strategy,
                                               instruments,
                                               initial_positions,
                                               initial_trades,
                                               initial_orders,
                                               validation_start_time,
                                               validation_end_time)