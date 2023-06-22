import random
import copy
from match_fred import Fred_configuration
from combined_cable_route import Combined_cable_route
from grid import Grid

MAX_STUCK: int = 1000

#grid.houses daarin in grid.cables begin en eindpunt
#ook nog op manhatten


class Hillclimber:
    """
    Loads an input configuration
    returns an output configuration
    finds matches in configuration and swaps batteries if possible.
    """

    def __init__(self, input_grid):
        """
        Loads an input configuration.
        Input grid and configuration always need to stay the same.
        current and last can be updated.
        """
        #haal config uit grid
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
        Performs mutations under certain conditions.
        """
        print("score_old: ", self.current_score)
        while self.stop_mutation() == False:
            #make a new configuration
            new_config = self.mutate_match(self.current_config)

            #replace the configuration in the grid with the new one
            self.current_grid.process_configuration_grid(new_config)

            score_new = self.score(new_config)

            improvement = self.implement_score(score_new)

            #if improved, saves the improvement
            if improvement == True:
                self.last_config = self.current_config
                self.last_grid = self.current_grid

            #if not improved, resets grid and configuration to best
            elif improvement == False:
                self.current_config = self.last_config
                self.current_grid = self.last_grid
        
        print("score_new: ", self.current_score)

    def mutate_match(self, configuration):
        """
        Mutate a single match.
        """
        place1, match1 = self.find_match(configuration)
        place2, match2 = self.find_match(configuration)
        while self.valid_mutation(match1, match2) == False:
            place1, match1 = self.find_match(configuration)
            place2, match2 = self.find_match(configuration)

        #switches batteries
        bat_switch = match1[1]
        match1[1] = match2[1]
        match2[1] = bat_switch

        #puts mutated matches in configuration
        configuration[place1] = match1
        configuration[place2] = match2

        return configuration

    def copy_configuration(self):
        """ Make a copy of the current configuration to manipulate. """
        self.last_config = copy.copy(self.current_config)

    def valid_mutation(self, match1, match2):
        """Checks if the mutation is valid and returns Bool. """
        if match1[1] == match2[1]:
            #print("match is invalid")
            return False

        #return false if battery capacity+house < house output
        b_cap1 = self.find_battery_capacity(match1[1])
        h_out1 = self.find_house_output(match1[0])
        cap1 = float(b_cap1 + h_out1)
        b_cap2 = self.find_battery_capacity(match2[1])
        h_out2 = self.find_house_output(match2[0])
        cap2 = float(b_cap2 + h_out2)

        if cap1 < h_out2:
            #print("mutation is invalid. cap:", cap1," out: ", h_out2)
            return False
        if cap2 < h_out1:
            #print("mutation is invalid")
            return False

        #print("mutation is valid")
        return True

    def find_match(self, configuration):
        """ Find a match to mutate. Returns place of match in configuration and the match. """
        x = random.choice(range(len(configuration)))
        match = configuration[x]
        return x, match

    def find_battery_capacity(self, battery):
        """ finds the capacity of a given battery. """
        return battery.current_capacity

    def find_house_output(self, house):
        """Finds the output of a house. """
        return house.max_output

    def score(self, configuration):
        """ Gets a configuration and measures cost. Assigns a score to the mutated configuration. """

         #resets the house_connections neccesary to lay new cables
        for battery in self.current_grid.batteries:
            battery.house_connections = []

        #reconnect houses to batteries according to new configuration
        self.current_grid.process_configuration_grid(configuration)

        #lays new cable routes
        Combined_cable_route(self.current_grid, configuration)

        #calculates new cost
        self.current_grid.calc_combined_cable_cost()

        score = self.current_grid.total_cost
        return score

    def implement_score(self, score_new):
        """ Decides if configuration should become mutated configuration. """
        score_old = self.current_score
        #if score 2 is better than 1, current config is updated
        if score_new < score_old:
            self.stuck = 0
            return True

        #tell to keep score 1 and redo 2
        #or return certain something
        elif score_new > score_old:
            self.stuck += 1
            #print("stuck:", self.stuck)
            return False

        elif score_old == score_new:
            self.stuck += 1
            #print("stuck:", self.stuck)
            return False

    def save_scores(self):
        """ Saves the scores of the mutation and"""
        pass

    def stop_mutation(self):
        """ Quits program if mutations do not improve configuration after X tries."""
        #maybe change into different return?
        if self.stuck > MAX_STUCK:
            return True
        return False
