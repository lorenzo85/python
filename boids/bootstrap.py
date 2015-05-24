from threading import Event
from boids import BoidsModel
from datatransfer import DataTransfer
from gui import GUI

WIDTH = 1000
HEIGHT = 600

class Controller:
    def __init__(self, model):
        self._model = model

    def on_down(self):
        self._model.on_scatter()

def main():
    thread_events = Event()

    data_transfer = DataTransfer()
    model = BoidsModel(thread_events, data_transfer, WIDTH, HEIGHT)
    controller = Controller(model)
    app = GUI(WIDTH, HEIGHT, data_transfer, controller)

    model.start()
    app.on_execute()

    thread_events.set()
    model.join()

if __name__ == "__main__":
    main()
    print("Program gracefully exiting")