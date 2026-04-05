"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""


#TODO: define the 'EXPECTED_BAKE_TIME' constant below.

EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2

#TODO: Remove 'pass' and complete the 'bake_time_remaining()' function below.
def bake_time_remaining(time):
    """Calculate the bake time remaining.

    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """
    awnser = EXPECTED_BAKE_TIME - time
    return awnser
    


#TODO: Define the 'preparation_time_in_minutes()' function below.
# You might also consider defining a 'PREPARATION_TIME' constant.
# You can do that on the line below the 'EXPECTED_BAKE_TIME' constant.
# This will make it easier to do calculations.

def preparation_time_in_minutes(number_of_layers):
    """ this function take the number of layers that you will prepare for the lasagna
    and will return how much time it will take to prepare it"""
    prep_time = number_of_layers * PREPARATION_TIME
    return prep_time

#TODO: define the 'elapsed_time_in_minutes()' function below.

def elapsed_time_in_minutes(number_of_layers,elapsed_bake_time):
    """ this function will tell you how much time in total will take to prepare the lasagna"""
    prep_time = preparation_time_in_minutes(number_of_layers)
    awnser = prep_time + elapsed_bake_time
    return awnser

# TODO: Remember to go back and add docstrings to all your functions


#  (you can copy and then alter the one from bake_time_remaining.)
