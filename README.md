This Python script uses the [multiprocessing]("http://docs.python.org/2/library/multiprocessing.html", "mulitprocessing") module to calculate ngrams in a txt file.

## Example Use ##
Calculate all the 3-grams in the txt file `HuckleberryFinn.txt`:

```bash
python pyngram.py HuckleberryFinn.txt 3
```
which will create a tab seperated file called `3grams.tsv` with the sorted counts of 3-grams in [The Adventures of Huckleberry Finn](http://www.gutenberg.org/ebooks/76) by [Mark Twain](http://www.gutenberg.org/ebooks/author/53). Take a look at the output file:

```bash
head -15 3grams.tsv
```
```
3gram    count
out of the	60
was going to	47
said it was	35
by and by	35
a lot of	32
and then he	29
the old man	28
the middle of	27
kind of a	25
and it was	25
it was a	24
one of them	23
a couple of	23
there was a	22
```

## Extending this example ##
Although the demo input txt file is small, the ngram counting script in this repo is capable of counting ngrams in *much* larger input files (which are currently first turned into one long list of lines/strings).
