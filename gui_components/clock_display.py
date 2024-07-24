import os
import sys
from datetime import datetime

from PySide6.QtGui import Qt
from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout, QApplication, QSizePolicy, QHBoxLayout

from model.clock import Clock


class ClockGui(QWidget):
    def __init__(self, name: str, clock: Clock = None):
        super().__init__()
        self.name = name
        self.clock = clock
        self.setup_ui()

    def setup_ui(self):
        self.create_widgets()
        self.create_layouts()
        self.add_widgets_to_layouts()
        self.modify_time_display_content(self.clock.actual_time)
        self.modify_widgets_properties()
        self.modify_widgets_styling(os.path.join("../resources/style.css"))
        self.setup_connections()

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, name: str) -> None:
        self._name = name
        self.setWindowTitle(self.name)

    @property
    def clock(self) -> Clock:
        return self._clock

    @clock.setter
    def clock(self, clock: Clock) -> None:
        self._clock = clock

    def create_widgets(self):
        self.time_display = QLabel()

    def create_layouts(self):
        self.main_layout = QVBoxLayout(self)
        self.time_layout = QHBoxLayout()

    def add_widgets_to_layouts(self):
        self.main_layout.addLayout(self.time_layout)
        self.time_layout.addWidget(self.time_display)

    def modify_time_display_content(self, time: datetime):
        self.time_display.setText(datetime.strftime(time, "%H:%M:%S"))

    def modify_widgets_styling(self, file: str):
        with open(file, 'r') as f:
            style_sheet = f.read()
            self.setStyleSheet(style_sheet)

    def modify_widgets_properties(self):
        # modifying for StyleSheet
        self.time_display.setObjectName("TimeDisplay")

        self.main_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.time_display.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        self.time_display.setAlignment(Qt.AlignmentFlag.AlignCenter)

    def setup_connections(self):
        self.clock.time_actualised.connect(self.modify_time_display_content)

    def closeEvent(self, event):
        self.clock.stop_clock()
        event.accept()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ClockGui('Orange Watch', Clock())
    window.show()
    sys.exit(app.exec())
