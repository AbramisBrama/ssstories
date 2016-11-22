# -*- coding: utf-8 -*-

from namedata import names
from namedata import endings
from namedata import separators
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
