#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 25 17:00:16 2022

@author: josephbriggs
"""

def rotate_matrix(mat: list[list[int]]) -> list[list[int]]:
    
    # every element is checked once, so its time complexity is O(m)
    
    # its a square matrix, so finding the length of one dimension gives all the
    # info. 
    size = len(mat) - 1
    output = []


    # this rotates the matrix counter-clockwise
    # the matrix is indexed with [a][b], a corresponds to the row index and 
    # b corresponds to the column index.
    # the [0][0] element goes to [0][n], where n is the size of the matrix
    # the [0][1] element goes to [1][n], 
    # the [0][x] element goes to [x][n], 
    # the [1][0] element goes to [0][n-1]
    # the [1][1] element goes to [1][n-1]
    # in general, element [a][b] goes to [b][n-a]
    for i in range(size+1):
        output.append([])
        for j in range(size+1):
            output[i].append(mat[j][size-i])
    
    # this rotates the matrix clockwise
    # for i in range(size+1):
    #     output.append([])
    #     for j in range(size+1):
    #         output[i].append(mat[size-j][i])

    for m,l in zip(mat,output):
        print(m,'   ',l)
    return output



rotate_matrix([[1,2,3],
               [4,5,6],
               [7,8,9]])

rotate_matrix([[1,2,3,4],
               [5,6,7,8],
               [9,0,1,2],
               [3,4,5,6]])