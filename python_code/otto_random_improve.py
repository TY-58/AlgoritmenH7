import random
from cable import Cable
from house import House
import copy
from itertools import combinations

class Otto_cable_route:
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

            if len(cable_route) > 2:
                previous_location = self.check_converge(cable_route)
                if previous_location != []:
                    if previous_location[0] - x_location == 1:
                        directions.remove('r')
                    if previous_location[0] - x_location == -1:
                        directions.remove('l')
                    if previous_location[1] - y_location == 1:
                        directions.remove('u')
                    if previous_location[1] - y_location == -1:
                        directions.remove('d')

            directions_choices = []

            for direct in directions:
                distance = self.get_current_distance(direct, x_location, y_location, end_location)

                directions_choices.append([direct, distance])

            directions_choices.sort(key=lambda a: a[1], reverse=False)
            #print(directions_choices)

            if len(directions_choices) == 0:
                direction = random.choice(self.get_directions(x_location, y_location, end_location))
            if len(directions_choices) == 1:
                direction = directions_choices[0][0]
            if len(directions_choices) == 2:
                direction = random.choices(directions_choices, weights=(95,5), k=1)[0][0]
            if len(directions_choices) == 3:
                direction = random.choices(directions_choices, weights=(85,10,5), k=1)[0][0]
            if len(directions_choices) == 4:
                direction = random.choices(directions_choices, weights=(70,15,10,5), k=1)[0][0]


            if direction == 'd':
                y_location -= 1

            if direction == 'u':
                y_location += 1

            if direction == 'l':
                x_location -= 1

            if direction == 'r':
                x_location += 1

            cable_route.append([x_location, y_location])
            #print(cable_route)

        #self.delete_loops(cable_route)
        #print(cable_route)
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
            #print(count)
            count += 1


    def get_current_distance(self, direction, x_location, y_location, end_location):
        """"return sitance"""

        if direction == 'd':
            y_location -= 1

        if direction == 'u':
            y_location += 1

        if direction == 'l':
            x_location -= 1

        if direction == 'r':
            x_location += 1

        return abs(x_location - end_location[0]) + abs(y_location - end_location[1])


    def check_converge(self, cable_route):
        """Check if algoritm bounces between two options and thus converges."""
        if cable_route[-1] == cable_route[-3]:
            return cable_route[-2]
        else:
            return []

    def delete_loops(self, cable_route):
        """Delete all loops in the route."""
        # duplicate = True
        # i = 0
        # while i < len(cable_route):
        #
        #     while duplicate == True:
        #         duplicate = False
        #         for counter in range(i + 1, len(cable_route)):
        #             print(i, counter)
        #             if cable_route[i] == cable_route[counter]:
        #                 print("hello")
        #                 duplicate = True
        #                 del cable_route[i + 1:counter]
        #                 break
        #
        #     i += 1
        duplicate = True
        while duplicate == True:
            duplicate = False
            for tuple in list(combinations(range(len(cable_route)), 2)):
                if cable_route[tuple[0]] == cable_route[tuple[1]]:
                    duplicate = True
                    del cable_route[tuple[0]+1:tuple[1]]
                    break
