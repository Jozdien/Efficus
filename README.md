# The Whats and Hows

Nearly every word in a normal piece of text is from a dictionary.  And it's likely that the average number of characters in these words is larger than three.
This means that we have a list of nearly every word that we might come across to compress.  Now, what do we do with this much information?

Well, we can convert the text we have into a list of numbers that tell us where to find those words in our list.

There are 171, 476 words in the Oxford English Dictionary, Second Edition.  And for the sake of overkill, this uses a dictionary of 370, 101 words.
And to account for all the numbers we need, and those pesky special characters (26 of them), we need more.

This means we need 19 bits (2^19 = 524288) to index everything.  The extra means we can index upto 100000 numbers (We could do more, but for the sake of chopping up the text easier, we split numbers in five-digit segments).  The rest we use to store words in the text that aren't in our dictionary.

So first, we order the dictionary by most frequently used words, to make the compression more efficient. 


## ELI5

First we chop it up.

Then we realize we've already seen them, so we chuck them out and get the ones we already had.

Then we mash 'em.


## Sample

