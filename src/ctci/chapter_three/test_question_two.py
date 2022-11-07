#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  7 12:26:40 2022

@author: josephbriggs
"""

import pytest

from ctci.chapter_three.question_two import stack_with_min

def test_stack_is_empty_on_creation():
    test_stack = stack_with_min()
    assert test_stack.is_empty()

def test_empty_stack_pop_is_none():
    test_stack = stack_with_min()
    assert test_stack.pop() is None

def test_stack_push_one_element():
    test_stack = stack_with_min()
    test_stack.push(1)
    assert test_stack.peek() == 1

def test_stack_pop_one_element():
    test_stack = stack_with_min()
    test_stack.push(1)
    assert test_stack.pop() == 1


def test_stack_push_many_elements():
    test_stack = stack_with_min()
    nums = [1,2,3,4,5]
    for i in nums:
        test_stack.push(i)

    assert test_stack.peek() == 5

def test_stack_pop_many_elements():
    test_stack = stack_with_min()
    nums = [1,2,3,4,5]
    for i in nums:
        test_stack.push(i)

    for i in nums[::-1]:
        assert test_stack.pop() == i

def test_stack_add_none():
    test_stack = stack_with_min()

    with pytest.raises(ValueError):
        test_stack.push(None)
        
def test_stack_get_min_empty():
    test_stack = stack_with_min()
    assert test_stack.get_min() is None
   
def test_stack_get_min_one_element():
    test_stack = stack_with_min()
    test_stack.push(1)
    assert test_stack.get_min() == 1
    
def test_stack_get_min_mulitiple_elements():
    test_stack = stack_with_min()
    nums = [5,1,3]
    for i in nums:
        test_stack.push(i)
    
    assert test_stack.get_min() == 1
    
def test_stack_get_min_mulitiple_elements_with_popping():
    test_stack = stack_with_min()
    nums = [10,3,9,2,2,8,1,7]
    mins = [10,3,3,2,2,2,1,1]
    for i in nums:
        test_stack.push(i)
    
    for n in mins[::-1]:
        print(test_stack.get_min())
        assert test_stack.get_min() == n
        test_stack.pop()
