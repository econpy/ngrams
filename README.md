This Python script uses the [multiprocessing]("http://docs.python.org/2/library/multiprocessing.html", "mulitprocessing") module to calculate ngrams in a txt file.

# Example Use #
Run the following command to calculate the 2 grams in the txt file `life_of_brian.txt`:

```bash
python pyngrams.py life_of_brian.txt 2
```
which will create an output file called `2grams.txt` with the sorted counts of 2-grams in `life_of_brian.txt`.
