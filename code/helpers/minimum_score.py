from __future__ import annotations
import copy

from code.visualisation.visualize import Gridplot
from .json_output import output_json

def update_minimum_score(minimum_score: int, grid: Grid):
    """
    Checks if current score is lower than minimum, updates and saves minimum score if so.
    """
    current_score = grid.total_cost

    if current_score < minimum_score:
        minimum_score = current_score

        # Save output of visualizer and json
        grid_visual: Gridplot = Gridplot(grid)
        grid_visual.make_plot()
        output_json(grid)
        print(f"New minimum score: {minimum_score}")
        return minimum_score
    else:
        return minimum_score