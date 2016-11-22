# -*- coding: utf-8 -*-

from namedata import names
from namedata import endings
from namedata import separators
from namedata import cases
from text.name import Name


def is_name(word):
    if not isinstance(word, str):
        return False
    return get_name(word) is not None


def get_name(word):
    if not isinstance(word, str):
        return None
    for nameMap in names.names:
        for key in nameMap:
            if word.startswith(key):
                for subSuff in nameMap[key]:
                    endingIndex = nameMap[key][subSuff]
                    for ending in endings.endings[endingIndex]:
                        if ending == "~":  # 0 case (Imenitel'ny)
                            ending = ""
                        if (word == key + subSuff + ending):
                            return Name("", key, subSuff, ending)
    return None


def get_case(name):
    return 0


def get_structured_sentence(sentence):
    seps = separators.get_separators()
    buf = ""
    rez = []
    for letter in sentence:
        if letter in seps:  # we've got a word
            if buf:
                rez.append(buf)
            rez.append(letter)
            buf = ""
        else:
            buf = buf + letter
    return rez


def get_preposition(sentence, name_index):
    structured_sentence = get_structured_sentence(sentence)
    if name_index > len(structured_sentence) or not is_name(structured_sentence[name_index]):
        return None
    prepositions_set = set()
    for prep_list in cases.prepositions:
        for prep in prep_list:
            prepositions_set.add(prep)
    max_prep_distance = 10  # Maximum 5 words between preposition and name
    word = ""
    i = 1
    punctuation = separators.get_separators().copy()
    punctuation.remove(' ')
    while word.lower() not in prepositions_set:
        word = structured_sentence[name_index - i]
        if i > max_prep_distance or name_index - i < 0:
            return ""
        i += 1
    return word.lower()





