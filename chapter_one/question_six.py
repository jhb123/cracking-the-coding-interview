#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 25 15:55:35 2022

@author: josephbriggs
"""

def string_compression(s: str) -> str:

    idx_1 = 0
    
    # appending to a resizable array is an order(1) time cost usually, but
    # sometimes you double the size of the array and copy the elements which 
    # has time complexity equal to the number of elements. On average, it takes
    # time(n) to insert (n) items into the array (see p89 of CTCI)
    strings = []
    
    for idx_2,letter in enumerate(s):
        if s[idx_1] != s[idx_2]:
            strings.append(s[idx_1] + str(idx_2-idx_1))
            idx_1 = idx_2
    
    strings.append(s[idx_1] + str(idx_2-idx_1+1))
    
    # this join operation is order(n)
    new_str = ''.join(strings)
    if len(new_str) > len(s): 
        return s 
    else:
        return new_str
    



assert(string_compression("aabcccccaaa") == "a2b1c5a3")
assert(string_compression("aabcccccaaab") == "a2b1c5a3b1")
assert(string_compression("a") == "a")
assert(string_compression("aab") == "aab")
assert(string_compression("abc") == "abc")

    

