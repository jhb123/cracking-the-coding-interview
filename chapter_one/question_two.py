#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 25 14:24:43 2022

@author: josephbriggs
"""

def check_permutation(s1,s2):
    # add some basic checks to avoid redundant work e.g. check if their legnths
    # are the same.
    
    hash_table_1 = {}
    hash_table_2 = {}
    
    for letter in s1:
        if letter not in hash_table_1:
            hash_table_1[letter] = 1 
        else:
            hash_table_1[letter] += 1
            
    for letter in s2:
        if letter not in hash_table_2:
            hash_table_2[letter] = 1 
        else:
            hash_table_2[letter] += 1
    
    return hash_table_1 == hash_table_2 

assert(check_permutation("qwertyuiop","poiuytrewq") == True)
assert(check_permutation("qwertyuiop","asdfghjklp") == False)
assert(check_permutation("aassdd","asd") == False)
