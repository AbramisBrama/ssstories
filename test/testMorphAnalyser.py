# -*- coding: utf-8 -*-

import unittest
import text.morph_analyser
from text.name import Name
from namedata import cases


class TestMorphAnalyser(unittest.TestCase):
    def test_is_name(self):
        self.assertTrue(text.morph_analyser.is_name("Виктор"))
        self.assertFalse(text.morph_analyser.is_name("WEefwe"))
        self.assertFalse(text.morph_analyser.is_name(" "))
        self.assertFalse(text.morph_analyser.is_name("324"))
        self.assertFalse(text.morph_analyser.is_name("WEВоваefwe"))
        self.assertFalse(text.morph_analyser.is_name("ей"))
        self.assertFalse(text.morph_analyser.is_name("же"))
        self.assertTrue(text.morph_analyser.is_name("Вова"))
        self.assertTrue(text.morph_analyser.is_name("Димону"))
        self.assertTrue(text.morph_analyser.is_name("Петькой"))
        self.assertTrue(text.morph_analyser.is_name("Владимиром"))
        self.assertTrue(text.morph_analyser.is_name("Петр"))
        self.assertTrue(text.morph_analyser.is_name("Димке"))
        self.assertFalse(text.morph_analyser.is_name(""))
        self.assertFalse(text.morph_analyser.is_name(1345))
        self.assertFalse(text.morph_analyser.is_name("облако"))
        self.assertFalse(text.morph_analyser.is_name("о"))
        self.assertFalse(text.morph_analyser.is_name("а"))

    def test_get_structured_sentence(self):
        self.assertEqual(text.morph_analyser.get_structured_sentence("Я бы, Вася, поел коня, - сказал Отец!"),
                         ['Я', ' ', 'бы', ',', ' ', 'Вася', ',', ' ', 'поел', ' ', 'коня', ',', ' ', '-', ' ',
                          'сказал', ' ', 'Отец', '!'])

    def test_get_case(self):
        self.assertEqual(text.morph_analyser.get_case(Name("на", "Кост", "", "е")), 'loct')
        self.assertEqual(text.morph_analyser.get_case(Name("", "Виктор", "", "")), 'nomn')
        self.assertEqual(text.morph_analyser.get_case(Name("", "Евгени", "", "ем")), 'ablt')
        self.assertEqual(text.morph_analyser.get_case(Name("без", "Вячеслав", "", "а")), 'gent')

    def test_get_name(self):
        self.assertEqual(text.morph_analyser.get_name("Петькой").print(), "Петькой")
        self.assertIsNone(text.morph_analyser.get_name("Псина"))

    def test_get_preposition(self):
        self.assertEqual(text.morph_analyser.get_preposition("Доктор Конь соскучился по мрачному Петьке в штанах.", 10), "по")
        self.assertEqual(text.morph_analyser.get_preposition("Без Володи мы все умрём.", 2), "без")
        self.assertEqual(text.morph_analyser.get_preposition("Чёрный Димон выхватил кинжал.", 2), "")
        self.assertIsNone(text.morph_analyser.get_preposition("Куоцуа жцуадл цуа.", 5))

    def test_is_preposition(self):
        for case_prep in cases.prepositions:
            for prep in case_prep:
                if not prep == '~':
                    self.assertTrue(text.morph_analyser.is_preposition(prep))


if __name__ == '__main__':
    unittest.main()
