__author__ = 'trevor'

import json

class Sentence(object):
    def __init__(self, ru_text=None, en_text=None, weight=0):
        self.ru_text = ru_text
        self.en_text = en_text
        self.weight = weight

    def get_json(self):
        return json.dumps(self.__dict__)
