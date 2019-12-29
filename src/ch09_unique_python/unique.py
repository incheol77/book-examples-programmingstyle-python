#!/usr/bin/env python

import sys, re, string, operator

class TFTheOne:
	def __init__(self, v):
		self._value = v

	def bind(self, func):
		self._value = func(self._value)
		return self

	def printme(self):
		print self._value

#######

def read_file(path_to_file):
	with open(path_to_file) as f:
		data = f.read()
	return data

def filter_chars(str_data):
	pattern = re.compile('\[W_]+')
	print str_data
	return pattern.sub(' ', str_data)

def normalize(str_data):
	return str_data.lower()

def scan(str_data):
	return str_data.split()

def remove_stop_words(word_list):
	with open('../../sample_data/stop_words.txt') as f:
		stop_words = f.read().split()
		stop_words.extend(list(string.ascii_lowercase))
	return [w for w in word_list if not w in stop_words]

def frequencies(word_list):
	word_freqs = {}
	for w in word_list:
		if w in word_freqs:
			word_freqs[w] += 1
		else:
			word_freqs[w] = 1
	return word_freqs

def sort(word_freqs):
	return sorted(word_freqs.iteritems(), key=operator.itemgetter(1), reverse=True)

def top25_freqs(word_freqs):
	top25 = ""
	for tf in word_freqs[0:25]:
		top25 += str(tf[0]) + ' - ' + str(tf[1]) + '\n'
	return top25



#######

TFTheOne(sys.argv[1])\
.bind(read_file)\
.bind(filter_chars)\
.bind(normalize)\
.bind(scan)\
.bind(remove_stop_words)\
.bind(frequencies)\
.bind(sort)\
.bind(frequencies)\
.bind(sort)\
.bind(top25_freqs)\
.printme()

	
