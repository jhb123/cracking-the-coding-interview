#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  3 12:19:00 2022

@author: josephbriggs
"""
from linked_list_functions import SLL
from question_4 import partition_SLL

def test_partition():
    # question 2.4, time complexity O(n), space complexity O(n)
    
    
    split_number = 3
    
    linked_list = SLL()
    left_ll = SLL()
    right_ll = SLL()

    for i in range(5):
        linked_list.add_node(i)
    for i in range(5,0,-1):
        linked_list.add_node(i)
        linked_list.add_node(i)
    for i in range(5):
        linked_list.add_node(i)
    partioned_linked_list = partition_SLL(split_number,linked_list,left_ll,right_ll)

    p1 = partioned_linked_list.head
    before_split = True
    
    while(p1):
        
        val = p1.data 
        p1 = p1.next_node

        if val < split_number and before_split: continue
        elif val >= split_number:
            before_split = False
        else:
            assert False

def test_partition_larger_number():
    # question 2.4, time complexity O(n), space complexity O(n)
    
    
    split_number = 10
    
    linked_list = SLL()
    left_ll = SLL()
    right_ll = SLL()

    for i in range(5):
        linked_list.add_node(i)
    for i in range(5,0,-1):
        linked_list.add_node(i)
        linked_list.add_node(i)
    for i in range(5):
        linked_list.add_node(i)
    partioned_linked_list = partition_SLL(split_number,linked_list,left_ll,right_ll)

    p1 = partioned_linked_list.head
    before_split = True
    
    while(p1):
        
        val = p1.data 
        p1 = p1.next_node

        if val < split_number and before_split: continue
        elif val >= split_number:
            before_split = False
        else:
            assert False

def test_partition_smaller_number():
    # question 2.4, time complexity O(n), space complexity O(n)
    
    
    split_number = -1
    
    linked_list = SLL()
    left_ll = SLL()
    right_ll = SLL()

    for i in range(5):
        linked_list.add_node(i)
    for i in range(5,0,-1):
        linked_list.add_node(i)
        linked_list.add_node(i)
    for i in range(5):
        linked_list.add_node(i)
    partioned_linked_list = partition_SLL(split_number,linked_list,left_ll,right_ll)

    p1 = partioned_linked_list.head
    before_split = True
    
    while(p1):
        
        val = p1.data 
        p1 = p1.next_node

        if val < split_number and before_split: continue
        elif val >= split_number:
            before_split = False
        else:
            assert False

            

if __name__ == "__main__":
    test_partition()
    test_partition_larger_number()
    test_partition_smaller_number()