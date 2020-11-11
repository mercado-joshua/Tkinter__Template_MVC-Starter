"""
Controller connects the view and the model by receiving user input and updating the model data.
This corresponds to callbacks, event handlers and the attributes needed.
"""
#===========================
# Imports
#===========================
from model import Model
from view import View

#===========================
# Controller
#===========================
class Controller:
    def __init__(self):
        self._model = Model()
        self._view = View(self)

    def main(self):
        self._view.main()

    # INSTANCE ---------------------------------
    # EVENTS -----------------------------------
    # PARAMETERS -------------------------------

#===========================
# Start GUI
#===========================
def main():
    app = Controller()
    app.main()

if __name__ == '__main__':
    main()