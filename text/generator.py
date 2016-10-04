# -*- coding: utf-8 -*-
import os
import random
import codecs

directory = 'D:\\python_code\\ssstories\\Data\\texts'

files = os.listdir(directory)

rndFilePath = directory + '\\' + random.choice(files)

rndfile = codecs.open(rndFilePath , "r", "utf_8_sig" )

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

random_abzats = random.randint(0,max_abzats_num)
result_string = ''
result_symb_count = 0
line = rndfile.readlines()

for paragraph in paragraphs[random_abzats-1:]:
    result_symb_count = result_symb_count + paragraph[1]
    if result_symb_count < max_symb_count:
        result_string = result_string + paragraph[3]
    else:
        break

print(result_string)


rndfile.close()
