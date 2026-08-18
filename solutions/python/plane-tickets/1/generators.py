"""Functions to automate Conda airlines ticketing system."""

from typing import Generator


def generate_seat_letters(number: int) -> Generator[str, None, None]:
    """Generate a series of letters for airline seats.

    :param number: int - total number of seat letters to be generated.
    :return: generator - generator that yields seat letters.

    Seat letters are generated from A to D.
    After D it should start again with A.

    Example: A, B, C, D

    """
    counter = 0
    while counter < number:
        yield chr(ord('A') + counter % 4)
        counter += 1

def generate_seats(number: int) -> Generator[str, None, None]:
    """Generate a series of identifiers for airline seats.

    :param number: int - total number of seats to be generated.
    :return: generator - generator that yields seat numbers.

    A seat number consists of the row number and the seat letter.

    There is no row 13.
    Each row has 4 seats.

    Seats should be sorted from low to high.

    Example: 3C, 3D, 4A, 4B

    """
    seat_counter = 0
    row_counter = 1
    letter = generate_seat_letters(number)
    
    while seat_counter < number:
        yield str(row_counter) + next(letter)
        seat_counter += 1
        if seat_counter % 4 == 0:
            row_counter += 1
        if row_counter == 13:
            row_counter += 1

def assign_seats(passengers: list[str]) -> dict[str, str]:
    """Assign seats to passengers.

    :param passengers: list[str] - a list of strings containing names of passengers.
    :return: dict - with the names of the passengers as keys and seat numbers as values.

    Example output: {"Adele": "1A", "Björk": "1B"}

    """
    seated_passengers = {}
    seat_number = generate_seats(len(passengers))
    
    for passenger in passengers:
        seated_passengers[passenger] = next(seat_number)

    return seated_passengers

def generate_codes(seat_numbers: list[str], flight_id: str) -> Generator[str, None, None]:
    """Generate codes for a ticket.

    :param seat_numbers: list[str] - list of seat numbers.
    :param flight_id: str - string containing the flight identifier.
    :return: generator - generator that yields 12 character long ticket codes.

    """
    for seat in seat_numbers:
        ticket_number: str = seat + flight_id
        yield ticket_number + '0' * (12 - len(ticket_number))
