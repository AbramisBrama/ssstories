# -*- coding: utf-8 -*-

"""
This module contains well known prepositions lists for all cases of Russian nouns.
It is two simple 2-dimension list, where each item corresponds to a case:

+---+-------------+--------------------+
|n/n| Case        | Pymorphy case name |
+---+-------------+--------------------+
| 0 | Imenitelny  | nomn               |
+---+-------------+--------------------+
| 1 | Roditelny   | gent, gen2         |
+---+-------------+--------------------+
| 2 | Datelny     | datv               |
+---+-------------+--------------------+
| 3 | Vinitelny   | accs, acc2         |
+---+-------------+--------------------+
| 4 | Tvoritelny  | ablt               |
+---+-------------+--------------------+
| 5 | Predlozhny  | loct, loc2         |
+---+-------------+--------------------+

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

morph_case_index = {
    'nomn': 0,
    'gent': 1,
    'gen2': 1,
    'datv': 2,
    'accs': 3,
    'acc2': 3,
    'ablt': 4,
    'loct': 5,
    'loc2': 5
}

