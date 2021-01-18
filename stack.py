# stack.py by nonetypes
# Last revised on 01/14/2021

class Stack:
    """List like object. Last in, first out.
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

            stack = Stack('a', 'b', 'c')
            stack[1]                # returns 'b'
        """
        return self.items[index]

    def __setitem__(self, index, new_item):
        """Item assignment.
        """
        self.items[index] = new_item

    def __add__(self, other_item):
        """
        Concatenation support:

            stack = Stack(1, 2, 3)
            stack + 4               # returns [1, 2, 3, 4]
            stack + 'string'        # returns [1, 2, 3, 'string']
            stack + [4, 5]          # returns [1, 2, 3, 4, 5]
            stack + (4, 5)          # returns [1, 2, 3, (4, 5)]
            stack + {'a': 1}        # returns [1, 2, 3, {'a': 1}]
        """
        if isinstance(other_item, type(self)):
            return self.items + other_item.items
        elif isinstance(other_item, list):
            return self.items + other_item
        else:
            return self.items + [other_item]

    def append(self, item):
        """Append an item to the end of the stack.
        """
        self.items += [item]

    def pop(self, index=None):
        """Remove an item at given index from the stack.

        Remove the last item if index is omitted.
        """
        if index:
            del self.items[index]
        else:
            del self.items[-1]

    def remove(self, item):
        """Remove the given item from the stack.
        """
        del self.items[self.items.index(item)]

    def contains(self, item):
        """Return True if the given item is within the stack. False otherwise.
        """
        if item in self.items:
            return True
        else:
            return False
