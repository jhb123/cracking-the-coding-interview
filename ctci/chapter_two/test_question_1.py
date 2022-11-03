#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  3 13:24:40 2022

@author: josephbriggs
"""
from ctci.linked_list.linked_list_functions import SLL
from ctci.chapter_two.question_1 import remove_duplicates

def test_remove_duplicates():
    # question 2.1
    linked_list = SLL()
    for i in range(4):
        linked_list.add_node(i)
        linked_list.add_node(i)
        # linked_list.add_node(i)

    for i in range(10):
        linked_list.add_node(i)

    linked_list.add_node(10)
    linked_list.add_node(10)


    new_ll = remove_duplicates(linked_list)

    p1 = new_ll.head
    i = 0
    while(p1):
        assert p1.data == i
        p1 = p1.next_node
        i += 1
        
        
def test_remove_duplicates_2():
    # question 2.1
    linked_list = SLL()
    for i in range(4):
        linked_list.add_node(2)
        # linked_list.add_node(i)

    for i in range(10):
        linked_list.add_node(1)

    linked_list.add_node(10)


    new_ll = remove_duplicates(linked_list)

    p1 = new_ll.head
    nums = [2,1,10]
    for n in nums:
        assert p1.data == n        
        p1 = p1.next_node
    
