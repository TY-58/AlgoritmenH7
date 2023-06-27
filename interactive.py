import random
import copy

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


print("Welcome! Our problem is divided into two seperate problems:")
print("matching houses to batteries (configuration) and laying cables from houses to batteries.\n")
print("Please answer by typing in the correct number.\n")

grid_version: int = int(input("Firstly, which grid do you want to run: grid 1, 2 or 3? Type grid: "))

configuration_version: int = int(input("Which configuration do you want to run: random (baseline) (type: '1') or greedy (type: '2')? Type configuration: "))

if configuration_version == 2:
    greedy_version: int = int(input("In which order do you want to assign houses to batteries in the configuration: ordered by max output with highest first (type: '1'), with lowest first (type: '2') or random (type: '3')? Type choice: "))

cable_route_version: int = int(input("And which cable route version do you want to use: random (baseline) (type: '1') or greedy with shared cables (type: '2')? Type cable route: "))

iteration: int = int(input("How many times do you want to run it? Type number: "))

if cable_route_version == 2:
    hillclimber: str = input("Do you want to run hillclimber afterwards? Type (y/n): ")

    if hillclimber == 'y':
        hill_iterations: int = int(input("How many iterations of hillclimber do you want to run? Type number: "))

# Set upper bound for minimum score
minimum_score = 500000
best_grid = Grid(51, grid_version)
best_grid.total_cost = 500000

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
        cable_route = Random_cable_route(grid, grid.configuration)
    else:
        cable_route = Shared_cable_extended(grid, grid.configuration)

    grid.calc_shared_cable_cost()
    minimum_score = update_minimum_score(minimum_score, grid)
    best_grid = update_best_grid(grid, best_grid)

if configuration_version == 2:
    if hillclimber == 'y':
        hclimb = Hillclimber(best_grid)
        hclimb.do_mutate()

        grid = hclimb.current_grid
        grid_visual: Gridplot = Gridplot(grid)
        grid_visual.make_plot()
        output_json(grid)



print(f"Minimum score is {minimum_score}! You can find the outputted json and visualisation of this solution in saved_output.")
