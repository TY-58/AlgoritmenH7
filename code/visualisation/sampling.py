#Partially taken from: https://matplotlib.org/stable/gallery/statistics/hist.html#sphx-glr-gallery-statistics-hist-py
#Partially taken from: https://www.tutorialspoint.com/drawing-average-line-in-histogram-in-matplotlib

NUMBER_OF_SAMPLES: int = 1000

import matplotlib.pyplot as plt
import numpy as np
import random
import csv
from code.helpers.loaders import load_houses, load_batteries
from .visualize import Gridplot
from code.helpers.json_output import output_json
from operator import itemgetter
from code.classes.grid import Grid
from code.algorithms.configurations.greedy_configuration import Greedy_configuration
from code.algorithms.configurations.random_configuration import Random_configuration
from code.algorithms.cable_routes.shared_cable_extended import Shared_cable_extended


class Sampleplot:
    """
    Takes random sample solutions and visualizes them in a histogram plot.
    """

    def __init__(self):
        self.scores: list[int] = []
        self.count: int = 0
        self.get_scores()
        self.make_hist()
        self.make_csv_hist()
        self.best_grid = []
        self.best_configuration = []

    def get_scores(self):

        count = 0
        for n in range(NUMBER_OF_SAMPLES):
            count += 1
            print("enters range #", count)
            #sample of random algorithm
            """
            grid_1 = Grid(51,1)
            x = Random_configuration(grid_1)
            config = x.make_configuration()
            cb = Random_cable_route(grid_1, config)
            grid_1.calc_total_cable_cost()
            """

            #sample of greedy config and shared route

            grid_1 = Grid(51,3)
            x = Greedy_configuration(grid_1)
            config = []
            while config == []:
                config = x.try_configuration()
            x.process_configuration(config)
            cb = Shared_cable_extended(grid_1, config)
            grid_1.calc_shared_cable_cost()


            #sample of greedy and A+
            # grid_1 = Grid(51,1)
            # x = Greedy_configuration(grid_1)
            # config = []
            # while config == []:
            #     config = x.try_configuration()
            # x.process_configuration(config)
            # cb = Greedy_cable_route(grid_1, config)
            # grid_1.calc_total_cable_cost()

            if grid_1.total_cost != 0:
                if self.count == 0:
                    self.best_grid = grid_1
                    self.best_configuration = config
                    self.best_score = grid_1.total_cost
                else:
                    self.save_best(grid_1.total_cost, grid_1, config)

                self.scores.append(grid_1.total_cost)
                self.count += 1

            #NTS: may print if not viable solution, make check.
            print(self.count)
            for score in self.scores:
                print(score)

    def save_best(self, score_new, grid_new, config_new):
        """
        Saves the best current grid judged on score.
        """
        if score_new < self.best_score:
            self.best_grid = grid_new
            self.best_configuration = config_new
            self.best_score = score_new


    def make_hist(self):

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

    def make_hist2(self):

        if self.count == 0:
            return "No viable results"

        plt.hist(self.scores, bins=2)
        plt.show()

    def make_csv_hist(self):

        with open('saved_output/hist_plot1.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            field = ["iteration", "cost"]
            count = 1

            writer.writerow(field)
            for i in self.scores:
                writer.writerow([count, i])
                count += 1
