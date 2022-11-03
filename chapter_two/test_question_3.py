#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  3 13:13:39 2022

@author: josephbriggs
"""

from linked_list_functions import SLL
from question_3 import delete_middle_node

def test_delete_middle_node_centre():
    
    linked_list = SLL()
    for i in range(10):
        linked_list.add_node(i)
    
    
    node_to_delete = 5
    p1 = linked_list.head
    for i in range(node_to_delete):
        p1 = p1.next_node

    
    delete_middle_node(p1)
    
    p1 = linked_list.head
    nums = [0,1,2,3,4,6,7,8,9]
    for n in nums:
        assert p1.data == n
        p1 = p1.next_node
        
        
def test_delete_middle_node_second_from_end():
    
    linked_list = SLL()
    for i in range(10):
        linked_list.add_node(i)
    
    
    node_to_delete = 8
    p1 = linked_list.head
    for i in range(node_to_delete):
        p1 = p1.next_node

    
    delete_middle_node(p1)
    
    p1 = linked_list.head
    nums = [0,1,2,3,4,5,6,7,9]
    for n in nums:
        assert p1.data == n
        p1 = p1.next_node
        
        

    
