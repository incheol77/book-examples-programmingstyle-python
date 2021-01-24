#!/usr/bin/env python3

import re, sys, operator

RECURSION_LIMIT = 9500

sys.setrecursionlimit(RECURSION_LIMIT+10)

def count(word_list, stop_words, word_freqs):
    if word_list == []:
        return
    word = word_list[0]
    if word not in stop_words:
        if word in word_freqs:
            word_freqs[word] += 1
        else:
            word_freqs[word] = 1
    count(word_list[1:], stop_words, word_freqs)

def wf_print(word_freqs):
    if word_freqs == []:
        return
    (w, c) = word_freqs[0]
    print(w, '-', c)
    wf_print(word_freqs[1:])

stop_words = set(open('../../sample_data/stop_words.txt').read().split(','))
words = re.findall('[a-z]{2,}', open(sys.argv[1]).read().lower())
word_freqs = {}
for i in range(0, len(words), RECURSION_LIMIT):
    count(words[i:i+RECURSION_LIMIT], stop_words, word_freqs)

wf_print(sorted(word_freqs.items(), key=operator.itemgetter(1)
                , reverse=True)[:25])