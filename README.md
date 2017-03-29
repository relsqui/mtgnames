## MTG Creature Name Analyzer

These are some scripts I ([Finn](mailto:relsqui@chiliahedron.com)) threw together to study the naming conventions of Magic creature cards. I release them into the public domain to the extent allowable by law. Extensive documentation fails a cost/benefit estimate pretty drastically, but here's a brief summary of what's in the repository and how to use it:


### Dependencies

* The Natural Language Tool Kit. `pip install nltk` will set you up. If it nags you about missing data, open `python` and `import nltk`, then `nltk.download("name-of-thing-it-asked-for")`.


### Scripts You Need to Replicate My Data

* `get_sets.py`: Create a directory for set data and fill it with JSON set files from mtgjson.com. (In retrospect, I could've done this with just the single all-cards file, but I needed the set files for my previous project so I had this script lying around.)
* `tag_sets.sh`: For each set in the set directory, run it through the creature name tagger and put the output in the tagged sets directory.
* `tagged_sets/make_unique.sh`: (You want to `cd tagged_sets` before running this because it uses relative paths.) For each tagged set, create a summary of the unique tag patterns and sort them by frequency.
* `make_summary.sh`: Generate a summary of the most-used tag patterns for each set, highlighting the patterns in `target_patterns.grep`, and print it in a nice human-readable way with examples.
* `tagged_sets/count_total.sh`: (Once again, `cd tagged_sets` to run this.) Count the frequency of cards with target patterns relative to the number of cards in each set, then print a summary.


### Other Scripts

* `creature_names.py`: List just the names of creatures that appear in a given set. You can either pass a set code as an argument (`./creature_names.py THS`) or pass in the entire JSON file for the set on STDIN (`./creature_names < sets/THS.json`).
* `parse_names.py`: Parse each creature name in a set, and output each name followed by its tags. See `tags` to learn what the tags mean. You can either give it a set code on the command line, or a set of names on STDIN (for example, the output of `creature_names.py`, which is what `tag_sets.sh` does).


### Static Files

* `target_patterns.grep`: A list of regular expressions to highlight in the summaries. You don't need to do anything with this, but you can change it if you're interested in other 
* `tags`: Definitions of the Penn Treebank part-of-speech tags.
* `ordered_sets.txt`: A list of Magic sets, in chronological order. This is just here so that other scripts can use it as a guide instead of listing things in lexographical order.


### Potential Improvements

* Filter the sets more thoughtfully (excluding reprint-only sets, for example).
* Exclude reprints altogether.
* Catch a couple of errors produced by `tag_sets.sh` in special cases (mostly but not entirely unicode).

### Why on Earth

Mani Cavalieri [nerdsniped me](https://www.facebook.com/mani.cavalieri/posts/10106113073234039).

### Other MTG Linguistics

If you like this nonsense, you might also enjoy:

* [MTG Corpus](https://github.com/relsqui/mtgcorpus), which is sort of like this except that it uses Parsey McParseFace (Google's English-parsing SyntaxNet model) for tagging and operates on rules and ruling text.
* [most_rulings](https://gist.github.com/relsqui/d5d4ccd8c4bf257b7be3a376cf007076), a previous rabbithole I went down to figure out which Magic card has the most unique rulings.
* [MTG Lexicology](https://twitter.com/mtgglossary), which I have no affiliation with but wish I did.
