from text_utils import count_words, count_characters
from text_utils import word_frequency

text = input("Enter a sentence: ")

print("Words:", count_words(text))
print("Characters:", count_characters(text))
print("Word frequency:", word_frequency(text))