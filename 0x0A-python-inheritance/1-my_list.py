#!/usr/bin/python3
"""a class MyList that inherits from list"""


class MyList(list):
    """
    Mylist that inherits list class
    print_sorted() - prints list in ascending order(sorted)
    """
    def print_sorted(self):
        """
        prints the sorted list
        """
        print(sorted(self))
