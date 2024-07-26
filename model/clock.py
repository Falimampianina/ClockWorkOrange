from datetime import datetime
from threading import Thread
from time import sleep

from PySide6.QtCore import QObject, Signal
from pytz import timezone

from assets.cities.cities import CITIES
from model.alarm import Alarm


class Clock(QObject):
    time_actualised = Signal(datetime)

    def __init__(self, alarms: list[Alarm] = None):
        super().__init__()
        self.actual_time = datetime.now()
        self.time_zone = "Local"
        self.alarms = alarms
        self.stop_clock_event = False
        self.time_updating_thread = Thread(target=self.update_time_every_second)
        self.run_clock()

    @property
    def actual_time(self) -> datetime:
        return self._actual_time

    @actual_time.setter
    def actual_time(self, actual_time: datetime):
        self._actual_time = actual_time

    @property
    def time_zone(self) -> str:
        return self._time_zone

    @time_zone.setter
    def time_zone(self, time_zone: str):
        self._time_zone = time_zone

    def get_actual_time_from_timezone(self, time_zone: str) -> datetime:
        if time_zone in CITIES["Europe"]:
            return self.actual_time.astimezone(timezone(f"Europe/{time_zone}"))
        elif time_zone in CITIES["Asia"]:
            return self.actual_time.astimezone(timezone(f"Asia/{time_zone}"))
        elif time_zone in CITIES["Indian"]:
            return self.actual_time.astimezone(timezone(f"Indian/{time_zone}"))
        elif time_zone in CITIES["America"]:
            return self.actual_time.astimezone(timezone(f"America/{time_zone}"))
        else:
            return self.actual_time

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
        self.time_actualised.emit(self.get_actual_time_from_timezone(self.time_zone))

    def update_time_every_second(self):
        while not self.stop_clock_event:
            sleep(1)
            self.actualize_time()

    def run_clock(self):
        self.time_updating_thread.start()

    def stop_clock(self):
        self.stop_clock_event = True
        self.time_updating_thread.join()

    def add_alarm(self, alarm: Alarm):
        self.alarms.append(alarm)

    def remove_alarm(self, alarm: Alarm):
        if alarm in self.alarms:
            self.alarms.remove(alarm)

    def _is_time_for_alarm(self, alarm: Alarm) -> bool:
        return datetime.strftime(self.actual_time, "%H:%M") == alarm.timing
