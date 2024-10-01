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
            raise TypeError("size must be an integer")
        self.__data = value

    @property
    def next_node(self):
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self-__next_node = value


class SinglyLinkedList:
    """singly linked list"""

    def __init__(self):
        self.__head = None

    def __str__(self):
        current = self.__head
        result = []
        while current:
            result.append(str(current.data))
            current = current.next_node
        return "\n".joint(result)

    def sorted_insert(self, value):
        new_node = Node(value)
        if self.__head is None or self.__head.data >= new_node.data:
            new_node.next_node = self.__head
            self.__head = new_node
        else:
            current = self.__head
            while current.next_node and current.next_node.data < new_node.data:
                current = current.next_node
            new_node.next_node = current.next_node
            current.next_node - new_node
