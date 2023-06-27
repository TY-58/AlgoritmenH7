# The Charged Batteries

## Introduction

This project is about solving two problems. We are given a grid with houses and batteries, and the goal is to connect each house to a battery via the shortest possible cable route. The two problems are the maximum capacity of a battery and the different outpouts of each house. The second problem is the reducing the cost of the cables as much as possible by having houses sharing cables, which is only possible if the houses are connected to the same battery.

This creates the main problem of the smartgrid assignment. How can you reduce as much of the cost while also making sure every house is connected to a battery and which not override the maximum capacity of the batteries.

## Approach

We have implemented different configurations that match houses with batteries and we have implemented different ways a route for the cables are laid from houses to the battery:

### Configurations

1. **Random Configuration**: We started to write a random Configuration that keeps running (thus tryin a lot of different states) until there is a match for every house with a battery. This configuration therefore does not take the distance from house to battery in consideration when making the match. 

2. **Greedy Configuration**: This configuration takes the output of all the houses into account before making a match. There are 3 different options with this configuration. You can choose for a configuration where the houses with the biggest output are matched first and the houses with the smallest output last. Then there is the option to do the opposite, thus the houses with the smallest outputs are matched first, and the houses with the biggest output are last. Finally we have an implementation that randomly matches the houses with the batteries.

### Cable Routes

1. **Random Cable Route**: This is cable route algorithm does not take into consideration whether it takes the shortest route, nor does it look whether it follows a path where other cables to the same battery run in order to save cost, as the name suggest every step in this algorithm is random. However it does not lay cables that connect 2 batteries with each other since that is a hard constraint.

2. **Shared Cable route**: The Shared cable route algorithm takes into consideration the shortest distance from an house to a battery, but it also tries to minimize the cost by sharing cables as much as it can. The algorithm looks for houses that have to go to the same battery, and then tries to find the cheapest way to get to the battery by sharing the cables as much as possible.


### Hillclimber

The Hillclimber algorithm starts running after the matches are made and the cables have been laid. The hillclimber then looks if it can find better matches, where the distance from the house to the battery is shorter and will make the change if its within the maximum capacity of the battery. The hillclimber will run as long it can find a better configuration, and will stop if it can't find a better match after a certain amount tries (you can provide the max iterations withouth improvement for the hillclimber to stop in the command line). If the hillclimber is done running, the shared cable route will then rearrange the cables in order to minimize the costs. The hillclimber is only possible with the shared cable route.

## Reproducing Results
You will need to Download at least Python3 version == 3.10.9

To reproduce our results, follow these steps:

1. Clone this repository to your local machine.
2. Install the necessary Python packages listed in `requirements.txt` using pip:
```bash
pip3 install -r requirements.txt
```

Or with Conda:
```bash
conda install --file requirements.txt
```

3. Run the main script with the desired algorithm: `python main.py`

After running main.py you will have to answer a couple questions:
1. The first question is about the Grid. There are 3 different Grids, which one would you like to run ? press the grid number and hit enter.
2. Choose configuration you want to run (matching houses with batteries). 1 = random, 2 = Greedy. Press the number of the configuration you wish to run and press enter.
3. Choose the cable route algorithm you would like to run. 1 = Random, 2, greedy cable route without sharing cables, 3 = Greedy route with sharing cables.
4. type in the number of times you would like the programme to run, and press enter.
5. If you chose for greedy route with sharing cables, there is the additional option of hillclimber. If you would like to run hill climber press y, if not press n and hit enter.
6. If you did run Hillclimber, type in the number of times you would the hillclimber to run without finding a better solution.

After following all these steps the results will be saved in the Saved_output folder. You will find the JSON output (the full route per house), pic.png (visual of the best result) and finally a graph with the grid cost probability (probability of value for x amount of runs).
## Authors

- Otto Jong
- Frederieke Loth
- Turhan Yildiz

## Acknowledgments
Code from third parties:

Loaders.py:
-   https://earthly.dev/blog/csv-python/
-   https://linuxhint.com/skip-header-row-csv-python/

Sampling.py:
-   Partially taken from: https://matplotlib.org/stable/gallery/statistics/hist.html#sphx-glr-gallery-statistics-hist-py
-   Partially taken from: https://www.tutorialspoint.com/drawing-average-line-in-histogram-in-matplotlib

Json_output.py:
-   https://www.geeksforgeeks.org/reading-and-writing-json-to-a-file-in-python/ 

Visualize.py
-   https://matplotlib.org/stable/plot_types/basic/step.html#sphx-glr-plot-types-basic-step-py