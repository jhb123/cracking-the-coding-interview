#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  3 12:19:00 2022

@author: josephbriggs
"""
from linked_list_functions import SLL

def partition_SLL(val,input_ll,left_ll,right_ll):
    
    
    p1 = input_ll.head
    p2 = None
    while(p1):
        # iterate through list once
        if p1.data < val:
            left_ll.add_node(p1.data)
            p2 = p1
            p1 = p1.next_node
        else:
            right_ll.add_node(p1.data)
            p1 = p1.next_node
    # iterate through list again
    if p2:
        p1 = right_ll.head 
        while(p1):
            left_ll.add_node(p1.data)
            p1 = p1.next_node
    
    return left_ll

def test_partition():
    # question 2.4, time complexity O(n), space complexity O(n)
    
    
    
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
    linked_list.print_list()
    partioned_linked_list = partition_SLL(3,linked_list,left_ll,right_ll)
    partioned_linked_list.print_list()

if __name__ == "__main__":
    test_partition()