import os,sys
from pathlib import Path
sys.path.append((Path(__file__).resolve()).parent)
from PySide2.QtWidgets import QApplication
from dupfinder.window import Win

if __name__ == "__main__":
    app = QApplication()
    win = Win()
    win.show()
    sys.exit(app.exec_())
