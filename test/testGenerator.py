import unittest
import text.generator

class TestGenerator(unittest.TestCase):

  def test_replace_name(self):
      self.assertEqual('kek', text.generator.getStory())

if __name__ == '__main__':
    unittest.main()