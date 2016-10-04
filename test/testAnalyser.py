# -*- coding: utf-8 -*-

import unittest
import text.analyser
import string


class TestAnalyser(unittest.TestCase):
    def test_is_name(self):
        self.assertFalse(text.analyser.is_name("WEefwe"))
        self.assertFalse(text.analyser.is_name(" "))
        self.assertFalse(text.analyser.is_name("324"))
        self.assertFalse(text.analyser.is_name("WEВоваefwe"))
        self.assertTrue(text.analyser.is_name("Вова"))
        self.assertTrue(text.analyser.is_name("Димону"))
        self.assertTrue(text.analyser.is_name("Петькой"))
        self.assertTrue(text.analyser.is_name("Владимиром"))
        self.assertTrue(text.analyser.is_name("Пётр"))
        self.assertTrue(text.analyser.is_name("Димке"))

    def test_get_structured_sentence(self):
        self.assertEquals(text.analyser.get_structured_sentence("Я бы, Вася, поел коня, - сказал Отец!"), ['Я', ' ', 'бы', ',', ' ', 'Вася', ',', ' ', 'поел', ' ', 'коня', ',', ' ', '-', ' ', 'сказал', ' ', 'Отец', '!'])


if __name__ == '__main__':
    unittest.main()
