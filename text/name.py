# -*- coding: utf-8 -*-

from namedata import names
from namedata import endings


class Name:
    name = ""
    suffix = ""
    preposition = ""
    ending = ""

    def __init__(self, preposition, name, suffix, ending):
        self.preposition = preposition
        self.name = name
        self.suffix = suffix
        self.ending = ending

    def parse(raw_word: str) -> object:
        curr_ending = ""
        curr_name = ""
        curr_suff = ""
        for case in endings.endings:
            for ending in case:
                if raw_word.endswith(ending):
                    curr_ending = ending
                    break
        for nameMap in names.names:
            for key in nameMap:
                for suffix in nameMap[key].keys():
                    if raw_word.startswith(key+suffix+curr_ending):
                        curr_name = key
                        curr_suff = suffix
        if curr_name == "":
            return None
        else:
            return Name("", curr_name, curr_suff, curr_ending)
