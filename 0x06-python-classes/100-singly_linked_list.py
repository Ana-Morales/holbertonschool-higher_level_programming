#!/usr/bin/python3
"""This module writes a class Node that defines a node
of a singly linked list

"""


class Node:
    """Defines a node of a singly linked list"""

    def __init__(self, data, next_node=None):
        """Initializes the data"""
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Getting data"""
        return self.__data

    @data.setter
    def data(self, value):
        """Setting data"""
        if type(value) != int:
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Getting next_node"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Setting next_node"""
        if value is None or type(value) == Node:
            self.__next_node = value
        else:
            raise TypeError("next_node must be a Node object")


class SinglyLinkedList:
    """Defines a singly linked list"""

    def __init__(self):
        """Initializes the data"""
        self.__head = None

    def sorted_insert(self, value):
        """inserts a new Node into the correct sorted position in the list
        (increasing order)"""
        nod = Node(value)

        if self.__head is None or self.__head.data >= value:
            nod.next_node = self.__head
            self.__head = nod
        else:
            tmp = self.__head
            while tmp.next_node is not None and tmp.next_node.data < value:
                tmp = tmp.next_node
            nod.next_node = tmp.next_node
            tmp.next_node = nod

    def __str__(self):
        """Method to be used when use print on SinglyLinkedList"""
        aux = self.__head
        while aux:
            print(aux.data, end="")
            if aux.next_node is not None:
                print()
            aux = aux.next_node
        return ""
