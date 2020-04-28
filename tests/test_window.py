from unittest import TestCase

class WinTest(TestCase):
    def test_math(self):
        self.assertEqual(1, 10-9)
        self.assertIn(14,[1,9,14])
        self.assertTrue([9])
        self.assertFalse("")
