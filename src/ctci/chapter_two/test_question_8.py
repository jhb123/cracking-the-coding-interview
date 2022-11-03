#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  3 15:51:16 2022

@author: josephbriggs
"""

from ctci.linked_list.linked_list_functions import SLL,splice
from ctci.chapter_two.question_8 import loop_detection

def test_loop_detection_even_walk_in_odd_loop():
    
    ll = SLL()
    for i in range(10):
        ll.add_node(i)
        
    loop_point = 3
    
    p1 = ll.head
    
    for i in range(loop_point):
        p1 = p1.next_node
        
    splice(ll.get_final_node(),p1)
        
    assert loop_detection(ll) == p1
    
def test_loop_detection_even_walk_in_even_loop():
    
    ll = SLL()
    for i in range(11):
        ll.add_node(i)
        
    loop_point = 3
    
    p1 = ll.head
    
    for i in range(loop_point):
        p1 = p1.next_node
        
    splice(ll.get_final_node(),p1)
        
    assert loop_detection(ll) == p1
    
def test_loop_detection_odd_walk_in_odd_loop():
    
    ll = SLL()
    for i in range(11):
        ll.add_node(i)
        
    loop_point = 2
    
    p1 = ll.head
    
    for i in range(loop_point):
        p1 = p1.next_node
        
    splice(ll.get_final_node(),p1)
        
    assert loop_detection(ll) == p1
    
def test_loop_detection_odd_walk_in_even_loop():
    
    ll = SLL()
    for i in range(10):
        ll.add_node(i)
        
    loop_point = 2
    
    p1 = ll.head
    
    for i in range(loop_point):
        p1 = p1.next_node
        
    splice(ll.get_final_node(),p1)
        
    assert loop_detection(ll) == p1
    
def test_loop_detection_no_loop():
    
    ll = SLL()
    for i in range(10):
        ll.add_node(i)
            
    assert loop_detection(ll) == None
    
