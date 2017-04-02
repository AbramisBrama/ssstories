from namedata import names, cases
from text import morph_analyser
from random import randint
import pymorphy2

morph = pymorphy2.MorphAnalyzer()

def get_ss_name(name, ss_id):
    """
    This function returns name of defined nazi leader in a proper case

    :param name: type - string. Name of a character.
    :param ss_id: type - int. Index for defined nazi name.
    :return: name of defined nazi leader in a proper case
    """
    curr_case = morph_analyser.get_case(name)
    return names.ssnames[ss_id][cases.morph_case_index[curr_case]]


def get_name_index(name_object):
    """
    This function returns index for given name in a names map from namedata module

    :param name_object: type - Name class object.
    :return: index for given name object in a names map from namedata module
    """
#   curr_index = 0
#    for nameMap in names.names:
#        if name_object.name in nameMap:
#            return curr_index
#        else:
#            curr_index += 1

    parsed = morph.parse(name_object.name)
    return parsed[0].normal_form


def get_ss_sentence(normal_sentence):
    """
    This function get source text fragment and changes every usual name in it to nazi name.

    :param normal_sentence: type - string. Source text fragment.
    :return: Source text fragment with every usual name changed to nazi name. Type is a list.
    """
    names_to_ss_map = {}
    structured_sentence = morph_analyser.get_structured_sentence(normal_sentence)
    curr_position = 0
    for word in structured_sentence:
        if morph_analyser.is_name(word):
            name_object = morph_analyser.get_name(word)
            name_object.preposition = morph_analyser.get_preposition(structured_sentence, curr_position)
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