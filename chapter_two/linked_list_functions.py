#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 27 17:47:30 2022

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


class SLL():
    '''
    A singly linked list
    '''

    def __init__(self):
        self.__head = None
        self.__tail = None

    @property
    def head(self):
        return self.__head
    @head.setter
    def head(self,node):
        self.__head = node

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
        print('[',end="")
        while(temp):
            print(temp.data,end=" ")
            temp = temp.next_node
        print(']')

    def delete_by_value(self, val):
        # delete one node only with this function.
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
                    break
                else:
                    current = current.next_node

                # this detects if you delete the tail
                if current == None:
                    break
                
    def get_node(self,data):
        p1 = self.__head
        
        while(p1):
            if p1.data == data:
                return p1
            else:
                p1 = p1.next_node

            
    def get_length(self):
        p1 = self.head
        size = 0
        while(p1):
            size +=1
            p1 = p1.next_node 
        return size
        


def test_create_sll():
    linked_list = SLL()
    for i in range(10):
        linked_list.add_node(i)

    temp = linked_list.head

    i = 0
    while(temp):
        assert temp.data == i
        temp = temp.next_node
        i += 1
    print('successfully created a linked list')

def delete_one_node_test():

    linked_list = SLL()

    for i in range(10):
        linked_list.add_node(i)

    # test deleting a value from the middle
    linked_list.delete_by_value(5)
    temp = linked_list.head
    while(temp):
        assert temp.data !=5
        temp = temp.next_node
        i += 1


    # test deleting a value from the start
    linked_list.delete_by_value(0)

    temp = linked_list.head

    while(temp):
        assert temp.data !=0
        temp = temp.next_node
        i += 1

    # test deleting a value from the end
    linked_list.delete_by_value(9)

    temp = linked_list.head
    while(temp):
        assert temp.data !=9
        temp = temp.next_node
        i += 1

    print('successfully deleted nodes')


if __name__ == "__main__":
    test_create_sll()
    delete_one_node_test()