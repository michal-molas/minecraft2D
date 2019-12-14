import gui.Container
import gui.Gui


class Bar:

    def __init__(self):
        self.picked_slot = None
        self.corners = (15, -2, 10, 1)
        self.bb = gui.Gui.getRegionBoundingBox(self.corners)
        self.container = gui.Container.Container(self.corners)

    def draw(self, window, gui_handler):
        gui_handler.drawGrid(window, self.container.content, 0, self.corners)
