import string

def count_words(text):
    return len(text.split())


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

