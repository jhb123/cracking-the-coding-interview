#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  2 10:35:54 2022

@author: josephbriggs
"""

import linked_list_functions as llf

def swap_order_recursive(p1):
    # time complexity = O(n), memory complexity = O(n)
    
    if p1.next_node is None or p1 is None:
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

    prev = None
    while(curr):
        next_node = curr.next_node
        curr.next_node = prev
        prev = curr
        curr = next_node        
    
    return prev

def reverse_ll_test():

    forward_list = llf.SLL()
    
    for i in range(10):
        forward_list.add_node(i)
    
    forward_list.print_list()
    
    # p1 = swap_order_recursive(forward_list.head)
    p1 = swap_order_iterative(forward_list.head)

    backward_list = llf.SLL()
    backward_list.head = p1
    backward_list.print_list()
        
if __name__ == "__main__":
    reverse_ll_test()
    