import gui.Container
import gui.Gui


class Equipment:

    def __init__(self):
        self.corners = (15, 14, 10, 3)
        self.bb = gui.Gui.getRegionBoundingBox(self.corners)
        self.container = gui.Container.Container(self.corners)

    def draw(self, window, gui_handler):
        gui_handler.drawGrid(window, self.container.content, 0, self.corners)
