# The Whats and Hows

Nearly every word in a **normal** piece of text is from a dictionary. This means that we have a list of nearly every word that we might come across to compress. We can convert the text we have into a list of numbers that tell us where to find those words in our list.

There are 171,476 words in the Oxford English Dictionary, Second Edition.  The Corpus of Contemporary American English contains over 1 billion words.  There are few dictionaries with that much spread and accompanying frequency analysis, the largest of which is the [Frequency data on the Corpus of Contemporary American English (COCA)](https://www.wordfrequency.info/).  But that costing money, and my being stingy, led to the use of the 41,284-word list over at [Wiktionary](https://en.wiktionary.org/wiki/Wiktionary:Frequency_lists#TV_and_movie_scripts).  Subsequently, its efficiency is reduced **significantly**, and yet still works with a compression factor of over 5, as tested on the plaintext version of Jane Austen's Pride and Prejudice, even with reduced accuracy of frequency levels, and 1152 words that aren't present on the shorter dictionary (the majority of which are present in the complete version).


## ELI5

First we chop it up.

Then we realize we've already seen them, so we chuck them out and get the ones we already had.

Then we mash 'em.


## Sample

"This is a string" with 128 bits, becomes "111111111000000010001101" in binary, amounting to 24 bits, for a compression factor of 5.33.


### Pride and Prejudice by Jane Austen:

Original length in bits: 5484560

Compressed length in bits: 1042991

Compression Factor: 5.258492

Average Compression Time per byte: 57075.97473 ns