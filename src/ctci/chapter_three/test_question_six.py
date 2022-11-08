#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  8 15:14:36 2022

@author: josephbriggs
"""
from ctci.chapter_three.question_six import animal_shelter


def test_dogs_then_cats():
    animal_types = [0,0,0,1,1,1]
    test_shelter = animal_shelter()
    solution = []
    for v,t in enumerate(animal_types):
        test_shelter.add(t,v)
        solution.append(v)
        
    i = 0 
    while not test_shelter.is_empty():
        assert test_shelter.remove_either() == solution[i]
        i += 1
        
def test_remove_dogs_then_cats():
    animal_types = [0,1,0,1,0,1]
    test_shelter = animal_shelter()
    for v,t in enumerate(animal_types):
        test_shelter.add(t,v)
        
    solution_a = [0,2,4]
    i = 0
    while not test_shelter.has_dogs():
        assert test_shelter.remove_dog() == solution_a[i]
        i += 1
        
    solution_a = [1,3,5]
    i = 0
    while not test_shelter.has_cats():
        assert test_shelter.remove_cat() == solution_a[i]
        i += 1
    
    assert not test_shelter.is_empty()