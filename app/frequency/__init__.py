__author__ = 'trevor'
from Frequency import FrequencyDictionary

dictionary = FrequencyDictionary.create()


def query_freq(word):
    return float(dictionary[word.encode('utf-8')][1])