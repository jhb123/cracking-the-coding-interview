#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  3 12:02:06 2022

@author: josephbriggs
"""
import linked_list_functions as llf
from question_5_follow_up import sum_two_linked_lists_2

def test_sum_two_linked_lists_lots_of_nines():
    # 999+9999 = 10998
    num1 = llf.SLL()
    num2 = llf.SLL()
    for i in range(3):
        num1.add_node(9)
        num2.add_node(9)
    num2.add_node(9)
    
    summed = sum_two_linked_lists_2(num1,num2)
    nums = [1,0,9,9,8]
    p1 = summed.head
    for i in nums:
        assert p1.data == i
        p1 = p1.next_node

def test_sum_two_linked_lists_output_longer_than_inputs():
    num1 = llf.SLL()
    num2 = llf.SLL()
    
    # example, 716+592 = 1308
    num1.add_node(7)
    num1.add_node(1)
    num1.add_node(6)
    
    num2.add_node(5)
    num2.add_node(9)
    num2.add_node(2)
    summed = sum_two_linked_lists_2(num1,num2)
    
    nums = [1,3,0,8]
    p1 = summed.head
    for i in nums:
        assert p1.data == i
        p1 = p1.next_node
        
    

def test_sum_two_linked_lists_one_missing_input():

    num1 = llf.SLL()
    num2 = llf.SLL()
    for i in range(3):
        num1.add_node(9)
    summed = sum_two_linked_lists_2(num1,num2)
    
    summed = sum_two_linked_lists_2(num1,num2)
    nums = [9,9,9]
    p1 = summed.head
    for i in nums:
        assert p1.data == i
        p1 = p1.next_node

    
# if __name__ == "__main__":
#     test_sum_two_linked_lists_2()