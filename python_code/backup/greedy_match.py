from operator import itemgetter
from helper import function_sort_output
import random
import copy

class Greedy_configuration:
    """ Class for Greedy algorithm to match houses with batteries without exceeding max capacity. """

    def __init__(self, input_grid):
        """."""
        grid_var = copy.copy(input_grid)
        self.grid = grid_var
        self.sorted_houses = self.sort_houses()

    def sort_houses(self):
        """."""
        return sorted(self.grid.houses, key=lambda x: x.max_output, reverse=True)

    def try_configuration(self):
        """."""
        configuration = []
        for house in self.sorted_houses:
            battery = random.choice(self.grid.batteries)
            error_counter = 0

            while battery.current_capacity < house.max_output:
                battery = random.choice(self.grid.batteries)
                error_counter += 1

                if error_counter > 50:
                    self.linked_houses = []
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

        while x == [] and error_counter < 100000000:
            x = self.try_configuration()
            error_counter += 1

        return x
