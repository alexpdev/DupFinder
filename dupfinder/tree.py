import os,sys
from pathlib import Path
# from PySide2.QtGui import Qt
from PySide2.QtCore import QItemSelectionModel

from PySide2.QtWidgets import QTableView,QFileSystemModel,QTreeView,QDirModel,QAction


class Tree(QTreeView):
    def __init__(self,parent=None,window=None):
        super().__init__(parent=parent)
        self.setObjectName("Tree View")
        self.window = window
        self.fsmodel = FileModel(parent=self)
        self.setModel(self.fsmodel)
        self.fsmodel.hideColumns()
        SM = self.selectionModel()






class FileModel(QFileSystemModel):
    def __init__(self,parent=None):
        super().__init__(parent=parent)
        self.view = parent
        self.setRootPath("C:")
        self.setResolveSymlinks(True)
        self.setReadOnly(False)

    def hideColumns(self):
        for i in range(1,self.columnCount()):
            self.view.hideColumn(i)

