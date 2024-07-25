from model.utilities import correct_timing_format


class Alarm:
    def __init__(self, timing: str, text: str = None):
        self.timing = timing
        self.text = text

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
