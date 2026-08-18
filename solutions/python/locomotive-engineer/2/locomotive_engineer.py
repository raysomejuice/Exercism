"""Functions which helps the locomotive engineer to keep track of the train."""
from typing import Union

def get_list_of_wagons(*wagon_ids: int) -> list[int]:
    """Return a list of wagons.

    :param: arbitrary number of wagons.
    :return: list - list of wagons.
    """
    return [*wagon_ids]


def fix_list_of_wagons(each_wagons_id: list[int], missing_wagons: [int]) -> list[int]:
    """Fix the list of wagons.

    :param each_wagons_id: list - the list of wagons.
    :param missing_wagons: list - the list of missing wagons.
    :return: list - list of wagons.
    """
    wagon_one, wagon_two, loco, *remaining = each_wagons_id
    return [loco, *missing_wagons, *remaining, wagon_one, wagon_two]


def add_missing_stops(route: dict[str, str], **stop_number: str) -> dict[str, Union[str, list[str]]]:
    """Add missing stops to route dict.

    :param route: dict - the dict of routing information.
    :param: arbitrary number of stops.
    :return: dict - updated route dictionary.
    """
    stops: dict[str, list[str]] = {'stops': [*stop_number.values()]}
    return {**route, **stops}



def extend_route_information(route: dict[str, str], more_route_information: dict[str, str]):
    """Extend route information with more_route_information.

    :param route: dict - the route information.
    :param more_route_information: dict -  extra route information.
    :return: dict - extended route information.
    """
    return {**route, **more_route_information}


def fix_wagon_depot(wagons_rows: list[list[tuple[int, str]]]) -> list[list[tuple[int, str]]]:
    """Fix the list of rows of wagons.

    :param wagons_rows: list[list[tuple]] - the list of rows of wagons.
    :return: list[list[tuple]] - list of rows of wagons.
    """
    row_one, row_two, row_three = zip(*wagons_rows)
    return [list(row_one), list(row_two), list(row_three)]

