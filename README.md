This Python script uses the [multiprocessing]("http://docs.python.org/2/library/multiprocessing.html", "mulitprocessing") module to calculate ngrams in a txt file.

# Example Use #
Calculate 2-grams in the txt file `meaning_of_life.txt`:

```bash
python pyngrams.py meaning_of_life.txt 2
```
which will create an output file called `2grams.txt` with the sorted counts of 2-grams in `meaning_of_life.txt`.

# About #
Although the demo input txt file is very small, the ngram counting script in this repo is capable of counting ngrams in *much* larger input files.
