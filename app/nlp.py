# -*- coding: utf-8 -*-
__author__ = 'trevor'
import nltk.tokenize, pymorphy2, requests, json
from app import frequency
from sentence import Sentence

morph = pymorphy2.MorphAnalyzer()
sentence_tokenizer = nltk.tokenize.PunktSentenceTokenizer()
word_tokenizer = nltk.tokenize.RegexpTokenizer('\w+')


def get_sentences(full_text):
    return sentence_tokenizer.sentences_from_text(full_text)


def get_sentence_weight(sentence):
    """
    Splits up the sentence by words and then finds the root word
    in order to look it up in the frequency dictionary

    :param sentence: Russian text to be evaluated and weighed
    :return: weight as a float
    """
    weight = 0
    true_length = 0
    words = word_tokenizer.tokenize(sentence)
    print 'sentence length: ' + str(len(words))
    for word in words:
        norm = morph.parse(word)[0].normal_form
        try:
            ww = float(frequency.query_freq(norm))
            if ww > 3000:
                continue
        except KeyError:
            print "Word not found in dictionary"
            continue
        weight += ww
        true_length += 1
    return weight / true_length


def translate_ru2en(sentences_list, api_key):
    """
    Calls Yandex Translate and translates from Russian to English
    :param sentences_list: list of sentences to translate
    :param api_key: your personal Yandex Translate API key
    :return: list of translated sentences
    """
    data = dict()
    data["key"] = api_key
    data["lang"] = "ru-en"
    data["text"] = sentences_list

    url = 'https://translate.yandex.net/api/v1.5/tr.json/translate'
    response = requests.post(url, data=data, files={})

    # might want to check 'code' here for 200 response...
    return json.loads(response.text)['text']


def process_text(full_text, api_key):
    """
    Translates and weighs each sentence and returns a giant JSON
    of the Sentence data.

    :param full_text: text to process
    :return: JSON of text with meta data
    """
    sentences = get_sentences(full_text)
    trans_sentences = translate_ru2en(sentences, api_key)
    sentence_obj_list = []
    # translate the text fully, then get the sentences in English
    for i in xrange(len(sentences)):
        ru_text = sentences[i]
        en_text = trans_sentences[i]
        weight = get_sentence_weight(ru_text)
        new_sentence = Sentence(ru_text, en_text, weight)
        sentence_obj_list.append(new_sentence.get_json())
    return json.dumps(sentence_obj_list)
