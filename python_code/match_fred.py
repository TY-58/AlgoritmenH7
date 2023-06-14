import random
import copy

class Fred_configuration:
    """ A Class for Random algorithm to match houses with batteries without exceeding max capacity. """

    def __init__(self, input_grid):
        """."""
        self.input_grid = input_grid
        self.grid = []
        self.make_grid_copy()
        self.houses = self.grid.houses
        #print(self.houses)

    def make_grid_copy(self):
        self.grid = copy.copy(self.input_grid)

    def try_configuration(self):
        """."""
        configuration = []

        for house in self.houses:
            battery = random.choice(self.grid.batteries)

            count = 0
            while battery.current_capacity < house.max_output:
                battery = (self.grid.batteries[count])
                count += 1
                if count == len(self.grid.batteries):
                    self.make_grid_copy()
                    return []

            configuration.append([house, battery])
            battery.current_capacity -= float(house.max_output)

        sum = 0
        for battery in self.grid.batteries:
            sum += battery.current_capacity

        return configuration

    def make_configuration(self):
        """."""
        x = []
        error_counter = 0

        while x == [] and error_counter < 10000:
            x = self.try_configuration()
            error_counter += 1

        return x

#if house is left, switch with houses with lower output where possible
