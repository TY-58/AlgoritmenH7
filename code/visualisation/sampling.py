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

from code.algorithms.cable_routes.shared_cable_route import Shared_cable_route
from code.algorithms.configurations.greedy_configuration import Greedy_configuration
from code.algorithms.configurations.random_configuration import Random_configuration
from code.algorithms.cable_routes.shared_cable_route import Shared_cable_route


class Sampleplot:
    """
    Takes random sample solutions and visualizes them in a histogram plot.
    """


    def __init__(self, score_list: list[int], bin_size: int):
        """
        Takes a generated score list and bin size and saves the information.
        Generates a histogram based on this input.
        """

        self.scores = score_list
        self.bin_size = bin_size
        self.make_hist()
        self.make_csv_hist()


    def make_hist(self) -> None:
        """
        Makes the histogram.
        Calculates y as a probability density function.
        Costs/ scores are assigned to the x-axis.
        """

        mu = np.mean(self.scores)
        sigma = np.std(self.scores)
        fig, ax = plt.subplots()
        _, bins, _ = ax.hist(self.scores, bins=self.bin_size, density=True)

        y = ((1 / (np.sqrt(2 * np.pi) * sigma)) *np.exp(-0.5 * (1 / sigma * (bins - mu))**2))
        ax.plot(bins, y, '--')

        ax.set_xlabel('Costs')
        ax.set_ylabel('Probability density')
        ax.set_title(r'Grid Cost Probability')
        fig.tight_layout()
        plt.savefig("saved_output/sample.")


    def make_csv_hist(self) -> None:
        """
        Makes a csv file of the scores plotted in the histogram.
        """

        with open('saved_output/hist_plot.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            field = ["iteration", "cost"]
            count = 1

            writer.writerow(field)
            for i in self.scores:
                writer.writerow([count, i])
                count += 1
