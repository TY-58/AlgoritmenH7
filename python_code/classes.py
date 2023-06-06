from loaders import load_houses, load_batteries

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


if __name__ == '__main__':
    grid_1 = Grid(51,1)
    grid_1.process_houses()
    grid_1.process_batteries()
    grid_1.print_grid()
