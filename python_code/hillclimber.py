import random
import copy
from match_fred import Fred_configuration
from combined_cable_route import Combined_cable_route

class Hillclimber:
    """ Loads an input configuration
    returns an output configuration
    finds matches in configuration and swaps batteries if possible.
    """

    def __init__(self, input_grid, input_config):
        """ Loads an input configuration.
        Input grid and configuration always need to stay the same.
        current and last can be updated.
        """
        self.input_grid = copy.copy(input_grid)
        self.last_grid = []
        self.current_grid = self.input_grid
        self.input_config = copy.copy(input_config)
        self.last_config = []
        self.current_config = self.input_config 

    def mutate_match(self, configuration):
        """ mutate a single match."""
        configuration_
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

    def copy_configuration(self):
        """ Make a copy of the current configuration to manipulate. """
        self.last_config = copy.copy(self.current_config)

    def valid_mutation(self, match1, match2):
        """Checks if the mutation is valid and returns Bool. """
        if match1[1] == match2[1]:
            print("match is invalid")
            return False

        #return false if battery capacity+house < house output
        b_cap1 = self.find_battery_capacity(match1[1])
        h_out1 = self.find_house_output(match1[0])
        cap1 = float(b_cap1 + h_out1)
        b_cap2 = self.find_battery_capacity(match2[1])
        h_out2 = self.find_house_output(match2[0])
        cap2 = float(b_cap2 + h_out2)

        if cap1 < h_out2:
            print("mutation is invalid. cap:", cap1," out: ", h_out2)
            return False
        if cap2 < h_out1:
            print("mutation is invalid")
            return False
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
        pass

    def implement_score(self):
        """ Decides if configuration should become mutated configuration. """
        pass

    def save_scores(self):
        """ Saves the scores of the mutation and"""
        pass

    def stop_mutation(self):
        """ Quits program if mutations do not improve configuration after X tries."""
        pass
        


        #get a random match
        #match with new battery
        #check if match is valid

