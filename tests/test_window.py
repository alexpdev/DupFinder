from unittest import TestCase
import sys,os
from pathlib import Path
sys.path.append(os.path.dirname(Path(__file__).resolve().parent))
from dupfinder.window import Win
from PySide2.QtWidgets import QWidget, QApplication

class WinTest(TestCase):

    def test_math(self):
        self.assertEqual(1, 10-9)
        self.assertIn(14,[1,9,14])
        self.assertTrue([9])
        self.assertFalse("")

    def test_window(self):
        win = Win()
        self.assertTrue(win)
        self.assertEqual(win.windowTitle(),"DupFinder")
        self.assertIsInstance(win.central,QWidget)






