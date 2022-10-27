#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 27 16:27:53 2022

@author: josephbriggs
"""


class Node():
    '''
    A node.
    '''

    def __init__(self, data):
        self.__data = data
        self.__next_node = None

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, data):
        self.__data = data

    @property
    def next_node(self):
        return self.__next_node

    @next_node.setter
    def next_node(self, node):
        self.__next_node = node


class SSL():
    '''
    A singly linked list
    '''

    def __init__(self):
        self.__head = None
        self.__tail = None

    @property
    def head(self):
        return self.__head

    def add_node(self, data):
        if not self.__head:
            self.__head = Node(data)
            self.__tail = self.__head
        else:
            n = Node(data)
            self.__tail.next_node = n
            self.__tail = n

    def print_list(self):
        temp = self.__head
        while(temp):
            print(temp.data)
            temp = temp.next_node

    def delete_by_value(self, val):

        # to deal with the scenario where the head is deleted, a new
        # head needs to be stored.
        if self.__head.data == val:
            self.__head = self.__head.next_node

        else:
            current = self.__head
            # the current node starts at the head.
            # While there are still nodes after the current node, see if
            # the next node is to be deleted. If it is to be deleted,
            # the the current nodes next_node to be the next next node
            # i.e. skip over that node.
            # always increment the current node to the next node.
            while(current.next_node):

                if current.next_node.data == val:

                    current.next_node = current.next_node.next_node
                current = current.next_node

                # this detects if you delete the tail
                if current == None:
                    break


if __name__ == "__main__":

    linked_list = SSL()

    for i in range(10):
        linked_list.add_node(i)

    linked_list.print_list()
    print('---')
    # linked_list.delete_by_value(5)
    linked_list.delete_by_value(9)

    # for i in range(4,10):
    #     linked_list.add_node(i)

    linked_list.print_list()
