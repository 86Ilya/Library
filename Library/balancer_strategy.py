from itertools import cycle


class FiftyFifty:
    def __init__(self, databases):
        self.databases = databases
        self.iterator = cycle(self.databases)

    def balance(self, model):
        # we don't use the model paramter in this strategy, but it's necessary
        # to implement the method with it
        return next(self.iterator)
