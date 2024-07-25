from model.utilities import correct_timing_format


class Alarm:
    def __init__(self, timing: str, text: str = None, active: bool = False):
        self.timing = timing
        self.text = text
        self.active = active

    @property
    def timing(self) -> str:
        return self._timing

    @timing.setter
    def timing(self, timing: str):
        if correct_timing_format(timing):
            self._timing = timing
        else:
            raise ValueError(f"Invalid timing format: {timing}")

    @property
    def text(self) -> str:
        return self._text

    @text.setter
    def text(self, text: str):
        self._text = text

    @property
    def is_alarm_active(self) -> bool:
        return self.active

    def activate(self):
        self.active = True

    def deactivate(self):
        self.active = False

    def __eq__(self, other):
        return self.timing == other.timing and self.text == other.text

    def __str__(self):
        return f"{self.timing}: {self.text}"
