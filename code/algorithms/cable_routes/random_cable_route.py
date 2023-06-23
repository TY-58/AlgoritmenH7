from __future__ import annotations
import random
import copy

from code.classes.cable import Cable
from code.classes.house import House

class Random_cable_route:
    """
    A class for deciding the routes from houses to the matched batteries.
    The path every route takes is random.
    """

    def __init__(self, grid: Grid, configuration: list[list[House, Battery]]):
        """
        Takes grid and configuration as input.
        Lays cables from houses to matched batteries.
        """

        self.grid: Grid = grid
        self.configuration: list[list[House, Battery]] = configuration
        self.lay_cables(configuration)


    def make_route(self, house: House, battery: Battery) -> list[list[int, int]]:
        """
        Creates a random route from a house to a battery and returns it
        as a list.
        """

        cable_route: list[list[int, int]] = []
        current_location: list[int, int] = house.location

        x_location: int = current_location[0]
        y_location: int  = current_location[1]

        end_location: list[int, int] = battery.location

        cable_route.append([x_location, y_location])

        # Keep moving to a random diretion as long as battery is not found
        while x_location != end_location[0] or y_location != end_location[1]:

            # Get all possible directions (other batteries than destination not allowed)
            directions: list[str] = self.get_directions(x_location, y_location, end_location)

            # Make a random choice and process choice
            direction: str = random.choice(directions)
            if direction == 'd':
                y_location -= 1

            if direction == 'u':
                y_location += 1

            if direction == 'l':
                x_location -= 1

            if direction == 'r':
                x_location += 1

            cable_route.append([x_location, y_location])

        return cable_route


    def get_directions(self, x_location: int, y_location: int, end_location: list[int, int]) -> list[str]:
        """
        Get all possible directions from current position.
        Batteries other than the destination battery are not allowed to move over.
        """
        directions: list[str] = []

        # Make sure route stays within the grid
        if y_location > 0 and (self.grid.grid[y_location-1][x_location] != 2 or [x_location, y_location-1] == end_location):
            directions.append('d')
        if y_location < 50 and (self.grid.grid[y_location+1][x_location] != 2 or [x_location, y_location+1] == end_location):
            directions.append('u')
        if x_location > 0 and (self.grid.grid[y_location][x_location-1] != 2 or [x_location-1, y_location] == end_location):
            directions.append('l')
        if x_location < 50 and (self.grid.grid[y_location][x_location+1] != 2 or [x_location+1, y_location] == end_location):
            directions.append('r')

        return directions


    def lay_cables(self, configuration: list[list[House, Battery]]):
        """
        A function that lays all the cables from houses to the matched batteries.
        """
        for combination in configuration:
            route: list[list[int, int]] = self.make_route(combination[0], combination[1])
            cable: Cable = Cable(route)
            self.grid.cables.append(cable)
