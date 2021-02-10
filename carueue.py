# carueue.py by nonetypes
# Last revised on 02/02/2021


def is_permutation(word, test):
    """Determines if the given word is a permutation of the given test word.
    """
    if len(word) != len(test):
        return False
    word = word.lower()
    test = list(test.lower())
    for letter in word:
        if letter in test:
            test.remove(letter)
    if test:
        return False
    else:
        return True


class Carueue:
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

            carueue = Carueue(1, 2, 3)
            carueue + 4               # returns [1, 2, 3, 4]
            carueue + 'string'        # returns [1, 2, 3, 'string']
            carueue + [4, 5]          # returns [1, 2, 3, 4, 5]
            carueue + (4, 5)          # returns [1, 2, 3, (4, 5)]
            carueue + {'a': 1}        # returns [1, 2, 3, {'a': 1}]
        """
        new_queue = Carueue()
        if isinstance(other_item, Carueue):
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

    def find_carmen(self):
        """Determine if Carmen Sandiego is within the queue, and print
        her position if she is.

        Determinations are not case sensitive, will disregard spaces, and will
        consider anagrams and scrambles of carmensandiego.
        """
        i = 0
        for item in self.items:
            if is_permutation(str(item).replace(' ', ''), 'carmensandiego'):
                formatted_index = i
                if formatted_index == 0:
                    formatted_index = '1st'
                elif formatted_index == 1:
                    formatted_index = '2nd'
                elif formatted_index == 2:
                    formatted_index = '3rd'
                else:
                    formatted_index = f'{formatted_index+1}th'
                print(f'Carmen Sandiego is {formatted_index} in line.')
                return
            i += 1
        print('Failed to find Carmen Sandiego...')


if __name__ == "__main__":
    carueue = Carueue(1, 2, 'not carmen sandiego')
    print(carueue)
    carueue.find_carmen()
    carueue.append('Nerd Egomaniacs')
    print(carueue)
    carueue.find_carmen()
    carueue.pop()
    print(carueue)
    carueue.find_carmen()
