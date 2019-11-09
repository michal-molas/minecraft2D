class Block:

    type = None
    breakable = True
    transparent = False
    collectable = True

    png = None

    def __init__(self, t):
        self.change_type(t)

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
