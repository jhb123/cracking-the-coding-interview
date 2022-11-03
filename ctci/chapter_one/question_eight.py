#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 25 17:57:22 2022

@author: josephbriggs
"""

def zero_matrix(mat: list[list[int]]) -> list[list[int]]:
    
    # can you do better than order n**2 time?
    print('Input')

    for l in mat:
        print(l)
        
    M = len(mat)
    N = len(mat[0])
    
    # create 2 hash tables for fast lookup later.
    banned_rows = dict()
    banned_cols = dict()

    # iterate over every element once to check if column and row are valid
    for i in range(M):
        for j in range(N):
            if mat[i][j] == 0:
                banned_rows[i] = 1
                banned_cols[j] = 1
            
    # check if element is valid, iterate over every element once. O(1) lookup 
    # with this hash table.
    for i in range(M):
        for j in range(N):
            if i in banned_rows or j in banned_cols:
                mat[i][j] = 0
    print('\nOutput')
    for l in mat:
        print(l)
    
    return mat



# zero_matrix([[1,2,3],
#              [4,5,6],
#              [7,8,9]])

zero_matrix([[1,2,3,4],
             [5,6,0,8],
             [9,1,1,1],
             [3,4,1,6]])