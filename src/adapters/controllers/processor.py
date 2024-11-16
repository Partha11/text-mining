import math
from collections import defaultdict
from src.adapters.controllers.tokenizer import tokenize


def calculate_frequencies(corpus):
    """
    Calculate word frequencies and co-occurrence frequencies within a window
    """
    window = 5
    word_freq = defaultdict(int)
    cooccurrence_freq = defaultdict(lambda: defaultdict(int))
    total_words = 0

    for document in corpus:
        words = tokenize(document)
        total_words += len(words)

        for word in words:
            word_freq[word] += 1

        for i, w in enumerate(words):
            for j in range(i + 1, min(i + window + 1, len(words))):
                word = words[j]
                if w != word:
                    cooccurrence_freq[w][word] += 1
                    cooccurrence_freq[word][w] += 1

    return word_freq, cooccurrence_freq, total_words


def calculate_mutual_information(
    word1, word2, word_freq, cooccurrence_freq, total_words
):
    """
    Calculate mutual information between two words
    """
    freq1 = word_freq[word1]
    freq2 = word_freq[word2]

    cooccur = cooccurrence_freq[word1][word2]

    if cooccur == 0:
        return 0.0

    p1 = freq1 / total_words
    p2 = freq2 / total_words
    p12 = cooccur / total_words

    return math.log2(p12 / (p1 * p2))


def find_word_associations(corpus, n=10, min_freq=5):
    """
    Find top n word associations based on mutual information
    """
    word_freq, cooccurrence_freq, total_words = calculate_frequencies(corpus)
    associations = []

    for word1 in word_freq:
        if word_freq[word1] < min_freq:
            continue

        for word2 in cooccurrence_freq[word1]:
            if word_freq[word2] < min_freq:
                continue

            mi = calculate_mutual_information(
                word1, word2, word_freq, cooccurrence_freq, total_words
            )
            cooccur = cooccurrence_freq[word1][word2]

            associations.append(
                {
                    "word1": word1,
                    "word2": word2,
                    "mutual_info": mi,
                    "cooccurrences": cooccur,
                }
            )

    associations.sort(key=lambda x: x["mutual_info"], reverse=True)

    return associations[:n]
