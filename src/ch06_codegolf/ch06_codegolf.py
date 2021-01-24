#!/usr/bin/env python3
import re, sys, collections

stops = open('../../sample_data/stop_words.txt').read().split(',')
words = re.findall('[a-z]{2,}', open(sys.argv[1]).read().lower())
counts = collections.Counter(w for w in words if w not in stops)
for (w, c) in counts.most_common(25):
    print(w, '-', c)