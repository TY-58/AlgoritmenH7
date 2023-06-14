import random
from cable import Cable
from house import House
import copy

class Random_cable_route:
    """Lay random cable"""

    def __init__(self, grid, configuration):
        """."""

        self.grid = grid
        self.configuration = configuration
        self.lay_cables(configuration)


    def make_route(self, house, battery):
        """Start route from a house to battery."""


        cable_route = []
        current_location = house.location

        x_location = current_location[0]
        y_location = current_location[1]

        end_location = battery.location

        cable_route.append([x_location, y_location])

        while x_location != end_location[0] or y_location != end_location[1]:

            directions = self.get_directions(x_location, y_location, end_location)
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

    #make route
    def get_directions(self, x_location, y_location, end_location):
        """Get all possible directions from current position"""
        directions = []

        if y_location > 0 and (self.grid.grid[y_location-1][x_location] == 0 or [x_location, y_location-1] == end_location):
            directions.append('d')
        if y_location < 50 and (self.grid.grid[y_location+1][x_location] == 0 or [x_location, y_location+1] == end_location):
            directions.append('u')
        if x_location > 0 and (self.grid.grid[y_location][x_location-1] == 0 or [x_location-1, y_location] == end_location):
            directions.append('l')
        if x_location < 50 and (self.grid.grid[y_location][x_location+1] == 0 or [x_location+1, y_location] == end_location):
            directions.append('r')


        return directions


    def lay_cables(self, configuration):
        """."""
        count = 0
        for combination in configuration:
            route = self.make_route(combination[0], combination[1])
            cable = Cable(route)
            self.grid.cables.append(cable)
            count += 1
