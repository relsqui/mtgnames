#!/usr/bin/python

import nltk

def clean_words():
    words = set()
    with open("/usr/share/dict/words") as f:
        for word in f:
            word = word[:-1]
            if (word.isalpha() and word == word.lower() and
               all(ord(c) < 128 for c in word)):
                words.add(word)
    return words.union(set(nltk.corpus.words.words()))

def break_compounds(word):
    word = word.lower()
    compounds = []
    for i in range(3, len(word)-2):
        first, second = (word[:i], word[i:])
        if first in wordlist and second in wordlist:
            compounds.append((first, second))
    if "-" in word:
        parts = word.split("-")
        if all(p in wordlist for p in parts):
            compounds.append(tuple(parts))
    return compounds

def break_actors(word):
    # Not actually using this right now, because it produces more false
    # negatives than just checking if the word ends in -er produces false
    # positives.
    if not (word.endswith("er") or word.endswith("or")):
        return []
    word = word.lower()
    test_words = set([word[:-1], word[:-2], word[:-2] + "e"])
    for w in [word[:-1], word[:-2]]:
        compounds = break_compounds(word)
        for c in compounds:
            test_words.add(c[1][:-1])
            test_words.add(c[1][:-2])
    print test_words
    return filter(lambda w: nltk.pos_tag([w])[0][1].startswith("V"), test_words)

wordlist = clean_words()
