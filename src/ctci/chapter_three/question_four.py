#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  7 16:41:31 2022

@author: josephbriggs
"""

from ctci.linked_list.stack import Stack

class QueueViaStacks:
    
    def __init__(self):
        self.__s0 = Stack() 
        self.__s1 = Stack()

    
    def push(self,val):
        self.__s0.push(val)
        

    def peek(self):
       if self.__s1.is_empty():
           while not self.__s0.is_empty():
               self.__s1.push(self.__s0.pop())
           return self.__s1.peek()
       else:
           val = self.__s1.peek()
           return val

    
    def pop(self):
    
        if self.__s1.is_empty():
            while not self.__s0.is_empty():
                self.__s1.push(self.__s0.pop())
            return self.__s1.pop()
        else:
            val = self.__s1.pop()
            return val

    def is_empty(self):
        is_empty = not self.__s0.is_empty() or not self.__s1.is_empty()
        return not is_empty
        
    # def remove(self):
    #     pass
    
if __name__ == "__main__":
    qvs = QueueViaStacks()
    
    nums = [1,2,3,4,5]
    

    for n in nums:
        qvs.push(n)
        
    print(qvs.pop(),'pop')
    print(qvs.pop(),'pop')
    print(qvs.peek(),'peek')

    # print(qvs.peek(),'peek')

    
    nums = [1,2,3,4,5]
    
    for n in nums:
        qvs.push(n)


    while not qvs.is_empty():
        print(qvs.pop())

