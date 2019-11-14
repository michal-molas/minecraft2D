import Slot


class Container:
    x_pos = 0
    y_pos = 0

    x_slots = 0
    y_slots = 0
    size = 0

    # TODO: Dodac przechowywanie danych o slotach w klasie
    content = []

    def __init__(self, x_slots, y_slots, x_pos, y_pos):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.x_slots = x_slots
        self.y_slots = y_slots
        self.size = x_slots * y_slots
        for i in range(self.size):
            self.content.append(Slot.Slot("empty"))

    def addItem(self, item, count, slot):
        print("Dodaje item")
        if slot[0] <= self.x_slots and slot[1] <= self.y_slots:
            for i in range(self.size):
                position = self.content[slot[0] * self.y_slots + slot[1] + i]
                if position.item == "empty" or position.item == item:
                    position.item = item
                    position.quantity += count
                    print([(el.item, el.quantity) for el in self.content])
                    return True
        return False
