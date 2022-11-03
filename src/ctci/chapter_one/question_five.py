#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 25 14:55:11 2022

@author: josephbriggs
"""

def one_away(s1: str, s2: str):
    
    # the general idea is to check the left hand side and the right hand side 
    # of the s1 ans s2. if the check is true, incremement/decrement the index
    # of the string that is to be checked. if the two pointers meet, then 
    # either 1 or zero edits has been made. If two edits are made, then the 
    # pointers won't meet; this is detected and False is returned. Order(n)
    
    #make sure s2 is longer than s1
    if len(s2) < len(s1):
        s1,s2 = s2,s1
        
    j = -1
    i = 0
    
    while i < len(s2) + j:
        cond1 = s1[i] == s2[i]
        cond2 = s1[j] == s2[j]
        if cond1: i +=1
        if cond2: j -=1
        if not cond1 and not cond2: return False
                   
    return True


assert(one_away("pale", "ple") == True)
assert(one_away("pales", "pale") == True)
assert(one_away("pale", "bale") == True)
assert(one_away("pale", "bake") == False)
