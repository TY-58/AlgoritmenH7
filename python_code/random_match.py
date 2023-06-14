import random
import copy

class Random_configuration:
    """ A Class for Random algorithm to match houses with batteries without exceeding max capacity. """

    def __init__(self, input_grid):
        """."""
        grid_var = copy.copy(input_grid)
        self.grid = grid_var
        self.shuffled_houses = self.randomize_houses()

    def randomize_houses(self):
        """."""
        random.shuffle(self.grid.houses)
        return self.grid.houses

    def try_configuration(self):
        """."""
        configuration = []
        for house in self.shuffled_houses:
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

        while x == [] and error_counter < 1000:
            x = self.try_configuration()
            error_counter += 1

        return x
