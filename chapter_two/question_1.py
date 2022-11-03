#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  3 13:19:26 2022

@author: josephbriggs
"""

from linked_list_functions import SLL

def remove_duplicates(ll):
    '''
    O(n) in time. uses hash table trick for O(1) look ups.
    The algorithm uses two 'pointers', p1 and p2. p1 precedes p2 always.
    The algorithm is initiated by adding the data at head to the hash
    table. p2 is set to be the node immediately after the head.

    then, while p1 and p2 are pointing at nodes, the data at p2 is checked:

    case 1:
    If the data has been used before, p2 is set to the node immediately
    after it. p1's next node is set to the node p2 has just changed to.

    case 2:
    If the data in p2 has not been used before, then the data is added to
    the hash table. p1 is incremented to the node next to p1 and p2 is
    incremented to the node after p2.

    If extra storage is not allowed, then an O(n^2) algorithm can be used
    instead. Its the same idea as above, but instead of checking the hash
    table, you iterate through the linked list each time.
    '''
    p2 = ll.head.next_node
    p1 = ll.head
    used_vals = {p1.data: 1}

    while p1 and p2:

        if p2.data in used_vals:
            p2 = p2.next_node
            p1.next_node = p2
        else:
            used_vals[p2.data] = 1
            p1 = p1.next_node
            p2 = p2.next_node
            
    new_ll = SLL()
    new_ll.head = ll.head
    return new_ll

