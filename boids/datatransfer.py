from threading import Lock


class DataTransfer:
    flock_configuration = []

    def __init__(self):
        self._data_lock = Lock()

    def publish(self, configuration):
        self._data_lock.acquire()
        self.flock_configuration.append(configuration)
        self._data_lock.release()

    def get_next_configuration(self):
        self._data_lock.acquire()
        conf = self.flock_configuration.pop() if self.flock_configuration else None
        self._data_lock.release()
        return conf
