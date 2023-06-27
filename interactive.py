import random
import copy
from tqdm import tqdm


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
from code.algorithms.configurations.configuration_helpers import make_configuration, process_configuration

print("Welcome! Our problem is divided into two seperate problems:")
print("matching houses to batteries (configuration) and laying cables from houses to batteries.\n")
print("Please answer by typing in the correct number.\n")

grid_version: int = int(input("Firstly, which grid do you want to run: grid 1, 2 or 3? Type grid: "))
print()
configuration_version: int = int(input("Which configuration do you want to run: random (baseline) (type: '1') or greedy (type: '2')? Type configuration: "))
print()
if configuration_version == 2:
    greedy_version: int = int(input("In which order do you want to assign houses to batteries in the configuration? Ordered by: \nmax output with highest output first (type: '1'), \nwith lowest output first (type: '2') or \nrandom (type: '3')? \nType choice: "))
print()
cable_route_version: int = int(input("And which cable route version do you want to use: random (baseline) (type: '1') or greedy with shared cables (type: '2')? Type cable route: "))
print()
iteration: int = int(input("How many times do you want to run it? Type number: "))
print()
if cable_route_version == 2:
    hillclimber: str = input("Do you want to run hillclimber afterwards? Type (y/n): ")
    print()
    if hillclimber == 'y':
        hill_iterations: int = int(input("How many iterations of hillclimber do you want to run? Type number: "))
        print()

histogram: str = input("Do you want to plot a histogram? Type (y/n): ")
print()
if histogram == 'y':
    bin_size: int = int(input("What bin size would you like? Choose a bin size lower than the number of iterations. Type number: "))
    print()

# Set upper bound for minimum score
minimum_score = 500000
best_grid = Grid(51, grid_version)
best_grid.total_cost = 500000
score_list: list[int] = []

# Running the chosen algorithm(s)
for _ in tqdm(range(iteration)):
    grid = Grid(51, grid_version)

    if configuration_version == 1:
        configuration: Random_configuration = Random_configuration(grid)
    else:
        configuration: Greedy_configuration = Greedy_configuration(grid, greedy_version)

    configured = make_configuration(configuration)
    process_configuration(configuration, configured)
    grid.configuration = configured

    if cable_route_version == 1:
        cable_route = Random_cable_route(grid, grid.configuration)
    else:
        cable_route = Shared_cable_extended(grid, grid.configuration)

    grid.calc_shared_cable_cost()
    minimum_score = update_minimum_score(minimum_score, grid)
    best_grid = update_best_grid(grid, best_grid)
    score_list.append(grid.total_cost)

if cable_route_version == 2:
    if hillclimber == 'y':
        hclimb = Hillclimber(best_grid, hill_iterations)
        hclimb.do_mutate()

        grid = hclimb.current_grid
        grid_visual: Gridplot = Gridplot(grid)
        grid_visual.make_plot()
        output_json(grid)

if histogram == 'y':
    hist_plot = Sampleplot(score_list, bin_size)


print(f"Best cost is {grid.total_cost}! You can find the outputted json, histogram and visualisation of this solution in saved_output.")
