from operator import itemgetter
import random
import copy

class Fred_configuration:
    """ Class for Greedy algorithm to match houses with batteries without exceeding max capacity. """

    def __init__(self, input_grid):
        """."""
        grid_var = copy.copy(input_grid)
        self.grid = grid_var
        self.sorted_houses = self.sort_houses()
        self.configuration = []

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
                    self.configuration = []
                    for battery in self.grid.batteries:
                        battery.current_capacity = float(battery.max_capacity)
                    return []

            configuration.append([house, battery])
            battery.current_capacity -= float(house.max_output)

        self.configuration = configuration
        return configuration


    def make_configuration(self):
        """."""
        self.configuration = []
        error_counter = 0

        while self.configuration == [] and error_counter < 100000000:
            self.try_configuration()
            error_counter += 1

        return self.configuration

    def distance_to_battery(self, house, battery):
        return abs(house.location[0]- battery.location[0]) + abs(house.location[1] - battery.location[1])


    def process_configuration(self, configuration):
        """f"""
        for battery in self.grid.batteries:
            for house in self.grid.houses:
                if [house, battery] in configuration:
                    battery.house_connections.append(house)



















# import random
# import copy

# class Fred_configuration:
#     """ A Class for Random algorithm to match houses with batteries without exceeding max capacity. """

#     def __init__(self, input_grid):
#         """."""
#         grid_var = copy.copy(input_grid)
#         self.grid = grid_var
#         self.batteries = input_grid.batteries
#         self.houses = input_grid.houses
#         self.configuration = []

#     def reset_values(self):
#         self.batteries = self.grid.batteries
#         self.houses = self.grid.houses
#         self.configuration = []

#     def print_evry(self):
#         for house in self.houses:
#             print(house)

#     def try_configuration(self):
#         """."""
#         self.reset_values()
#         #print("houses: ", self.houses)
#         #print("batteries: ", self.batteries)
#         for house in self.houses:
#             battery = random.choice(self.batteries)
#             error_counter = 0

#             while battery.current_capacity < house.max_output:
#                 battery = random.choice(self.batteries)
#                 print("battery: ", battery)
#                 error_counter += 1

#                 if error_counter > 50:

#                     self.reset_values()
#                     print(self.configuration)
#                     return self.configuration

#             self.configuration.append([house, battery])
#             battery.current_capacity -= float(house.max_output)

#         sum = 0
#         for battery in self.batteries:
#             sum += battery.current_capacity

#         print(self.configuration)
#         return self.configuration

#     def make_configuration(self):
#         """."""
#         error_counter = 0

#         while self.configuration == [] and error_counter < 10000:
#             self.try_configuration()
#             print("configuration: ", self.configuration)
#             error_counter += 1

#         self.grid.batteries = self.batteries
#         self.grid.houses = self.houses
#         return self.configuration
























# # class Fred_configuration:
# #     """ A Class for Random algorithm to match houses with batteries without exceeding max capacity. """

# #     def __init__(self, input_grid):
# #         """."""
# #         self.grid = input_grid
# #         self.houses = input_grid.houses
# #         self.batteries = input_grid.batteries
# #         self.configuration = []
# #         self.make_configuration()

# #     def reset_hb(self):
# #         self.houses = self.grid.houses
# #         self.batteries = self.grid.batteries

# #     def try_configuration(self):
# #         """Matches houses with battery if it does not exceed battery capacity"""
# #         self.reset_hb()
# #         configuration = []
# #         for house in self.houses:
# #             battery = random.choice(self.batteries)

# #             if battery.current_capacity >= house.max_output:
# #                 battery.current_capacity -= float(house.max_output)
# #                 configuration.append([house, battery])
# #             else:
# #                 for b in self.batteries:
# #                     if b.current_capacity > battery.current_capacity:
# #                         battery = b
# #                 if battery.current_capacity >= house.max_output:
# #                     battery.current_capacity -= float(house.max_output)
# #                     configuration.append([house, battery])

# #                 else:
# #                     configuration.append([house, 0])
# #         return configuration

# #     def reassign_house(self, configuration, postition):
# #         h, b = configuration[position]
# #         battery = random.choice(self.batteries)
# #         return h, battery

# #     def check_battery_capacity(self, battery):
# #         pass

# #     def make_configuration(self):
# #         """ Performs try_configuration until a max error value is exceeded or all houses are succesfully matched"""
# #         error_counter = 0
# #         self.reset_hb()
# #         configuration = []
# #         while self.check_unmatched(configuration) == False and error_counter < 1000:
# #             error_counter += 1
# #             configuration = self.try_configuration()

# #         self.configuration = configuration
# #         print(self.configuration)

# #     def check_unmatched(self, configuration):
# #         """Returns True if all houses are matched with a battery without exceeding capacity. """
# #         if configuration == []:
# #             return False

# #         for combo in configuration:
# #             if combo[1] == 0:
# #                 return False
# #         return True


# #  #       return x
# #  #   def simulated_ann():

# #     """
# # 1.

# #     """


























# # """
# #     def try_configuration(self):
# #         configuration = []
# #         for house in self.shuffled_houses:
# #             battery = random.choice(self.grid.batteries)
# #             error_counter = 0

# #             if battery.current_capacity < house.max_output:
# #                 for b in self.batteries:
# #                     if b.current_capacity > battery.current_capacity:
# #                         battery = b
# #             if battery.current_capacity < house.max_output:
# #                     self.linked_houses = []

# #                     return []

# #             configuration.append([house, battery])
# #             battery.current_capacity -= float(house.max_output)

# #         return configuration


# #         ----


# #     def try_configuration(self):
# #         self.configuration = []
# #         for house in self.houses:
# #             battery = random.choice(self.batteries)

# #             if battery.current_capacity < house.max_output:
# #                 for b in self.batteries:
# #                     if b.current_capacity > battery.current_capacity:
# #                         battery = b
# #             if battery.current_capacity < house.max_output:
# #                 self.configuration = []
# #                 return

# #             self.configuration.append([house, battery])
# #             battery.current_capacity -= float(house.max_output)

# #         ---
# #     def make_configuration(self):
# #         error_counter = 0

# #         while self.configuration == [] and error_counter < 1000:
# #             self.try_configuration()
# #             error_counter += 1

# #         print(self.configuration)

# # """
