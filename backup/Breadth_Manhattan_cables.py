from code.classes.cable import Cable
from code.classes.house import House
from code.classes.grid import Grid

class Breadth_manhattan_cables:
    """A class for deciding the route for the cables from a house to a battery.
    It looks at all options it could go at every step (breadth first like) but
    only looks at a breadth further if that stap has to shortest distance from
    the house to the battery """

    def __init__(self, grid, configuration):
        """ Takes grid and a matching configuration as input
        lays cables from the matched houses to the batteries"""

        self.grid = grid
        self.configuration = configuration
        self.lay_cables(configuration)

    def make_route(self, house, battery):
        """ Makes a route based on the shortes distance from start location till end location,
        Every time it has selected the shortest distance to the battery, the new location will be 
        add to the path, and when the distance is 0 it means it has reached the battery"""

        cable_route = []
        start_location = house.location
        end_location = battery.location

        # list with start location, next location which is the start at first and distance to battery
        queue = [(start_location, [start_location], 0)]

        # Max number of tries
        max_locations = 150
        num_locations = 0

        # Start of the queue, with every new location the pop function will update the newest path and distance
        while queue and num_locations < max_locations:
            (location, path, _) = queue.pop(0)
            num_locations += 1

            # Check for every direction what the shortesest distance is by sorting for distance
            directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            for direction_x, direction_y in directions:
                new_location = (location[0] + direction_x, location[1] + direction_y)

                # Checks whehter the next step is within the grid and is not a battery and append new location if not
                if (0 <= new_location[0] < self.grid.size and
                    0 <= new_location[1] < self.grid.size and
                    new_location not in path and self.grid.grid[new_location[1]][new_location[0]] != '2'):
                        distance = abs(new_location[0] - end_location[0]) + abs(new_location[1] - end_location[1])
                        if distance == 0:
                            return path + [new_location]
                        queue.append((new_location, path + [new_location], distance))
            queue.sort(key=lambda x: x[2])

        return cable_route


    def lay_cables(self, configuration):
        """ This function lays all the cables from houses to batteries that are matched to each other"""
        count = 0
        for combination in configuration:
            route = self.make_route(combination[0], combination[1])
            cable = Cable(route)
            self.grid.cables.append(cable)
            count += 1



