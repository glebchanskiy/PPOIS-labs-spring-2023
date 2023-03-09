from lab4.core import Controller

from lab4.gui import ApplicationGUI


def gui():
    app = ApplicationGUI(Controller())
    app.run()
