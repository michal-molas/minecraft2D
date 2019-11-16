import Slot


class Container:

    def __init__(self, corners):
        self.corners = corners  # tuple
        self.content = []
        self.size = self.corners[2] * self.corners[3]
        for i in range(self.size):
            self.content.append(Slot.Slot("empty"))

    def getItemInSlot(self, slot):
        if slot[0] <= self.corners[2] and slot[1] <= self.corners[3]:
            return self.content[slot[1] * self.corners[2] + slot[0]]

    def addItem(self, item, count, slot):
        # print("Dodaje item")
        if slot[0] <= self.corners[2] and slot[1] <= self.corners[3]:
            for i in range(self.size):
                position = self.content[slot[1] * self.corners[2] + slot[0] + i]
                # print(slot)
                # print(slot[1] * self.corners[2] + slot[0] + i)
                if position.item == "empty" or position.item == item:
                    position.item = item
                    position.quantity += count
                    # print([(el.item, el.quantity) for el in self.content])
                    return True
        return False

    def takeItem(self, count, slot):
        # print("Zabieram item")
        if slot[0] <= self.corners[2] and slot[1] <= self.corners[3]:
            position = self.content[slot[1] * self.corners[2] + slot[0]]
            # print(position.item, position.quantity)
            if position.item != "empty":
                if position.quantity >= count:
                    position.quantity -= count
                else:
                    return False
                if position.quantity == 0:
                    position.item = "empty"
                return True
        return False
