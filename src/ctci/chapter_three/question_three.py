#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  7 14:11:17 2022

@author: josephbriggs
"""
from ctci.linked_list.stack import Stack
from ctci.linked_list.linked_list_functions import Node
from ctci.chapter_two.question_6 import swap_order_recursive


class SetOfStacks:

    def __init__(self, max_height):
        self.__stacks = Stack()
        self.__max_height = max_height
    
    def push(self,val):
        if self.__stacks.peek() is None:
            self.__add_stack(val)
        elif self.__stacks.peek()["size"] == self.__max_height:
            self.__add_stack(val)
        else:
            self.__stacks.peek()["stack"].push(val)
            self.__stacks.peek()["size"] += 1

        
    def peek(self):
        return self.__stacks.peek()["stack"].peek()
            
    
    def pop(self):
        data = self.__stacks.peek()
        if data["size"] == 1:
            val = data["stack"].pop()
            self.__stacks.pop()
            return val
        else:
            val = data["stack"].pop()
            self.__stacks.peek()["size"] -= 1
            return val
        
    def peek_current_stack_height(self):
        return self.__stacks.peek()["size"]

    def pop_at_index(self,idx):
        '''
        
        '''        
        idx = self.__stacks.size - idx
        p1 = self.__stacks.get_top_node()
        for i in range(idx-1):
            p1 = p1.next_node
        
        p1.data["size"] -=1
        
        return p1.data["stack"].pop()
    
    def __add_stack(self,val):
        new_stack = Stack()
        new_stack.push(val)
        # add a tuple with the stack and its current size
        self.__stacks.push({"stack":new_stack,"size":1}) 
        
        