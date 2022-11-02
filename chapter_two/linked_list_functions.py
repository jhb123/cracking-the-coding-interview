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


    def remove_duplicates(self):
        '''
        O(n) in time. uses hash table trick for O(1) look ups.
        The algorithm uses two 'pointers', p1 and p2. p1 precedes p2 always.
        The algorithm is initiated by adding the data at head to the hash
        table. p2 is set to be the node immediately after the head.

        then, while p1 and p2 are pointing at nodes, the data at p2 is checked:

        case 1:
        If the data has been used before, p2 is set to the node immediately
        after it. p1's next node is set to the node p2 has just changed to.

        case 2:
        If the data in p2 has not been used before, then the data is added to
        the hash table. p1 is incremented to the node next to p1 and p2 is
        incremented to the node after p2.

        If extra storage is not allowed, then an O(n^2) algorithm can be used
        instead. Its the same idea as above, but instead of checking the hash
        table, you iterate through the linked list each time.
        '''
        p2 = self.__head.next_node
        p1 = self.__head
        used_vals = {p1.data: 1}

        while p1 and p2:

            if p2.data in used_vals:
                p2 = p2.next_node
                p1.next_node = p2
            else:
                used_vals[p2.data] = 1
                p1 = p1.next_node
                p2 = p2.next_node


    def remove_k_from_the_end(self,k):
        '''
        order (n) in time
        '''
        
        p1 = self.__head
        p2 = p1

        # make a node that is seperated by k from p1.
        for i in range(k):
            if p2.next_node:
                p2 = p2.next_node
            else:
                #delete whole list if you reach this point
                break
        # print(p2.data)
        # modes to the end of the linked list
        while p2.next_node:
            p1 = p1.next_node
            p2 = p2.next_node

        # set p2 to the node after p1. set p1's next_node to p2's next_node
        # delete the current p2, and set p2 to p1's next node (the former next
        # node of p2)
        p2 = p1.next_node
        while(p2):
            p1.next_node = p2.next_node
            del p2
            p2 = p1.next_node
            
        # if p1 is at the head, set the head node to None.
        if p1 == self.__head:
            self.__head = None
            
    def get_length(self):
        p1 = self.head
        size = 0
        while(p1):
            size +=1
            p1 = p1.next_node 
        return size
        
def sum_two_linked_lists_2(num1,num2):
    '''
    Problem 2.5
    
    Time complexity = O(n) where n is the number of digits of the longest 
    number.
    
    Space complexity = O(n), this is the number of recursive calls 
    
    To solve this problem, first we need to pad the two numbers with zeros so 
    that the linked lists are the same length (this makes it easier later).
    
    Next we recursively generate the numbers in the linked list. We have a 
    function that takes 2 nodes and returns a tuple with a value to carry and 
    a node. If the nodes are None, then we return a tuple of (0, None) i.e.
    nothing to carry and a None node -> this is the behaviour which needs to 
    happen at the end of the list.
    
    If the nodes are not None, then the function needs to return the 
    current node (node which corresponds to the power of 10 which is being 
    summed) along with the remainder from adding.
    
    This may be clearer with a concrete example.
    
    The recursive algorithm zooms into the lowest digit and then backs out, 
    so imagine a set of digits that had to be summed: A,B,C,None
    (None represents the None nodes at the end of the linked list)
    
    the algorithm starts at A:
        since A is not None, it moves to B,
        since B is not None, it moves to C
        since C is not Nonce it moves to None,
        At None, it returns carry = 0 and None,
        it backs out to C:
            it adds the values at pair C and the carry value.
            it makes a Node and sets its data to (value%10)
            it sets the next node to None
            it returns carry = value//10 and the Node (NodeC)
        if backs out to B:
            it adds the values at pair B and the carry value.
            it makes a Node and sets its data to (value%10)
            it sets the next node to NodeC
            it returns carry = value//10 and the Node (NodeB)
        it backs out to A:
            it adds the values at pair A and the carry value.
            it makes a Node and sets its data to (value%10)
            it sets the next node to NodeB
            it returns carry = value//10 and the Node (NodeA)
            
    after this has happened, we just need to check that there isn't a leading
    1. If there is, add it to the front.
    
    '''
    
    size_num1 = num1.get_length()
    size_num2 = num2.get_length()
    
    # swap the two numbers so that the longer one is first.  
    # num1 should be longer than num2
      
    delta = size_num1 - size_num2
    if delta < 0:
        num3 = num1
        num1 = num2
        num2 = num3
        delta = -1*delta
        
    # pad the shorter linked list with leading zeros
    pad_ll = SLL()
    for i in range(delta):
        pad_ll.add_node(0)
    p1 = num2.head
    while(p1):
        pad_ll.add_node(p1.data)
        p1 = p1.next_node
        
    # rename pal_ll to num2 for readability
    num2 = pad_ll

    p1 = num1.head
    p2 = num2.head
    
    def sum_recurrsive(p1,p2):
        
        if not p1:
            return 0, None
        
        carry, smaller_node = sum_recurrsive(p1.next_node,p2.next_node)
        
        val = p1.data + p2.data + carry
        current_node = Node(val%10)
        current_node.next_node = smaller_node
        return val//10, current_node
    
    c,p3 = sum_recurrsive(p1, p2)
    if c:
        n = Node(c)
        n.next_node = p3
        p3 = n

    
    summed = SLL()
    summed.head = p3
    
    return summed
    
def test_sum_two_linked_lists_2():

    num1 = SLL()
    num2 = SLL()
    
    # example, 716+592 = 1308
    num1.add_node(7)
    num1.add_node(1)
    num1.add_node(6)
    
    num2.add_node(5)
    num2.add_node(9)
    num2.add_node(2)
    summed = sum_two_linked_lists_2(num1,num2)
    num1.print_list()
    print('+')
    num2.print_list()
    print('=')
    summed.print_list()
    print('~~~~')

    # example, 716+5921 = 6637
    num2.add_node(1)
    summed = sum_two_linked_lists_2(num1,num2)
    # summed.print_list()
    
    # 999+999 = 1998
    num1 = SLL()
    num2 = SLL()
    for i in range(3):
        num1.add_node(9)
        num2.add_node(9)
    num2.add_node(9)
    
    summed = sum_two_linked_lists_2(num1,num2)
    num1.print_list()
    print('+')
    num2.print_list()
    print('=')
    summed.print_list()
    print('~~~~')

    # 0 + 999 = 999
    num1 = SLL()
    num2 = SLL()
    for i in range(3):
        num1.add_node(9)
    summed = sum_two_linked_lists_2(num1,num2)
    
    num1.print_list()
    print('+')
    num2.print_list()
    print('=')
    summed.print_list()
    print('~~~~')

def sum_two_linked_lists(num1,num2):
    # question 2.5, turning the lists into ints is not allowed
    summed = SLL()

    rem = 0
    
    p1 = num1.head
    p2 = num2.head
    
    while(p1 or p2 or rem):
        if(p1 and p2):

            sum_val = p1.data + p2.data + rem
            p1 = p1.next_node
            p2 = p2.next_node

        elif(p1):
            sum_val = p1.data + rem
            p1 = p1.next_node
        elif(p2):
            sum_val = p2.data + rem
            p2 = p2.next_node

        else:
            sum_val = rem
        
        digit = sum_val%10
        rem = sum_val // 10
        
        summed.add_node(digit)
    
    return summed

def test_sum_two_linked_lists():
    num1 = SLL()
    num2 = SLL()
    
    # example, 617 + 295 = 912
    num1.add_node(7)
    num1.add_node(1)
    num1.add_node(6)
    
    num2.add_node(5)
    num2.add_node(9)
    num2.add_node(2)
    summed = sum_two_linked_lists(num1,num2)
    summed.print_list()
    
    
    num2.add_node(1)
    summed = sum_two_linked_lists(num1,num2)
    summed.print_list()
    
    num1 = SLL()
    num2 = SLL()
    for i in range(3):
        num1.add_node(9)
        num2.add_node(9)
    num2.add_node(9)
    
    summed = sum_two_linked_lists(num1,num2)
    summed.print_list()

    num1 = SLL()
    num2 = SLL()
    for i in range(3):
        num1.add_node(9)
    summed = sum_two_linked_lists(num1,num2)
    summed.print_list()

def test_partition():
    # question 2.4, time complexity O(n), space complexity O(n)
    
    def partition_SLL(val,input_ll,left_lll,right_ll):
        
        
        p1 = input_ll.head
        p2 = None
        while(p1):
            # iterate through list once
            if p1.data < val:
                left_ll.add_node(p1.data)
                p2 = p1
                p1 = p1.next_node
            else:
                right_ll.add_node(p1.data)
                p1 = p1.next_node
        # iterate through list again
        if p2:
            p1 = right_ll.head 
            while(p1):
                left_ll.add_node(p1.data)
                p1 = p1.next_node
        
        return left_ll
    
    linked_list = SLL()
    left_ll = SLL()
    right_ll = SLL()

    for i in range(5):
        linked_list.add_node(i)
    for i in range(5,0,-1):
        linked_list.add_node(i)
        linked_list.add_node(i)
    for i in range(5):
        linked_list.add_node(i)
    linked_list.print_list()
    partioned_linked_list = partition_SLL(3,linked_list,left_ll,right_ll)
    partioned_linked_list.print_list()

def test_get_middle_node():
    # question 2.3
    linked_list = SLL()
    for i in range(10):
        linked_list.add_node(i)
    linked_list.print_list()
    
    
    p1 = linked_list.get_node(5)
    
    p1.data = p1.next_node.data
    p1.next_node = p1.next_node.next_node
    
    linked_list.print_list()
    
    

def test_remove_k_from_the_end():
    # question 2.2
    linked_list = SLL()
    for i in range(3):
        linked_list.add_node(i)
    linked_list.print_list()
    
    linked_list.remove_k_from_the_end(-1)
    linked_list.print_list()
    

def test_remove_duplicates():
    # question 2.1
    linked_list = SLL()
    for i in range(4):
        linked_list.add_node(i)
        linked_list.add_node(i)
        # linked_list.add_node(i)

    for i in range(10):
        linked_list.add_node(i)

    linked_list.add_node(10)
    linked_list.add_node(10)

    linked_list.print_list()
    linked_list.remove_duplicates()
    linked_list.print_list()

    temp = linked_list.head

    i = 0
    while(temp):
        assert temp.data == i
        temp = temp.next_node
        i += 1
    print('successfully removed duplicate elements')

def test_create_sll_test():
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
    # test_create_sll_test()
    # delete_one_node_test()
    # test_remove_duplicates()
    # test_remove_k_from_the_end()
    # test_get_middle_node()
    # test_partition()
    # test_sum_two_linked_lists()
    test_sum_two_linked_lists_2()
