import blocks.Block


class Sky(blocks.Block.Block):

    def __init__(self):
        super().__init__("sky")
        self.transparent = True
        self.collectable = False
        self.breakable = False
