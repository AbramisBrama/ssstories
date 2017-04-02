# -*- coding: utf-8 -*-

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

    # 'Name' grammem must be in the most probable parsed case
    return 'Name' in morph.parse(word)[0].tag


def get_name(word):
    """
        This function instantiates a Name class from the word.

        :param word:  The word to construct a Name.
        :return: Name instance if the word is a name, None - if not.
    """
    if not is_name(word):
        return None

    return Name("", word, "", "")


def get_case(name):
    """
        This function analyses a case of the name.

        :param name: The Name instance.
        :return: integer index of case from :mod:`namedata.cases`.
    """
    if not is_name(name.print()):
        return None

    parsed_name = morph.parse(name.print())
    if len(parsed_name) > 1:
        possible_cases = set()
        for name_case in parsed_name:
            possible_cases.add(name_case.tag.case)
        for case in possible_cases:
            if name.preposition in cases.prepositions[cases.morph_case_index[case]]:
                return case
        return None  # case not found
    return morph.parse(name.print())[0].tag.case


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


def is_preposition(word):
    return 'PREP' in morph.parse(word)[0].tag
