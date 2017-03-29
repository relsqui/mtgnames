#!/usr/bin/python

import sys
import nltk
import creature_names as cn

wordlist = None

class TaggedName(object):
    def __init__(self, name):
        self.name = name
        self.tagged = nltk.pos_tag(nltk.word_tokenize(name))
        self.novel_words = set()
        self.modified = map(self.retag, self.tagged)

    def __str__(self):
        tags = [t[1] for t in self.modified]
        return "{0}: {1}".format(self.name, " ".join(tags))

    def retag(self, word_tag):
        word, tag = word_tag
        word = word.lower()
        compounds = []
        if word[0].isalpha() and not word in wordlist:
            self.novel_words.add(word)
            compounds = break_compounds(word)
            if compounds:
                ctags = set()
                for c in compounds:
                    ctags.add("-".join(map(single_tag, c)))
                tag = "/".join(ctags)
        if word.endswith("er"):
            tag += "-R"
        return (word, tag)

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

def single_tag(word):
    return nltk.pos_tag([word])[0][1]

def main():
    global wordlist
    wordlist = clean_words()
    if len(sys.argv) > 1:
        raw_names = cn.set_to_names(sys.argv[1])
    else:
        raw_names = sys.stdin.read().splitlines()
    names = [TaggedName(name) for name in raw_names]
    novel = set.union(*(n.novel_words for n in names))
    print("\n".join(str(n) for n in names))

if __name__ == "__main__":
    main()
