#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  4 15:12:46 2022

@author: josephbriggs
"""

# pylint: disable=missing-function-docstring

import pytest

from ctci.linked_list.stack import Stack

def test_stack_is_empty_on_creation():
    test_stack = Stack()
    assert test_stack.is_empty()

def test_empty_stack_pop_is_none():
    test_stack = Stack()
    assert test_stack.pop() is None

def test_stack_push_one_element():
    test_stack = Stack()
    test_stack.push(1)
    assert test_stack.peek() == 1

def test_stack_push_many_elements():
    test_stack = Stack()
    nums = [1,2,3,4,5]
    for i in nums:
        test_stack.push(i)

    for i in nums[::-1]:
        assert test_stack.pop() == i

def test_stack_peek_many_elements():
    test_stack = Stack()
    nums = [1,2,3,4,5]
    for i in nums:
        test_stack.push(i)

    for i in nums[::-1]:
        assert test_stack.peek() == i
        assert test_stack.pop() == i

def test_stack_add_none():
    test_stack = Stack()

    with pytest.raises(ValueError):
        test_stack.push(None)
