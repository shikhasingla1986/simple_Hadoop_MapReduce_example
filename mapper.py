#!/usr/bin/env python
import sys, string

# get all lines from stdin
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()

    # removes punctuation
    line = line.translate( string.maketrans(string.punctuation, ' ' * len(string.punctuation)) )

    # make lower case
    line = line.lower()

    # split the line into words; splits on any whitespace
    words = line.split()

    # output tuples (word, 1) in tab-delimited format
    stopwords = set(['the', 'and'])

    for word in words:
        if word not in stopwords:
         print '%s\t%s' % (word, "1")
