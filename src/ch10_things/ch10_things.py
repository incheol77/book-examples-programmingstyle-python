#!/user/bin/env pytnon
import sys, re, operator, string
from abc import ABCMeta

### class
class TFExercise():
	__metaclass__ = ABCMeta

	def info(self):
		return self.__class__.__name__

class DataStorageManager(TFExercise):
	def __init__(self, path_to_file):
		with open(path_to_file) as f:
			self._data = f.read()
		pattern = re.compile('[\W_]+')
		self._data = pattern.sub(' ', self._data).lower()

	def words(self):
		return self._data.split()

	def info(self):
		return super(DataStorageManager, self).info() + \
				": My major data structure is a " + self._data.__class__.__name__


class StopWordManager(TFExercise):
	def __init__(self):
		with open('../../sample_data/stop_words.txt') as f:
			self._stop_words = f.read().split(',')
		self._stop_words.extend(list(string.ascii_lowercase))

	def is_stop_word(self, word):
		return word in self._stop_words


	def info(self):
		return super(StopWordManager, self).info() + \
				": My major data structure is a " + self._stop_words.__class__.__name__


class WordFrequencyManager(TFExercise):
	def __init__(self):
		self._word_freqs = {}

	def increment_count(self, word):
		if word in self._word_freqs:
			self._word_freqs[word] += 1
		else:
			self._word_freqs[word] = 1

	def sorted(self):
		return sorted(self._word_freqs.items(), key=operator.itemgetter(1), reverse=True)

	def info(self):
		return super(WordFrequencyManager, self).info() + \
				": My major data structure is a " + self._word_freqs.__class__.__name__


class WordFrequencyController(TFExercise):
	def __init__(self, path_to_file):
		self._storage_manager = DataStorageManager(path_to_file)
		self._stop_word_manager = StopWordManager()
		self._word_freq_manager = WordFrequencyManager()

	def run(self):
		for w in self._storage_manager.words():
			if not self._stop_word_manager.is_stop_word(w):
				self._word_freq_manager.increment_count(w)

		word_freqs = self._word_freq_manager.sorted()
		for (w, c) in word_freqs[0:25]:
			print(w, ' - ', c)


##############3
WordFrequencyController(sys.argv[1]).run()








