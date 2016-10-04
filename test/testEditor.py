import unittest
import text.editor


class TestEditor(unittest.TestCase):
    def test_replace_name(self):
        self.assertEqual('kek', text.editor.replaceName())


if __name__ == '__main__':
    unittest.main()
