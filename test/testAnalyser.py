# -*- coding: utf-8 -*-

import unittest
import text.analyser
from text.name import Name


class TestAnalyser(unittest.TestCase):
    def test_is_name(self):
        self.assertFalse(text.analyser.is_name("WEefwe"))
        self.assertFalse(text.analyser.is_name(" "))
        self.assertFalse(text.analyser.is_name("324"))
        self.assertFalse(text.analyser.is_name("WEВоваefwe"))
        self.assertFalse(text.analyser.is_name("ей"))
        self.assertFalse(text.analyser.is_name("же"))
        self.assertTrue(text.analyser.is_name("Вова"))
        self.assertTrue(text.analyser.is_name("Димону"))
        self.assertTrue(text.analyser.is_name("Петькой"))
        self.assertTrue(text.analyser.is_name("Владимиром"))
        self.assertTrue(text.analyser.is_name("Пётр"))
        self.assertTrue(text.analyser.is_name("Димке"))
        self.assertFalse(text.analyser.is_name(""))
        self.assertFalse(text.analyser.is_name(1345))
        self.assertFalse(text.analyser.is_name("о"))
        self.assertFalse(text.analyser.is_name("а"))

    def test_get_structured_sentence(self):
        self.assertEquals(text.analyser.get_structured_sentence("Я бы, Вася, поел коня, - сказал Отец!"), ['Я', ' ', 'бы', ',', ' ', 'Вася', ',', ' ', 'поел', ' ', 'коня', ',', ' ', '-', ' ', 'сказал', ' ', 'Отец', '!'])

    def test_get_case(self):
        name = Name()
        name.preposition = "на"
        name.text = "Коле"

    def test_get_name(self):
        word = "Петькой"
        self.assertEquals(text.analyser.get_name(word).name, "Пет")
        self.assertEquals(text.analyser.get_name(word).suffix, "ьк")
        self.assertEquals(text.analyser.get_name(word).ending, "ой")

        word = "Володя"
        self.assertEquals(text.analyser.get_name(word).name, "Волод")
        self.assertEquals(text.analyser.get_name(word).suffix, "")
        self.assertEquals(text.analyser.get_name(word).ending, "я")

        word = "Витеньку"
        self.assertEquals(text.analyser.get_name(word).name, "Вит")
        self.assertEquals(text.analyser.get_name(word).suffix, "еньк")
        self.assertEquals(text.analyser.get_name(word).ending, "у")

        self.assertIsNone(text.analyser.get_name("Псина"))

if __name__ == '__main__':
    unittest.main()
