# Taken from: https://matplotlib.org/stable/plot_types/basic/step.html#sphx-glr-plot-types-basic-step-py

import matplotlib.pyplot as plt
import numpy as np

class Gridplot:
       """A class for visualizing the grid as a plot"""

       def __init__(self, grid):
              self.cables_routes = grid.cables
              self.houses = grid.houses 
              self.batteries = grid.batteries
       
       def find_house_cor(self):
              house_locations = []
              for house in self.houses:
                     house_locations.append(house.location)
              return house_locations

       def find_battery_cor(self):
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

       def make_plot(self):
              
              plt.style.use('_mpl-gallery')

              # make data
              np.random.seed(3)
              x = 0.5 + np.arange(8)
              y = np.random.uniform(2, 7, len(x))
              
              fig, ax = plt.subplots()

              ax.step(x, y, linewidth=2.5)
              ax.set(xlim=(0, 50), xticks=np.arange(1, 50),
                     ylim=(0, 50), yticks=np.arange(1, 50))

              plt.savefig(".")
              plt.show()
