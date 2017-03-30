# -*- coding: utf-8 -*-

from namedata import names
from namedata import endings

"""
This module contains a definition of Name class
"""
class Name:
    """
        Class is used to store structured information about the name
    """
    name = ""
    """Main part of the name"""
    suffix = ""
    """Suffix of the name"""
    preposition = ""
    """Preposition of the name"""
    ending = ""
    """Suffix of the name"""

    def __init__(self, preposition, name, suffix, ending):
        self.preposition = preposition
        self.name = name
        self.suffix = suffix
        self.ending = ending

    def parse(raw_word: str) -> object:
        """
        Instantiate the Name with a raw string word

        :param raw_word: The string that contains one word - name.
        :return: Name instance.
        """
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
                    if raw_word.startswith(key + suffix + curr_ending):
                        curr_name = key
                        curr_suff = suffix
        if curr_name == "":
            return None
        else:
            return Name("", curr_name, curr_suff, curr_ending)

    def print(self):
        return self.name+self.suffix+self.ending
