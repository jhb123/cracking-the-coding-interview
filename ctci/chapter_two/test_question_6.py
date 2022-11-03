#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  3 13:47:42 2022

@author: josephbriggs
"""
from ctci.linked_list.linked_list_functions import SLL
from ctci.chapter_two.question_6 import swap_order_iterative,swap_order_recursive,is_palidrome

def test_reverse_iterative():
    forward_list = SLL()
    
    word = "asdfghjkl"
    for letter in word:
        forward_list.add_node(letter)
    
    p1 = swap_order_iterative(forward_list.head)
    
    backwards_list = SLL()
    backwards_list.head = p1
    p1 = backwards_list.head
    
    for letter in word[::-1]:
        print(letter,p1.data)
        assert letter == p1.data
        p1 = p1.next_node
        
        
def test_reverse_iterative_one_letter():
    forward_list = SLL()
    
    word = "a"
    for letter in word:
        forward_list.add_node(letter)
    
    p1 = swap_order_iterative(forward_list.head)
    
    backwards_list = SLL()
    backwards_list.head = p1
    p1 = backwards_list.head
    
    for letter in word[::-1]:
        print(letter,p1.data)
        assert letter == p1.data
        p1 = p1.next_node
        
def test_reverse_iterative_two_letter():
    forward_list = SLL()
    
    word = "ab"
    for letter in word:
        forward_list.add_node(letter)
    
    p1 = swap_order_iterative(forward_list.head)
    
    backwards_list = SLL()
    backwards_list.head = p1
    p1 = backwards_list.head
    
    for letter in word[::-1]:
        print(letter,p1.data)
        assert letter == p1.data
        p1 = p1.next_node
        
def test_reverse_iterative_empty():
    forward_list = SLL()
    
    word = ""
    for letter in word:
        forward_list.add_node(letter)
    
    p1 = swap_order_iterative(forward_list.head)
    
    backwards_list = SLL()
    backwards_list.head = p1
    p1 = backwards_list.head
    
    for letter in word[::-1]:
        print(letter,p1.data)
        assert letter == p1.data
        p1 = p1.next_node
              

        
        
def test_reverse_recursive():
    forward_list = SLL()
    
    word = "asdfghjkl"
    for letter in word:
        forward_list.add_node(letter)
    
    p1 = swap_order_recursive(forward_list.head)
    
    backwards_list = SLL()
    backwards_list.head = p1
    p1 = backwards_list.head
    
    for letter in word[::-1]:
        print(letter,p1.data)
        assert letter == p1.data
        p1 = p1.next_node
        

def test_reverse_recursive_one_letter():
    forward_list = SLL()
    
    word = "a"
    for letter in word:
        forward_list.add_node(letter)
    
    p1 = swap_order_recursive(forward_list.head)
    
    backwards_list = SLL()
    backwards_list.head = p1
    p1 = backwards_list.head
    
    for letter in word[::-1]:
        print(letter,p1.data)
        assert letter == p1.data
        p1 = p1.next_node
        
def test_reverse_recursive_two_letter():
    forward_list = SLL()
    
    word = "ab"
    for letter in word:
        forward_list.add_node(letter)
    
    p1 = swap_order_recursive(forward_list.head)
    
    backwards_list = SLL()
    backwards_list.head = p1
    p1 = backwards_list.head
    
    for letter in word[::-1]:
        print(letter,p1.data)
        assert letter == p1.data
        p1 = p1.next_node
        
def test_reverse_recursive_empty():
    forward_list = SLL()
    
    word = ""
    for letter in word:
        forward_list.add_node(letter)
    
    p1 = swap_order_recursive(forward_list.head)
    
    backwards_list = SLL()
    backwards_list.head = p1
    p1 = backwards_list.head
    
    for letter in word[::-1]:
        print(letter,p1.data)
        assert letter == p1.data
        p1 = p1.next_node
              

def test_palidrome_positive():

    forward_list = SLL()
    
    word = "asdfghjklkjhgfdsa"
    for letter in word:
        forward_list.add_node(letter)
        
    assert is_palidrome(forward_list)
    
def test_palidrome_negative():

    forward_list = SLL()
    
    word = "asdfghjkl"
    for letter in word:
        forward_list.add_node(letter)
        
    assert not is_palidrome(forward_list)
    
def test_palidrome_one_letter():

    forward_list = SLL()
    
    word = "a"
    for letter in word:
        forward_list.add_node(letter)
        
    assert is_palidrome(forward_list)

def test_palidrome_empty():

    forward_list = SLL()
    
    word = ""
    for letter in word:
        forward_list.add_node(letter)
        
    assert is_palidrome(forward_list)
    
def test_palidrome_nearly_palidrome_final_letter():

    forward_list = SLL()
    
    word = "asdfghjklkjhgfdsaa"
    for letter in word:
        forward_list.add_node(letter)
        
    assert not is_palidrome(forward_list)
    
def test_palidrome_nearly_palidrome():

    forward_list = SLL()
    
    word = "asdfgzhjklkjhgfdsa"
    for letter in word:
        forward_list.add_node(letter)
        
    assert not is_palidrome(forward_list)
