from cable import Cable
from house import House

class Cable_route:
    """A class for deciding the route for the cables from a house to a battery. """

    def __init__(self, grid, configuration):
        """."""

        self.grid = grid
        self.configuration = configuration
        self.lay_cables(configuration)

    def make_route(self, house, battery):
        """."""
        cable_route = []

        start_location = house.location
        end_location = battery.location

        x_direction = abs(int(end_location[0] - start_location[0]))
        y_direction = abs(int(end_location[1] - start_location[1]))

        x_location = start_location[0]
        y_location = start_location[1]

        check = True

        if start_location[0] > end_location[0]:
            for x_counter in range(x_direction):
                if x_location != start_location[0]:
                    check = self.check_surroundings(x_location, y_location)
                cable_route.append([x_location, y_location])
                x_location -= 1

        elif start_location[0] < end_location[0]:
            for x_counter in range(x_direction):
                if x_location != start_location[0]:
                    check = self.check_surroundings(x_location, y_location)
                cable_route.append([x_location, y_location])
                x_location += 1

        if start_location[1] > end_location[1]:
            for y_counter in range(y_direction + 1):

                if y_location != start_location[1]:
                    check = self.check_surroundings(x_location, y_location)
                cable_route.append([x_location, y_location])
                y_location -= 1

        elif start_location[1] < end_location[1]:
            for y_counter in range(y_direction + 1):

                if y_location != start_location[1]:
                    check = self.check_surroundings(x_location, y_location)
                cable_route.append([x_location, y_location])
                y_location += 1

        return cable_route

    def check_surroundings(self, x_location, y_location):
        """ Prints a statement if route crosses with house. """
        for combination in self.configuration:
            house = combination[0]
            if house.location[0] == x_location and house.location[1] == y_location:
                print("This path crosses a house at x, y: ", x_location, y_location)
                return False
        return True

    def lay_cables(self, configuration):
        """."""
        for combination in configuration:
            route = self.make_route(combination[0], combination[1])
            cable = Cable(route)
            #append niet aan cables in de grid
            self.grid.cables.append(cable)


    #def check_free_path(self, x_location, y_location, direction):
        #if direction == 'u':
            #if grid.
        #elif direction == 'd':
