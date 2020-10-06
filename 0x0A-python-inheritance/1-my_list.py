#!/usr/bin/python3
"""This module writes a class that inherits from list"""


class MyList(list):
    """A class that inherits from list"""

    def print_sorted(self):
        """Prints the list, but sorted (ascending order)"""

        slist = self[:]
        slist.sort()
        print(slist)
