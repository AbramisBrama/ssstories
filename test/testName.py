# -*- coding: utf-8 -*-

import unittest
from text.name import Name


class TestEditor(unittest.TestCase):
    def test_parse(self):
        n = Name.parse("Володьку")
        self.assertEqual((n.name, n.suffix, n.ending), ("Волод", "ьк", "у"))
        n = Name.parse("Димона")
        self.assertEqual((n.name, n.suffix, n.ending), ("Дим", "он", "а"))
        n = Name.parse("Петром")
        self.assertEqual((n.name, n.suffix, n.ending), ("Петр", "", "ом"))
        n = Name.parse("Виктор")
        self.assertEqual((n.name, n.suffix, n.ending), ("Виктор", "", ""))
        self.assertIsNone(Name.parse("Козельск"))

if __name__ == '__main__':
    unittest.main()
