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
    health: int = 3
    total_aliens_created: int = 0

    def __init__(self, x_position: int, y_position: int) -> None:
        self.x_coordinate: int = x_position
        self.y_coordinate: int = y_position
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
        pass

#TODO:  create the new_aliens_collection() function below to call your Alien class with a list of coordinates.
def new_aliens_collection(alien_start_positions: list[tuple[int, int]]) -> list[Alien]:
    created_aliens: list[tuple[int, int]] = []
    for alien in alien_start_positions:
        created_aliens.append(Alien(alien[0], alien[1]))

    return created_aliens