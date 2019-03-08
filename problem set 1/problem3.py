# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 18:12:31 2019

@author: asus
"""

s = 'xbbryxnkb'

temp = ""
ans = ""

for i in range(len(s)):
    if s[i] >= s[i-1]:
        temp += s[i]
        if len(temp)>len(ans):
            ans = temp
    else:
        temp = s[i]
print("Longest substring in alphabetical order is:", ans)


