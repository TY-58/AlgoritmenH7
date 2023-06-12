from cable import Cable
from house import House

class Cable_route:
    """B"""
    def __init__(self, grid, configuration):
        """f"""

        self.grid = grid
        self.configuration = configuration
        self.lay_cables(configuration)

    def make_route(self, house, battery):
        """F"""
        cable_route = []

        start_location = house.location
        end_location = battery.location
        #print(start_location)
        #print(end_location)

        x_direction = abs(int(end_location[0] - start_location[0]))
        y_direction = abs(int(end_location[1] - start_location[1]))

        x_location = start_location[0]
        y_location = start_location[1]

        if start_location[0] > end_location[0]:
            for x_counter in range(x_direction):
                cable_route.append([x_location, y_location])
                x_location -= 1
                self.check_surroundings(x_location, y_location)
        else:
            for x_counter in range(x_direction):
                cable_route.append([x_location, y_location])
                x_location += 1
                self.check_surroundings(x_location, y_location)
            
        if start_location[1] > end_location[1]:
            for y_counter in range(y_direction + 1):
                cable_route.append([x_location, y_location])
                y_location -= 1
                self.check_surroundings(x_location, y_location)
            
        else:
            for y_counter in range(y_direction + 1):
                cable_route.append([x_location, y_location])
                y_location += 1
                self.check_surroundings(x_location, y_location)

        return cable_route

    #prints statement where path crosses with houses
    def check_surroundings(self, x_location, y_location):

        for house in self.configuration:
            if x_location == house[0].location[0]:
                print(x_location, house[0].location[0])
                print("path crosses house at x: ", x_location, "and y: ", house[0].location[1])
            elif y_location == house[0].location[1]:
                print(y_location, house[0].location[1])
                print("path crosses house at x: ", house[0].location[0], "and y: ", y_location)

    def lay_cables(self, configuration):
        """f"""

        for combination in configuration:
            route = self.make_route(combination[0], combination[1])
            cable = Cable(route)
            self.grid.cables.append(cable)
