#!/usr/bin/env python3
import sys, string

def read_file(path_to_file):
    data = []
    with open(path_to_file) as f:
        data = data + list(f.read())
    return data

def filter_chars_and_normalize(data):
    for i in range(len(data)):
        if not data[i].isalnum():
            data[i] = ' '
        else:
            data[i] = data[i].lower()
    return data

def scan(data):
    words = []
    data_str = ''.join(data)
    words = words + data_str.split()
    return words

def remove_stop_words(words):
    with open('../../sample_data/stop_words.txt') as f:
        stop_words = f.read().split(',')
    stop_words.extend(list(string.ascii_lowercase))
    indexes = []
    for i in range(len(words)):
        if words[i] in stop_words:
            indexes.append(i)
    for i in reversed(indexes):
        words.pop(i)
    return words


def frequencies(words):
    word_freqs = []
    for w in words:
        keys = [wd[0] for wd in word_freqs]
        if w in keys:
            word_freqs[keys.index(w)][1] += 1
        else:
            word_freqs.append([w, 1])
    return word_freqs

def sort(word_freqs):
    word_freqs.sort(reverse=True, key=lambda x: (x[1], x[0]))
    return word_freqs

#################
# main
data = read_file(sys.argv[1])
norm_data = filter_chars_and_normalize(data)
raw_words = scan(norm_data)
words = remove_stop_words(raw_words)
word_freqs = frequencies(words)
sort(word_freqs)

for tf in word_freqs[0:25]:
    print(tf[0], ' - ', tf[1])




