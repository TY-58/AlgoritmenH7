# The Charged Batteries

## Introduction

This project is about solving two problems. We are given a grid with houses and batteries, and the goal is to connect each house to a battery via the shortest possible cable route. The two problems are the maximum capacity of a battery and the different outpouts of each house. The second problem is the reducing the cost of the cables as much as possible by having houses sharing cables, which is only possible if the houses are connected to the same battery. This creates the main problem of the smartgrid assignment. How can you reduce as much of the cost while also making sure every house is connected to a battery and does not override the maximum capacity of the batteries.

## Approach

We have implemented the following algorithms to solve this problem:

1. **Random Algorithm**: Waarom deze en hoe werkt het
2. **Greedy Configuration with Pathfinder**: 
3. **Greedy Confuguration with Shared Cables**: 

## Reproducing Results

To reproduce our results, follow these steps:

1. Clone this repository to your local machine.
2. Install the necessary Python packages listed in `requirements.txt` using pip: `pip install -r requirements.txt`
3. Run the main script with the desired algorithm: `python main.py` 

You can replace ` the algorithm` with the name of the algorithm you want to use (`Random Algorithm`, `Greedy Configuration with Pathfinder`, or `Greedy Confuguration with Shared Cables`) by changing the name of the algorithm in main.

## Authors

- Otto Jong
- Frederieke Loth
- Turhan Yildiz

## Acknowledgments

- Alle bronnen hier denk ik ?