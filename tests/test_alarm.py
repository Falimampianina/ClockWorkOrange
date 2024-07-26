import pytest

from model.alarm import Alarm


def test_alarm_init():
    with pytest.raises(ValueError):
        alarm = Alarm("25:00", "Alarm for nothing")

    assert Alarm("06:00", "Wake up my friend")


def test_alarm_activate():
    alarm = Alarm("06:00", "Alarm for nothing")
    assert alarm.is_alarm_active is False
    alarm.activate()
    assert alarm.is_alarm_active is True


def test_alarm_deactivate():
    alarm = Alarm("06:00", "Alarm for nothing", True)
    assert alarm.is_alarm_active is True
    alarm.deactivate()
    assert alarm.is_alarm_active is False


def test_alarm_eq():
    alarm1 = Alarm("06:00", "Alarm for nothing")
    alarm2 = Alarm("06:00", "Alarm for nothing")
    assert alarm1 == alarm2
