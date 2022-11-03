#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  3 22:07:29 2022

@author: josephbriggs
"""

from distutils.core import setup
setup(name='ctci',
      version='1.0',
      # py_modules=['foo'],
      # packages = ['chapter_one',
      #             'chapter_two',
      #             'linked_list']
      packages = ['ctci/chapter_one',
                  'ctci/chapter_two',
                  'ctci/linked_list']
      )