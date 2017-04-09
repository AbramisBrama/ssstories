# -*- coding: utf-8 -*-

"""

This module contains functions to generate random text fragments, restricted with some conditions. And to replace character names in this fragments.

"""
import os
import codecs
import os.path
import random
from text import analyser, morph_analyser

def text_contains_name(text_for_story):
    """
    This functions checks if there are any names in generated fragment.

    :param text_for_story: type - string, text fragment to check for containing names in it.
    :return: True if text_for_story contains name and False if not.
    """
    result = False
    words_array = analyser.get_structured_sentence(text_for_story)
    for word in words_array:
        if morph_analyser.is_name(word):
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

    rndfile = codecs.open(rndFilePath, "r", "utf-8")

    abzats_num = 0
    name_ext = 1

    paragraphs = []

    for line in rndfile:
        symb_count = len(line)
        abzats_num += 1
        paragraphs.append([abzats_num, symb_count, name_ext, line])

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



