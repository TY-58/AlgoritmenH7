import random
import copy
#from .match_fred import Fred_configuration
from .cable_routes.shared_cable_route import Shared_cable_route
from .configurations.greedy_configuration import Greedy_configuration
from code.classes.grid import Grid

MAX_STUCK: int = 1000

class Hillclimber:
    """
    A class for performing a simple Hill Climber algorithm on a given grid.
    Takes a grid as input and mutates matches of houses and batteries from configuration list.
    Mutations are only performed when they are valid.
    Performs mutations for the duration of a global variable MAX_STUCK.
    """

    def __init__(self, input_grid):
        """
        Takes a grid as input and stores the grid.
        Makes deepcopies of the input grid to make mutations without loss of input grid.
        """

        self.input_grid = input_grid
        self.input_config = input_grid.configuration
        self.last_grid = copy.deepcopy(self.input_grid)
        self.last_config = self.last_grid.configuration
        self.current_grid = copy.deepcopy(self.input_grid)
        self.current_config = self.current_grid.configuration
        self.current_score = input_grid.total_cost
        self.stuck = 0

    def do_mutate(self):
        """
        Calls for configuration mutations while score is improved at least once every X iterations.
        X: Global Variable MAX_STUCK
        """

        print("score_old: ", self.current_score)

        # Performs mutations while at least 1 in every X iterations is an improvement
        while self.stop_mutation() == False:

            new_config = self.mutate_match(self.current_config)

            # Replaces configuration in the grid with new_config
            self.current_grid.process_configuration_grid(new_config)

            score_new = self.score(new_config)

            # Checks if the score is an improvement from last
            improvement = self.implement_score(score_new)

            # Saves the improvement
            if improvement == True:
                self.last_grid = self.current_grid
                self.last_config = self.current_config
                self.current_score = score_new
                self.current_grid = copy.deepcopy(self.last_grid)
                self.current_config = self.current_grid.configuration

            # Resets grid and configuration to last
            elif improvement == False:
                self.current_config = self.last_config
                self.current_grid = self.last_grid

        print("score_new: ", self.current_score)

    def mutate_match(self, configuration):
        """
        Mutates a single match in the given configuration and retursn the mutated configuration.
        """

        # Finds valid mutations
        place1, match1 = self.find_match(configuration)
        place2, match2 = self.find_match(configuration)
        while self.valid_mutation(match1, match2) == False:
            place1, match1 = self.find_match(configuration)
            place2, match2 = self.find_match(configuration)

        # Switches batteries
        bat_switch = match1[1]
        match1[1] = match2[1]
        match2[1] = bat_switch

        # Puts mutated matches in configuration
        configuration[place1] = match1
        configuration[place2] = match2

        return configuration

    def valid_mutation(self, match1, match2):
        """
        Checks if the mutation is valid and returns Bool.
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

    def find_match(self, configuration):
<<<<<<< HEAD
        """
        Finds a match to mutate. Returns place of match in configuration and match.
=======
        """ 
        Finds a match to mutate. Returns place of match in configuration and the match. 
>>>>>>> 4f5c78971e3f13bce0a2928f454fdae97f45da65
        """

        # Picks a random location in the configuration list
        x = random.choice(range(len(configuration)))
        match = configuration[x]

        return x, match

    def find_battery_capacity(self, battery):
        """
        Finds the capacity of a given battery.
        """

        return battery.current_capacity

    def find_house_output(self, house):
        """
        Finds the output of a given house.
        """

        return house.max_output

    def score(self, configuration):
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

        # Lays new cable routes for new configuration
        Shared_cable_route(self.current_grid, configuration)

        # Calculates new cost
        self.current_grid.calc_shared_cable_cost()
        score = self.current_grid.total_cost

        return score

    def implement_score(self, score_new):
        """
        Checks if the newly calculated score is better than the last score.
        Updates self.stuck if the new score is not an improvement.
        Resets self.stuck if the new score is an improvement
        Returns False if not, else True.
        """

        score_old = self.current_score
        if score_new < score_old:
            self.stuck = 0
            return True

        else:
            self.stuck += 1
            return False

    def stop_mutation(self):
        """
        Returns Bool if self.stuck exceeds global variable MAX_STUCK.
        """

        if self.stuck > MAX_STUCK:
            return True

        return False
