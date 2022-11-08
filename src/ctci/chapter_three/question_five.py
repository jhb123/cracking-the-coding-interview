#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  7 18:31:14 2022

@author: josephbriggs
"""
from ctci.linked_list.stack import Stack

def sort_stack(unsorted_stack):
    '''
    Returns a stack which is sorted such that the top element is the smallest.

    Algorithm:
    Create a new Stack called sorted_stack.
    pop the top off the unsorted_stack and store it in a temporary value.

    While the sorted_Stack is not empyt:
    If the temporary value is less than the top of the sorted_stack, push the
    temporary value to the sorted_stack.

    else, it is greater than the top of the sorted_stack. Pop the sorted_stack
    and push this value to the top of the unsorted_stack and attempted to push
    the temporary value to the sorted_stack based on the above condition.

    If the unsorted_stack is empty, push temp to the unsorted stack

    Complete the above steps while the unsorted_list is not empty.

    Time complexity: O(n^2) where n is the number of elements in the stack
    Space complexity: O(n)

    Reasoning:

    '''

    sorted_stack = Stack()

    while not unsorted_stack.is_empty():

        temp_val = unsorted_stack.pop()

        if sorted_stack.is_empty():
            sorted_stack.push(temp_val)
        else:
            while not sorted_stack.is_empty():
                if sorted_stack.peek() >= temp_val:
                    sorted_stack.push(temp_val)
                    break
                else:
                    unsorted_stack.push(sorted_stack.pop())

            if sorted_stack.is_empty():
                sorted_stack.push(temp_val)


    return sorted_stack

