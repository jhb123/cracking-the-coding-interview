#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 25 19:08:14 2022

@author: josephbriggs
"""

def is_rotation(s1,s2):
    s3 = s2+s2
    cycle = s3.find(s1)
    if cycle == -1:
        return False
    else:
        return True

assert(is_rotation("waterbottle","erbottlewat") == True)
assert(is_rotation("waterbottle","lewaterbott") == True)