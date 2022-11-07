#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  7 12:19:34 2022

@author: josephbriggs
"""

from ctci.linked_list.stack import Stack

class stack_with_min(Stack):
    '''
    This class has all the same functionality as a stack, except it also has
    O(1) retrieval of the minimum value. This is implemented using a second
    stack which has the tracks the current minimum value in the stack. This 
    comes at the expense of O(n) space complexity in the worst case (a list 
    of numbers added to the stack in decending order).
    '''
    def __init__(self):
        super().__init__()
        self.__min_stack = Stack()
        
    
    def push(self,val):
        
        if self.__min_stack.peek() is None:
            self.__min_stack.push(val)
        elif val <= self.__min_stack.peek():
            self.__min_stack.push(val)
            
        super().push(val)

            
    def pop(self):
        
        val = self.peek()
        if val is None: pass
        elif val == self.__min_stack.peek():
            self.__min_stack.pop()
            
        return super().pop()

    def get_min(self):
        return self.__min_stack.peek()