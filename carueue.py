# carueue.py by nonetypes
# Last revised on 02/12/2021
# A simple queue with a Carmen Sandiego themed method.

def is_permutation(test, word, case_sensitive=False):
    """Determines if the given test word is a permutation of the given word.

    Not case-sensitive by default.
    """
    # For speed and so that cars will not be determined to be a permutation of car.
    if len(test) != len(word):
        return False
    if not case_sensitive:
        test = test.lower()
        word = word.lower()
    # If an exact match is found, return true to save time.
    if test == word:
        return True
    word = list(word)
    # Remove letters from word as they are matched from test.
    for letter in test:
        if letter in word:
            word.remove(letter)
    if word:
        return False
    # word is empty: All letters were matched -- permutation confirmed.
    else:
        return True


class Carueue:
    """Queue. First in, first out.

    Specially designed for determining if Carmen Sandiego is within the queue.
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
        """Determine if Carmen Sandiego is within the queue and print
        her position if she is.

        Determinations are not case sensitive, will disregard spaces, and will
        consider anagrams and scrambles of carmensandiego.

        If multiple Carmen Sandiegos exist in the list, the first one found
        is considered the real one -- the rest are assumed to be imposters.
        """
        i = 0
        for item in self.items:
            item = str(item).lower().replace(' ', '')
            if is_permutation(item, 'carmensandiego'):
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
    carueue = Carueue(1, 2, 'Not Carmen Sandiego')
    print(carueue)
    carueue.find_carmen()
    carueue.append('Nerd Egomaniacs')
    print(carueue)
    carueue.find_carmen()
    carueue.pop()
    print(carueue)
    carueue.find_carmen()

    # Time complexity of find_carmen():
    #
    # Version 1:
    # Permutations are not considered. An exact match was found at the end of the list.
    # Approach: 1, 2, and 4 million items are appended to a carueue,
    # followed by 'Carmen Sandiego'. carueue.find_carmen() is timed for each.
    # 1,000,000: ~ .28 seconds
    # 2,000,000: ~ .56 seconds
    # 4,000,000: ~ 1.1 seconds
    # Complexity: O(n)
    #
    # Version 2:
    # Permutations are considered and a match is found at the end of the list.
    # Approach: 'aaaaaaaaaaaaaa' is appended to a carueue 1, 2, and 4 million times,
    # followed by an anagram of Carmen Sandiego. carueue.find_carmen() is timed for each.
    # 'aaaaaaaaaaaaaa' is 14 characters long and therefore a letter by letter comparison
    # will be initiated for every item in the list to determine if it is a permutation.
    # 1,000,000: ~ 4 seconds
    # 2,000,000: ~ 8 seconds
    # 4,000,000: ~ 16 seconds
    # Complexity: O(n)
    #
    # Complexity in both cases is linear, i.e.
    # Time increases linearly with the size of the list.
