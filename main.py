import random
from code.helpers.loaders import load_houses, load_batteries
from code.classes.battery import Battery
from code.classes.cable import Cable
from code.classes.house import House
from code.visualisation.visualize import Gridplot
from code.helpers.json_output import output_json
from operator import itemgetter
from code.algorithms.configurations.greedy_configuration import Greedy_configuration
#from code.algorithms.match_fred import Fred_configuration
from code.algorithms.configurations.random_configuration import Random_configuration
from code.classes.grid import Grid
from code.algorithms.cable_routes.random_cable_route import Random_cable_route
from code.algorithms.cable_routes.greedy_cable_route import Greedy_cable_route
#from code.algorithms.cable_routes.shared_cable_route import Shared_cable_route
from code.algorithms.cable_routes.shared_cable_extended import Shared_cable_extended
from code.visualisation.sampling import Sampleplot
from code.algorithms.hillclimber import Hillclimber


if __name__ == '__main__':
    #sample = Sampleplot()

    #een-na
    # grid_1 = Grid(51,1)
    # x = Greedy_configuration(grid_1)
    # config = []
    # while config == []:
    #     config = x.try_configuration()
    # x.process_configuration(config)
    # cb = Greedy_cable_route(grid_1, config)
    # grid_1.calc_total_cable_cost()
    # grid_1_visual = Gridplot(grid_1)
    # grid_1_visual.make_plot()


    #beste
    for _ in range(10000):
        grid_1 = Grid(51,3)
        x = Random_configuration(grid_1)
        config = []
        while config == []:
            config = x.try_configuration()
        x.process_configuration(config)
        cb = Shared_cable_extended(grid_1, config)
        grid_1.calc_shared_cable_cost()
        # grid_1_visual = Gridplot(grid_1)
        # grid_1_visual.make_plot()
        print(grid_1.total_cost)
    #
        # output_json(grid_1)

    # #random route and config
    # grid_1 = Grid(51,1)
    # config = Random_configuration(grid_1)
    # x = config.make_configuration()
    # cb = Random_cable_route(grid_1, x)
    # grid_1_visual = Gridplot(grid_1)
    # grid_1_visual.make_plot()

    # minimum = 40000
    # for _ in range(2000):
    #     grid_1 = Grid(51,3)
    #     x = Greedy_configuration(grid_1)
    #     config = x.make_configuration()
    #     x.process_configuration(config)
    #     cb = Shared_cable_route(grid_1, config)
    #     grid_1.calc_shared_cable_cost()
    #     if grid_1.total_cost < minimum:
    #         minimum = grid_1.total_cost
    #         print(minimum)
    #         grid_1_visual = Gridplot(grid_1)
    #         grid_1_visual.make_plot()
    #         output_json(grid_1)


    #HILLCLIMBER
    # grid_1 = Grid(51,1)
    # x = Greedy_configuration(grid_1)
    # config = []
    # while config == []:
    #     config = x.try_configuration()
    # x.process_configuration(config)
    # grid_1.configuration = x.configuration
    # cb = Shared_cable_route(grid_1, config)
    # grid_1.calc_shared_cable_cost()
    # #print(grid_1.total_cost)
    # hclimb = Hillclimber(grid_1)
    # hclimb.do_mutate()
    # grid_1_visual = Gridplot(grid_1)
    # grid_1_visual.make_plot()

    # x = []
    # while x == []:
    #     x = config.try_configuration()
    # cb = Greedy_cable_route(grid_1, x)
    #grid_1_visual = Gridplot(grid_1)
    #grid_1_visual.make_plot()

    #grid_1.calc_total_cable_cost()
    #print(grid_1.total_cost)



    # x = Greedy_configuration(grid_1)
    #
    # config = x.try_configuration()
    # cb = Greedy_cable_route(grid_1, config)
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
    # minimum = 40000
    # for _ in range(0,1):
    #     grid_1 = Grid(51,1)
    #     x = Greedy_configuration(grid_1)
    #     config = []
    #     while config == []:
    #         config = x.try_configuration()
    #         #print(config)
    #
    #     #print(config)
    #     x.process_configuration(config)
    #     if config != []:
    #         print('hey')
    #         cb = Shared_cable_route(grid_1, config)
    #     grid_1.calc_shared_cable_cost()
    #     print(grid_1.total_cost)
    #     if grid_1.total_cost < minimum:
    #         minimum = grid_1.total_cost
    #     if minimum < 25000:
    #         print(minmum)
    #         raise ValueError ("te laag")
    #     grid_1_visual = Gridplot(grid_1)
    #     grid_1_visual.make_plot()

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
    #grid_1.calc_shared_cable_cost()
    # print(minimum)



#     #output_json(grid_1)
 #   minimum = 40000
#     for _ in range(0,5000):
#         grid_1 = Grid(51,1)
#         x = Greedy_configuration(grid_1)
#         config = []
#         while config == []:
#             config = x.try_configuration()
#             #print(config)

#         #print(config)
#         x.process_configuration(config)
#         if config != []:
#             print('hey')
#             cb = Shared_cable_route(grid_1, config)
        # grid_1.calc_shared_cable_cost()
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
#     grid_1.calc_shared_cable_cost()
#     print(grid_1.total_cost)
    # grid_1_visual = Gridplot(grid_1)
    # grid_1_visual.make_plot()

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
