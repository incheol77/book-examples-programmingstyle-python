#!/usr/bin/env python

import string
import sys

# global list ([word, frequency])
word_freqs = []

# meaningless word list
with open("../../sample_data/stop_words.txt") as f:
    stop_words = f.read().split(',')
stop_words.extend(list(string.ascii_lowercase))

for line in open(sys.argv[1]):
    start_char = None
    i = 0
    for c in line:
        if start_char == None:
            if c.isalnum():
                start_char = i
        else:
            if not c.isalnum():
                # find end of word
                found = False
                word = line[start_char:i].lower()
                # ignore meaningless words
                if word not in stop_words:
                    pair_index = 0
                    for pair in word_freqs:
                        if word == pair[0]:
                            pair[1] += 1
                            found = True
                            found_at = pair_index
                            break
                        pair_index += 1
                    if not found:
                        word_freqs.append([word, 1])
                elif len(word_freqs) > 1:
                    for n in reversed(range(pair_index)):
                        if word_freqs[pair_index][1] > word_freqs[n][1]:
                            word_freqs[n], word_freqs[pair_index] = word_freqs[pair_index], word_freqs[n]
                            pair_index = n
            start_char = None
        i += 1
for tf in word_freqs[0:25]:
    print(tf[0], ' - ', tf[1])






