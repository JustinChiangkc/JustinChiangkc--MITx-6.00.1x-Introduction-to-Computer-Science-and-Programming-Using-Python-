# -*- coding: utf-8 -*-
"""
Created on Sat May 12 16:07:30 2018

@author: asus
"""

def uniqueValues(aDict):
    '''
    aDict: a dictionary
    returns: a sorted list of keys that map to unique aDict values, empty list if none
    '''
    inputd = aDict.copy()
    retrnl = []
    
    ky = list(inputd.keys())
    vl = list(inputd.values())
    

    for k in ky :
        vlt = vl[:]
        vlt.remove(inputd[k])
        if inputd[k] not in vlt:
            retrnl.append(k)
    retrnl.sort()   
    return retrnl