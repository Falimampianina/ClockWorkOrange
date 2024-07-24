from datetime import datetime
from threading import Event, Thread
from time import sleep

from PySide6.QtCore import QObject, Signal


class Clock(QObject):
    time_actualised = Signal(datetime)

    def __init__(self):
        super().__init__()
        self.actual_time = datetime.now()
        self._stop_clock_event = Event()
        self.run_clock()

    @property
    def actual_time(self) -> datetime:
        return self._actual_time

    @actual_time.setter
    def actual_time(self, actual_time: datetime):
        self._actual_time = actual_time

    def actualize_time(self):
        self.actual_time = datetime.now()
        self.time_actualised.emit(self.actual_time)

    def update_time_every_second(self):
        while not self._stop_clock_event.is_set():
            sleep(1)
            self.actualize_time()

    def run_clock(self):
        self.main_thread = Thread(target=self.update_time_every_second)
        self.main_thread.start()

    def stop_clock(self):
        self._stop_clock_event.set()
        self.main_thread.join()
