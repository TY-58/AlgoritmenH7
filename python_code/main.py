import random
from loaders import load_houses, load_batteries
from battery import Battery
from cable import Cable
from house import House
from visualize import Gridplot
from json_output import output_json
from operator import itemgetter
from greedy_match import Greedy_configuration
from otto_greedy_match_improve import Otto_greedy_configuration
from cable_route import Cable_route
from match_fred import Fred_configuration
from random_match import Random_configuration
from grid import Grid
from random_cable_route import Random_cable_route
from otto_random_improve import Otto_cable_route
from sampling import Sampleplot
from combined_cable_route import Combined_cable_route
from otto_random_improve import Otto_cable_route
from sampling import Sampleplot
#from hillclimber import Hillclimber


if __name__ == '__main__':
    sample = Sampleplot()

    #een-na
    grid_1 = Grid(51,1)
    x = Otto_greedy_configuration(grid_1)
    config = []
    while config == []:
        config = x.try_configuration()
    x.process_configuration(config)
    cb = Otto_cable_route(grid_1, config)
    grid_1.calc_total_cable_cost()
    grid_1_visual = Gridplot(grid_1)
    grid_1_visual.make_plot()


    #beste
    # grid_1 = Grid(51,3)
    # x = Otto_greedy_configuration(grid_1)
    # config = []
    # while config == []:
    #     config = x.try_configuration()
    # x.process_configuration(config)
    # cb = Combined_cable_route(grid_1, config)
    # grid_1.calc_combined_cable_cost()
    # grid_1_visual = Gridplot(grid_1)
    # grid_1_visual.make_plot()

    # #random route and config
    # grid_1 = Grid(51,1)
    # config = Random_configuration(grid_1)
    # x = config.make_configuration()
    # cb = Random_cable_route(grid_1, x)
    # grid_1_visual = Gridplot(grid_1)
    # grid_1_visual.make_plot()

    #make = Fred_configuration(grid_1)

    # grid_1 = Grid(51,1)
    # x = Otto_greedy_configuration(grid_1)
    # config = []
    # while config == []:
    #     config = x.try_configuration()
    # x.process_configuration(config)
    # cb = Otto_cable_route(grid_1, config)
    # grid_1_visual = Gridplot(grid_1)
    # grid_1_visual.make_plot()
    # print(x)
    # print(grid_1.configuration)

     #beste
    # grid_1 = Grid(51,1)
    # x = Otto_greedy_configuration(grid_1)
    # config = []
    # while config == []:
    #     config = x.try_configuration()
    # x.process_configuration(config)
    # cb = Combined_cable_route(grid_1, config)
    # grid_1.calc_combined_cable_cost()
    # grid_1_visual = Gridplot(grid_1)
    # grid_1_visual.make_plot()
    

    grid_1 = Grid(51,1)
    x = Fred_configuration(grid_1)
    config = []
    while config == []:
        config = x.try_configuration()
    x.process_configuration(config)
    grid_1.configuration = x.configuration
    cb = Combined_cable_route(grid_1, config)
    grid_1.calc_combined_cable_cost()
    #print(grid_1.total_cost)
    hclimb = Hillclimber(grid_1)
    hclimb.do_mutate()


    # x = []
    # while x == []:
    #     x = config.try_configuration()
    # cb = Otto_cable_route(grid_1, x)
    #grid_1_visual = Gridplot(grid_1)
    #grid_1_visual.make_plot()

    #grid_1.calc_total_cable_cost()
    #print(grid_1.total_cost)



    # x = Otto_greedy_configuration(grid_1)
    #
    # config = x.try_configuration()
    # cb = Otto_cable_route(grid_1, config)
    #
    # grid_1.calc_total_cable_cost()
    # print(grid_1.total_cost)
    #
    # grid_1 = Grid(51,1)
    # x = Fred_configuration(grid_1)
    # config = x.make_configuration()
    # cb = Random_cable_route(grid_1, config)
    #
    # #for cable in grid_1.cables:
    #  #   print(cable.route)
    #   #  print(cable.cable_length())
    #
    # grid_1.calc_total_cable_cost()
    # grid_1_visual = Gridplot(grid_1)
    # grid_1_visual.make_plot()

    #output_json(grid_1)
    minimum = 40000
    for _ in range(0,1):
        grid_1 = Grid(51,1)
        x = Otto_greedy_configuration(grid_1)
        config = []
        while config == []:
            config = x.try_configuration()
            #print(config)

        #print(config)
        x.process_configuration(config)
        if config != []:
            print('hey')
            cb = Combined_cable_route(grid_1, config)
        grid_1.calc_combined_cable_cost()
        print(grid_1.total_cost)
        if grid_1.total_cost < minimum:
            minimum = grid_1.total_cost
        if minimum < 25000:
            print(minmum)
            raise ValueError ("te laag")
        grid_1_visual = Gridplot(grid_1)
        grid_1_visual.make_plot()

        # for cable in grid_1.cables:
            # for loc in range(len(cable.route) - 1) :
            #     if abs(cable.route[loc][0] - cable.route[loc + 1][0]) + abs(cable.route[loc][1] - cable.route[loc + 1][1]) != 1:
            #         print(cable.route)
            #         raise ValueError ("misss")

    # for battery in grid_1.batteries:
    #     b = battery.location
    #     for cable in grid_1.cables:
    #         for loc in cable.route:
    #             if b == loc:
    #                 print("over bat")

    #for cable in grid_1.cables:
     #   print(cable.route)
      #  print(cable.cable_length())

    #grid_1.calc_total_cable_cost()
    #grid_1.calc_combined_cable_cost()
    # print(minimum)
    # grid_1_visual = Gridplot(grid_1)
    # grid_1_visual.make_plot()

    # output_json(grid_1)


#     #output_json(grid_1)
 #   minimum = 40000
#     for _ in range(0,5000):
#         grid_1 = Grid(51,1)
#         x = Otto_greedy_configuration(grid_1)
#         config = []
#         while config == []:
#             config = x.try_configuration()
#             #print(config)

#         #print(config)
#         x.process_configuration(config)
#         if config != []:
#             print('hey')
#             cb = Combined_cable_route(grid_1, config)
        # grid_1.calc_combined_cable_cost()
        # print(grid_1.total_cost)
        # if grid_1.total_cost < minimum:
        #     minimum = grid_1.total_cost
        # if minimum < 25000:
        #     print(minmum)
        #     raise ValueError ("te laag")

#     # for battery in grid_1.batteries:
#     #     b = battery.location
#     #     for cable in grid_1.cables:
#     #         for loc in cable.route:
#     #             if b == loc:
#     #                 print("over bat")

#     #for cable in grid_1.cables:
#      #   print(cable.route)
#       #  print(cable.cable_length())

#     #grid_1.calc_total_cable_cost()
#     grid_1.calc_combined_cable_cost()
#     print(grid_1.total_cost)
#     grid_1_visual = Gridplot(grid_1)
#     grid_1_visual.make_plot()

#     #output_json(grid_1)


#     #     print(cable.route)
#     #    print(cable.cable_length())
#     # grid_1.calc_total_cable_cost()
#     # print(grid_1.total_cost)
#     # if grid_1.total_cost != 25000:
#     #     x.process_configuration(config)
#     #     for battery in grid_1.batteries:
#     #         print(cb.find_center_location(battery))
#     #
#     #
#     cable_length = 0
#     for cable in grid_1.cables:
#         cable_length += cable.cable_length()
#     #print(cable_length)
#     # output_json(grid_1)
#    # grid_1_visual = Gridplot(grid_1)
#     #grid_1_visual.make_plot()
    #     print(cable.route)
    #    print(cable.cable_length())
    # grid_1.calc_total_cable_cost()
    # print(grid_1.total_cost)
    # if grid_1.total_cost != 25000:
    #     x.process_configuration(config)
    #     for battery in grid_1.batteries:
    #         print(cb.find_center_location(battery))
    #
    #



    #print(cable_length)
    # output_json(grid_1)
   # grid_1_visual = Gridplot(grid_1)
    #grid_1_visual.make_plot()