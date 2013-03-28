from collections import Counter
from datetime import datetime
from itertools import islice
from multiprocessing import Pool,cpu_count
from operator import itemgetter
import sys


def IterRows():
    for datarow in datarows:
        yield datarow.strip()


def get_ngrams(thestr):
    s = ' '.join(thestr.split()).split(' ')
    return [tuple(s[i:i+n]) for i in range(len(s)-n+1)]

# Accept the input file from the arguments
inputfile = sys.argv[1]

start_time = datetime.now()

print 'reading the data into memory'
infile = open(inputfile, 'r')
datarows = infile.readlines()
infile.close()

# We'll use this later
numrows = len(datarows)

# Take the value of n from the arguments
n = int(sys.argv[2])

pool = Pool(processes=cpu_count())
iterrows = IterRows()
print 'building full %sgram list' % n
    
# Make a shared counter that all processes can use
counter = Counter()
    
# Chunk the data into 40000 rows per process at one time. This can be optimized
N = 40000
for i in range(numrows//N+1):
    g2 = pool.imap(get_ngrams, islice(iterrows, N))
    for ngrams in g2:
        for ngram in ngrams:
            counter.update({' '.join(ngram): 1})

print 'writting sorted dict of ngram sums to disk'
outfile = '%sgrams.txt' % n
f = open(outfile, 'w')
for gram in sorted(counter.iteritems(), key=itemgetter(1), reverse=True):
    f.write('%s\t%s\n' % (gram[0], gram[1]))
f.close()

print 'COMPLETE:', datetime.now() - start_time
