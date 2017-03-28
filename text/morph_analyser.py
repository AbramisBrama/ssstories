# -*- coding: utf-8 -*-

from namedata import names
from namedata import endings
from namedata import separators
from namedata import cases
from text.name import Name

import pymorphy2

morph = pymorphy2.MorphAnalyzer()

"""
This module contains a set of functions for names analysis
"""
def is_name(word):
    """
        This function checks whether the word is a name or not.

        :param word:  The word to check.
        :return: True in case of word is a name, False - if not.

        The function parses the word with PyMorphy and checks, whether its tags contain 'Name' grammeme.
        (https://pymorphy2.readthedocs.io/en/0.2/user/index.html)
    """
    if not isinstance(word, str):
        return False

    parsed_name = morph.parse(word)

    for i in parsed_name:
        if ('Name' in i.tag):
            return True
    return False


def get_name(word):
    """
        This function instantiates a Name class from the word.

        :param word:  The word to construct a Name.
        :return: Name instance if the word is a name, None - if not.
    """
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
    """
        This function analyses a case of the name.

        :param name: The Name instance.
        :return: integer index of case from :mod:`namedata.cases`.
    """
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
    """
        This function divides the sentence string into the list of words and delimiters.

        :param sentence: The string containing a sentence. Must end with a dot.
        :return: the list of sentence's words and delimiters from :mod:`namedata.separators`.
    """
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
    """
        This function finds a preposition of given word in the sentence.

        :param sentence: The string containing a sentence or the structured sentence.
        :param name_index: The index of name in the sentence from 0 including separators.
        :return: the preposition from :mod:`namedata.prepositions`.
    """
    if isinstance(sentence, str):
        structured_sentence = get_structured_sentence(sentence)
    else:
        structured_sentence = sentence
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





