# The Charged Batteries

## Introduction

In this project we are tasked with a case named SmartGrid. We are given a 3 grids with houses and batteries, and the goal is to connect each house to a battery via the shortest possible cable route. This poses two problems, that we tackle seperately. The first of them is fitting each house with a corresponding maximum output on a battery without exceeding the capacity of the battery. Secondly, we want to lay cables from houses to batteries as efficiently as possible as to reduce the costs. Here, cables coming from different houses may be connected to each other if they are connected to the same battery.

This creates the main problem of the SmartGrid case: How can you reduce as much of the cost while also making sure every house is connected to a battery and without exceeding the maximum capacity of the batteries?

## Approach

We have implemented different configurations that match houses with batteries and have implemented different ways for a route to be laid from houses to batteries:

### Configurations

1. **Random Configuration**: The random Configuration randomly assigns batteries to houses until there is a match for every house with a battery without exceeding the capacity of the batteries. It restarts if the current configuration is invalid and will therefore always return a valid solution. Additionally, this configuration does not take the distance from house to battery in consideration when making the match. 

2. **Greedy Configuration**: This configuration takes the output of all the houses into account before making a match. Additionally, it considers the distance from the house to different batteries and prefers a match with a battery that is closer. There are 3 different options with this configuration. You can choose for a configuration where the houses with the biggest output are matched first and the houses with the smallest output last. Then there is the option to do the opposite, thus the houses with the smallest outputs are matched first, and the houses with the biggest output are last. Finally we have an implementation that randomly matches the houses with the batteries.  

### Cable Routes

1. **Random Cable Route**: This cable route algorithm does not take into consideration whether it takes the shortest route, nor does it look prefer a path that alligns with another path to the same battery in order to save cost, as the name suggest every step in this algorithm is random. However, a hard constraint has been set such that cables do not directly connect 2 batteries with each other.

2. **Shared Cable route**: The shared cable route finds the center point of the houses connected to a battery and lays a cable from that point to the battery. Each house, starting from the furthest house, is then laid to connect to the closest unit on this center cable or any previously laid cable to the same battery. Costs are therefore minimized by sharing cables.

### Hillclimber

This Hillclimber algorithm takes an already made grid from any combination of configuration with the Shared Cable Route. A provided variable (conned iterations) dictates how many times the algorithm can try to improve the current state without any improvement before quitting. This variable resets when a better state has been found within this set number of iterations. During the algorithm two matches within the configuration list are tasked to swap batteries after which cables are laid again. If the cost of the new grid is improved, it is taken as the current state and the provided variable is reset. The hillclimber is only possible with the shared cable route.

## Requirements
You will need to Download at least Python3 version == 3.10.9

In order to execute our code, follow these steps:

1. Clone this repository to your local machine.
2. Install the necessary Python packages listed in `requirements.txt` using pip:
```bash
pip3 install -r requirements.txt
```

Or with Conda:
```bash
conda install --file requirements.txt
```


## Usage

Start by running the main script in the terminal with: `python main.py`

While running main.py you will have to answer a couple of questions as posed in the terminal. Please do not deviate from the specified input (for example pressing '1' where 'y' or 'n' is asked):

### Usage Example

This is an example on how to run main.py.

1. Choose the configuration
```bash
Which configuration do you want to run:
1. Random (baseline) (type: '1') or
2. Greedy (type: '2')?
Type configuration:.
```
press 2 and hit enter.

2. Choose the configuration you want to run (matching houses with batteries): 1 = Random, 2 = Greedy. Press the number of the configuration you wish to run. Hit enter.

3. (Only if Greedy configuration is chosen) Choose in which order you want to assign the houses to the batteries: 1 = Max output first, 2 = Lowest output first and 3 = random. Hit enter.

4. Choose the cable route algorithm you would like to run: 1 = Random, 2 = Greedy.

5. Type in the number of times you would like the programme to run. Hit enter.

6. (Only if Greedy cable route is chosen) Choose if you want to run hillclimber. If you would like to run hill climber press 'y', if not press 'n' and hit enter.

7. (Only if Hillclimber is chosen) Type the number of times you would like the hillclimber to try improvements without finding a better solution. this number is reset after every improvement. Hit enter.

8. (Only if iterations > 0) Choose if you want to plot a histogram of the results. press 'y' if you do and 'n' if you do not. Hit enter.

9. (only if a Histogram is chosen) Choose the number of bins to be displaced in the histogram. Type in the number, preferably lower than the specified number of iterations. Hit enter.





1. The first question is about the Grid. There are 3 different Grids, which one would you like to run? Press the grid number and hit enter.

2. Choose the configuration you want to run (matching houses with batteries): 1 = Random, 2 = Greedy. Press the number of the configuration you wish to run. Hit enter.

3. (Only if Greedy configuration is chosen) Choose in which order you want to assign the houses to the batteries: 1 = Max output first, 2 = Lowest output first and 3 = random. Hit enter.

4. Choose the cable route algorithm you would like to run: 1 = Random, 2 = Greedy.

5. Type in the number of times you would like the programme to run. Hit enter.

6. (Only if Greedy cable route is chosen) Choose if you want to run hillclimber. If you would like to run hill climber press 'y', if not press 'n' and hit enter.

7. (Only if Hillclimber is chosen) Type the number of times you would like the hillclimber to try improvements without finding a better solution. this number is reset after every improvement. Hit enter.

8. (Only if iterations > 0) Choose if you want to plot a histogram of the results. press 'y' if you do and 'n' if you do not. Hit enter.

9. (only if a Histogram is chosen) Choose the number of bins to be displaced in the histogram. Type in the number, preferably lower than the specified number of iterations. Hit enter.

After following all these steps the results will be saved in the saved_output folder. You will find the JSON output (the full route per house), pic.png (visual of the best result) and finally a graph with the grid cost probability (probability of value for x amount of runs).

## Structure
The following list contains the most important maps and brief explanations.

- code
    - algorithms
        - cable_routes: contains the cable route algorithms for this case
        - configurations: contains configuration algorithms for this case
    - classes: contains all 4 neccesary classes for this case
    - visualisation
- data_grids: contains csv files with information house and battery information per district
- saved_ouput: contains generated output after a run

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