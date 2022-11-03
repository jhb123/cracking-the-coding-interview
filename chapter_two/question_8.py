#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  3 14:46:32 2022

@author: josephbriggs
"""
from linked_list_functions import SLL,splice

def loop_detection(ll):
    
    # step 1, detect when slow and fast meet (this is guarenteed)
    p1 = ll.head
    p2 = p1.next_node
    
    while p1 is not p2:
        
        if p2.next_node is None:
            return None
        elif p2.next_node.next_node is None:
            return None
        
        p1 = p1.next_node
        p2 = p2.next_node.next_node

    # step 2, calculate the size of the loop
    p3 = p1.next_node
    loop_size = 1
    
    while p3 is not p1:
        p3 = p3.next_node
        loop_size +=1
    

    # make 2 nodes at the start, separted by the length of the loop.
    p1 = ll.head
    p2 = p1
    for i in range(loop_size):
        p2 = p2.next_node

    while p1 is not p2:
        p1 = p1.next_node
        p2 = p2.next_node

    return p2
    

    
