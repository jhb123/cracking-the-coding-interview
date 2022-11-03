#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  3 11:55:13 2022

@author: josephbriggs
"""
import linked_list_functions as llf

def sum_two_linked_lists_2(num1,num2):
    '''
    Problem 2.5
    
    Time complexity = O(n) where n is the number of digits of the longest 
    number.
    
    Space complexity = O(n), this is the number of recursive calls 
    
    To solve this problem, first we need to pad the two numbers with zeros so 
    that the linked lists are the same length (this makes it easier later).
    
    Next we recursively generate the numbers in the linked list. We have a 
    function that takes 2 nodes and returns a tuple with a value to carry and 
    a node. If the nodes are None, then we return a tuple of (0, None) i.e.
    nothing to carry and a None node -> this is the behaviour which needs to 
    happen at the end of the list.
    
    If the nodes are not None, then the function needs to return the 
    current node (node which corresponds to the power of 10 which is being 
    summed) along with the remainder from adding.
    
    This may be clearer with a concrete example.
    
    The recursive algorithm zooms into the lowest digit and then backs out, 
    so imagine a set of digits that had to be summed: A,B,C,None
    (None represents the None nodes at the end of the linked list)
    
    the algorithm starts at A:
        since A is not None, it moves to B,
        since B is not None, it moves to C
        since C is not Nonce it moves to None,
        At None, it returns carry = 0 and None,
        it backs out to C:
            it adds the values at pair C and the carry value.
            it makes a Node and sets its data to (value%10)
            it sets the next node to None
            it returns carry = value//10 and the Node (NodeC)
        if backs out to B:
            it adds the values at pair B and the carry value.
            it makes a Node and sets its data to (value%10)
            it sets the next node to NodeC
            it returns carry = value//10 and the Node (NodeB)
        it backs out to A:
            it adds the values at pair A and the carry value.
            it makes a Node and sets its data to (value%10)
            it sets the next node to NodeB
            it returns carry = value//10 and the Node (NodeA)
            
    after this has happened, we just need to check that there isn't a leading
    1. If there is, add it to the front.
    
    '''
    
    size_num1 = num1.get_length()
    size_num2 = num2.get_length()
    
    # swap the two numbers so that the longer one is first.  
    # num1 should be longer than num2
      
    delta = size_num1 - size_num2
    if delta < 0:
        num3 = num1
        num1 = num2
        num2 = num3
        delta = -1*delta
        
    # pad the shorter linked list with leading zeros
    pad_ll = llf.SLL()
    for i in range(delta):
        pad_ll.add_node(0)
    p1 = num2.head
    while(p1):
        pad_ll.add_node(p1.data)
        p1 = p1.next_node
        
    # rename pal_ll to num2 for readability
    num2 = pad_ll

    p1 = num1.head
    p2 = num2.head
    
    def sum_recurrsive(p1,p2):
        
        if not p1:
            return 0, None
        
        carry, smaller_node = sum_recurrsive(p1.next_node,p2.next_node)
        
        val = p1.data + p2.data + carry
        current_node = llf.Node(val%10)
        current_node.next_node = smaller_node
        return val//10, current_node
    
    c,p3 = sum_recurrsive(p1, p2)
    if c:
        n = llf.Node(c)
        n.next_node = p3
        p3 = n

    
    summed = llf.SLL()
    summed.head = p3
    
    return summed

