import math
from collections import defaultdict
from src.adapters.controllers.processor import find_word_associations
from definitions import STORAGE_DIR


if __name__ == "__main__":
    with open(f'{STORAGE_DIR}/files/data.txt', "r") as f:
        lines = f.readlines()
        temp = ""
        for line in lines:
            if line.strip():
                temp += line

        corpus = temp.split("\n")

    # Find top 5 word associations
    results = find_word_associations(corpus, n=5, min_freq=4)

    for assoc in results:
        print(f"Words: {assoc['word1']} - {assoc['word2']}")
        print(f"Mutual Information: {assoc['mutual_info']:.2f}")
        print(f"Co-occurrences: {assoc['cooccurrences']}")
        print()
