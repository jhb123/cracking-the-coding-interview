# !/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  2 10:35:54 2022

@author: josephbriggs
"""

from linked_list_functions import SLL

def swap_order_recursive(p1):
    # time complexity = O(n), memory complexity = O(n)
    # inplace reversal

    if p1 is None:
        # deals with case where no input is given.
        return p1
    elif p1.next_node is None:
        # bases cases: if the next node is None, then the list is
        # reversed by returning the Node. if no node is input, then 
        # return it.
        return p1
    else:
        
        # get the head of the simpler case
        p2 = swap_order_recursive(p1.next_node)
        
        # by setting the node after p1 to have its next node be p1,
        # the link is reversed. This means that whatever p1 one was pointing
        # now points at p1. 
        p1.next_node.next_node = p1
                    
        # finally set p1.next to be the end of the list by setting its
        # next node to None
        p1.next_node = None
        
        # return the new head of the simpler case.
        return p2
    
def swap_order_iterative(curr):
    # time complexity = O(n), memory complexity = O(1)
    # inplace reversal
    prev = None
    while(curr):
        next_node = curr.next_node
        curr.next_node = prev
        prev = curr
        curr = next_node        
    
    return prev


def is_palidrome(forward_list):
    # time complexity (n), memory complexity = O(n) where n is the length of 
    # the input list.
    
    
    # copy the input list.
    new_forward_list = SLL()
    p1 = forward_list.head
    while(p1):
        new_forward_list.add_node(p1.data)
        p1 = p1.next_node
    
    # reverse the input list
    p1 = swap_order_iterative(forward_list.head)
    backward_list = SLL()
    backward_list.head = p1
    
    # set p1 and p2 to start of the lists and iteterate through them. If they
    # are ever not equal, then return false
    p1 = new_forward_list.head
    p2 = backward_list.head
    
    while(p1):
        
        if p1.data != p2.data:
            return False
        p1 = p1.next_node
        p2 = p2.next_node
        
    return True
    