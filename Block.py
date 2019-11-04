class Block:
    type = "default"
    breakable = True
    transparent = False

    def __init__(self, t):
        self.type = t
        self.update()

    def update(self):
        if self.type == "bedrock":
            self.breakable = False
        if self.type == "sky" or self.type == "water":
            self.transparent = True

    def changeType(self, t):
        self.type = t
        self.update()
