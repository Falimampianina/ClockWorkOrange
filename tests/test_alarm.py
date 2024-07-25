import pytest

from model.alarm import Alarm


def test_alarm_init():
    with pytest.raises(ValueError):
        alarm = Alarm("25:00", "Alarm for nothing")

    assert Alarm("06:00", "Wake up my friend")
