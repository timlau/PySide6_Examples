import sys
import qdarktheme

from PySide6.QtWidgets import QApplication
from widgets.videomode import VideoMode

if __name__ == "__main__":
    # Qt application setup
    app = QApplication(sys.argv)
    # Apply the complete dark theme to your Qt App.
    qdarktheme.setup_theme()

    vm = VideoMode()
    vm.show()
    sys.exit(app.exec())
