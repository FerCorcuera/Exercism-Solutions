def square_of_sum(number):
    suma = 0
    for x in range(0,number):
        suma = suma + (x + 1)

    return suma ** 2

def sum_of_squares(number):

    squares = 0

    for x in range(0,number):
        squares = squares + (x+1)**2

    return squares


def difference_of_squares(number):

    return square_of_sum(number) - sum_of_squares(number)
