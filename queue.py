# queue.py by nonetypes
# Last revised on 01/16/2021

class Queue:
    """List like object. First in, first out.
    Concatenation support between various built-in objects.
    """
    def __init__(self, *items):
        self.items = list(items)

    def __repr__(self):
        """Return a printable string version of self.items
        """
        return str(self.items)

    def __getitem__(self, index):
        """
        Return an item from an index:

            queue = Queue('a', 'b', 'c')
            queue[1]                # returns 'b'
        """
        return self.items[index]

    def __setitem__(self, index, item):
        """Item assignment.
        """
        self.items[index] = item

    def __add__(self, other_item):
        """
        Concatenation support:

            queue = Queue(1, 2, 3)
            queue + 4               # returns [1, 2, 3, 4]
            queue + 'string'        # returns [1, 2, 3, 'string']
            queue + [4, 5]          # returns [1, 2, 3, 4, 5]
            queue + (4, 5)          # returns [1, 2, 3, (4, 5)]
            queue + {'a': 1}        # returns [1, 2, 3, {'a': 1}]
        """
        if isinstance(other_item, Queue):
            return self.items + other_item.items
        elif isinstance(other_item, list):
            return self.items + other_item
        else:
            return self.items + [other_item]

    def append(self, item):
        """Append an item to the end of the queue.
        """
        self.items += [item]

    def pop(self, index=None):
        """Remove an item at given index from the queue.

        Remove the first item if index is omitted.
        """
        if index is not None:
            del self.items[index]
        else:
            del self.items[0]

    def remove(self, item):
        """Remove the given item from the queue.
        """
        del self.items[self.items.index(item)]

    def contains(self, item):
        """Return True if the given item is within the queue. False otherwise.
        """
        if item in self.items:
            return True
        else:
            return False


if __name__ == "__main__":
    queue = Queue(1, 2, 3)
    queue.append(4)
    print(queue)
    print(queue.contains(1))
    queue.pop()
    print(queue.contains(1))
    print(queue)
