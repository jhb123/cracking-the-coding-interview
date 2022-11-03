#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  3 14:46:32 2022

@author: josephbriggs
"""
from linked_list_functions import SLL,splice

def loop_detection(ll):
    # linear time solution. Step 1 takes at most the length of the linked list
    # before it starts repeating itself (n). Step 2 takes the length of the 
    # loop in the linked list (k). Step 3 takes the lenght of the loop, so
    # time is O(n+k)
    
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

    # step 2, calculate the size of the loop by seeing when a slow moving node 
    # reaches itself again.
    p3 = p1.next_node
    loop_size = 1
    
    while p3 is not p1:
        p3 = p3.next_node
        loop_size +=1
    
    # step 3. Use 2 slow moving nodes separated by the length of the loop to 
    # find the start of the loop. This works because when the lagging node 
    # reaches the start of the node, the leading node will be looping back to
    # this same node because it is separated by the length of the loop from 
    # the lagging node.
    p1 = ll.head
    p2 = p1
    for i in range(loop_size):
        p2 = p2.next_node

    while p1 is not p2:
        p1 = p1.next_node
        p2 = p2.next_node

    return p2
    

    
