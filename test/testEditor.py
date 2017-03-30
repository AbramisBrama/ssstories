# -*- coding: utf-8 -*-

import unittest

import namedata.names
import text.editor


class TestEditor(unittest.TestCase):
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
        hitler_sentence = text.editor.get_printable_sentence(
            text.editor.get_ss_sentence("У Вовы был конь."))
        self.assertEqual(hitler_sentence, "У Адольфа Гитлера был конь.")

        hitler_sentence = text.editor.get_printable_sentence(text.editor.get_ss_sentence("Вождь дал Егору топор."))
        self.assertEqual(hitler_sentence, "Вождь дал Адольфу Гитлеру топор.")

        hitler_sentence = text.editor.get_printable_sentence(text.editor.get_ss_sentence("Этот город был основан Великим Петром."))
        self.assertEqual(hitler_sentence, "Этот город был основан Великим Адольфом Гитлером.")


if __name__ == '__main__':
    unittest.main()
