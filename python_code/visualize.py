# Taken from: https://matplotlib.org/stable/plot_types/basic/step.html#sphx-glr-plot-types-basic-step-py

import matplotlib.pyplot as plt
import numpy as np

class Gridplot:
       """A class for visualizing the grid as a plot"""

       def __init__(self, grid):
              self.cables_routes = grid.cables
              self.houses = grid.houses 
              self.batteries = grid.batteries
       
       def find_house_cor (self):
              house_locations = []
              for house in self.houses:
                     house_locations.append(house.location)
              return house_locations

       def find_battery_cor (self):
              battery_locations = []
              for battery in self.batteries:
                     battery_locations.append(battery.location)
              return battery_locations
       #self.houses print de objecten, krijg toegang tot x en y

 #      def find_cable_routes (self):
 #             cable_routes = []
 #             for cable in self.cables_routes:
 #                    cable_routes.append(cable.route)
 #             return cable_routes

