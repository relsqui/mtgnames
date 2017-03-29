#!/usr/bin/python

import sys
import nltk

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
        if not word[0].isalpha() or word.lower() in wordlist:
            return (word, tag)
        self.novel_words.add(word)
        tag += "*"
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

if __name__ == "__main__":
    if len(sys.argv) > 1:
        import creature_names as cn
        raw_names = cn.set_to_names(sys.argv[1])
    else:
        raw_names = sys.stdin.read().splitlines()
    wordlist = clean_words()
    names = [TaggedName(name) for name in raw_names]
    novel = set.union(*[n.novel_words for n in names])
    print("\n".join(str(n) for n in names))
