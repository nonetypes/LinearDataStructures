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
    def __init__(self, item=None):
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
        link = self.head
        while not link.is_tail():
            link = link.next
        link.next = item

    def pop_left(self):
        """
        """
        self.head = self.head.next

    def pop_right(self):
        """
        """
        link = self.head
        while not link.is_tail():
            link = link.next
            if link.next.is_tail():
                link.next = None

    def contains(self, item):
        """
        """
        link = self.head
        while not link.is_tail():
            if link.item == item:
                return True
            link = link.next

        if link.item == item:
            return True
        else:
            return False

    def py_list(self):
        """Return a list of all items from head to tail.
        """
        link = self.head
        py_list = [link]
        while not link.is_tail():
            py_list.append(link.next)
            link = link.next
        return py_list
