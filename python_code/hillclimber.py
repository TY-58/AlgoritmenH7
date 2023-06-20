import random
import copy
from match_fred import Fred_configuration

class HillClimber:
    """."""

    def __init__(self, input_config):
        """ Loads an input configuration. """
        self.input_config = input_config
        self.current_config = input_config

    def copy_configuration(self):
        """ Make a copy of the current configuration to manipulate. """
        pass

    def find_match(self, configuration):
        """ Find a match to mutate."""
        match = random.choice(configuration)
        print(match)

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
        
    def mutate_match(self):
        """ mutate a single match."""
        pass



        #get a random match
        #match with new battery
        #check if match is valid

