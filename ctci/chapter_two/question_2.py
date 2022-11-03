#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  3 13:29:00 2022

@author: josephbriggs
"""

def find_k_from_the_end(ll,k):
    '''
    order (n) in time. If k is larger than the length of the list, return the 
    first element of the linked list.
    '''
    
    p1 = ll.head
    p2 = p1.next_node

    # make a node that is seperated by k from p1.
    for i in range(k):
        if p2:
            p2 = p2.next_node
        else:
            #delete whole list if you reach this point
            break
    # print(p2.data)
    # modes to the end of the linked list
    while p2:
        p1 = p1.next_node
        p2 = p2.next_node

    return p1


