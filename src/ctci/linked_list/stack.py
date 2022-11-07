 # -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from ctci.linked_list.linked_list_functions import Node


class Stack:
    
    def __init__(self):
        
        self.__top = None
    
    def push(self,val):
        if val is None:
            raise ValueError("Cannot push None to stack")
            
        if self.__top:
            
            new_node = Node(val)
            
            new_node.next_node = self.__top
            
            self.__top = new_node
            
        else:
            self.__top = Node(val)
        
        
    def peek(self):
        if self.__top:
            return self.__top.data
        else:
            return None
        
    def pop(self):
        if self.__top:
            val  = self.__top.data
            self.__top = self.__top.next_node
            return val
        else:
            return None
        
    def is_empty(self):
        if self.__top:
            return False
        else:
            return True


    