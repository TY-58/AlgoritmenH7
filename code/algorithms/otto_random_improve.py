import random
from code.classes.cable import Cable
from code.classes.house import House
import copy
from itertools import combinations

class Otto_cable_route:
    """
    A class for deciding the routes from houses to the matched batteries.
    Routes are decided by an algorithm that sorts possible directions, best option
    first. Some randomness in choosing direction is allowed so the path doesn´t
    get stuck in the grid.
    """

    def __init__(self, grid, configuration):
        """
        Takes grid and configuration as input.
        Lays cables from houses to matched batteries.
        """

        self.grid = grid
        self.configuration = configuration
        self.lay_cables(configuration)


    def make_route(self, house, battery):
        """
        Creates a route from input house to input battery.
        Tries to find quickest route but allows for random choice sometimes to
        ensure that the route doesn't get stuck in a loop.
        """

        cable_route = []
        current_location = house.location

        x_location = current_location[0]
        y_location = current_location[1]

        end_location = battery.location

        cable_route.append([x_location, y_location])

        # Keep adding to the route as long as destination is not yet reached
        while x_location != end_location[0] or y_location != end_location[1]:

            # Get all possible directions from current location
            directions = self.get_directions(x_location, y_location, end_location)

            # Route can never go back, so remove option to go back from directions
            if len(cable_route) > 2:
                if previous_location != []:
                    if previous_location[0] - x_location == 1:
                        directions.remove('r')
                    if previous_location[0] - x_location == -1:
                        directions.remove('l')
                    if previous_location[1] - y_location == 1:
                        directions.remove('u')
                    if previous_location[1] - y_location == -1:
                        directions.remove('d')

            # Create a list of tuples of the direction and the distance to destination
            directions_choices = []
            for direct in directions:
                distance = self.get_current_distance(direct, x_location, y_location, end_location)

                directions_choices.append([direct, distance])

            # Sort directions_choices by the distance to destination, ascending
            directions_choices.sort(key=lambda a: a[1], reverse=False)

            # Depending on how many directions are possible, create a distribution and choose direction
            # If there are none, take a step back to previous location
            if len(directions_choices) == 0:
                direction = random.choice(self.get_directions(x_location, y_location, end_location))
            if len(directions_choices) == 1:
                direction = directions_choices[0][0]
            if len(directions_choices) == 2:
                direction = random.choices(directions_choices, weights=(98,2), k=1)[0][0]
            if len(directions_choices) == 3:
                direction = random.choices(directions_choices, weights=(90,6,4), k=1)[0][0]
            if len(directions_choices) == 4:
                direction = random.choices(directions_choices, weights=(80,10,6,4), k=1)[0][0]

            # Move in chosen direction and append to route
            if direction == 'd':
                y_location -= 1

            if direction == 'u':
                y_location += 1

            if direction == 'l':
                x_location -= 1

            if direction == 'r':
                x_location += 1

            cable_route.append([x_location, y_location])

            # Check for loops in the route and delete them
            self.delete_loops(x_location, y_location, cable_route)

        return cable_route



    def get_directions(self, x_location, y_location, end_location):
        """
        Get all possible directions from current position.
        Batteries other than the destination battery are not allowed to move over.
        """

        directions = []

        if y_location > 0 and (self.grid.grid[y_location-1][x_location] != 2 or [x_location, y_location-1] == end_location):
            directions.append('d')
        if y_location < 50 and (self.grid.grid[y_location+1][x_location] != 2 or [x_location, y_location+1] == end_location):
            directions.append('u')
        if x_location > 0 and (self.grid.grid[y_location][x_location-1] != 2 or [x_location-1, y_location] == end_location):
            directions.append('l')
        if x_location < 50 and (self.grid.grid[y_location][x_location+1] != 2 or [x_location+1, y_location] == end_location):
            directions.append('r')


        return directions


    def get_current_distance(self, direction, x_location, y_location, end_location):
        """
        Get distance to destination, if moved in a given direction from current location.
        """

        # Move in given location
        if direction == 'd':
            y_location -= 1

        if direction == 'u':
            y_location += 1

        if direction == 'l':
            x_location -= 1

        if direction == 'r':
            x_location += 1

        # Return distance to destination from new location
        return abs(x_location - end_location[0]) + abs(y_location - end_location[1])


    def check_converge(self, cable_route):
        """
        Check if algoritm keeps moving between two locations and thus converges.
        """

        if cable_route[-1] == cable_route[-3]:
            return cable_route[-2]
        else:
            return []


    def delete_loops(self, x_location, y_location, cable_route):
        """
        Delete all loops in the route thusfar.
        """

        counter = 0
        
        # Check every location in list
        for location in cable_route:

            # If current location is already in list, delete everything after that first location
            if [x_location, y_location] == location:
                del cable_route[counter+1:len(cable_route)]
                break


    def lay_cables(self, configuration):
        """
        A function that lays all the cables from houses to the matched batteries.
        """

        for combination in configuration:
            route = self.make_route(combination[0], combination[1])
            cable = Cable(route)
            self.grid.cables.append(cable)