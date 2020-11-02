""" 
    File: latin_square.py
    
    Descriptions: The program is going to create some examples to test
                  whether the program itself can detect a latin square.
                  This program is a practice on object oriented
                  programming.
"""

def contains_duplicates(a_list):
    """ Return True if there is any duplicate value in a_list.
    For exampls, contains_duplicates([4, 1, 8, 5]) is False, but
    contains_duplicates([4, 1, 8, 1]) is True. """

    assert type(a_list) is list

    duplicate = []

    # Append of all checked item into a list. If the next item is
    # equal to an item that is already in the list, a repitition 
    # has occurred.  
    for item in a_list:
        if item not in duplicate:
            duplicate.append(item)
        else:
            return True
    return False

def has_all_values(required, a_list):
    """ Return True if and only if every value in required appears in a_list.
    For example, has_all_values([3,5,2,1], [1,5,3,8,2]) is True. """

    assert type(required) is list
    assert type(a_list) is list

    # If one of the item of the required list cannot be found in the random
    # list (a_list), then the random list does not have all the required items. 
    # Required items are items from the first row. 
    for item in required:
        if item not in a_list:
            return False
    return True

class Rectangle:
    """ represents a 2D array of numbers """

    def __init__(self, num_rows, num_cols, content):
        """ Initializes this rectangle as having the given number of rows
        and columns, filled with the data from the list
        content, given in row major order. """

        assert type(num_rows) is int
        assert type(num_cols) is int
        assert type(content) is list
        assert num_rows > 0
        assert num_cols > 0
        assert len(content) == num_rows * num_cols

        self._num_rows = num_rows
        self._num_cols = num_cols
        self._content = content
        self._rect = []

        # With given length for column and rows, a for-loops is 
        # used to create a nested list of items. 
        for _ in range(self._num_rows):
            row = content[:self._num_cols]
            self._rect.append(row)
            content = content[self._num_cols:]

    def get_num_rows(self):
        """ return the number of rows"""

        return self._num_rows

    def get_num_cols(self):
        """ return the number of columns"""

        return self._num_cols

    def get_column(self, column_index):
        """ return a list consisting of data from the given column. """

        assert type(column_index) is int
        assert 0 <= column_index and column_index < self.get_num_cols()

        # For each row in the rectangle, put the number 
        # in the requested column into a list
        col_items = []
        for row in self._rect:
            col_items.append(row[column_index])
        return col_items

    def is_square(self):
        """ return True if and only this rectangle is square """

        # Because a square has four equal sides, therefore, a rectangle is
        # a square if its row and its column are equal in length
        if self._num_rows == self._num_cols:
            return True
        return False

    def print1(self):
        """ Display this rectangle on the standard output, in this format:
            {{1, 2, 3},
             {4, 5, 6}}
        """

        output = ""
        items = []

        # Turn all items in the rectangle to strings, 
        # and the store these them into a list to edit. 
        for item in str(self._rect):
            items.append(item)

        # Change the last two squared braces to the curly braces.
        items[-1] = "}"
        items[-2] = "}"

        # For every squared braces in the list (beside the last two braces),
        # change it to curly braces. For each closing braces, add a comma 
        # and new line.
        for i in range(len(items) - 2):
            if items[i] == "[":
                items[i] = "{"
            if items[i] == "]":
                items[i] = "}"
                items[i + 1] = ",\n"

        # Take all the string in the list out
        # and put them into a big string to print.
        for item in items:
            output += item
        print(output)

    def is_latin_square(self):
        """ Return True if this rectangle is a Latin Square, False otherwise.
        A Rectangle of numbers is a Latin Square if and only if all of the
        following:
          * It is square.
          * Its first row contains no duplicates.
          * All of the values of the first row appear in each subsequent row.
          * All of the values of the first row appear in each column.
        """

        # Check if the rectangle is a square
        if self.is_square() is False:
            return False

        # Check if the first row of the rectangle has any duplicates.
        if contains_duplicates(self._rect[0]) is True:
            return False

        # Check if all values of the first row are found in each subsequent row.
        for i in range(1, self._num_rows):
            if has_all_values(self._rect[0], self._rect[i]) is False:
                return False

        # Check if all values of the first row are found in each column.
        for i in range(self._num_cols):
            if has_all_values(self._rect[0], self.get_column(i)) is False:
                return False
        return True

def example():
    """ Latin Squares program testing examples """

    rect1 = Rectangle(2, 3, [1, 2, 3, 4, 5, 6])
    rect1.print1()   # {{1, 2, 3},
                    #  {4, 5, 6}}
    print(rect1.is_square())  # False
    print(rect1.get_column(1))  # [2, 5]

    rect2 = Rectangle(3, 3, [1, 2, 3, 2, 3, 1, 3, 1, 2])
    rect2.print1()
    print(rect2.is_square())  # True
    print(rect2.is_latin_square()) # True

    rect3 = Rectangle(2, 2, [1, 2, 1, 2])
    print(rect3.is_latin_square()) # False

    rect4 = Rectangle(3, 3, [1, 2, 3, 3, 1, 2, 7, 8, 9])
    print(rect4.is_latin_square()) # False

    rect5 = Rectangle(4, 4, [10, 30, 20, 0, 0, 20, 30, 10, 30, 0, 10, 20,
                             20, 10, 0, 30])
    print(rect5.is_latin_square()) # True

def main():
    """ The main program """
    example()

if __name__ == "__main__":
    main()
