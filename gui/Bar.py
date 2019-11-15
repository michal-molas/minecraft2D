import gui.Container


class Bar:
    container = None
    picked_slot = 0

    def __init__(self):
        self.container = gui.Container.Container(1, 10, -5, 2)

    def draw(self, window, gui_handler):
        gui_handler.drawGrid(window, self.container.content, 0, self.container.x_slots, self.container.y_slots,
                             self.container.x_pos, self.container.y_pos)
