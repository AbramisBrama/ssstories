# -*- coding: utf-8 -*-

import unittest
import text.analyser

class TestAnalyser(unittest.TestCase):

  def test_is_name(self):
      self.assertFalse(text.analyser.isName("WEefwe"))
      self.assertFalse(text.analyser.isName(" "))
      self.assertFalse(text.analyser.isName("324"))
      self.assertFalse(text.analyser.isName("WEВоваefwe"))
      self.assertTrue(text.analyser.isName("Вова"))
      self.assertTrue(text.analyser.isName("Димону"))
      self.assertTrue(text.analyser.isName("Петькой"))
      self.assertTrue(text.analyser.isName("Владимиром"))
      self.assertTrue(text.analyser.isName("Пётр"))
      self.assertTrue(text.analyser.isName("Димке"))

if __name__ == '__main__':
    unittest.main()