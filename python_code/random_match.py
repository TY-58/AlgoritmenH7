import random
import copy

class Random_configuration:
    """
    A class for a random algorithm to match houses with batteries without
    exceeding maximum capacity of the batteries.
    """

    def __init__(self, input_grid):
        """
        Takes a grid as input.
        Shuffles house list.
        """

        grid_var = copy.copy(input_grid)
        self.grid = grid_var
        self.shuffled_houses = self.shuffle_houses()


    def shuffle_houses(self):
        """
        Function that shuffles the list of houses in a random order.
        """

        random.shuffle(self.grid.houses)
        return self.grid.houses


    def try_configuration(self):
        """
        Function that tries to make a random configuration, assigning
        a randomly chosen house to a randomly chosen battery.
        """

        configuration = []
        for house in self.shuffled_houses:
            battery = random.choice(self.grid.batteries)

            # Try to find a battery with enough capacity
            error_counter = 0

            # Keep choosing battery and see if house fits
            while battery.current_capacity < house.max_output:
                battery = random.choice(self.grid.batteries)
                error_counter += 1

                # If more than 50 tries are needed, there is probably no battery left
                if error_counter > 50:

                    # Reset configuration and return empty list.
                    self.linked_houses = []
                    for battery in self.grid.batteries:
                        battery.current_capacity = float(battery.max_capacity)

                    return []

            # If a battery is found, append it to the configuration
            configuration.append([house, battery])
            battery.current_capacity -= float(house.max_output)

        return configuration


    def make_configuration(self):
        """
        Run try_configuration until a configuration is found.
        Return it if this is the case
        """
        x = []
        error_counter = 0

        while configuration == []:
            configuration = self.try_configuration()

        return configuration
