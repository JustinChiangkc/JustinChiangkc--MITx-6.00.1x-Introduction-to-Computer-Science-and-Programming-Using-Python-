# -*- coding: utf-8 -*-
"""
Created on Sat May 12 14:40:01 2018

@author: asus
"""

def sum_digits(s):
    tot = 0
    ll = []
    for x in s:

        try:
            tot += int(x)
            ll.append(x)
        except:
            continue

    if ll == []:
        raise ValueError
    if ll != []:
        return tot
    
    