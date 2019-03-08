# -*- coding: utf-8 -*-
"""
Created on Sat May 12 15:07:19 2018

@author: asus
"""

def primes_list(N):
    '''
    N: an integer
    Return Prime list that samller than N
    '''
    fac = {}
    pri = []
    for x in range(2,N+1):
        for y in range(1,x+1):
            if x%y == 0:
                try:
                    fac[x] += [y]
                except KeyError:
                    fac[x] =[y]
        if fac[x] == [1,x]:
            pri.append(x)
    return pri
