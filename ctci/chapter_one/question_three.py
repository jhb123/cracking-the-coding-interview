#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 25 14:28:55 2022

@author: josephbriggs
"""

def urlify(s):
    # python has a replace function. This is what we will implement
    new_word = ''
    for letter in s:
        if letter == ' ':
            letter = "%20"
        new_word += letter
    print(new_word)
    return new_word


assert(urlify("Mr John Smith") == "Mr%20John%20Smith")
