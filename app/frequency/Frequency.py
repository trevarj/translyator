# -*- coding: utf-8 -*-


class FrequencyDictionary(dict):
    @staticmethod
    def create():
        f = open('D:\py_projects\\translyator\\app\\frequency\\freqrnc2011.csv')
        dictionary = {}
        f.readline()  # dump header
        for line in f:
            data = line.split()
            try:
                if float(data[2]) < float(dictionary[data[0]][2]):
                    continue
            except KeyError:
                # Key doesn't exist yet
                pass
            dictionary[data[0]] = data[1:]
        return dictionary

