"""Functions to automate Conda airlines ticketing system."""


def generate_seat_letters(number):
    """Generate a series of letters for airline seats.

    :param number: int - total number of seat letters to be generated.
    :return: generator - generator that yields seat letters.

    Seat letters are generated from A to D.
    After D it should start again with A.

    Example: A, B, C, D

    """
    letters = ['A','B','C','D']
    seats = 0
    for a in range(0,number):
        yield letters[seats]
        seats += 1
        if seats > 3:
            seats = 0

def generate_seats(number):
    """Generate a series of identifiers for airline seats.

    :param number: int - total number of seats to be generated.
    :return: generator - generator that yields seat numbers.

    A seat number consists of the row number and the seat letter.

    There is no row 13.
    Each row has 4 seats.

    Seats should be sorted from low to high.

    Example: 3C, 3D, 4A, 4B

    """
    

    sits = generate_seat_letters(number)
    line = 1
    for a in range(0,number):
        letter = next(sits)
        yield str(line) + letter
        if letter == 'D': line += 1
        if line == 13: line +=1
        
        
        
                

def assign_seats(passengers):
    """Assign seats to passengers.

    :param passengers: list[str] - a list of strings containing names of passengers.
    :return: dict - with the names of the passengers as keys and seat numbers as values.

    Example output: {"Adele": "1A", "Björk": "1B"}

    """
    seat = generate_seats(len(passengers))
    dic = {}
    for x in passengers:
        seat_number = next(seat)
        dic[x] = seat_number
    return dic

def generate_codes(seat_numbers, flight_id):
    """Generate codes for a ticket.

    :param seat_numbers: list[str] - list of seat numbers.
    :param flight_id: str - string containing the flight identifier.
    :return: generator - generator that yields 12 character long ticket codes.

    """

    
    for x in seat_numbers:
        zero = ['0']
        zeros = 12 - len(x) - len(flight_id)
        zero[0] = zero[0]*(zeros)
        ticket_id = x + flight_id + zero[0]
        yield ticket_id
