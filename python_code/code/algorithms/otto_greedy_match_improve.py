from operator import itemgetter
import random
import copy

class Otto_greedy_configuration:
    """
    Class for Greedy algorithm to match houses with batteries without exceeding max capacity.
    Matches every house to closest battery, starting with houses with the biggest capacity.
    Allows for a bit of randomness in choosing the closest battery for a house.
    """


    def __init__(self, input_grid):
        """
        Takes a grid as input.
        Sorts houses by max_output (descending).
        """

        grid_var = copy.copy(input_grid)
        self.grid = grid_var
        self.sorted_houses = self.sort_houses()


    def sort_houses(self):
        """
        Sort houses by max_output (descending).
        """

        return sorted(self.grid.houses, key=lambda x: x.max_output, reverse=True)

    def sort_batteries(self, house):
        """
        Sorts batteries by distance, closest to input house first.
        """

        batteries_sorted = []

        for bat in self.grid.batteries:
            batteries_sorted.append([bat, self.distance_to_battery(house, bat)])

        batteries_sorted.sort(key=lambda a: a[1], reverse=False)

        return batteries_sorted


    def try_configuration(self):
        """
        Start matching houses (in order) to closest batteries.
        If configuration fails (no legit option possible), return empty list.
        Else, return configuration as list with items [house, battery].
        """

        configuration = []

        for house in self.sorted_houses:

            batteries_sorted = self.sort_batteries(house)

            # Give a margin to make a suboptimal choice when choosing a battery to connect to
            battery = random.choices(batteries_sorted, weights=(90, 4, 3,2,1), k=1)[0][0]

            # Keep choosing until a battery with enough capacity is found
            error_counter = 0
            while float(battery.current_capacity) < house.max_output:
                battery = random.choices(batteries_sorted, weights=(0, 90,5,3,2), k=1)[0][0]
                error_counter += 1

                # If battery is not found after a 100 times, no battery has capacity left
                if error_counter > 100:

                    # Reset configuration and return empty list
                    self.linked_houses = []
                    for battery in self.grid.batteries:
                        battery.current_capacity = float(battery.max_capacity)
                    return []

            # If a battery is found, add tuple to the configuration and adjust capacity
            configuration.append([house, battery])
            battery.current_capacity -= float(house.max_output)

        return configuration


    def make_configuration(self):
        """
        Run try_configuration until a configuration is found.
        Return it if this is the case
        """
        configuration = []

        while configuration == []:
            configuration = self.try_configuration()

        return configuration


    def distance_to_battery(self, house, battery):
        """
        Return (Manhattan) distance between house and battery.
        """
        return abs(house.location[0]- battery.location[0]) + abs(house.location[1] - battery.location[1])


    def process_configuration(self, configuration):
        """
        Add all houses to the house_connections of the batteries that they've matched with.
        """
        for battery in self.grid.batteries:
            for house in self.grid.houses:
                if [house, battery] in configuration:
                    battery.house_connections.append(house)
