from datetime import datetime
from threading import Event, Thread
from time import sleep

from PySide6.QtCore import QObject, Signal

from model.alarm import Alarm


class Clock(QObject):
    time_actualised = Signal(datetime)

    def __init__(self, alarms: list[Alarm] = None):
        super().__init__()
        self.actual_time = datetime.now()
        self.alarms = alarms
        self._stop_clock_event = Event()
        self.run_clock()

    @property
    def actual_time(self) -> datetime:
        return self._actual_time

    @actual_time.setter
    def actual_time(self, actual_time: datetime):
        self._actual_time = actual_time

    @property
    def alarms(self) -> list[Alarm]:
        return self._alarms

    @alarms.setter
    def alarms(self, alarms: list[Alarm]):
        if not alarms:
            self._alarms = []
        else:
            self._alarms = alarms

    def actualize_time(self):
        self.actual_time = datetime.now()
        self.time_actualised.emit(self.actual_time)

    def update_time_every_second(self):
        while not self._stop_clock_event.is_set():
            sleep(1)
            self.actualize_time()

    def run_clock(self):
        self.time_updating_thread = Thread(target=self.update_time_every_second)
        self.time_updating_thread.start()

    def stop_clock(self):
        self._stop_clock_event.set()
        self.time_updating_thread.join()

    def add_alarm(self, alarm: Alarm):
        self.alarms.append(alarm)

    def remove_alarm(self, alarm: Alarm):
        if alarm in self.alarms:
            self.alarms.remove(alarm)

    def _is_time_for_alarm(self, alarm: Alarm) -> bool:
        return datetime.strftime(self.actual_time, "%H:%M") == alarm.timing
