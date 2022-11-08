#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  7 18:31:14 2022

@author: josephbriggs
"""

import random

from ctci.chapter_three.question_five import sort_stack
from ctci.linked_list.stack import Stack


def test_random_stack():
    random.seed(0)
    random_numbers = [random.randint(-10, 10) for i in range(100)]

    unsorted_stack = Stack()
    for val in random_numbers:
        unsorted_stack.push(val)

    sorted_nums = sorted(random_numbers)

    sorted_stack = sort_stack(unsorted_stack)
    assert not sorted_stack.is_empty()

    i = 0
    while not sorted_stack.is_empty():
        assert sorted_stack.pop() == sorted_nums[i]
        i += 1


def test_empty_stack():
    # guarrenteed duplicates, negative
    numbers = []

    unsorted_stack = Stack()
    for val in numbers:
        unsorted_stack.push(val)

    sorted_nums = sorted(numbers)

    sorted_stack = sort_stack(unsorted_stack)

    i = 0
    while not sorted_stack.is_empty():
        assert sorted_stack.pop() == sorted_nums[i]
        i += 1


def test_rev_ordered_stack():
    # guarrenteed duplicates, negative
    numbers = [1, 2, 3, 4, 5]

    unsorted_stack = Stack()
    for val in numbers:
        unsorted_stack.push(val)

    sorted_nums = sorted(numbers)

    sorted_stack = sort_stack(unsorted_stack)
    assert not sorted_stack.is_empty()

    i = 0
    while not sorted_stack.is_empty():
        assert sorted_stack.pop() == sorted_nums[i]
        i += 1


def test_ordered_stack():
    # guarrenteed duplicates, negative
    numbers = [5, 4, 3, 2, 1]

    unsorted_stack = Stack()
    for val in numbers:
        unsorted_stack.push(val)

    sorted_nums = sorted(numbers)

    sorted_stack = sort_stack(unsorted_stack)
    assert not sorted_stack.is_empty()

    i = 0

    while not sorted_stack.is_empty():
        assert sorted_stack.pop() == sorted_nums[i]
        i += 1


def test_multiple_same_nums():
    # guarrenteed duplicates, negative
    numbers = [1, 1, 1, 1]

    unsorted_stack = Stack()
    for val in numbers:
        unsorted_stack.push(val)

    sorted_nums = sorted(numbers)

    sorted_stack = sort_stack(unsorted_stack)
    assert not sorted_stack.is_empty()
    i = 0
    while not sorted_stack.is_empty():
        assert sorted_stack.pop() == sorted_nums[i]
        i += 1


def test_simple_sequence():
    # guarrenteed duplicates, negative
    numbers = [3, 1, 2]

    unsorted_stack = Stack()
    for val in numbers:
        unsorted_stack.push(val)

    sorted_nums = sorted(numbers)

    sorted_stack = sort_stack(unsorted_stack)

    i = 0
    while not sorted_stack.is_empty():
        assert sorted_stack.pop() == sorted_nums[i]
        i += 1
