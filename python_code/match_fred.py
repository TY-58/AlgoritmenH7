import random
import copy

class Fred_configuration:
    """ A Class for Random algorithm to match houses with batteries without exceeding max capacity. """

    def __init__(self, input_grid):
        """."""
        self.grid = input_grid
        self.houses = input_grid.houses
        self.batteries = input_grid.batteries
        self.configuration = []
        self.make_configuration()

    def try_configuration(self):
        configuration = []
        for house in self.houses:
            battery = random.choice(self.batteries)

            if battery.current_capacity >= house.max_output:
                battery.current_capacity -= float(house.max_output)
                configuration.append([house, battery])
            else:
                for b in self.batteries:
                    if b.current_capacity > battery.current_capacity:
                        battery = b 
                if battery.current_capacity >= house.max_output:
                    battery.current_capacity -= float(house.max_output)
                    configuration.append([house, battery])

                else: 
                    configuration.append([house, 0])

        return configuration

    def make_configuration(self):
        error_counter = 0
        configuration = []
        while self.check_unmatched(configuration) == False and error_counter < 1000:
            error_counter += 1
            configuration = self.try_configuration()
            
        self.configuration = configuration
        print(self.configuration)

    def check_unmatched(self, configuration):
        if configuration == []:
            return False

        for combo in configuration:
            if combo[1] == 0:
                return False
        return True


 #       return x
 #   def simulated_ann():
        
    """
1. 

    """


























"""
    def try_configuration(self):
        configuration = []
        for house in self.shuffled_houses:
            battery = random.choice(self.grid.batteries)
            error_counter = 0

            if battery.current_capacity < house.max_output:
                for b in self.batteries:
                    if b.current_capacity > battery.current_capacity:
                        battery = b 
            if battery.current_capacity < house.max_output:
                    self.linked_houses = []

                    return []

            configuration.append([house, battery])
            battery.current_capacity -= float(house.max_output)

        return configuration


        ----


    def try_configuration(self):
        self.configuration = []
        for house in self.houses:
            battery = random.choice(self.batteries)

            if battery.current_capacity < house.max_output:
                for b in self.batteries:
                    if b.current_capacity > battery.current_capacity:
                        battery = b 
            if battery.current_capacity < house.max_output:
                self.configuration = []
                return

            self.configuration.append([house, battery])
            battery.current_capacity -= float(house.max_output)

        ---
    def make_configuration(self):
        error_counter = 0

        while self.configuration == [] and error_counter < 1000:
            self.try_configuration()
            error_counter += 1

        print(self.configuration)

"""
