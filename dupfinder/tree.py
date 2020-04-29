import os,sys
from pathlib import Path
from PySide2.QtGui import Qt
from PySide2.QtWidgets import QTableView,QFileSystemModel,QTreeView


class Tree(QTreeView):
    def __init__(self,parent=None):
        super().__init__(parent=parent)
        self.setObjectName("Tree View")
        self.window = parent
        self.fsmodel = FileModel(parent=self)
        self.setModel(self.fsmodel)



class FileModel(QFileSystemModel):
    def __init__(self,parent=None):
        super().__init__(parent=parent)
        self.view = parent
        self.setRootPath("C:")
        self.setResolveSymlinks(True)
        self.setReadOnly(False)
        # self.setRootIndex(self.rootDirectory())

