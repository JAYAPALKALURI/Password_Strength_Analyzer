#wordlist_generator
import itertools
import re

LEETS = {'a': ['4', '@'], 'e': ['3'], 'i': ['1', '!'], 'o': ['0'], 's': ['5', '$']}


def leetspeak_variants(word):
    variants = set([word])
    for i, c in enumerate(word):
        if c in LEETS:
            for l in LEETS[c]:
                for var in list(variants):
                    variants.add(var[:i] + l + var[i + 1:])
    return variants


def generate_wordlist(inputs):
    base_words = set()
    for word in inputs:
        word = word.lower()
        base_words.update(leetspeak_variants(word))
        base_words.add(word)

    final_words = set()
    for word in base_words:
        for year in ['2023', '2024', '2025']:
            final_words.add(word + year)
            final_words.add(year + word)
        final_words.add(word)

    return sorted(final_words)


# def save_wordlist(wordlist, filename='wordlists/custom_wordlist.txt'):
#     with open(filename, 'w') as f:
#         for word in wordlist:
#             f.write(f"{word}\n")


import os

def save_wordlist(wordlist, filename='wordlists/custom_wordlist.txt'):
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    with open(filename, 'w') as f:
        for word in wordlist:
            f.write(f"{word}\n")
