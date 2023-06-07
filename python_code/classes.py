from loaders import load_houses, load_batteries
import random

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
            print(row)
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

class House:
    """Class for houses
    autoincrement: https://stackoverflow.com/questions/1045344/how-do-you-create-an-incremental-id-in-a-python-class"""

    house_id_counter = 0

    def __init__(self, x_location: int, y_location: int, max_output: int):

        self.id = House.house_id_counter
        self.location = [x_location, y_location]
        self.max_output = max_output
        self.connected = False
        self.battery_connection = None
        House.house_id_counter += 1

class Battery:
    """Class for batteries"""

    battery_id_counter = 0

    def __init__(self, x_location: int, y_location: int, max_capacity: int):

        self.id = Battery.battery_id_counter
        self.location = [x_location, y_location]
        self.max_capacity = max_capacity
        self.house_connections = []
        Battery.battery_id_counter += 1

class Cable:
    """Class for cables"""

    cable_id_counter = 0

    def __init__(self, route: list[list[int,int]]):

        self.id = Cable.cable_id_counter
        self.route = route

    def cable_length(self):

        return len(self.route) - 1

    def start_cable(self):
        return route[0]

    def end_cable(self):
        return route[-1]


if __name__ == '__main__':
    grid_1 = Grid(51,1)
    grid_1.process_houses()
    grid_1.process_batteries()
    grid_1.make_route(1)
    print(grid_1.cables[0].route)
