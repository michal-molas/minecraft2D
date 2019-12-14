import blocks.Block


class Bedrock(blocks.Block.Block):

    def __init__(self):
        super().__init__("bedrock")
        self.breakable = False
        self.collectable = False
