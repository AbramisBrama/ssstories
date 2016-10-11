# -*- coding: utf-8 -*-

from namedata import names
from namedata import endings
from namedata import separators
from text.name import Name


def is_name(word):
    rezult = False
    for nameMap in names.names:
        for key in nameMap:
            if word.startswith(key):
                rezult = True
                break
        if rezult: break
    if rezult and len(key) == len(word):  # the simplest case
        return True
    else:
        for subsuff in nameMap[key]:
            if len(subsuff) > 0 and (len(word) - len(key) > 2):  # suffix found
                if word.startswith(key + subsuff):
                    rezult = True
                    for suff in endings.endings[nameMap[key][subsuff]]:
                        if word.endswith(suff):
                            rezult = True
                            break
                    else:
                        rezult = False
                    break
                else:
                    rezult = False
            elif len(word) - len(key) < 3:  # the first form of name
                for suff in endings.endings[nameMap[key][""]]:
                    if word.endswith(suff):
                        rezult = True
                        break
                    else:
                        rezult = False
    return rezult

def get_name(word):
    rezult = False
    name = Name()
    for nameMap in names.names:
        for key in nameMap:
            if word.startswith(key):
                rezult = True
                name.name = key
                break
        if rezult: break
    if rezult and len(key) == len(word):  # the simplest case
        return name
    else:
        for subsuff in nameMap[key]:
            if len(subsuff) > 0 and (len(word) - len(key) > 2):  # suffix found
                if word.startswith(key + subsuff):
                    rezult = True
                    name.suffix = subsuff
                    for suff in endings.endings[nameMap[key][subsuff]]:
                        if word.endswith(suff):
                            rezult = True
                            name.ending = suff
                            break
                    else:
                        rezult = False
                        return None
                    break
                else:
                    rezult = False
            elif len(word) - len(key) < 3:  # the first form of name
                for suff in endings.endings[nameMap[key][""]]:
                    if word.endswith(suff):
                        rezult = True
                        name.ending = suff
                        break
                    else:
                        rezult = False
                        return None
    return name

def get_case(name):
    return 0

def get_structured_sentence(sentence):
    seps = separators.get_separators()
    buf = ""
    rez = []
    for letter in sentence:
        if letter in seps: #we've got a word
            if buf:
                rez.append(buf)
            rez.append(letter)
            buf = ""
        else:
            buf = buf + letter
    return rez

