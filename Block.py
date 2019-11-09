class Block:

    type = None
    breakable = True
    transparent = False
    collectable = True

    index_x = None
    index_y = None

    png = None

    def __init__(self, t, x, y):
        self.change_type(t)
        self.index_x = x
        self.index_y = y

    def update(self):
        if self.type == "bedrock":
            self.breakable = False
        else:
            self.breakable = True

        if self.type == "sky" or self.type == "water":
            self.transparent = True
        else:
            self.transparent = False

        if self.type == "sky" or self.type == "leaves" or self.type == "bedrock" or self.type == "water" \
                or self.type == "grass":
            self.collectable = False
        else:
            self.collectable = True

    def change_type(self, t):
        self.type = t
        self.update()
