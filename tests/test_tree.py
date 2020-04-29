from unittest import TestCase
import sys,os
from pathlib import Path
sys.path.append(os.path.dirname(Path(__file__).resolve().parent))
from dupfinder.tree import Tree
from PySide2.QtWidgets import QWidget,QTreeView,QFileSystemModel, QApplication

class TreeTest(TestCase):
    qApp = QApplication(sys.argv)

    def test_tree(self):
        tree = Tree()
        self.assertIsInstance(tree,QTreeView)
        model = tree.model()
        self.assertIsInstance(model,QFileSystemModel)
        tree.destroy()

    def test_model(self):
        tree = Tree()
        model = tree.model()
        self.assertTrue(model.rootDirectory())
        self.assertTrue(os.path.isdir((model.rootDirectory()).absolutePath()))
        self.assertEqual(tree.fsmodel,model)
        self.assertEqual(tree, model.view)
        tree.destroy()

    def test_directories(self):
        tree = Tree()
        self.assertTrue(tree.fsmodel.myComputer())
        model = tree.model()
        myc = model.myComputer()
        print(myc)
        print(myc.absolutePath())






