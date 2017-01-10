# -*- coding: utf-8 -*-

import os
import random
import codecs
import text.analyser
import os.path
import analyser
import names

def text_contains_name(text_for_story):
    result = False
    word = ' '
    words_array = text.analyser.get_structured_sentence(text_for_story)
    for word in words_array:
        if text.analyser.is_name(word):
            result = True
            break
    return result

def get_text():
    directory = './/Data//texts'

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
        tries_counter = tries_counter+1
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

# print(get_text()) - WTF?

def get_ss_name(name, ss_id):
    curr_case = analyser.get_case(name)
    return names.ssnames[ss_id][curr_case]