# -*- coding: utf-8 -*-

from namedata import names
from namedata import suffixes

def isName(word):
    rezult = False
    for nameMap in names.names:
        for key in nameMap:
            if word.startswith(key):
                rezult = True
                break
        if rezult: break
    if rezult and len(key) == len(word): # the simplest case
        return True
    else:
        for subsuff in nameMap[key]:
            if len(subsuff) > 0 and (len(word) - len(key) > 2):  # suffix found
                if word.startswith(key+subsuff):
                    rezult = True
                    for suff in suffixes.suffixes[nameMap[key][subsuff]]:
                        if word.endswith(suff):
                            rezult = True
                            break
                    else:
                        rezult = False
                    break
                else:
                    rezult = False
            elif (len(word) - len(key) < 3):  # the first form of name
                for suff in suffixes.suffixes[nameMap[key][""]]:
                    if word.endswith(suff):
                        rezult = True
                        break
                    else:
                        rezult = False
    return rezult