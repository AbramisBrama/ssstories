# -*- coding: utf-8 -*-

import unittest
import text.generator
import namedata.names


class TestGenerator(unittest.TestCase):
    def test_text_contains_name(self):
        self.assertTrue(text.generator.text_contains_name('Петр - жопа!'))
        self.assertTrue(text.generator.text_contains_name(
            'Вася, Владимир и прочие мужики залезли в код и думают: "Куда бы нам запихнуть анализатор падежа? В аналайзер.пай или в класс?'))
        self.assertTrue(
            text.generator.text_contains_name('Мы с друзьями - ингибиторы обратного обмена. Катерина и Витька.'))
        self.assertFalse(text.generator.text_contains_name('Заходит тетенька в собаковозку, а там собачки ей и говорят'))
        self.assertFalse(text.generator.text_contains_name('"Ква-Ква-Ква! Ква-Ква-Ква!" - И тут же поправились: "Гав, то есть."'))
        self.assertFalse(text.generator.text_contains_name(
            'Тут тетенька поняла, что собачки и есть муржевляне, которых она ищет. И без промедления аннигилировала их.'))

    def test_get_ss_sentence(self):
        namedata.names.ssnames = [
            [
                "Адольф Гитлер",
                "Адольфа Гитлера",
                "Адольфу Гитлеру",
                "Адольфа Гитлера",
                "Адольфом Гитлером",
                "Адольфе Гитлере"
            ]
        ]
        hitler_sentence = text.generator.get_printable_sentence(text.generator.get_ss_sentence("У Вовы был конь."))
        self.assertEqual(hitler_sentence, "У Адольфа Гитлера был конь.")


if __name__ == '__main__':
    unittest.main()
