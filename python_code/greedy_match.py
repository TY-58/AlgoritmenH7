from operator import itemgetter
from helper import function_sort_output
import random
import copy

class Greedy:
    """Class for Greedy algorithm to match houses with batteries without exceeding max capacity"""

    #neccesary: all houses and batteries and their max output and capacity.
    def __init__(self, grid):
        self.houses = grid.houses
        self.batteries = grid.batteries
        self.sort_houses(self.houses)
        self.linked_houses = []
        self.assign_houses()

    def sort_houses(self, houses):
        #in place sort: sorted_houses = self.houses.sort(key=function_sort_output)
        #niet inplace
        sorted_houses = sorted(houses, key=function_sort_output)

    def assign_houses(self):
        """ greedily assign houses to a random battery, restart if battery capacity is exceeded.
        OR
        make a list of tuples where the first is the house and the second tuple is a battery.
        Both point to the location of the battery and the house object as found in class Grid
        """
        # Matches houses to batteries
        for house in self.houses:
            battery = random.choice(self.batteries)
            #add if statement: only assign house to battery if capacity not exceeded
            #need to access battery capacity, and house output

            self.linked_houses.append([house, battery])

        #print(self.linked_houses)




class Greedy_configuration:
    """Class for Greedy algorithm to match houses with batteries without exceeding max capacity"""

    #neccesary: all houses and batteries and their max output and capacity.
    def __init__(self, input_grid):
        grid_var = copy.copy(input_grid)
        self.grid = grid_var
        self.sorted_houses = self.sort_houses()


    def sort_houses(self):
        return sorted(self.grid.houses, key=lambda x: x.max_output, reverse=True)


    def try_configuration(self):
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

        #for i in configuration:
        #    print(i[0].id, i[1].id)
        sum = 0
        for battery in self.grid.batteries:
            sum += battery.current_capacity
            #print(battery.current_capacity)
        #print(sum)
        return configuration


    def make_configuration(self):
        x = []
        error_counter = 0

        while x == [] and error_counter < 10000:
            x = self.try_configuration()
            error_counter += 1

        return x
