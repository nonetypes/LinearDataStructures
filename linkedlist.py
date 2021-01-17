# linkedlist.py by nonetypes
# Last revised on 01/17/2021

class Node:
    """Node obect to make up the links within a LinkedList.

    Contains an item and the next node in the chain.
    """
    def __init__(self, item=None):
        self.item = item
        self.next_node = None

    def __repr__(self):
        return str(self.item)


class LinkedList:
    """List like object.
    Contains a head node which contains an item and the next node,
    containing the next item and so forth.

    Arguments are optional.
    Multiple argumets can be given to create multiple nodes in the list.
    """
    def __init__(self, *items):
        items = [item if isinstance(item, Node) else Node(item) for item in items]
        for i in range(len(items)-1):
            items[i].next_node = items[i+1]
        self.head = items[0] if items else None

    def append_left(self, item):
        """Append an item to the beginning of the list, creating a new head node.
        """
        item = item if isinstance(item, Node) else Node(item)
        item.next_node = self.head
        self.head = item

    def append_right(self, item):
        """Append an item to the end of the list.
        """
        item = item if isinstance(item, Node) else Node(item)
        if self.head is None:
            self.head = item
        else:
            link = self.head
            while link.next_node is not None:
                link = link.next_node
            link.next_node = item

    def pop_left(self):
        """Remove the left most item in the list, creating a new head.
        """
        self.head = self.head.next_node

    def pop_right(self):
        """Remove the right most item in the list.
        """
        if self.head.next_node is None:
            self.head = None
        else:
            link = self.head
            while link.next_node is not None:
                if link.next_node.next_node is None:
                    link.next_node = None
                else:
                    link = link.next_node

    def contains(self, item):
        """Return True if the given item is within the list. False otherwise.
        """
        link = self.head
        while link.next_node is not None:
            if link.item == item:
                return True
            link = link.next_node

        if link.item == item:
            return True
        else:
            return False

    def py_list(self):
        """Return a python list of all items from head to tail.
        """
        py_list = []
        link = self.head
        if link is not None:
            py_list.append(link.item)
            while link.next_node is not None:
                py_list.append(link.next_node.item)
                link = link.next_node
        return py_list
