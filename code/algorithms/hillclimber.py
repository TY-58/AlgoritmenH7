from __future__ import annotations
import random
import copy

from .cable_routes.shared_cable_route import Shared_cable_route
#from .cable_routes.shared_cable_route import Shared_cable_route
from .configurations.greedy_configuration import Greedy_configuration
from code.classes.grid import Grid
from code.visualisation.visualize import Gridplot

class Hillclimber:
    """
    A class for performing a simple Hill Climber algorithm on a given grid.
    Takes a grid as input and mutates matches of houses and batteries from configuration list.
    Mutations are only performed when they are valid.
    Performs mutations for the duration of a a given number of iterations.
    """


    def __init__(self, grid: Grid, var: int):
        """
        Takes a grid as input and stores the grid.
        Takes a variable for iterations and stores the iterations.
        Makes deepcopies of the input grid to make mutations without loss of input grid.
        """
        self.iterations = var
        self.input_grid = grid
        self.input_config = grid.configuration
        self.last_grid = copy.deepcopy(self.input_grid)
        self.last_config = self.last_grid.configuration
        self.current_grid = copy.deepcopy(self.input_grid)
        self.current_config = self.current_grid.configuration
        self.first_score = grid.total_cost
        self.current_score = grid.total_cost
        self.stuck = 0


    def do_mutate(self) -> None:
        """
        Calls for configuration mutations while score is improved at least once every X iterations.
        X: a given number of iterations.
        """

        improvements = 0

        # Performs mutations while at least 1 in every X iterations is an improvement
        while self.stop_mutation() == False:
            new_config = self.mutate_match(self.current_config)

            # Replaces configuration in the grid with new_config
            self.current_grid.process_configuration_grid(new_config)

            score_new = self.score(new_config)
            improved = self.check_if_improved(score_new)

            # Saves the improvement
            if improved == True:
                improvements += 1
                print("Improved after", self.stuck, "iterations")
                print("Improved costs: ", score_new)
                self.last_grid = self.current_grid
                self.last_config = self.current_config
                self.current_score = score_new
                self.current_grid = copy.deepcopy(self.last_grid)
                self.current_config = self.current_grid.configuration
                self.stuck = 0

            # Resets grid and configuration to last
            elif improved == False:
                self.current_grid = copy.deepcopy(self.last_grid)
                self.current_config = self.current_grid.configuration

        if improvements == 0:
            print("There was no improvement made")
            print("Costs: ", self.first_score)

        else:
            print("Improved ", improvements, " time(s)")
            print("Old costs ", self.first_score)
            print("New costs: ", self.current_score)


    def mutate_match(self, configuration: list[list[House, Battery]]) -> list[list[House, Battery]]:
        """
        Mutates a single match in the given configuration and returns the mutated configuration.
        """

        # Finds valid mutations
        place1, match1 = self.find_match(configuration)
        place2, match2 = self.find_match(configuration)
        while self.valid_mutation(match1, match2) == False:
            place1, match1 = self.find_match(configuration)
            place2, match2 = self.find_match(configuration)

        # Switches batteries
        bat_switch: [House, Battery] = match1[1]
        match1[1] = match2[1]
        match2[1] = bat_switch

        # Places mutated matches in configuration
        configuration[place1] = match1
        configuration[place2] = match2

        return configuration


    def valid_mutation(self, match1: [House, Battery], match2: [House, Battery]) -> bool:
        """
        Checks if the mutation is valid and returns a Bool.
        """

        if match1[1] == match2[1]:
            return False

        # Calculates if batteries can be switched according to capacity
        b_cap1 = self.find_battery_capacity(match1[1])
        h_out1 = self.find_house_output(match1[0])
        cap1 = float(b_cap1 + h_out1)
        b_cap2 = self.find_battery_capacity(match2[1])
        h_out2 = self.find_house_output(match2[0])
        cap2 = float(b_cap2 + h_out2)

        if cap1 < h_out2:
            return False
        if cap2 < h_out1:
            return False

        return True


    def find_match(self, configuration: list[list[House, Battery]]) -> Tuple(int, [House, Battery]):
        """
        Finds a match to mutate. Returns place of match in configuration and match.
        """

        # Takes a random location in the configuration list
        x = random.choice(range(len(configuration)))
        match_ = configuration[x]

        return x, match_


    def find_battery_capacity(self, battery: Battery) -> float:
        """
        Finds the capacity of a given battery.
        """

        return battery.current_capacity


    def find_house_output(self, house: House) -> float:
        """
        Finds the output of a given house.
        """

        return house.max_output


    def score(self, configuration: list[list[House, Battery]]) -> int:
        """
        Gets a configuration and measures cost.
        Calls to calculate new score.
        Returns the new calculated score.
        """

        # Empties house connections from batteries
        for battery in self.current_grid.batteries:
            battery.house_connections = []

        # Reconnects houses to batteries according to new configuration
        self.current_grid.process_configuration_grid(configuration)

        # Lays the cables in the grid
        Shared_cable_route(self.current_grid, configuration)

        # Calculates new cost
        self.current_grid.calc_shared_cable_cost()
        score = self.current_grid.total_cost

        return score


    def check_if_improved(self, score_new: int) -> bool:
        """
        Checks if the newly calculated score is better than the last score.
        Updates self.stuck if the new score is not an improvement.
        Resets self.stuck if the new score is an improvement
        Returns False if not, else True.
        """

        score_old = self.current_score
        if score_new < score_old:
            return True

        else:
            self.stuck += 1
            return False


    def stop_mutation(self) -> bool:
        """
        Returns Bool if self.stuck exceeds a given number of iterations.
        """

        if self.stuck > self.iterations:
            return True

        return False
