# queue.py by nonetypes
# Last revised on 01/29/2021

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

    def __len__(self):
        """Return the len() of self.items
        """
        return len(self.items)

    def __getitem__(self, index):
        """
        Return an item from an index:

            queue = Queue('a', 'b', 'c')
            queue[1]                # returns 'b'
        """
        return self.items[index]

    def __setitem__(self, index, new_item):
        """Item assignment.
        """
        self.items[index] = new_item

    def __add__(self, other_item):
        """
        Concatenation support.

            queue = Queue(1, 2, 3)
            queue + 4               # returns [1, 2, 3, 4]
            queue + 'string'        # returns [1, 2, 3, 'string']
            queue + [4, 5]          # returns [1, 2, 3, 4, 5]
            queue + (4, 5)          # returns [1, 2, 3, (4, 5)]
            queue + {'a': 1}        # returns [1, 2, 3, {'a': 1}]
        """
        new_queue = Queue()
        if isinstance(other_item, Queue):
            for item in self.items + other_item.items:
                new_queue.append(item)
        elif isinstance(other_item, list):
            for item in self.items + other_item:
                new_queue.append(item)
        else:
            for item in self.items + [other_item]:
                new_queue.append(item)
        return new_queue

    def append(self, item):
        """Append an item to the end of the queue.
        """
        self.items += [item]

    def pop(self, index=None):
        """Remove an item at given index from the queue and return it.

        Remove the first item if index is omitted.
        """
        if index is not None:
            popped_item = self.items[index]
            del self.items[index]
        else:
            popped_item = self.items[0]
            del self.items[0]
        return popped_item

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
    queue += {'a': 1}
    print(type(queue), queue)
