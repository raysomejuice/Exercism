"""Solution to Ellen's Alien Game exercise."""


class Alien:
    """Create an Alien object with location x_coordinate and y_coordinate.

    Attributes
    ----------
    (class)total_aliens_created: int
    x_coordinate: int - Position on the x-axis.
    y_coordinate: int - Position on the y-axis.
    health: int - Number of health points.

    Methods
    -------
    hit(): Decrement Alien health by one point.
    is_alive(): Return a boolean for if Alien is alive (if health is > 0).
    teleport(new_x_coordinate, new_y_coordinate): Move Alien object to new coordinates.
    collision_detection(other): Implementation TBD.
    """
    health = 3
    total_aliens_created = 0

    def __init__(self, x_position: int, y_position: int) -> None:
        self.x_coordinate = x_position
        self.y_coordinate = y_position
        Alien.total_aliens_created += 1

    def hit(self) -> None:
        if self.health > 0:
            self.health -= 1

    def is_alive(self) -> bool:
        return self.health > 0

    def teleport(self, new_x_coordinate: int, new_y_coordinate: int) -> None:
        self.x_coordinate = new_x_coordinate
        self.y_coordinate = new_y_coordinate

    def collision_detection(self, other_object):
        """Detects if an alien has been hit.

        :param other_object: Has not been decided what this object will be. Possible what is hitting the alien.
        :return unknown
        """
        pass


def new_aliens_collection(alien_start_positions: list[tuple[int, int]]) -> list[Alien]:
    return [Alien(x_value, y_value) for x_value, y_value in alien_start_positions]
    