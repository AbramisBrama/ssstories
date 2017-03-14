# -*- coding: utf-8 -*-

"""
This module contains well known endings lists for all cases of Russian nouns.
It is a simple 2-dimension list, where each item corresponds to a case:

0. Imenitelny;
1. Roditelny;
2. Datelny;
3. Vinitelny;
4. Tvoritelny;
5. Predlozhny

Tilde symbol ("~") means, that a word in current case may not have an ending (uses in the 1st form).
"""
endings = [
    ["~", "а", "у", "а", "ом", "е"],  # 0 - Владимир, Антон, Пётр, Михаил, Егор
    ["а", "ы", "е", "у", "ой", "е"],  # 1 - Вов-а, Дим-а
    ["я", "и", "е", "ю", "ей", "е"],  # 2 - Пет-я, Волод-я, Вов-к-а, Дим-к-а, Афон-ьк-а, Егор-к-а
    ["й", "я", "ю", "я", "ем", "е"],  # 3 - Алексе-й
    ["й", "я", "ю", "я", "ем", "и"],  # 4 - Дмитри-й
]
