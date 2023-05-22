from pathlib import Path
import sys

from PySide6.QtWidgets import QApplication

from widgets.videomode import VideoMode

if __name__ == "__main__":
    # Qt application setup
    app = QApplication(sys.argv)
    vm = VideoMode()
    vm.show()
    css_file = Path(__file__).parent / Path("style.css")
    with css_file.open("r") as f:
        _style = f.read()
        app.setStyleSheet(_style)
    sys.exit(app.exec())
