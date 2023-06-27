from __future__ import annotations

def update_best_grid(grid: Grid, best_grid: Grid):
    """
    Checks if current score is lower than minimum, updates and saves minimum score if so.
    """

    if grid.total_cost < best_grid.total_cost:

        return grid
    else:
        return best_grid
