import random
from loaders import load_houses, load_batteries
from battery import Battery
from cable import Cable
from house import House
from visualize import Gridplot
from json_output import output_json
from operator import itemgetter
from greedy_match import Greedy_configuration
from otto_greedy_match_improve import Otto_greedy_configuration
from cable_route import Cable_route
from random_match import Random_configuration
from grid import Grid
from random_cable_route import Random_cable_route
from otto_random_improve import Otto_cable_route


if __name__ == '__main__':
    grid_1 = Grid(51,1)

    x = Otto_greedy_configuration(grid_1)

    config = x.try_configuration()
    cb = Otto_cable_route(grid_1, config)

    grid_1.calc_total_cable_cost()
    print(grid_1.total_cost)

    grid_1_visual = Gridplot(grid_1)
    grid_1_visual.make_plot()
    #output_json(grid_1)
