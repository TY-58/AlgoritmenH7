from operator import itemgetter
from helper import function_sort_output

class Greedy:
    """Class for Greedy algorithm to match houses with batteries without exceeding max capacity"""

    #neccesary: all houses and batteries and their max output and capacity.
    def __init__(self, grid: list[list[int, int]]):
        self.houses = grid.houses
        self.batteries = grid.batteries

    def sort_houses(self):
        #print(self.houses)

        #in place:
        #sorted_houses = self.houses.sort(key=function_sort_output)
        #niet inplace
        sorted_houses = sorted(self.houses, key=function_sort_output)
        print(sorted_houses)



      
