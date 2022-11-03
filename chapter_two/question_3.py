#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  3 13:01:43 2022

@author: josephbriggs
"""

def delete_middle_node(node):
    
    # set the node's data to the next nodes data
    node.data = node.next_node.data
    # skip the next node.
    node.next_node = node.next_node.next_node
    
    
