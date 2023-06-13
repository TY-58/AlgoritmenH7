
class Random_cable_route:
    """Lay random cable"""

    def __init__(self, grid, configuration):
        """."""

        self.grid = grid
        self.configuration = configuration
        self.lay_cables(configuration)


    def make_route(self, house, battery):
        """Start route from a house to battery."""


        cable_route = []
        current_location = house.location
        end_location = battery.location

        route.append(current_location)

        while current_location != end_location:

            directions = self.get_directions(current_location)
            direction = random.choice(directions)
            if direction == 'd':
                current_location[1] -= 1

            if direction == 'u':
                current_location[1] += 1

            if direction == 'l':
                current_location[0] -= 1

            if direction == 'r':
                current_location[0] += 1

            route.append(current_location)

        route.append(current_location)

        return cable_route

    #make route
    def get_directions(self, current_location):
        """Get all possible directions from current position"""
        x_location = current_location[0]
        y_location = current_location[1]
        directions = []

        if y_location > 0 and self.grid[y_location-1][x_location] != 1:
            directions.append('d')
        if y_location < 50 and self.grid[y_location+1][x_location] != 1:
            directions.append('u')
        if x_location > 0 and self.grid[y_location][x_location-1] != 1:
            directions.append('l')
        if x_location < 50 and self.grid[y_location][x_location+1] != 1:
            directions.append('r')

        return directions


    def lay_cables(self, configuration):
        """."""
        count = 0
        for combination in configuration:
            route = self.make_route(combination[0], combination[1])
            cable = Cable(route)
            self.grid.cables.append(cable)
            count += 1
        print(count)
