#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  8 14:38:30 2022

@author: josephbriggs
"""
from ctci.linked_list.queue import Queue

class animal_shelter():

    def __init__(self):
        self.__dogs = Queue()
        self.__cats = Queue()
        # keep track of animal idx. Increment this every time an animal is added
        self.__i = 0

    def add(self,animal_type,value):


        if animal_type == 0:
            self.__dogs.add((value,self.__i))
        elif animal_type == 1:
            self.__cats.add((value,self.__i))
        else:
            raise ValueError("animal type must be 0 or 1")
        self.__i += 1

    def remove(self,animal_type):

        if animal_type == 0 and not self.__dogs.is_empty():
            return self.__dogs.remove()[0]
        elif animal_type == 1 and not self.__cats.is_empty():
            return self.__cats.remove()[0]
        elif animal_type == 2:

            if self.__dogs.is_empty():
                return self.__cats.remove()[0]
            elif self.__cats.is_empty():
                return self.__dogs.remove()[0]
            elif self.__cats.peek()[1] > self.__dogs.peek()[1]:
                return self.__dogs.remove()[0]
            else:
                return self.__cats.remove()[0]
        else:
            raise ValueError("animal type must be 0, 1 or 2")


    def remove_dog(self):
        return self.remove(0)
    def remove_cat(self):
        return self.remove(1)
    def remove_either(self):
        return self.remove(2)

    def is_empty(self):
        return not( not self.__dogs.is_empty() or not self.__cats.is_empty())

    def has_cats(self):
        return not self.__cats.is_empty()
    def has_dogs(self):
        return not self.__cats.is_empty()

animal_types = [0,0,0,1,1,1]
test_shelter = animal_shelter()

for v,t in enumerate(animal_types):
    test_shelter.add(t,v)

while not test_shelter.is_empty():
    print(test_shelter.remove_either())


