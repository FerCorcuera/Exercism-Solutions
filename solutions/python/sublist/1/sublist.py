"""
This exercise stub and the test suite contain several enumerated constants.

Enumerated constants can be done with a NAME assigned to an arbitrary,
but unique value. An integer is traditionally used because it’s memory
efficient.
It is a common practice to export both constants and functions that work with
those constants (ex. the constants in the os, subprocess and re modules).

You can learn more here: https://en.wikipedia.org/wiki/Enumerated_type
"""

# Possible sublist categories.
# Change the values as you see fit.
SUBLIST = 1
SUPERLIST = 2
EQUAL = 3
UNEQUAL = 4


def sublist(list_one, list_two):
    len_1 = len(list_one)
    len_2 = len(list_two)
    diff = abs(len_2 - len_1)
    if list_one == list_two:
        return EQUAL
    elif len_1 > len_2:
        for x in range(0,diff + 1):
            if list_one[x:x + len_2] != list_two:
                continue
            else:
                return SUPERLIST
    elif len_2 > len_1:
        for x in range(0,diff + 1):
            if list_two[x:x+len_1] != list_one:
                continue
            else:
                return SUBLIST
    return UNEQUAL