#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  3 14:19:52 2022

@author: josephbriggs
"""
from ctci.chapter_two.question_7 import intersecting_node
from ctci.linked_list.linked_list_functions import SLL,splice

def test_intersection():
    
    
    ll1 = SLL()
    
    for i in range(3):
        ll1.add_node(i)

    ll2 = SLL()
    for i in range(4,7):
        ll2.add_node(i)
    
    ll3 = SLL()
    for i in range(7,11):
        ll3.add_node(i)
        
    
   
    
    splice(ll1.get_final_node(),ll3.head)
    splice(ll2.get_final_node(),ll3.head)
   
    p1 = intersecting_node(ll1,ll2)
    
    assert p1 == ll3.head
    
def test_no_intersection():
    
    
    ll1 = SLL()
    
    for i in range(3):
        ll1.add_node(i)

    ll2 = SLL()
    for i in range(4,7):
        ll2.add_node(i)
    
    p1 = intersecting_node(ll1,ll2)
    
    assert p1 == None
    