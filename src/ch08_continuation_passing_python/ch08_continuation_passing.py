#!/usr/bin/env python3
import sys, re, operator, string

def read_file(path_to_file, func):
    with open(path_to_file) as f:
        data = f.read()
    func(data, normalize)

def filter_chars(str_data, func):
    pattern = re.compile('[\W_]+')
    func(pattern.sub(' ', str_data), scan)

def normalize(str_data, func):
    func(str_data.lower(), remove_stop_words)

def scan(str_data, func):
    func(str_data.split(), frequencies)

def remove_stop_words(word_list, func):
    with open("../../sample_data/stop_words.txt") as f:
        stop_words = f.read().split(',')
    stop_words.extend(list(string.ascii_lowercase))
    func([w for w in word_list if not w in stop_words], sort)

def frequencies(word_list, func):
    wf = {}
    for w in word_list:
        if w in wf:
            wf[w] += 1
        else:
            wf[w] = 1
    func(wf, print_text)

def sort(wf, func):
    func(sorted(wf.items(), key=operator.itemgetter(1), 
            reverse=True), no_op)

def print_text(word_freqs, func):
    for (w,c) in word_freqs[0:25]:
        print(w, "-", c)
    func(None)

def no_op(func):
    return


##################
read_file(sys.argv[1], filter_chars)


