#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 25 14:16:10 2022

@author: josephbriggs
"""

def is_unique(s):
    hash_table = {}
    
    for letter in s:
        if letter not in hash_table:
            hash_table[letter] = 1 
        else:
            return False
    
    return True


assert(is_unique("asdfghjkl") == True)
assert(is_unique("1234567890asdfghjkl") == True)
assert(is_unique("aa") == False)
assert(is_unique("esdtfyuibnoaa") == False)