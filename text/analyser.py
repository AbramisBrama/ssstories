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

    correct_endings = set()
    correct_prepositions = set()

    curr_preposition = name.preposition
    if curr_preposition == "":
        curr_preposition = "~"

    curr_case = 0
    for case_preps in cases.prepositions:
        for curr_prep in case_preps:
            if curr_preposition == curr_prep:
                correct_prepositions.add(curr_case)
        curr_case += 1

    curr_ending = name.ending
    if curr_ending == "":
        curr_ending = "~"

    curr_ending_id = 0
    for nameMap in names.names:
        if name.name in nameMap:
            suffMap = nameMap[name.name]
            if name.suffix in suffMap:
                curr_ending_id = suffMap[name.suffix]
            else:  # name not found
                return None

    curr_case = 0
    for ending in endings.endings[curr_ending_id]:
        if curr_ending == ending:
            correct_endings.add(curr_case)
        curr_case += 1

    rez = correct_endings.intersection(correct_prepositions)
    if len(rez) == 1:
        return list(rez)[0]
    else:
        return None


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





