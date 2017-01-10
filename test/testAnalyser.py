# -*- coding: utf-8 -*-

import unittest
import text.analyser
from text.name import Name


class TestAnalyser(unittest.TestCase):
    def test_is_name(self):
        self.assertTrue(text.analyser.is_name("Виктор"))
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
        self.assertTrue(text.analyser.is_name("Петр"))
        self.assertTrue(text.analyser.is_name("Димке"))
        self.assertFalse(text.analyser.is_name(""))
        self.assertFalse(text.analyser.is_name(1345))
        self.assertFalse(text.analyser.is_name("о"))
        self.assertFalse(text.analyser.is_name("а"))

    def test_get_structured_sentence(self):
        self.assertEqual(text.analyser.get_structured_sentence("Я бы, Вася, поел коня, - сказал Отец!"),
                         ['Я', ' ', 'бы', ',', ' ', 'Вася', ',', ' ', 'поел', ' ', 'коня', ',', ' ', '-', ' ',
                          'сказал', ' ', 'Отец', '!'])

    def test_get_case(self):
        name = Name("на", "Кост", "", "е")
        self.assertEqual(text.analyser.get_case(name), 2)
        name = Name("", "Виктор", "", "")
        self.assertEqual(text.analyser.get_case(name), 0)
        name = Name("", "Дим", "он", "ом")
        self.assertEqual(text.analyser.get_case(name), 5)

    def test_get_name(self):
        word = "Петькой"
        self.assertEqual(text.analyser.get_name(word).name, "Пет")
        self.assertEqual(text.analyser.get_name(word).suffix, "ьк")
        self.assertEqual(text.analyser.get_name(word).ending, "ой")

        word = "Володя"
        self.assertEqual(text.analyser.get_name(word).name, "Волод")
        self.assertEqual(text.analyser.get_name(word).suffix, "")
        self.assertEqual(text.analyser.get_name(word).ending, "я")

        word = "Витеньку"
        self.assertEqual(text.analyser.get_name(word).name, "Вит")
        self.assertEqual(text.analyser.get_name(word).suffix, "еньк")
        self.assertEqual(text.analyser.get_name(word).ending, "у")

        self.assertIsNone(text.analyser.get_name("Псина"))

    def test_get_preposition(self):
        self.assertEqual(text.analyser.get_preposition("Доктор Конь соскучился по мрачному Петьке в штанах.", 10), "по")
        self.assertEqual(text.analyser.get_preposition("Без Володи мы все умрём.", 2), "без")
        self.assertEqual(text.analyser.get_preposition("Чёрный Димон выхватил кинжал.", 2), "")
        self.assertIsNone(text.analyser.get_preposition("Куоцуа жцуадл цуа.", 5))


if __name__ == '__main__':
    unittest.main()
