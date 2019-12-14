from copy import copy

class Slot:

    def __init__(self, item, quantity=0):
        self.item = item
        self.quantity = quantity

    def __copy__(self):
        return type(self)(self.item, self.quantity)
