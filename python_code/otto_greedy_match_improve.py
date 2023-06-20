from operator import itemgetter
from helper import function_sort_output
import random
import copy

# class Otto_greedy_configuration:
#     """ Class for Greedy algorithm to match houses with batteries without exceeding max capacity. """
#
#     def __init__(self, input_grid):
#         """."""
#         grid_var = copy.copy(input_grid)
#         self.grid = grid_var
#         self.sorted_houses = self.sort_houses()
#
#     def sort_houses(self):
#         """."""
#         return sorted(self.grid.houses, key=lambda x: x.max_output, reverse=True)
#
#     def try_configuration(self):
#         """."""
#         configuration = []
#         for house in self.sorted_houses:
#             battery = random.choice(self.grid.batteries)
#             error_counter = 0
#
#             while battery.current_capacity < house.max_output:
#                 battery = random.choice(self.grid.batteries)
#                 error_counter += 1
#
#                 if error_counter > 50:
#                     self.linked_houses = []
#                     return []
#
#             configuration.append([house, battery])
#             battery.current_capacity -= float(house.max_output)
#
#         sum = 0
#         for battery in self.grid.batteries:
#             sum += battery.current_capacity
#         return configuration
#
#
#     def make_configuration(self):
#         """."""
#         x = []
#         error_counter = 0
#
#         while x == [] and error_counter < 100000000:
#             x = self.try_configuration()
#             error_counter += 1
#
#         return x

class Otto_greedy_configuration:
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
            batteries_sorted = []
            for bat in self.grid.batteries:
                batteries_sorted.append([bat, self.distance_to_battery(house, bat)])

            batteries_sorted.sort(key=lambda a: a[1], reverse=False)

            battery = random.choices(batteries_sorted, weights=(90, 4, 3,2,1), k=1)[0][0]
            error_counter = 0

            while float(battery.current_capacity) < house.max_output:
                battery = random.choices(batteries_sorted, weights=(0, 90,5,3,2), k=1)[0][0]
                error_counter += 1

                if error_counter > 200:
                    self.linked_houses = []
                    for battery in self.grid.batteries:
                        battery.current_capacity = float(battery.max_capacity)
                    return []

            configuration.append([house, battery])
            battery.current_capacity -= float(house.max_output)

        return configuration


    def make_configuration(self):
        """."""
        x = []
        error_counter = 0

        while x == [] and error_counter < 100000000:
            x = self.try_configuration()
            error_counter += 1

        return x

    def distance_to_battery(self, house, battery):
        return abs(house.location[0]- battery.location[0]) + abs(house.location[1] - battery.location[1])


    def process_configuration(self, configuration):
        """f"""
        for battery in self.grid.batteries:
            for house in self.grid.houses:
                if [house, battery] in configuration:
                    battery.house_connections.append(house)
