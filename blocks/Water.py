import blocks.Block


class Water(blocks.Block.Block):

    def __init__(self):
        super().__init__("water")
        self.transparent = True
        self.collectable = False
        self.breakable = False
