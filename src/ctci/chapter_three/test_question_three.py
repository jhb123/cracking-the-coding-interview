#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  7 14:59:01 2022

@author: josephbriggs
"""

from ctci.chapter_three.question_three import SetOfStacks

def test_adding_many_stacks_size():
    test_stack = SetOfStacks(2)

    nums = [1,2,3]
    for n in nums:

        test_stack.push(n)

    assert test_stack.peek() == 3
    assert test_stack.peek_current_stack_height() == 1

def test_popping_many_stacks_size():
    test_stack = SetOfStacks(2)

    nums = [1,2,3]
    stack_sizes = [1,2,1]
    for n in nums:
        test_stack.push(n)

    for n,s in zip(nums[::-1],stack_sizes):
        assert test_stack.peek_current_stack_height() == s
        assert test_stack.pop() == n


def test_adding_pop_at_index_size():

    test_stack = SetOfStacks(2)

    nums = [1,2,3,4,5]
    expected_answer = [5,3,None]
    expected_sizes = [1,1,0]
    for n in nums:
        test_stack.push(n)

    test_stack.pop_at_index(1)
    test_stack.pop_at_index(0)
    test_stack.pop_at_index(0)



    for n,s in zip(expected_answer,expected_sizes):

        assert test_stack.peek_current_stack_height() == s
        assert test_stack.pop() == n

