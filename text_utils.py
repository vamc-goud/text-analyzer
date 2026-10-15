import string

def count_words(text):
    translator = str.maketrans("", "", string.punctuation)
    cleaned_text = text.lower().translate(translator)
    words = cleaned_text.split()
    return len(words)

def count_characters(text):
    return len(text)


def word_frequency(text):
    text = text.lower()

    translator = str.maketrans("", "", string.punctuation)
    text = text.translate(translator)

    words = text.split()
    frequency = {}

    for word in words:
        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1

    return frequency


def most_frequent_word(text):
    frequency = word_frequency(text)

    if not frequency:
        return None, 0

    word = max(frequency, key=frequency.get)

    return word, frequency[word]


def word_percentages(text):
    frequency = word_frequency(text)
    total = sum(frequency.values())

    percentages = {}

    if total == 0:
        return percentages

    for word, count in frequency.items():
        percentage = (count / total) * 100
        percentages[word] = percentage

    return percentages


def longest_and_shortest_words(text):
    frequency = word_frequency(text)
    words = list(frequency.keys())

    if not words:
        return None, None

    longest = max(words, key=len)
    shortest = min(words, key=len)

    return longest, shortest



import re

def count_sentences(text):
    # Split text at sentence-ending punctuation.
    parts = re.split(r"[.!?]+", text)

    # Keep only parts containing at least one word character.
    sentences = [
        part for part in parts
        if re.search(r"\w", part)
    ]

    return len(sentences)




def average_word_length(text):
    translator = str.maketrans("", "", string.punctuation)
    cleaned_text = text.lower().translate(translator)
    words = cleaned_text.split()

    if not words:
        return 0

    total_characters = 0

    for word in words:
        total_characters += len(word)

    return total_characters / len(words)


