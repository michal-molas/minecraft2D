

class Block:

    def __init__(self, t):
        self.type = t
        self.breakable = True
        self.transparent = False
        self.collectable = True

    def update(self):
        # logic function
        pass
