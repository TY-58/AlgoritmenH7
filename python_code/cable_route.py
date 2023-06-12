from cable import Cable

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

        x_direction = abs(int(end_location[0] - start_location[0]))
        print(x_direction)
        y_direction = abs(int(end_location[1] - start_location[1]))
        print(y_direction)

        x_location = start_location[0]
        y_location = start_location[1]

        if x_direction < 0:

            for x_counter in range(abs(x_direction)):
                cable_route.append([x_location - x_counter, y_location])

            if y_direction < 0:

                for y_counter in range(abs(y_direction)):
                    cable_route.append([x_location + x_direction, y_location - y_counter])
            else:
                for y_counter in range(y_direction):
                    cable_route.append([x_location + x_direction, y_location + y_counter])


        else:
            for x_counter in range(x_direction):
                cable_route.append([x_location + x_counter, y_location])

        for y_counter in range(y_direction ):
            cable_route.append([x_location, y_location + y_counter])

        print(cable_route)
        return cable_route

    def lay_cables(self, configuration):
        """f"""

        for combination in configuration:
            route = self.make_route(combination[0], combination[1])
            cable = Cable(route)
            self.grid.cables.append(cable)
