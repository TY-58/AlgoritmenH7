import random
import copy
from tqdm import tqdm

from code.visualisation.visualize import Gridplot
from code.helpers.json_output import output_json
from operator import itemgetter
from code.algorithms.configurations.greedy_configuration import Greedy_configuration
from code.algorithms.configurations.random_configuration import Random_configuration
from code.classes.grid import Grid
from code.algorithms.cable_routes.random_cable_route import Random_cable_route
from code.algorithms.cable_routes.shared_cable_route import Shared_cable_route
from code.visualisation.sampling import Sampleplot
from code.algorithms.hillclimber import Hillclimber
from code.helpers.minimum_score import update_minimum_score
from code.helpers.best_grid import update_best_grid
from code.algorithms.configurations.configuration_helpers import make_configuration, process_configuration

# Introduces Case
print("\nWelcome! Our problem is divided into two seperate problems:")
print("matching houses to batteries (configuration) and laying cables from houses to batteries (cable route).\n")
print("Please answer by typing in the chosen number.\n")

# Asks for grid type
grid_version: int = int(input("Firstly, which grid do you want to run: grid 1, 2 or 3? \nType grid: "))

# Asks for configuration algorithm
configuration_version: int = int(input("\nWhich configuration do you want to run:\n"
"1.random (baseline) (type: '1') or\n"
"2.greedy (type: '2')?\n"
"Type configuration: "))

# Asks for assignment order if greedy configuration
if configuration_version == 2:
    greedy_version: int = int(input("\nIn which order do you want to assign houses to batteries in the configuration? Ordered by:\n"
    "1.max output with highest output first (type: '1'),\n"
    "2.with lowest output first (type: '2') or\n"
    "3.random (type: '3')? \n"
    "Type choice: "))

# Asks for cable route algorithm
cable_route_version: int = int(input("\nAnd which cable route version do you want to use:\n"
"1.random (baseline) (type: '1') or\n"
"2.greedy with shared cables (type: '2')?\n"
"Type cable route: "))

# Asks for number iterations 
iteration: int = int(input("\nHow many times do you want to run it? \nType number: "))

# Asks for Hillclimber
if cable_route_version == 2:
    hillclimber: str = input("\nDo you want to run hillclimber afterwards? \nType (y/n): ")

    if hillclimber == 'y':
        hill_iterations: int = int(input("\nWhat is the maximum of iterations you want it to run for a single improvement? \nType number: "))

# Asks for Histogram
if cable_route_version != 1:
    histogram: str = input("\nDo you want to plot a histogram? \nType (y/n): ")

    if histogram == 'y':
        bin_size: int = int(input("\nWhat bin size would you like? Choose a bin size lower than the number of iterations. \nType number: "))


# Set upper bound for minimum score
minimum_score = 500000
best_grid = Grid(51, grid_version)
best_grid.total_cost = 500000
score_list: list[int] = []
states_visited: list[int] = []

# Running the chosen algorithm(s)
for _ in tqdm(range(iteration)):
    grid = Grid(51, grid_version)

    if configuration_version == 1:
        configuration: Random_configuration = Random_configuration(grid)
    else:
        configuration: Greedy_configuration = Greedy_configuration(grid, greedy_version)

    configured = make_configuration(configuration, states_visited)
    process_configuration(configuration, configured)
    grid.configuration = configured

    if cable_route_version == 1:
        cable_route = Random_cable_route(grid, grid.configuration)
    else:
        cable_route = Shared_cable_route(grid, grid.configuration)

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
if cable_route_version != 1:
    if histogram == 'y':
        hist_plot = Sampleplot(score_list, bin_size)


print(f"\nBest cost is {grid.total_cost}!\n"
"You can find the outputted json, histogram and/or visualisation of the solution(s) in saved_output.\n")
print(f"The algorithm visited an average of {float(sum(states_visited))/len(states_visited)} states per solution.")
