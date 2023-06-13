import random
from loaders import load_houses, load_batteries
from battery import Battery
from cable import Cable
from house import House
from visualize import Gridplot
from json_output import output_json
from operator import itemgetter
from greedy_match import Greedy_configuration
from cable_route import Cable_route
from random_match import Random_configuration
from grid import Grid


if __name__ == '__main__':
    grid_1 = Grid(51,1)
    grid_1.process_houses()
    grid_1.process_batteries()

    x = Random_configuration(grid_1)
    config = x.make_configuration()
    cb = Cable_route(grid_1, config)

    grid_1_visual = Gridplot(grid_1)
    grid_1_visual.make_plot()
    #output_json(grid_1)