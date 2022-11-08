#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  7 11:18:52 2022

@author: josephbriggs
"""
from ctci.linked_list.linked_list_functions import Node

class Queue:
    
    def __init__(self):
        self.__top = None
        self.__last = None
        
    def add(self,val):
        if val is None:
            raise ValueError("Cannot add None to Queue")
 
        if self.__top:
            self.__last.next_node = Node(val)
            self.__last = self.__last.next_node
        else:
            self.__top = Node(val)
            self.__last = self.__top
    
    def remove(self):
        if self.__top is None:
            return None
        elif self.__top is self.__last:
            data = self.__top.data
            self.__top = None
            self.__last = None
            return data
        else:
            data = self.__top.data
            self.__top = self.__top.next_node   
            return data
    
    def peek(self):
        if self.__top:
            return self.__top.data
        else:
            return None
    
    
    def is_empty(self):
        if self.__top:
            return False
        else:
            return True