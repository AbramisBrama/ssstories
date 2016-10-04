# -*- coding: utf-8 -*-
import string


def get_separators():
    rezult = {"—", "«", "»", "(", ")"}
    for char in string.punctuation:
        rezult.add(char)
    for char in string.whitespace:
        rezult.add(char)
    return rezult
