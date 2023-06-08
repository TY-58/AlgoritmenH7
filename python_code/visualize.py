# Taken from: https://matplotlib.org/stable/plot_types/basic/step.html#sphx-glr-plot-types-basic-step-py

import matplotlib.pyplot as plt
import numpy as np
from grid import Grid
from loaders import load_houses, load_batteries

class Gridplot:
       """A class for visualizing the grid as a plot"""

       def __init__(self, grid):
              self.cables_routes = cables
              self.houses = grid.houses 
              self.batteries = []
       #load houses
       #load batteries
       #load cable routes



plt.style.use('_mpl-gallery')

# make data
#np.random.seed(3)
#x = 0.5 + np.arange(8)
#y = np.random.uniform(2, 7, len(x))

# plot
fig, ax = plt.subplots()

#ax.step(x, y, linewidth=2.5)

ax.set(xlim=(0, 50), xticks=np.arange(1, 50),
       ylim=(0, 50), yticks=np.arange(1, 50))

#plt.savefig(".")
plt.show()
