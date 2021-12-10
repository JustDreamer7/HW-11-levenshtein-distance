import unittest

from levenshtein import levenshtein


class LevenshteinTest(unittest.TestCase):
    def setUp(self):
        self.word_1 = "колокол"
        self.word_2 = "молоко"
        self.word_empty = ""

    def test_result(self):
        self.assertEqual(levenshtein(self.word_1, self.word_empty), len(self.word_1))
        self.assertEqual(levenshtein(self.word_2, self.word_empty), len(self.word_2))
        self.assertEqual(levenshtein(self.word_empty, self.word_empty), 0)
        self.assertEqual(levenshtein(self.word_1, self.word_2), 2)

    def test_type_result(self):
        with self.assertRaises(TypeError):
            levenshtein(231, 1231)
            levenshtein(True, False)


if __name__ == "__main__":
    unittest.main()
