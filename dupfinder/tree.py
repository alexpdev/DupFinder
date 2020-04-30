import os,sys
from pathlib import Path
# from PySide2.QtGui import Qt
from PySide2.QtCore import QItemSelectionModel
from PySide2.QtGui import QStandardItem,QStandardItemModel
from PySide2.QtWidgets import QTableView,QFileSystemModel,QTreeView,QDirModel,QAction,QAbstractItemView


class Tree(QTreeView):
    def __init__(self,parent=None,window=None,table=None):
        super().__init__(parent=parent)
        self.setObjectName("Tree View")
        self.window = window
        self.table = table
        self.fsmodel = FileModel(parent=self,window=self.window)
        self.setModel(self.fsmodel)
        self.fsmodel.hideColumns()
        self.sModel = self.selectionModel()
        self.sModel.selectionChanged.connect(self.change_item)

    def change_item(self):
        items = self.currentIndex()
        self.fsmodel.table_data(items)



class FileModel(QFileSystemModel):
    def __init__(self,parent=None,window=None):
        super().__init__(parent=parent)
        self.view = parent
        self.setRootPath("C:")
        self.setResolveSymlinks(True)
        self.setReadOnly(True)

    def hideColumns(self):
        for i in range(1,self.columnCount()):
            self.view.hideColumn(i)

    def table_data(self,item):
        name = self.fileName(item)
        path = self.filePath(item)
        self.view.table.setdir(path)

class DuplicateTable(QTableView):
    def __init__(self, parent=None,window=None):
        super().__init__(parent=parent)
        self.window = window
        self.itemModel = StandardModel(parent=self,window=self.window)
        s = self.SelectionBehavior.SelectRows
        print(s)
        self.setSelectionBehavior(s)
        self.setModel(self.itemModel)
        vertHead = self.verticalHeader()
        vertHead.setHidden(True)
        self.drives = ["A:","V:","C:","D:"]

    def update_dups(self,lst):
        pathlst = [Path(i).resolve() for i in lst]
        for drive in self.drives:
            d = Path(drive).resolve()
            self.find_dups(pathlst,d)

    def find_dups(self,lst,path):
        for fd in path.iterdir():
            if fd.is_dir():
                try: self.find_dups(lst,fd)
                except: continue
            elif fd.name in [i.name for i in lst]:
                item = QStandardItem()
                item.setText(os.path.abspath(fd))
                self.itemModel.addItem(item)

class Table(QTableView):
    def __init__(self, parent=None,window=None):
        super().__init__(parent=parent)
        self.window = window
        self.itemModel = StandardModel(parent=self,window=self.window)
        self.setModel(self.itemModel)
        self.selectModel = self.selectionModel()
        self.setSelectionBehavior(self.SelectionBehavior.SelectRows)
        s = self.SelectionBehavior.SelectRows
        vertHead = self.verticalHeader().setHidden(True)
        self.selectModel.selectionChanged.connect(self.update_dups)

    def update_dups(self):
        lst,indeces = [],self.selectModel.selectedIndexes()
        for index in indeces:
            r,c = index.row(),index.column()
            item = self.itemModel.item(r,1)
            path = item.text()
            if path not in lst:
                lst.append(path)
        self.window.duptable.update_dups(lst)

    def clear_rows(self):
        r = self.itemModel.rowCount()
        for idx in range(r):
            row = self.itemModel.takeRow(idx)
            del row
        return

    def setdir(self,item):
        p = Path(item).resolve()
        self.itemModel.setdir(p)
        self.resizeColumnsToContents()
        self.resizeRowsToContents()


class StandardModel(QStandardItemModel):
    def __init__(self,parent=None,window=None):
        super().__init__(parent=parent)
        self.window = window
        self.view = parent
        self.setHorizontalHeaderLabels(["Name","Path"])

    def setdir(self,item):
        for i,path in enumerate(item.iterdir()):
            name = QStandardItem(path.name)
            p = QStandardItem(os.path.abspath(path))
            self.setItem(i,0,name)
            self.setItem(i,1,p)
        return

    def addItem(self,item):
        self.setItem(self.rowCount(),0,item)
