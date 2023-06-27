#Partially taken from: https://matplotlib.org/stable/gallery/statistics/hist.html#sphx-glr-gallery-statistics-hist-py
#Partially taken from: https://www.tutorialspoint.com/drawing-average-line-in-histogram-in-matplotlib

import matplotlib.pyplot as plt
import numpy as np
import random
import csv
from code.helpers.loaders import load_houses, load_batteries
from .visualize import Gridplot
from code.helpers.json_output import output_json
from operator import itemgetter
from code.classes.grid import Grid

from code.algorithms.cable_routes.shared_cable_extended import Shared_cable_extended
from code.algorithms.configurations.greedy_configuration import Greedy_configuration
from code.algorithms.configurations.random_configuration import Random_configuration
from code.algorithms.cable_routes.shared_cable_extended import Shared_cable_extended


class Sampleplot:
    """
    Takes random sample solutions and visualizes them in a histogram plot.
    """


    def __init__(self, grid_version, ):
        self.scores: list[int] = []
        self.count: int = 0
        self.grid_version = grid_version
        self.get_scores()
        self.make_hist()
        self.make_csv_hist()


    def get_scores(self):
        """
        .
        """

        print("For which configuration algorithm would you like to retrieve a histogram?")
        print("Press 1 for Random.")
        print("Press 2 for Greedy.")

        valid = False
        while valid == False:
            algorithm_type = int(input("Enter Choice: "))

            if algorithm_type == 1 or algorithm_type == 2:
                valid = True
            else:
                print("Invalid choice.")

        print("How many samples would you like?")
        print("Please insert positive integer.")
        number_of_samples = int(input("Number of samples: "))

        if algorithm_type == 1:
            valid = True
            self.random_config_sampling()
        elif algorithm_type == 2:
            valid = True
            self.greedy_config_sampling()

        taken_samples = 0
        for n in range(number_of_samples):  
            taken_samples += 1
            print("Performs sample #", taken_samples)

            if algorithm_type == 1:
                score, grid, configuration = self.random_config_sampling()
            elif algorithm_type == 2:
                score, grid, configuration = self.greedy_config_sampling()


            # Stores the cost
            if score != 0:
                if self.count == 0:
                    self.best_grid = grid
                    self.best_configuration = configuration
                    self.best_score = score
                else:
                    self.save_best(score, grid, configuration)

                self.scores.append(score)
                self.count += 1


    def random_config_sampling(self):
        """
        .
        """

        grid = Grid(51, self.grid_version)
        x = Random_configuration(grid)
        config = []
        while config == []:
            config = x.try_configuration()
        x.process_configuration(config)
        grid.configuration = x.configuration
        cb = Shared_cable_extended(grid, config)
        grid.calc_shared_cable_cost()
        score = grid.total_cost

        return score, grid, config


    def greedy_config_sampling(self):
        """
        .
        """

        grid = Grid(51,self.grid_version)
        x = Greedy_configuration(grid)
        config = []
        while config == []:
            config = x.try_configuration()
        x.process_configuration(config)
        grid.configuration = x.configuration
        cb = Shared_cable_extended(grid, config)
        cb = Shared_cable_extended(grid, config)
        grid.calc_shared_cable_cost()
        score = grid.total_cost

        return score, grid, config


    def save_best(self, score_new, grid_new, config_new):
        """
        Saves the best current grid judged on score.
        """

        if score_new < self.best_score:
            self.best_grid = grid_new
            self.best_configuration = config_new
            self.best_score = score_new


    def make_hist(self):
        """
        .
        """

        if self.count == 0:
            return "No viable results"

        mu = np.mean(self.scores)
        sigma = np.std(self.scores)
        fig, ax = plt.subplots()
        _, bins, _ = ax.hist(self.scores, bins=50, density=True)

        y = ((1 / (np.sqrt(2 * np.pi) * sigma)) *np.exp(-0.5 * (1 / sigma * (bins - mu))**2))
        ax.plot(bins, y, '--')

        ax.set_xlabel('Costs')
        ax.set_ylabel('Probability density')
        ax.set_title(r'Grid Cost Probability')
        fig.tight_layout()
        plt.show()
        plt.savefig("saved_output/sample.")


    def make_csv_hist(self):
        """
        .
        """

        with open('saved_output/hist_plot.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            field = ["iteration", "cost"]
            count = 1

            writer.writerow(field)
            for i in self.scores:
                writer.writerow([count, i])
                count += 1
