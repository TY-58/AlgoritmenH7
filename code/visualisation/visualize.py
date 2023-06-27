# Partially taken from: https://matplotlib.org/stable/plot_types/basic/step.html#sphx-glr-plot-types-basic-step-py

import matplotlib.pyplot as plt
import numpy as np

class Gridplot:
       """
       A class for visualizing the grid as a plot.
       """


       def __init__(self, grid):
              """
              Takes a grid as input and stores the grid information in self.
              Initializes code to print the grid.
              """

              self.cables = grid.cables
              self.houses = grid.houses
              self.batteries = grid.batteries
              self.house_locations = self.find_house_cor()
              self.battery_locations = self.find_battery_cor()
              self.cable_routes = self.find_cable_routes()


       def find_house_cor(self):
              """
              Finds the coordinates of all houses and returns them as a list.
              """

              house_locations = []
              for house in self.houses:
                     house_locations.append(house.location)
              return house_locations


       def find_battery_cor(self):
              """
              Finds the coordinates of all batteries and returns them as a list.
              """

              battery_locations = []
              for battery in self.batteries:
                     battery_locations.append(battery.location)
              return battery_locations


       def find_cable_routes (self):
              """
              Finds all cable routes and returns a list of cables with a list of houses.
              """

              cable_routes = []
              for cable in self.cables:
                     cable_routes.append(cable.route)
              return cable_routes


       def make_plot(self):
              """
              Makes the plot of batteries, houses and cables.
              """

              plt.style.use('_mpl-gallery')
              fig, ax = plt.subplots(figsize=(15, 10))

              x1 = []
              y1 = []
              x2 = []
              y2 = []
              x3 = []
              y3 = []

              # Assigns house, battery and route coordinates to x and y
              for house in self.house_locations:
                     x1.append(int(house[0]))
                     y1.append(int(house[1]))

              for battery in self.battery_locations:
                     x2.append(int(battery[0]))
                     y2.append(int(battery[1]))

              for cable in self.cable_routes:
                     x3 = []
                     y3 = []
                     for route in cable:
                            x3.append(int(route[0]))
                            y3.append(int(route[1]))
                     ax.step(x3, y3, linewidth=2.5, color='blue')

              # Places the house and battery coordinates and makes route steps
              plt.plot(x2, y2, 'g*', markersize = 15)
              plt.plot(x1, y1, 'r*', markersize = 15)

              ax.set(xlim=(0, 50), xticks=np.arange(1, 50),
                     ylim=(0, 50), yticks=np.arange(1, 50))

              plt.savefig("saved_output/pic.")
              #plt.show()
