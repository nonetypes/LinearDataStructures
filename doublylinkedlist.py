# doublylinkedlist.py by nonetypes
# Last revised on 01/21/2021

class Node:
    """Node obect to make up the links within a DoublyLinkedList.

    Contains an item and the next and previous nodes in the chain.
    """
    def __init__(self, item=None):
        self.item = item
        self.prev_node = None
        self.next_node = None

    def __repr__(self):
        return str(self.item)


class DoublyLinkedList:
    """Linear data structure -- list like object.
    Contains a head node and a tail node.
    Each node contains an item and the previous and next node in the list.

    Arguments are optional.
    Multiple argumets can be given to create multiple nodes in the list.
    """
    def __init__(self, *items):
        items = [item if isinstance(item, Node) else Node(item) for item in items]
        for i in range(len(items)-1):
            items[i].next_node = items[i+1]
            items[i+1].prev_node = items[i]
        self.head = items[0] if items else None
        self.tail = items[-1] if items else None

    def __repr__(self):
        return str(self.py_list())

    def __getitem__(self, index):
        """
        Return an item from an index:

            linked = DoublyLinkedList('a', 'b', 'c')
            linked[1]                # returns 'b'
        Negative indexes not supported.
        """
        if not isinstance(index, int):
            raise TypeError('list indices must be integers or slices')
        i = 0
        link = self.head
        while link is not None:
            if index == i:
                return link.item
            link = link.next_node
            i += 1
        if index >= i:
            raise IndexError('list index out of range')

    def __setitem__(self, index, new_item):
        """Item assignment. Negative indexes not supported.
        """
        if not isinstance(index, int):
            raise TypeError('list indices must be integers')
        i = 0
        link = self.head
        while link is not None:
            if i == index:
                link.item = new_item
            link = link.next_node
            i += 1
        if index >= i:
            raise IndexError('list index out of range')

    def append_left(self, item):
        """Append an item to the beginning of the list, creating a new head node.
        """
        item = item if isinstance(item, Node) else Node(item)
        item.next_node = self.head
        if self.head is not None:
            self.head.prev_node = item
        if self.tail is None:
            self.tail = item
        self.head = item

    def append_right(self, item):
        """Append an item to the end of the list, creating a new tail node.
        """
        item = item if isinstance(item, Node) else Node(item)
        item.prev_node = self.tail
        if self.tail is not None:
            self.tail.next_node = item
        if self.head is None:
            self.head = item
        self.tail = item

    def append(self, item):
        """Append an item to the end of the list.
        """
        self.append_right(item)

    def pop_left(self):
        """Remove the left most item in the list.
        """
        if self.head is None:
            raise IndexError('pop from empty list')
        else:
            self.head = self.head.next_node
            if self.head is not None:
                self.head.prev_node = None

    def pop_right(self):
        """Remove the right most item in the list.
        """
        if self.head is None:
            raise IndexError('pop from empty list')
        elif self.head is self.tail:
            self.head, self.tail = None, None
        else:
            self.tail = self.tail.prev_node
            self.tail.next_node = None

    def pop(self, index=None):
        """Remove an item at the given index from the list.

        Remove the last item if index is omitted.
        """
        if index is None or self.head is self.tail:
            self.pop_right()
        else:
            if not isinstance(index, int):
                raise TypeError('list indices must be integers')
            link = self.head
            i = 0
            while link is not None:
                if i == index:
                    if link.prev_node is not None:
                        link.prev_node.next_node = link.next_node
                    else:
                        self.pop_left()
                    if link.next_node is not None:
                        link.next_node.prev_node = link.prev_node
                    else:
                        self.pop_right()
                link = link.next_node
                i += 1
            if index >= i:
                raise IndexError('list index out of range')

    def contains(self, item):
        """Return True if the given item is within the list. False otherwise.
        """
        link = self.head
        while link is not None:
            if link.item == item:
                return True
            link = link.next_node
        return False

    def py_list(self):
        """Return a python list of all items from head to tail.
        """
        py_list = []
        link = self.head
        while link is not None:
            py_list.append(link)
            link = link.next_node
        return py_list

    def print_nodes(self):
        L = self.py_list()
        for x in L:
            print((x.prev_node, x.next_node))


if __name__ == "__main__":
    linked = DoublyLinkedList()
    linked.append(2)
    linked.append_left(1)
    linked.append_right(3)
    print(linked[1])
    print(linked.contains(2))
    linked[1] = 'two'
    print(linked.contains('two'))
    print(linked)
    linked.pop(1)
    print(linked)
    linked.pop_left()
    linked.pop_right()
    print(linked)
