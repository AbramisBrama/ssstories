# -*- coding: utf-8 -*-

"""

This module contains functions to generate random text fragments, restricted with some conditions. And to replace character names in this fragments.

"""
import os
import codecs
import os.path
import random
from text import analyser
from namedata import names
from random import randint


def text_contains_name(text_for_story):
    """
    This functions checks if there are any names in generated fragment.

    :param text_for_story: type - string, text fragment to check for containing names in it.
    :return: True if text_for_story contains name and False if not.
    """
    result = False
    word = ' '
    words_array = analyser.get_structured_sentence(text_for_story)
    for word in words_array:
        if analyser.is_name(word):
            result = True
            break
    return result


def get_text():
    """
    This function selects random text file from Data/text folder. And then cuts form it text fragment that should satisfy the conditions below.

*   Conditions:

    - symbols count between 780 and 1000;
    - paragraph should be solid (all sentences should be ended);
    - text fragment should contain at least one name;

    :return: text fragment (type string) that satisfies the conditions above
    """
    directory = 'Data//texts'

    files = os.listdir(os.path.normpath(directory))

    rndFilePath = os.path.normpath(directory + '//' + random.choice(files))

    rndfile = codecs.open(rndFilePath, "r", "utf_8_sig")

    abzats_num = 0
    symb_count = 0
    name_ext = 1

    paragraphs = []

    for line in rndfile:
        symb_count = len(line)
        abzats_num += 1
        paragraphs.append([abzats_num, symb_count, name_ext, line])

    paragraph = 0
    fin_string_symb_count = 0
    min_symb_count = 780
    max_symb_count = 1100

    for paragraph in reversed(paragraphs):
        fin_string_symb_count = fin_string_symb_count + paragraph[1]
        if fin_string_symb_count > min_symb_count:
            max_abzats_num = paragraph[0]
            break

    result_string = ''
    tries_counter = 0

    while not text_contains_name(result_string):
        random_abzats = random.randint(0, max_abzats_num)
        result_symb_count = 0
        tries_counter = tries_counter + 1
        line = rndfile.readlines()
        if tries_counter > max_abzats_num:
            result_string = 'None'
            break
        else:
            for paragraph in paragraphs[random_abzats - 1:]:
                result_symb_count = result_symb_count + paragraph[1]
                if result_symb_count < max_symb_count:
                    result_string = result_string + paragraph[3]
                else:
                    break

    rndfile.close()

    return result_string

def get_ss_name(name, ss_id):
    """
    This function returns name of defined nazi leader in a proper case

    :param name: type - string. Name of a character.
    :param ss_id: type - int. Index for defined nazi name.
    :return: name of defined nazi leader in a proper case
    """
    curr_case = analyser.get_case(name)
    return names.ssnames[ss_id][curr_case]


def get_name_index(name_object):
    """
    This function returns index for given name in a names map from namedata module

    :param name_object: type - Name class object.
    :return: index for given name object in a names map from namedata module
    """
    curr_index = 0
    for nameMap in names.names:
        if name_object.name in nameMap:
            return curr_index
        else:
            curr_index += 1


def get_ss_sentence(normal_sentence):
    """
    This function get source text fragment and changes every usual name in it to nazi name.

    :param normal_sentence: type - string. Source text fragment.
    :return: Source text fragment with every usual name changed to nazi name. Type is a list.
    """
    names_to_ss_map = {}
    structured_sentence = analyser.get_structured_sentence(normal_sentence)
    curr_position = 0
    for word in structured_sentence:
        if analyser.is_name(word):
            name_object = analyser.get_name(word)
            name_object.preposition = analyser.get_preposition(structured_sentence, curr_position)
            name_index = get_name_index(name_object)
            if name_index not in names_to_ss_map:
                ss_name_index = randint(0, len(names.ssnames) - 1)
                names_to_ss_map[name_index] = ss_name_index
                structured_sentence[curr_position] = get_ss_name(name_object, ss_name_index)
            else:
                structured_sentence[curr_position] = get_ss_name(name_object, names_to_ss_map[name_index])
        curr_position += 1
    return structured_sentence


def get_printable_sentence(structured_sentence):
    """
    This function converts list of strings to one solid string

    :param structured_sentence: type - list of strings
    :return: strings concatenation
    """
    rez = ""
    for word in structured_sentence:
        rez += word
    return rez


