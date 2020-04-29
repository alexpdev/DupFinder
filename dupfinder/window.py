import os
import sys
from PySide2.QtWidgets import QApplication,QMainWindow,QWidget,QGridLayout,QHBoxLayout,QTableView,QSplitter
from PySide2.QtCore import Qt
from dupfinder.tree import Tree
print(Qt)
print(Qt.Orientation.Vertical)
print(Qt.Orientation.Horizontal)


class Win(QMainWindow):
    def __init__(self,parent=None):
        super().__init__(parent=parent)
        self.setObjectName("name")
        self.setWindowTitle("DupFinder")
        self.resize(1400,800)
        self.central = QWidget()
        self.central.setObjectName("Central Widget")
        self.tree1 = Tree()
        self.tree2 = Tree()
        self.table1 = QTableView()
        self.table2 = QTableView()
        self.layout = QHBoxLayout()
        self.central.setLayout(self.layout)
        self.splitter1 = QSplitter(Qt.Orientation.Horizontal)
        self.splitter2 = QSplitter()
        self.layout.addWidget(self.splitter1)
        self.layout.addWidget(self.splitter2)
        self.splitter1.addWidget(self.tree1)
        self.splitter1.addWidget(self.table1)
        self.splitter2.addWidget(self.table2)
        self.splitter2.addWidget(self.tree2)
        self.setCentralWidget(self.central)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Win()
    win.show()

    sys.exit(app.exec_())


