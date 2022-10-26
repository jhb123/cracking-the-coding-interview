#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 25 14:44:02 2022

@author: josephbriggs
"""

def palidrome_permulation_check(s: str):
    
    s = s.replace(' ','')
    
    s = s.lower()
    
    hash_table = {}

    for letter in s:
        if letter not in hash_table:
            hash_table[letter] = 1
            
        else:
            hash_table[letter] += 1
            
    
    # we could perform this check as we go along by adding and subtracting 
    num_odd = 0
    
    for frequency in hash_table.values():
        if frequency%2 == 1:
            num_odd += 1
            if num_odd > 1:
                return False

    return True


assert(palidrome_permulation_check("asdfg    ASDF") == True)
assert(palidrome_permulation_check("asdfg    ASDFG")== True)
assert(palidrome_permulation_check("qwertyuiop")== False)