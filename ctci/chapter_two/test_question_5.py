#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  3 12:02:06 2022

@author: josephbriggs
"""
from ctci.linked_list.linked_list_functions import SLL
from ctci.chapter_two.question_5 import sum_two_linked_lists


def test_sum_two_linked_lists_with_carrying():
    num1 = SLL()
    num2 = SLL()
    
    # example, 617 + 295 = 912
    num1.add_node(7)
    num1.add_node(1)
    num1.add_node(6)
    
    num2.add_node(5)
    num2.add_node(9)
    num2.add_node(2)
    
    summed = sum_two_linked_lists(num1,num2)
    
    nums = [2,1,9]    
    p1 = summed.head
    for i in nums:
        assert p1.data == i
        p1 = p1.next_node
        
def test_sum_two_linked_lists_with_carrying_and_different_lengths():
    
    num1 = SLL()
    num2 = SLL()
    
    # example, 617 + 295 = 912
    num1.add_node(7)
    num1.add_node(1)
    num1.add_node(6)
    
    num2.add_node(5)
    num2.add_node(9)
    num2.add_node(2)
    num2.add_node(1)

    summed = sum_two_linked_lists(num1,num2)
    
    nums = [2,1,9,1]    
    p1 = summed.head
    for i in nums:
        assert p1.data == i
        p1 = p1.next_node
    

def test_sum_two_linked_lists_lots_of_nines():

    num1 = SLL()
    num2 = SLL()
    for i in range(3):
        num1.add_node(9)
        num2.add_node(9)
    num2.add_node(9)
    
    summed = sum_two_linked_lists(num1,num2)

    nums = [8,9,9,0,1]    
    p1 = summed.head
    for i in nums:
        assert p1.data == i
        p1 = p1.next_node
        
def test_sum_two_linked_lists_one_input():

    num1 = SLL()
    num2 = SLL()
    for i in range(3):
        num1.add_node(9)
    
    summed = sum_two_linked_lists(num1,num2)

    nums = [9,9,9]    
    p1 = summed.head
    for i in nums:
        assert p1.data == i
        p1 = p1.next_node
        
def test_sum_two_linked_lists_no_input():

    num1 = SLL()
    num2 = SLL()
    
    
    summed = sum_two_linked_lists(num1,num2)

    nums = []    
    p1 = summed.head
    for i in nums:
        assert p1.data == i
        p1 = p1.next_node
        
        