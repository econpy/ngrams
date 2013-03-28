from collections import Counter
from datetime import datetime
from itertools import islice
from multiprocessing import Pool
from operator import itemgetter


def GoGadgetGo():
	for datarow in datarows:
		yield datarow.strip()


def get_ngrams(thestr):
	s = ' '.join(thestr.split()).split(' ')
	return [tuple(s[i:i+n]) for i in range(len(s)-n+1)]

if __name__ == '__main__':
	print 'reading in the data'
	infile = open('inputfile.txt', 'r')
	datarows = infile.readlines()
	infile.close()

	for n in [1, 2, 3]: # Calculate 1-grams, 2-grams and 3-grams
		print 'BEGIN: %s-grams' % n
		start_time = datetime.now()
		# Use all 8 cores on my CPU
		pool = Pool(processes=8)
		go = GoGadgetGo()

		print 'building full ngram list'
		# Make a shared counter that all processes can use
		counter = Counter()
		# Chunk the data into 40000 rows per process at one time. This can be optimized
		N = 40000
		for i in range(len(datarows)//N+1):
			g2 = pool.imap(get_ngrams, islice(go, N))
			for ngrams in g2:
				for ngram in ngrams:
					tmpdct = {' '.join(ngram): 1}
					counter.update(tmpdct)

		print 'sorting dict of ngram sums'
		sorted_ngrams = sorted(counter.iteritems(), key=itemgetter(1), reverse=True)
		del counter

		print 'Writing to file...'
		outfile = '%sgrams.txt' % n
		f = open(outfile, 'w')
		for gram in sorted_ngrams:
			f.write('%s\t%s\n' % (gram[0], gram[1]))
		f.close()
		del sorted_ngrams

		end_time = datetime.now()
		print 'COMPLETE:',end_time - start_time
