# -*- coding: utf-8 -*-
"""
Created on Sat Aug 24 16:46:57 2024

@author: ADMIN
"""

s = "i'm a cat"
s = s[0].upper() + s[1:4] + s[4].upper() + s[5] + s[6].upper() +  s[7:]
print(s)
print(s.upper())
s = "i'm a cat"
s = s[0:2] + s[2].upper() + s[3:7] + s[7:9].upper() 
print(s)
print(s.lower())