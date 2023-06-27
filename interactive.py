import random
import copy
from cs50 import get_int, get_string

from code.helpers.loaders import load_houses, load_batteries
from code.classes.battery import Battery
from code.classes.cable import Cable
from code.classes.house import House
from code.visualisation.visualize import Gridplot
from code.helpers.json_output import output_json
from operator import itemgetter
from code.algorithms.configurations.greedy_configuration import Greedy_configuration
#from code.algorithms.match_fred import Fred_configuration
from code.algorithms.configurations.random_configuration import Random_configuration
from code.classes.grid import Grid
from code.algorithms.cable_routes.random_cable_route import Random_cable_route
from code.algorithms.cable_routes.greedy_cable_route import Greedy_cable_route
#from code.algorithms.cable_routes.shared_cable_route import Shared_cable_route
from code.algorithms.cable_routes.shared_cable_extended import Shared_cable_extended
from code.visualisation.sampling import Sampleplot
from code.algorithms.hillclimber import Hillclimber
from code.helpers.minimum_score import update_minimum_score
from code.helpers.best_grid import update_best_grid


print("Welcome! Our problem is divided into two seperate problems: matching houses to batteries (configuration) and laying cables from houses to batteries.")
print("Please answer by typing in the correct number.")

grid_version: int = get_int("Firstly, which grid do you want to run: grid 1, 2 or 3? Type grid: ")

configuration_version: int = get_int("Which configuration do you want to run: random (type 1) or greedy (type 2)? Type configuration: ")

cable_route_version: int = get_int("And which cable route version do you want to use: random without shared cables (type 1), greedy without shared cables(type 2) or greedy with shared cables (type 3)? Type cable route: ")

iteration: int = get_int("How many times do you want to run it? Type number: ")

if cable_route_version == 3:
    hillclimber: str = get_string("Do you want to run hillclimber afterwards? Type (y/n): ")

    if hillclimber == 'y':
        hill_iterations: int = get_int("How many iterations of hillclimber do you want to run? Type number: ")

# Set upper bound for minimum score
minimum_score = 40000
best_grid = Grid(51, grid_version)
best_grid.total_cost = 40000

# Running the chosen algorithm(s)
for _ in range(iteration):
    grid = Grid(51, grid_version)

    if configuration_version == 1:
        configuration: Random_configuration = Random_configuration(grid)
    else:
        configuration: Greedy_configuration = Greedy_configuration(grid)

    configured = configuration.make_configuration()
    configuration.process_configuration(configured)
    grid.configuration = configured

    if cable_route_version == 1:
        cable_route = Random_cable_route(grid, configuration)
    elif cable_route_version == 2:
        cable_route = Greedy_cable_route(grid, configuration)
    else:
        cable_route = Shared_cable_extended(grid, configuration)

    grid.calc_shared_cable_cost()
    minimum_score = update_minimum_score(minimum_score, grid)
    best_grid = update_best_grid(grid, best_grid)

print('klaar')
print(best_grid.total_cost)
print(best_grid.configuration)
if hillclimber == 'y':
    hclimb = Hillclimber(best_grid)
    hclimb.do_mutate()

    grid = hclimb.current_grid
    grid_visual: Gridplot = Gridplot(grid)
    grid_visual.make_plot()
    output_json(grid)


print(f"Minimum score is {minimum_score}! You can find the outputted json and visualisation of this solution in saved_output.")
