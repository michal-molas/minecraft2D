import blocks.Block


class Leaves(blocks.Block.Block):

    def __init__(self):
        super().__init__("leaves")
        self.collectable = False
