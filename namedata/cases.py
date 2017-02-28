# -*- coding: utf-8 -*-

"""
This module contains well known prepositions lists for all cases of Russian nouns.
It is a simple 2-dimension list, where each item corresponds to a case:

0. Imenitelny;
1. Roditelny;
2. Datelny;
3. Vinitelny;
4. Tvoritelny;
5. Predlozhny

Tilde symbol ("~") in the list of prepositions means, that a word in current case may not have a preposition at all.
"""
prepositions = (
    ("~"),
    ("~", "у", "от", "до", "из", "для", "без", "около"),
    ("~", "к", "по"),
    ("~", "в", "на", "за", "под", "через", "про"),
    ("~", "с", "за", "под", "перед", "над"),
    ("о", "об", "в", "во", "при", "на")
)
