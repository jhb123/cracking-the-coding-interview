#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  3 11:55:13 2022

@author: josephbriggs
"""
import linked_list_functions as llf


def sum_two_linked_lists(num1,num2):
    # question 2.5, turning the lists into ints is not allowed
    summed = llf.SLL()

    rem = 0
    
    p1 = num1.head
    p2 = num2.head
    
    while(p1 or p2 or rem):
        if(p1 and p2):

            sum_val = p1.data + p2.data + rem
            p1 = p1.next_node
            p2 = p2.next_node

        elif(p1):
            sum_val = p1.data + rem
            p1 = p1.next_node
        elif(p2):
            sum_val = p2.data + rem
            p2 = p2.next_node

        else:
            sum_val = rem
        
        digit = sum_val%10
        rem = sum_val // 10
        
        summed.add_node(digit)
    
    return summed
