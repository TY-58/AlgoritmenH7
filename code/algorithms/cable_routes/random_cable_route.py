from __future__ import annotations
import random
import copy

from code.classes.cable import Cable

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

        self.grid = grid
        self.configuration = configuration
        self.lay_cables(configuration)


    def make_route(self, house: House, battery: Battery) -> list[list[int, int]]:
        """
        Creates a random route from a house to a battery and returns it
        as a list.
        """

        cable_route = []
        current_location = house.location

        x_location = current_location[0]
        y_location = current_location[1]

        end_location = battery.location

        cable_route.append([x_location, y_location])

        # Keeps moving to a random diretion as long as battery is not found
        while x_location != end_location[0] or y_location != end_location[1]:

            # Gets all possible directions (other batteries than destination not allowed)
            directions = self.get_directions(x_location, y_location, end_location)

            # Makes a random choice and processes choice
            direction = random.choice(directions)
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
        Gets all possible directions from current position.
        Batteries other than the destination battery are not allowed to move over.
        """

        directions = []

        # Makes sure route stays within grid
        if y_location > 0 and (self.grid.grid[y_location-1][x_location] != 2 or [x_location, y_location-1] == end_location):
            directions.append('d')
        if y_location < 50 and (self.grid.grid[y_location+1][x_location] != 2 or [x_location, y_location+1] == end_location):
            directions.append('u')
        if x_location > 0 and (self.grid.grid[y_location][x_location-1] != 2 or [x_location-1, y_location] == end_location):
            directions.append('l')
        if x_location < 50 and (self.grid.grid[y_location][x_location+1] != 2 or [x_location+1, y_location] == end_location):
            directions.append('r')

        return directions


    def lay_cables(self, configuration: list[list[House, Battery]]) -> None:
        """
        A function that lays all the cables from houses to the matched batteries.
        """

        for combination in configuration:
            route = self.make_route(combination[0], combination[1])
            cable = Cable(route)
            self.grid.cables.append(cable)
