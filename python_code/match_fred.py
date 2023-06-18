import random
import copy

class Fred_configuration:
    """ A Class that matches houses with batteries without exceeding max capacity. """

    def __init__(self, input_grid):
        self.grid = input_grid
        self.houses = input_grid.houses
        self.batteries = input_grid.batteries

        #a list storing combination of house with battery
        self.configuration = []
        self.make_configuration()
        self.fit_unmatched()
        self.repeat_finish()
        self.show_combo()

    def show_combo(self):
        for combo in self.configuration:
            print(combo)
        for battery in self.batteries:
            print(battery.current_capacity)

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
                print("cannot match house ", house)
            
            else:
                battery.current_capacity -= float(house.max_output)
                self.configuration.append([house, battery])
        
        #print(self.configuration)
        return self.configuration
            #assign to battery
    
    def make_configuration2(self):
        for combo in self.configuration:
            if combo[1] == 0:
                house = combo[0]
                battery = self.batteries[0]
                for b in self.batteries:
                    if b.current_capacity > battery.current_capacity:
                        battery = b 

                #checks if the house still fits on a battery
                if battery.current_capacity < house.max_output:
                    #print(house, "house does not fit anymore")
                    self.configuration.append([house, 0])
                    print("cannot match house ", house)
            
                else:
                    battery.current_capacity -= float(house.max_output)
                    self.configuration.append([house, battery])

    #match houses with batteries based on capacity until fixed
    def fit_unmatched(self):
        for combination in self.configuration:
            if combination[1] == 0:
                #print("no match found for", match[0])
                battery = self.find_swap(combination[0], combination[1])
                #inserts the new battery for the combination
                combination[1] = battery


    #find houses to swap swaps part and returns the battery to swap at other place
    def find_swap(self, house_1, battery_1):
        for combination in self.configuration:
            capacity = 0
            house = combination[0]
            battery = combination[1]
            if battery != 0:
                capacity = battery.current_capacity + house.max_output
            if capacity >= house_1.max_output and house.max_output < house_1.max_output:
                print(house_1, "can switch with ", house)
                #uncombines the found house
                combination = [house, battery_1]
                return battery
        return 0


    def repeat_finish(self):
        for combo in self.configuration:
            if combo[1] == 0:
                self.make_configuration2()
                self.fit_unmatched
                combo = 0
    

        #house + battery capacity
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