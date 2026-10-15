from text_utils import count_words, count_characters
from text_utils import word_frequency, most_frequent_word, word_percentages

text = input("Enter a sentence: ")

print("Words:", count_words(text))
print("Characters:", count_characters(text))
print("Word frequency:", word_frequency(text))

word, count = most_frequent_word(text)

if word is not None:
    print("Most frequent word:", word)
    print("Frequency:", count)
else:
    print("No words found.")

percentages = word_percentages(text)

print("\nWord percentages:")

if percentages:
    for word, percentage in percentages.items():
        print(f"{word}: {percentage:.2f}%")
else:
    print("No words found.")