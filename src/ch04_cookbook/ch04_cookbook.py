#!/usr/bin/env python3
import sys, string

data = []
words = []
word_freqs = []

def read_file(path_to_file):
    global data
    with open(path_to_file) as f:
        data = data + list(f.read())

def filter_chars_and_normalize():
    global data
    for i in range(len(data)):
        if not data[i].isalnum():
            data[i] = ' '
        else:
            data[i] = data[i].lower()

def scan():
    global data
    global words
    data_str = ''.join(data)
    words = words + data_str.split()


def remove_stop_words():
    global words
    with open('../../sample_data/stop_words.txt') as f:
        stop_words = f.read().split(',')
    stop_words.extend(list(string.ascii_lowercase))
    indexes = []
    for i in range(len(words)):
        if words[i] in stop_words:
            indexes.append(i)
    for i in reversed(indexes):
        words.pop(i)


def frequencies():
    global words
    global word_freqs
    for w in words:
        keys = [wd[0] for wd in word_freqs]
        if w in keys:
            word_freqs[keys.index(w)][1] += 1
        else:
            word_freqs.append([w, 1])

def sort():
    global word_freqs
    word_freqs.sort(reverse=True, key=lambda x: (x[1], x[0]))

#################
# main
read_file(sys.argv[1])
filter_chars_and_normalize()
scan()
remove_stop_words()
frequencies()
sort()

for tf in word_freqs[0:25]:
    print(tf[0], ' - ', tf[1])




