from operator import itemgetter
from helper import function_sort_output
import random

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
            hb = house, battery
            self.linked_houses.append(hb)

        #print(self.linked_houses)







      
