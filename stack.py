# stack.py by Alexander Ralston
# Last revised on 14/01/2021
#

class Stack:
    """List like object. Last in, first out.
    Concatenation support between various built-in objects.
    """
    def __init__(self, *items):
        self.items = list(items)

    def __repr__(self):
        """Return a printable (string) version of self.items
        """
        return str(self.items)

    def __getitem__(self, item):
        """Return the index of self.items
        """
        return self.items[item]

    def __add__(self, other_item):
        """Concatenation support.
        """
        if isinstance(other_item, type(self)):
            return self.items + other_item.items
        elif isinstance(other_item, list):
            return self.items + other_item
        else:
            return self.items + [other_item]

    def append(self, item):
        """
        """
        self.items += [item]

    def pop(self, item=None):
        """
        """
        if item:
            del self.items[self.items.index(item)]
        else:
            del self.items[-1]

    def contains(self, item):
        """
        """
        if item in self.items:
            return True
        else:
            return False
