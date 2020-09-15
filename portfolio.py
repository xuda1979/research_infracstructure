

class Portfolio():
    def __init__(self,
                 instruments,
                 initial_positions):
        self.instruments = instruments
        self.initial_positions = {}
        if initial_positions is None:
            self.initial_positions = initial_positions
        else:
            for instrument in instruments:
                self.initial_positions[instrument] = 0

