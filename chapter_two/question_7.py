#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  3 14:14:03 2022

@author: josephbriggs
"""

def intersecting_node(ll1,ll2):
    
    p1 = ll1.head
    p2 = ll2.head
    
    while(p1):
        
        if p1 == p2:
            return p1
        else:
            p1 = p1.next_node
            p2 = p2.next_node
            
    return None