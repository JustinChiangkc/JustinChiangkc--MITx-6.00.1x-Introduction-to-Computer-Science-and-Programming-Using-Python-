# -*- coding: utf-8 -*-
"""
Created on Sat May 12 15:07:19 2018

@author: asus
"""

def primes_list(N):
    '''
    N: an integer
    '''
    fac = {}
    pri = []
    for x in range(2,N+1):
        #print('x=',x)
        for y in range(1,x+1):
            #print('y=',y)
            if x%y == 0:
                try:
                    fac[x] += [y]
                    #print('try')
                except KeyError:
                    #print('fac[',x,'] =[',y,']')
                    fac[x] =[y]
                    
        #print(list(fac.items()))
        if fac[x] == [1,x]:
            pri.append(x)
    return pri