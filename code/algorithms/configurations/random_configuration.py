from __future__ import annotations
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

        grid_var: Grid = copy.copy(input_grid)
        self.grid: Grid = grid_var
        self.shuffled_houses: list[House] = self.shuffle_houses()
        self.configuration: list[list[House, Battery]] = []


    def shuffle_houses(self) -> list[House]:
        """
        Function that shuffles the list of houses in a random order.
        """

        random.shuffle(self.grid.houses)
        return self.grid.houses


    def try_configuration(self) -> list[list[House, Battery]]:
        """
        Function that tries to make a random configuration, assigning
        a randomly chosen house to a randomly chosen battery.
        """

        configuration: list[list[House, Battery]] = []
        for house in self.shuffled_houses:
            battery: Battery = random.choice(self.grid.batteries)

            # Tries to find a battery with enough capacity
            error_counter: int = 0

            # Keeps choosing battery and see if house fits
            while battery.current_capacity < house.max_output:
                battery: Battery = random.choice(self.grid.batteries)
                error_counter += 1

                # If more than 50 tries are needed, there is probably no battery left
                if error_counter > 50:

                    # Resets configuration and return empty list
                    self.linked_houses: list[House] = []
                    self.configuration: list[list[House, Battery]] = []
                    for battery in self.grid.batteries:
                        battery.current_capacity: float = float(battery.max_capacity)

                    return []

            # If a battery is found, appends it to the configuration
            configuration.append([house, battery])
            battery.current_capacity -= float(house.max_output)

        self.configuration: list[list[House, Battery]] = configuration
        return configuration


    def make_configuration(self) -> list[list[House, Battery]]:
        """
        Runs try_configuration until a configuration is found.
        Returns the found configuration.
        """

        configuration: list[list[House, Battery]] = []

        while configuration == []:
            configuration = self.try_configuration()

        return configuration


    def process_configuration(self, configuration: list[list[House, Battery]]):
        """
        Adds all houses to the house_connections of the batteries that they're matched with.
        """

        for battery in self.grid.batteries:
            for house in self.grid.houses:
                if [house, battery] in configuration:
                    battery.house_connections.append(house)
