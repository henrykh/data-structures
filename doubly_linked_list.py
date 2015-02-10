# -*- coding: utf-8 -*-

"""This module creates the functionality of a linked list data structure.
find more information at http://en.wikipedia.org/wiki/Linked_list
"""

from __future__ import unicode_literals


class DoublyLinkedList(object):
    """Methods to manipulate the linked list data"""

    def __init__(self):
        self.head = None
        self.tail = None

    def __repr__(self):
        return self.__str__()

    def __unicode__(self):
        pointer = self.head
        printout = "("

        while pointer:
            if type(pointer.val) in (unicode, str):
                printout += "'{}'".format(pointer.val)
            else:
                printout += "{}".format(pointer.val)
            pointer = pointer.next
            if pointer:
                printout += ", "

        printout += ")"

        return printout

    def __str__(self):
        printout = unicode(self)
        return printout.encode("utf-8")

    def insert(self, val):
        """insert the value 'val' at the head of the list"""
        new_node = Node(val, next_node=self.head)
        try:
            self.head.prev_node = new_node
        except AttributeError:
            self.tail = new_node

        self.head = new_node

    def append(self, val):
        '''insert the value 'val' at the tail of the list'''
        new_node = Node(val, prev_node=self.tail)
        try:
            self.tail.next_node = new_node
        except AttributeError:
            self.head = new_node

        self.tail = new_node

    def pop(self):
        """Pop the first value off the head of the list and return it."""
        oldHead = self.head
        try:
            self.head = self.head.next_node
            try:
                self.head.prev_node = None
            except AttributeError:
                pass
        except AttributeError:
            raise ValueError("The list is empty")

        return oldHead.val

    def size(self):
        """Return the length of the list"""
        counter = 0
        pointer = self.head

        while pointer:
            pointer = pointer.next
            counter += 1

        return counter

    def search(self, val):
        """Return the node containing 'val' if present, else None"""
        pointer = self.head

        while pointer:
            if pointer.val == val:
                return pointer

            pointer = pointer.next

    def remove(self, node):
        """Remove the given node from the list (node must
        be an item in the list)
        """
        pointer = self.head

        # is node the first item?
        if pointer is node:
            self.head = pointer.next
            return

        while pointer.next:
            if pointer.next is node:
                pointer.next = pointer.next.next
                return

            pointer = pointer.next

    def display(self):
        """print the list represented as a Python tuple literal"""
        print self.__str__()


class Node(object):
    """Create a node object to add into the linked list"""

    def __init__(self, val, prev_node=None, next_node=None):
        self.val = val
        self.next_node = next_node
        self.prev_node = prev_node
