
import unittest

from text_utils import (
    count_words,
    count_characters,
    word_frequency,
    most_frequent_word,
    word_percentages,
    longest_and_shortest_words,
    count_sentences,
    average_word_length,
)


class TestTextUtils(unittest.TestCase):

    def test_count_words(self):
        self.assertEqual(count_words("Python is easy"), 3)

    def test_count_words_ignores_punctuation(self):
        self.assertEqual(count_words("!!! ,,, ..."), 0)

    def test_count_characters(self):
        self.assertEqual(count_characters("Python"), 6)

    def test_word_frequency(self):
        self.assertEqual(
            word_frequency("Python python AI"),
            {"python": 2, "ai": 1},
        )

    def test_most_frequent_word(self):
        self.assertEqual(
            most_frequent_word("cat dog cat"),
            ("cat", 2),
        )

    def test_word_percentages(self):
        result = word_percentages("cat dog cat")
        self.assertAlmostEqual(result["cat"], 66.6667, places=3)
        self.assertAlmostEqual(result["dog"], 33.3333, places=3)

    def test_longest_and_shortest_words(self):
        self.assertEqual(
            longest_and_shortest_words("Python is powerful"),
            ("powerful", "is"),
        )

    def test_count_sentences(self):
        self.assertEqual(
            count_sentences("Python is easy. AI is powerful!"),
            2,
        )

    def test_punctuation_only_has_no_sentences(self):
        self.assertEqual(count_sentences("!!! ,,, ..."), 0)

    def test_average_word_length(self):
        self.assertAlmostEqual(
            average_word_length("cat dogs"),
            3.5,
        )

    def test_average_word_length_empty(self):
        self.assertEqual(average_word_length("!!!"), 0)


if __name__ == "__main__":
    unittest.main()


def test_empty_text(self):
    self.assertEqual(count_words(""), 0)
    self.assertEqual(word_frequency(""), {})
    self.assertEqual(average_word_length(""), 0)

def test_spaces_only(self):
    self.assertEqual(count_words("   "), 0)
    self.assertEqual(word_frequency("   "), {})

def test_frequency_is_case_insensitive(self):
    self.assertEqual(
        word_frequency("Python python PYTHON"),
        {"python": 3},
    )

def test_punctuation_is_removed(self):
    self.assertEqual(
        word_frequency("Hello, hello!"),
        {"hello": 2},
    )

def test_tied_word_frequencies(self):
    word, count = most_frequent_word("cat dog")
    self.assertIn(word, ("cat", "dog"))
    self.assertEqual(count, 1)
