#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  7 11:48:08 2022

@author: josephbriggs
"""

# pylint: disable=missing-function-docstring

import pytest

from ctci.linked_list.queue import Queue

def test_queue_is_empty_on_creation():
    test_queue = Queue()
    assert test_queue.is_empty()

def test_empty_queue_remove_is_none():
    test_queue = Queue()
    assert test_queue.remove() is None
    
def test_queue_push_one_element():
    test_queue = Queue()
    test_queue.add(1)
    assert test_queue.peek() == 1
    
def test_queue_push_many_elements():
    test_queue = Queue()
    nums = [1,2,3,4,5]
    for i in nums:
        test_queue.add(i)

    for i in nums:
        assert test_queue.remove() == i
    
def test_queue_peek_many_elements():
    test_queue = Queue()
    nums = [1,2,3,4,5]
    for i in nums:
        test_queue.add(i)

    for i in nums:
        assert test_queue.peek() == i
        assert test_queue.remove() == i

def test_queue_add_none():
    test_queue = Queue()

    with pytest.raises(ValueError):
        test_queue.add(None)

