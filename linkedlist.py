# linkedlist.py by nonetypes
# Last revised on 01/16/2021

class Node:
    """
    """
    def __init__(self, item):
        self.item = item
        self.next = None

    def __repr__(self):
        return str(self.item)

    def is_tail(self):
        """
        """
        if self.next is None:
            return True
        else:
            return False


class LinkedList:
    """
    """
    def __init__(self, item):
        self.head = item if type(item) == type(Node) else Node(item)

    def append_left(self, item):
        """
        """
        item = item if type(item) == type(Node) else Node(item)
        item.next = self.head
        self.head = item

    def append_right(self, item):
        """
        """
        item = item if type(item) == type(Node) else Node(item)
        value = self.head
        while not value.is_tail():
            value = value.next
        value.next = item

    def py_list(self):
        """Return a list of all items from head to tail.
        """
        value = self.head
        py_list = [value]
        while not value.is_tail():
            py_list.append(value.next)
            value = value.next
        return py_list
