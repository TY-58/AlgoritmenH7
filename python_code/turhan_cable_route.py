from cable import Cable
from house import House

class Turhan_cable_route:
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

        # 0 --> distance
        queue = [(start_location, [start_location], 0)]

        # Max number of tries
        max_locations = 100
        num_locations = 0

        while queue and num_locations < max_locations:
            (location, path, _) = queue.pop(0)
            num_locations += 1

            directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            for direction_x, direction_y in directions:
                new_location = (location[0] + direction_x, location[1] + direction_y)

                if (0 <= new_location[0] < self.grid.size and
                    0 <= new_location[1] < self.grid.size and
                    new_location not in path):
                        distance = abs(new_location[0] - end_location[0]) + abs(new_location[1] - end_location[1])
                        #print('-', start_location, path, end_location, distance, '-')
                        if distance == 0:
                            #print("succes")
                            return path + [new_location]
                        queue.append((new_location, path + [new_location], distance))
            queue.sort(key=lambda x: x[2])

        return cable_route


    def lay_cables(self, configuration):
        """."""
        count = 0
        for combination in configuration:
            route = self.make_route(combination[0], combination[1])
            cable = Cable(route)
            self.grid.cables.append(cable)
            count += 1
        print(count)


