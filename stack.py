# stack.py by nonetypes
# Last revised on 01/14/2021
#

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

    def __getitem__(self, item):
        """Return the index of self.items
        """
        return self.items[item]

    def __add__(self, other_item):
        """
        Concatenation support:

            stack = Stack(1, 2, 3)
            stack + 4 -> [1, 2, 3, 4]
            stack + 'string' -> [1, 2, 3, 'string']
            stack + [4, 5] -> [1, 2, 3, 4, 5]
            stack + (4, 5) -> [1, 2, 3, (4, 5)]
            stack + {'a': 1} -> [1, 2, 3, {'a': 1}]
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

    def pop(self, item=None):
        """Remove the given item from the stack.

        Remove the last item if item is omitted.
        """
        if item:
            del self.items[self.items.index(item)]
        else:
            del self.items[-1]

    def contains(self, item):
        """Return True if the given item is within the stack. False otherwise.
        """
        if item in self.items:
            return True
        else:
            return False
