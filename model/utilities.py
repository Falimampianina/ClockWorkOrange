import re


def correct_timing_format(timing: str) -> bool:
    pattern = "^([0-1][0-9]|[2][0-3]):[0-5][0-9]$"
    if re.match(pattern, timing):
        return True
    return False
