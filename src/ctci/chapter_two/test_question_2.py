#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  3 13:35:47 2022

@author: josephbriggs
"""
from ctci.linked_list.linked_list_functions import SLL
from ctci.chapter_two.question_2 import find_k_from_the_end

def test_find_k_from_the_end_last_number():
    
    ll = SLL()
    for i in range(10):
        ll.add_node(i)
        
    p1 = find_k_from_the_end(ll,0)
    assert p1.data == 9
    
    
def test_find_k_from_the_end_huge_number():
    
    ll = SLL()
    for i in range(10):
        ll.add_node(i)
        
    p1 = find_k_from_the_end(ll,100)
    assert p1.data == 0
    

def test_find_k_from_the_end_middle_number():
    
    ll = SLL()
    for i in range(10):
        ll.add_node(i)
        
    p1 = find_k_from_the_end(ll,4)
    assert p1.data == 5
    
