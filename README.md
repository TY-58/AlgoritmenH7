# The Charged Batteries

## Introduction

This project is about solving two problems. We are given a grid with houses and batteries, and the goal is to connect each house to a battery via the shortest possible cable route. The two problems are the maximum capacity of a battery and the different outpouts of each house. The second problem is the reducing the cost of the cables as much as possible by having houses sharing cables, which is only possible if the houses are connected to the same battery. 

This creates the main problem of the smartgrid assignment. How can you reduce as much of the cost while also making sure every house is connected to a battery and which not override the maximum capacity of the batteries.

## Approach

We have implemented the following algorithms to solve this problem:

1. **Random Algorithm**: We started by writing a random Algorithm. As could be understood from the name both the matching of houses and batteries (configuration) is random as the route to the matched battery from the house is randomized. This algorithm is not optimal and it is the most expansive algorithm that could be used for this problem

2. **Greedy Configuration with Pathfinder**: This Algorithm matches the houses to batteries by sorting from biggest output to smallest output and tries to match all the houses to a battery. While the configurations are mostly succesfull, it might be that the distance from houses to batteries are on the longer side. After the houses and batteries are matched the "pathfinder" tries to find the smallest distance for laying the cables. This is not determenistic since we introduced a probabilty for every choice the pathfinder can make. even though most of the time it will choose the smallest distance, it will try another route.
3. **Greedy Confuguration with Shared Cables**: This algorithm uses the same configuration as the previous algorithm, but the cable routes from houses to batteries is different. In this algoritm we try to not only find the shortest route, but also a way to share cables in order to reduce cost, since cables that go the same route share the costs.

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