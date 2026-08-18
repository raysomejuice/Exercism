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
    seats_per_row = 4
    for counter in range(number):
        yield chr(ord('A') + counter % seats_per_row)


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
    row_counter = 1
    seats_per_row = 4
    letter = generate_seat_letters(number)
    
    for seat_counter in range(number):
        yield str(row_counter) + next(letter)
        if seat_counter % seats_per_row == seats_per_row - 1:
            row_counter += 1
        if row_counter == 13:
            row_counter += 1


def assign_seats(passengers: list[str]) -> dict[str, str]:
    """Assign seats to passengers.

    :param passengers: list[str] - a list of strings containing names of passengers.
    :return: dict - with the names of the passengers as keys and seat numbers as values.

    Example output: {"Adele": "1A", "Björk": "1B"}

    """
    seat_number = generate_seats(len(passengers))
    return dict(zip(passengers, seat_number))

def generate_codes(seat_numbers: list[str], flight_id: str) -> Generator[str, None, None]:
    """Generate codes for a ticket.

    :param seat_numbers: list[str] - list of seat numbers.
    :param flight_id: str - string containing the flight identifier.
    :return: generator - generator that yields 12 character long ticket codes.

    """
    for seat in seat_numbers:
        ticket_number = seat + flight_id
        yield ticket_number.ljust(12, '0')
