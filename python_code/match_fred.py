import random
import copy

class Fred_configuration:
    """ A Class that matches houses with batteries without exceeding max capacity. """

    def __init__(self, input_grid):
        self.grid = input_grid
        self.houses = input_grid.houses
        self.batteries = input_grid.batteries
        self.unmatched = 0
        self.configuration = []
        self.add_houses_to_config()
        #self.make_configuration()
        self.repeat_to_finish()
        self.do_calcs()
        self.do_unmatch()
        self.unmatch_houses()
  
    

    def repeat_to_finish(self):
        """ Swaps and assigns batteries to houses until everything is matched. """
        finished = self.check_unmatched()
        while finished == False:
            self.make_configuration()
            self.find_unmatched()
            finished = self.check_unmatched()
        
        #if finished == True:
            #print("every house is matched")
            #for battery in self.batteries:
                #print(battery.current_capacity)

    def add_houses_to_config(self):
        """ Puts the houses in the configuration, unmatched to a battery. """
        for house in self.houses:
            self.configuration.append([house, 0])

    def make_configuration(self):
        """ Checks self.configuration for unmatched houses and assigns to available batteries. """
        count1 = 0
        count2 = 0
        for combo in self.configuration:
            if combo[1] == 0:
                house = combo[0]
                battery = self.batteries[0]
                for b in self.batteries:
                    if b.current_capacity > battery.current_capacity:
                        battery = b 

                #checks if the house still fits on a battery
                if battery.current_capacity < house.max_output:
                    count1 += 1
                    pass
                    #print("cannot match house ", house)

                else:
                    count2 += 1
                    #print("before: ", battery.current_capacity)
                    battery.current_capacity -= float(house.max_output)
                    #print("after: ", battery.current_capacity)
                    combo[1] = battery

    def find_unmatched(self):
        """ Finds unmatched houses, swaps with another battery """
        for combo in self.configuration:
            if combo[1] == 0:§
                battery = self.find_swap(combo[0], combo[1])
                combo[1] = battery

    def find_swap(self, house1, battery1):
        #krijgt house1 en battery1 van plek waar house is gematched aan 0
        print("battery1 is: ", battery1)
        #for combination in self.configuration:
        for i in range(len(self.configuration)):
            #zoekt naar een batterij en huis combo waarvan battery + huis capaciteit genoeg is om te ruilen
            house, battery = self.configuration[i]
            capacity = 0
            if battery != 0:
                capacity = battery.current_capacity + house.max_output

            if capacity >= house1.max_output and house.max_output < house1.max_output:
                #updates battery capacities
                print("Capacity of battery to switch before: ", battery.current_capacity, "out: ", house.max_output," in: ", house1.max_output)
                battery.current_capacity += float(house.max_output)
                battery.current_capacity -= float(house1.max_output)
                print("Capacity of battery to switch after: ", battery.current_capacity)
                if battery1 != 0:
                    battery1.current_capacity += float(house1.max_ouput)
                    battery1.current_capacity -= float(house.max_ouput)
                
                print("battery1 before combining is: ", battery1)
                self.configuration[i] = [house, battery1]
                return battery
        return 0 

        #what to do if space spread over all capacities

    def do_calcs(self):
        house_caps = 0
        battery_caps = 0
        battery_cur = 0
        for house in self.houses:
            house_caps += house.max_output

        for battery in self.batteries:
            battery_caps += float(battery.max_capacity)
            battery_cur += float(battery.current_capacity)

        print("house output: ", house_caps)
        print("battery max cap: ", battery_caps)
        print("battery cap left: ", battery_cur)

    def do_unmatch(self):
        count = 0
        for combo in self.configuration:
            count += 1
            if combo[1] == 0:
                print("house ", combo[0], "has no match. With output: ", combo[0].max_output)
        print(count, "houses in list")
 
    def unmatch_houses(self):
        """ Take random houses to unmatch and make space for leftover houses"""
        count = 0
        for combo in self.configuration:
            print(combo)
            if combo[1] == 0:
                count +=1
        print(count,"unmatched houses")

    def check_unmatched(self):
        for combo in self.configuration:
            if combo[1] == 0:
                return False
        return True

#na aantal iteraties opnieuw indelen
#simulated annealing toepassen
