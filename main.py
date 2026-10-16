
from text_utils import (
    count_words,
    count_characters,
    word_frequency,
    most_frequent_word,
    word_percentages,
    longest_and_shortest_words,
    count_sentences,
    average_word_length
)

text = input("Enter a sentence: ")

print("Words:", count_words(text))
print("Characters:", count_characters(text))

print("Sentences:", count_sentences(text))
print(f"Average word length: {average_word_length(text):.2f}")

frequency = word_frequency(text)

if not frequency:
    print("No words found.")
else:
    print("Word frequency:", frequency)

    word, count = most_frequent_word(text)
    print("Most frequent word:", word)
    print("Frequency:", count)

    percentages = word_percentages(text)

    print("\nWord percentages:")
    for word, percentage in percentages.items():
        print(f"{word}: {percentage:.2f}%")

    longest, shortest = longest_and_shortest_words(text)
    print("Longest word:", longest)
    print("Shortest word:", shortest)
