#!/usr/bin/python

import sys
import nltk
import creature_names as cn
import split_words as sw

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
        action = sw.break_action(word)
        if action:
            tag += "-R"
            word = action
        if word[0].isalpha() and not word.lower() in sw.wordlist:
            self.novel_words.add(word)
            compounds = sw.break_compounds(word)
            if compounds:
                ctags = set()
                for c in compounds:
                    ctags.add("-".join(map(single_tag, c)))
                tag = "/".join(ctags)
        return (word, tag)

def single_tag(word):
    print word
    return nltk.pos_tag([word])[0][1]

def main():
    if len(sys.argv) > 1:
        raw_names = cn.set_to_names(sys.argv[1])
    else:
        raw_names = sys.stdin.read().splitlines()
    names = [TaggedName(name) for name in raw_names]
    novel = set.union(*(n.novel_words for n in names))
    print("\n".join(str(n) for n in names))

if __name__ == "__main__":
    main()
