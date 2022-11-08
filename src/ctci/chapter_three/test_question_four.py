#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  7 18:14:24 2022

@author: josephbriggs
"""

from ctci.chapter_three.question_four import QueueViaStacks

def test_qvs():
    qvs = QueueViaStacks()
    
    nums = [1,2,3,4,5]
    

    for n in nums:
        qvs.push(n)
        
    assert qvs.pop() == 1
    assert qvs.pop() == 2
    assert qvs.peek() == 3


    
    nums = [1,2,3,4,5]
    
    for n in nums:
        qvs.push(n)

    ans = [3,4,5,1,2,3,4,5]
    i = 0
    
    while not qvs.is_empty():
        assert qvs.pop() == ans[i]
        i += 1


