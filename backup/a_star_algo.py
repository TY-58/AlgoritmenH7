import copy
from cable import Cable
from house import House

class DepthFirst:
    def __init__(self, grid, configuration):
        
        self.grid = grid
        self.configuration = configuration
        self.lay_cables(configuration)
        
        #self.grid = copy.deepcopy(grid)
        #self.batteries = batteries
        #self.houses = [copy.deepcopy(self.grid)]

       #self.best_solution = None
        #self.best_value = float('inf')

    def make_route(self, house, battery):
        """."""
        cable_route = []
        start_location = house.location
        end_location = battery.location

        # 0 --> distance
        queue = [(start_location, [start_location])]

        # Max number of tries
        max_locations = 1000000
        num_locations = 0

        while queue and num_locations < max_locations:
            (location, path) = queue.pop(0)
            num_locations += 1

            directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            for direction_x, direction_y in directions:
                new_location = (location[0] + direction_x, location[1] + direction_y)

                print('-', start_location, path, end_location, '-')
                if (0 <= new_location[0] < self.grid.size and
                    0 <= new_location[1] < self.grid.size and
                    new_location not in path):
                        if new_location == end_location:
                            print("succes")
                            return path + [new_location]
                        queue.append((new_location, path + [new_location]))

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
