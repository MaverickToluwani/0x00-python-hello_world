#!/usr/bin/python3

"""My node module"""


class Node:
    """Class to describe a node structure
    Attributes:
        __data (int): value of the node
        __next_node (class): Pointer to the Node class
    """

    def __init__(self, data, next_node=None):
        """Initializing node data and pointer to the next Node object
        Args:
            data (int): value of the node
            __next_node (Node): Pointer to the Node class
        """
        self.data = data
        self.__next_node = next_node

    @property
    def data(self):
        """Gets the data of Node
        Returns: data of Node
        """
        return self.__data

    @data.setter
    def data(self, value):
        """Sets the value of the Node data
        Raises:
            TypeError If value if not an integer
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """gets the next Node
        Returns:
            Next_node (class): Pointer to the Node class
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """ sets the Next Node object to be pointed too
        Raises:
            TypeError: If next_node is not a Node object
        """
        if not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """A class that describes a singlylinkedlist structure"""

    def __init__(self, head=None):
        """Initializes the head of the Node
        Args:
            head (class): A node class object
        """
        self.__head = head

    def sorted_insert(self, value):
        """Inserts data to the singlylinkedlist
        Args:
            value (int): value to be inserted into the linked list
        """
        new_node = Node(value, self.__head)
        self.__head = new_node

    def __str__(self):
        curr = self.__head
        nodelist = []
        while curr is not None:
            nodelist.append((curr.data))
            curr = curr.next_node
        sorter = sorted(nodelist)
        return "\n".join(list(map(str, sorter)))
