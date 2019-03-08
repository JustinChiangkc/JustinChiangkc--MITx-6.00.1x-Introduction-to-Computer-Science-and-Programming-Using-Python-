# -*- coding: utf-8 -*-
"""
Created on Wed May  9 21:03:45 2018

@author: asus
"""

def newsearch(L, e):
    size = len(L)
    for i in range(size):
# =============================================================================
#         print('for i = ',i)
#         print('size-i-1=',size-i-1)
#         print('L[size-i-1]=',L[size-i-1])
# =============================================================================
        if L[size-i-1] == e:
# =============================================================================
#             print('L[',size-i-1,']==',e)
# =============================================================================
            return True
        if L[size-i-1] < e:
# =============================================================================
#             print(L[size-i-1],'<', e)
# =============================================================================
            return False
    return False


def search(L, e):
    for i in range(len(L)):
        if L[i] == e:
            return True
        if L[i] > e:
            return False
    return False
 
def swapSort(L): 
    """ L is a list on integers """
    print("Original L: ", L)
    for i in range(len(L)):
        print('for i =', i )
        for j in range(i+1, len(L)):
            print('for j =', j )
            if L[j] < L[i]:
                # the next line is a short 
                # form for swap L[i] and L[j]
                L[j], L[i] = L[i], L[j] 
                print(L)
    print("Final L: ", L)
    
def modSwapSort(L): 
    """ L is a list on integers """
    print("Original L: ", L)
    for i in range(len(L)):
        print('for i =', i )
        print('for L[i] =', L[i] )
        for j in range(len(L)):
            print('for j =', j )
            print('for L[j] =', L[j] )
            if L[j] < L[i]:
                # the next line is a short 
                # form for swap L[i] and L[j]
                L[j], L[i] = L[i], L[j] 
                print(L)
    print("Final L: ", L)