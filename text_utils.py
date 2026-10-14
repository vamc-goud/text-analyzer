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