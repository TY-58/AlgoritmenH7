#Partially taken from: https://matplotlib.org/stable/gallery/statistics/hist.html#sphx-glr-gallery-statistics-hist-py
#Partially taken from: https://www.tutorialspoint.com/drawing-average-line-in-histogram-in-matplotlib

NUMBER_OF_SAMPLES: int = 10000

import matplotlib.pyplot as plt
import numpy as np
import random
import csv
from loaders import load_houses, load_batteries
from battery import Battery
from cable import Cable
from house import House
from visualize import Gridplot
from json_output import output_json
from operator import itemgetter
##from greedy_match import Greedy_configuration
from cable_route import Cable_route
#from match_fred import Fred_configuration
#from random_match import Random_configuration
from grid import Grid
#from random_cable_route import Random_cable_route
from otto_greedy_match_improve import Otto_greedy_configuration
from combined_cable_route import Combined_cable_route
from otto_random_improve import Otto_cable_route


class Sampleplot:
    """ Takes random sample solutions and visualizes them in a histogram plot. """

    def __init__(self):
        self.scores = []
        self.count: int = 0
        self.get_scores()
        self.make_hist()
        self.make_csv_hist()

    def get_scores(self):
        print("starts get_scores")

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

            #sample of greedy config and combined route
            
            grid_1 = Grid(51,3)
            x = Otto_greedy_configuration(grid_1)
            config = []
            while config == []:
                config = x.try_configuration()
            x.process_configuration(config)
            cb = Combined_cable_route(grid_1, config)
            grid_1.calc_combined_cable_cost()
            

            #sample of greedy and A+
            # grid_1 = Grid(51,1)
            # x = Otto_greedy_configuration(grid_1)
            # config = []
            # while config == []:
            #     config = x.try_configuration()
            # x.process_configuration(config)
            # cb = Otto_cable_route(grid_1, config)
            # grid_1.calc_total_cable_cost()

            if grid_1.total_cost != 0:
                print(grid_1.total_cost)
                self.scores.append(grid_1.total_cost)
                self.count += 1

            #NTS: may print if not viable solution, make check.
        print(self.count)
        for score in self.scores:
            print(score)

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
        plt.savefig("sample.")

    def make_hist2(self):

        if self.count == 0:
            return "No viable results"

        plt.hist(self.scores, bins=2)
        plt.show()

    def make_csv_hist(self):

        with open('hist_plot1.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            field = ["iteration", "cost"]
            count = 1

            writer.writerow(field)
            for i in self.scores:
                writer.writerow([count, i])
                count += 1



