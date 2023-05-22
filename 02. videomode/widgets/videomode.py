import sys

from PySide6.QtWidgets import QWidget, QApplication
from ui.videomode_ui import Ui_VideoMode


class VideoMode(QWidget, Ui_VideoMode):
    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)


if __name__ == "__main__":
    # Qt application setup
    app = QApplication(sys.argv)
    vm = VideoMode()
    vm.show()
    sys.exit(app.exec())
