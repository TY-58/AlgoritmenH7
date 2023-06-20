import random
import copy
from match_fred import Fred_configuration

class Hillclimber:
    """."""

    def __init__(self, input_config):
        """ Loads an input configuration. """
        self.input_config = input_config
        self.current_config = input_config

    def mutate_match(self, configuration):
        """ mutate a single match."""
        match1 = self.find_match(configuration)
        match2 = self.find_match(configuration)
        while self.valid_mutation(match1, match2) == False:
            print(match1, match2)
            match1 = self.find_match(configuration)
            match2 = self.find_match(configuration)

        print(match1, match2)

    def copy_configuration(self):
        """ Make a copy of the current configuration to manipulate. """
        pass

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
        """ Find a match to mutate."""
        match = random.choice(configuration)
        return match

    def find_battery_capacity(self, battery):
        """ finds the capacity of a given battery. """
        return battery.current_capacity

    def find_house_output(self, house):
        """Finds the output of a house. """
        return house.max_output

    def score(self):
        """ Assigns a score to the mutated configuration. """
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

