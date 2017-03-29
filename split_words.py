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

def break_action(word):
    if not (word.endswith("er") or word.endswith("or")):
        return None
    maybe_verb = word[:-1]
    if nltk.pos_tag([maybe_verb])[0][1].startswith("V"):
        return maybe_verb
    maybe_verb = maybe_verb[:-1]
    if nltk.pos_tag([maybe_verb])[0][1].startswith("V"):
        return maybe_verb
    return None

wordlist = clean_words()
