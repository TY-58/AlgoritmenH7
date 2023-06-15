import random
import copy

class Fred_configuration:
    """ A Class for Random algorithm to match houses with batteries without exceeding max capacity. """

    def __init__(self, input_grid):
        self.grid = input_grid
        self.houses = input_grid.houses
        self.batteries = input_grid.batteries

        #a list storing combination of house with battery
        self.configuration = []
        self.make_configuration()
        self.fit_unmatched()

    def make_configuration(self):

        for house in self.houses:

            battery = self.batteries[0]
            for b in self.batteries:
                
                if b.current_capacity > battery.current_capacity:
                    battery = b 

            #checks if the house still fits on a battery
            if battery.current_capacity < house.max_output:
                #print(house, "house does not fit anymore")
                self.configuration.append([house, 0])
            
            else:
                battery.current_capacity -= float(house.max_output)
                self.configuration.append([house, battery])
        
        #print(self.configuration)
        return self.configuration
            #assign to battery

        #match houses with batteries based on capacity until fixed
    def fit_unmatched(self):
        for match in self.configuration:
            if match[1] == 0:
                print("no match found for", match[0])

        #rematches based on distance
        
        """
        #van Otto
        def try_configuration(self):
        configuration = []
        for house in self.sorted_houses:
            batteries_sorted = []
            for bat in self.grid.batteries:
                batteries_sorted.append([bat, self.distance_to_battery(house, bat)])

            #een lijst met tuples eerste tuple is batterij en tweede distance
            batteries_sorted.sort(key=lambda a: a[1], reverse=False)

        def distance_to_battery(self, house, battery):
        return abs(house.location[0]- battery.location[0]) + abs(house.location[1] - battery.location[1])
        """