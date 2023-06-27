from __future__ import annotations
from operator import itemgetter
import random
import copy

class Greedy_configuration:
    """
    Class for Greedy algorithm to match houses with batteries without exceeding max capacity.
    Matches every house to closest battery, starting with houses with the biggest capacity.
    Allows for a bit of randomness in choosing the closest battery for a house.
    """


    def __init__(self, input_grid: Grid):
        """
        Takes a grid as input.
        Sorts houses by max_output (descending).
        """

        grid_var: Grid = copy.copy(input_grid)
        self.grid: Grid = grid_var
        self.sorted_houses: list[House] = self.sort_houses()
        self.configuration: list[list[House, Battery]] = []


    def sort_houses(self) -> list[House]:
        """
        Sorts houses by max_output (descending).
        """

        random.shuffle(self.grid.houses)
        return self.grid.houses


    def sort_batteries(self, house: House) -> list[list[Battery, int]]:
        """
        Sorts batteries by distance, closest to input house first.
        """

        batteries_sorted: list[list[Battery, int]] = []

        for bat in self.grid.batteries:
            batteries_sorted.append([bat, self.distance_to_battery(house, bat)])

        batteries_sorted.sort(key=lambda a: a[1], reverse=False)

        return batteries_sorted


    def try_configuration(self) -> list[list[House, Battery]]:
        """
        Starts matching houses (in order) to closest batteries.
        If configuration fails (no legit option possible), returns empty list.
        Else, returns configuration as list with items [house, battery].
        """

        # Creates temporary configuration.
        temp_configuration: list[list[House, Battery]] = []

        for house in self.sorted_houses:

            batteries_sorted: list[list[Battery, int]] = self.sort_batteries(house)

            # Gives a margin to make a suboptimal choice when choosing a battery to connect to.
            battery: Battery = random.choices(batteries_sorted, weights=(90, 4, 3,2,1), k=1)[0][0]

            # Keeps choosing until a battery with enough capacity is found.
            error_counter: int = 0
            while float(battery.current_capacity) < house.max_output:
                battery: Battery = random.choices(batteries_sorted, weights=(0, 90,5,3,2), k=1)[0][0]
                error_counter += 1

                # If battery is not found after 50 times, probably no battery has capacity left.
                if error_counter > 50:

                    # Resets configuration and return empty list
                    self.linked_houses: list[House] = []
                    self.configuration: list[list[House, Battery]] = []
                    for battery in self.grid.batteries:
                        battery.current_capacity: float = float(battery.max_capacity)

                    return []

            # If a battery is found, adds tuple to the configuration and adjust capacity.
            temp_configuration.append([house, battery])
            battery.current_capacity -= float(house.max_output)

        self.configuration: list[list[House, Battery]] = temp_configuration

        return temp_configuration


    def make_configuration(self) -> list[list[House, Battery]]:
        """
        Runs try_configuration until a configuration is found.
        Returns found configuration.
        """

        self.configuration: list[list[House, Battery]] = []

        while self.configuration == []:
            self.try_configuration()

        return self.configuration


    def distance_to_battery(self, house: House, battery: Battery) -> int:
        """
        Returns (Manhattan) distance between house and battery.
        """

        return abs(house.location[0]- battery.location[0]) + abs(house.location[1] - battery.location[1])


    def process_configuration(self, configuration: list[list[House, Battery]]):
        """
        Adds all houses to the house_connections of the batteries that they've matched with.
        """

        for battery in self.grid.batteries:
            for house in self.grid.houses:
                if [house, battery] in configuration:
                    battery.house_connections.append(house)
