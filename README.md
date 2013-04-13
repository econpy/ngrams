This Python script uses the [multiprocessing]("http://docs.python.org/2/library/multiprocessing.html", "mulitprocessing") module to calculate ngrams in a txt file.

## Example Use ##
Calculate all the 3-grams in the txt file `HuckleberryFinn.txt`:

```bash
python pyngrams.py HuckleberryFinn.txt 3
```
which will create an output file called `2grams.txt` with the sorted counts of 2-grams in [The Adventures of Huckleberry Finn](http://www.gutenberg.org/ebooks/76) by [Mark Twain](http://www.gutenberg.org/ebooks/author/53).

## Note ##
Although the demo input txt file is small, the ngram counting script in this repo is capable of counting ngrams in *much* larger input files.
