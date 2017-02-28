# -*- coding: utf-8 -*-
import string

"""
This module contains only a function that returns the separators list

"""
def get_separators():
    """
    :return: a list of possible separators between the words in any sentence.
    """
    rezult = {"—", "«", "»", "(", ")"}
    for char in string.punctuation:
        rezult.add(char)
    for char in string.whitespace:
        rezult.add(char)
    return rezult
