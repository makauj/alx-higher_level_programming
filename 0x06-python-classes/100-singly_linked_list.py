#!/usr/bin/python3
"""Singly linked list module"""


class Node:
    """node"""
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """singly linked list"""

    def __init__(self):
        self.head = None

    def __str__(self):
        printall = ""
        current = self.head
        while current:
            printall += str(current.data) + "\n"
            current = current.next_node
        return printall[:-1]

    def sorted_insert(self, value):
        new = Node(value)
        if not self.head:
            self.head = new
            return
        if value < self.head.data:
            new.next_node = self.head
            self.head = new
            return
        current = self.head
        while current.next_node and current.next_node.data < value:
            current = current.next_node
        if current.next_node:
            new.next_node = current.next_node
        current.next_node = new
