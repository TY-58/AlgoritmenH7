import random
from loaders import load_houses, load_batteries
from battery import Battery
from cable import Cable
from house import House
from visualize import Gridplot


class Grid:
    """A class that stores all the data to play Crowther's Adventure. It loads
    all the rooms from a game text-file. It also keeps track of the current room
    and the player's inventory."""

    def __init__(self, size: int, district: int):
        """Creates the grid with all relevant information on coordinates."""

        # initialize
        self.district = district
        self.size: int = size
        self.grid: list[list[int]] = []
        self.houses = []
        self.batteries = []
        self.cables = []
        self.initialize_grid()

    def initialize_grid(self) -> None:
        """Function that initializes a grid with the correct sizing. Fills every
        spot with a 0."""

        for height in range(self.size):
            self.grid.append([])
            for width in range(self.size):
                self.grid[height].append(0)


    def process_houses(self) -> None:
        """ Loads
        """
        houses_data = load_houses(self.district)

        for house_row in houses_data:
            x_location = int(house_row[0])
            y_location = int(house_row[1])
            max_output = house_row[2]

            house = House(x_location, y_location, max_output)
            self.houses.append(house)
            self.grid[y_location][x_location] = 1

        return None

    def process_batteries(self) -> None:
        """ Loads
        """
        batteries_data = load_batteries(self.district)

        for battery_row in batteries_data:
            x_location = int(battery_row[0])
            y_location = int(battery_row[1])
            max_capacity = battery_row[2]

            battery = Battery(x_location, y_location, max_capacity)
            self.batteries.append(battery)
            self.grid[y_location][x_location] = 2

        return None

    def print_grid(self):
        for row in self.grid:
            for place in row:
                if place == 0:
                    print(" ", end="")
                if place == 1:
                    print("#", end="")
                if place == 2:
                    print("+", end="")
                if place == 3:
                    print("/", end="")
            print("")

    def make_route(self, house_id: int):
        """Start route from a house."""
        for house in self.houses:
            if house.id == house_id:
                x_location = house.location[0]
                y_location = house.location[1]
                current_house = house
                break

        if self.grid[y_location][x_location] != 1:
            print("This coordinate does not contain a house")

        else:
            route = []
            route.append([x_location, y_location])
            while self.battery_found(x_location, y_location) == []:

                directions = self.get_directions(x_location, y_location)
                direction = random.choice(directions)
                if direction == 'd':
                    y_location -= 1

                if direction == 'u':
                    y_location += 1

                if direction == 'l':
                    x_location -= 1

                if direction == 'r':
                    x_location += 1

                route.append([x_location, y_location])

            route.append(self.battery_found(x_location, y_location))

            cable = Cable(route)
            self.cables.append(cable)

            current_house.connected = True

            for coordinate in route:
                if self.grid[coordinate[1]][coordinate[0]] == 0:
                    self.grid[coordinate[1]][coordinate[0]] = 3

    def get_directions(self, x_location: int, y_location: int):
        """Get all possible directions from current position"""
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

    def battery_found(self, x_location: int, y_location: int):
        """Function that checks if a battery is adjacent to current location"""

        if y_location > 0 and self.grid[y_location-1][x_location] == 2:
            return [x_location, y_location-1]

        if y_location < 50 and self.grid[y_location+1][x_location] == 2:
            return [x_location, y_location+1]

        if x_location > 0 and self.grid[y_location][x_location-1] == 2:
            return [x_location-1, y_location]

        if x_location < 50 and self.grid[y_location][x_location+1] == 2:
            return [x_location+1, y_location]

        return []


    def lay_cables(self):
        for house in self.houses:
            self.make_route(house.id)

if __name__ == '__main__':
    grid_1 = Grid(51,1)
    grid_1.process_houses()
    grid_1.process_batteries()
    grid_1.lay_cables()
    #for cable in grid_1.cables:
        #print(cable.cable_length(), cable.start_cable(), cable.end_cable())

    #call visualize here since this is where grid information is stored
    grid_1_visual = Gridplot(grid_1)
    x = grid_1_visual.find_house_cor()
    y = grid_1_visual.find_battery_cor()
    grid_1_visual.make_plot()
    #print(z)
    #print(grid_1_visual.batteries)
    #print(grid_1_visual.cables_routes)

    sum = 0
    for house in grid_1.houses:
        sum += float(house.max_output)
    #grid_1.print_grid()
