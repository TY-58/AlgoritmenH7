from loaders import load_houses, load_batteries
from battery import Battery
from house import House

class Grid:
    """ A class that stores and processes information and data required in the SmartGrid. """

    def __init__(self, size: int, district: int):
        """Creates the grid with all relevant information on coordinates. """

        self.district = district
        self.size: int = size
        self.grid: list[list[int]] = []
        self.houses = []
        self.batteries = []
        self.cables = []
        self.configuration = []
        self.total_cost = 0
        self.initialize_grid()
        self.process_houses()
        self.process_batteries()

    def initialize_grid(self) -> None:
        """Function that initializes a grid with correct sizing.
        Assigns a '0' to every spot to signify it as empty."""

        for height in range(self.size):
            self.grid.append([])
            for width in range(self.size):
                self.grid[height].append(0)

    def process_houses(self) -> None:
        """ Processes all house data from loader function.
        Assigns a '1' to the spot of the house on the grid. """

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
        """ Processes all battery data from loader function.
        Assigns a '2' to the spot of the battery on the grid. """

        batteries_data = load_batteries(self.district)

        for battery_row in batteries_data:
            x_location = int(battery_row[0])
            y_location = int(battery_row[1])
            max_capacity = battery_row[2]

            battery = Battery(x_location, y_location, max_capacity)
            self.batteries.append(battery)
            self.grid[y_location][x_location] = 2

        return None

    def calc_total_cable_cost(self):
        """ Calculates the cost of all cables on the grid. """
        total_cost: int = 0
        for cable in self.cables:
            total_cost = total_cost + cable.cost
        self.total_cost = total_cost + 25000

    def calc_combined_cable_cost(self):
        """for combined cables"""
        total_length = 0
        for battery in self.batteries:

            battery_route = []
            for cable in self.cables:
                if cable.route[-1] == battery.location:
                    cable_route = [tuple(x) for x in cable.route]
                    #print(cable_route)
                    battery_route += cable_route
            #print()

            #print(battery_route)
            battery_route = set(battery_route)
            #print(battery_route)

            total_length += len(battery_route) - 1

        #print(total_length)
        self.total_cost = 9 * total_length + 25000

    def process_configuration_grid(self, configuration):
        """f"""
        for battery in self.batteries:
            for house in self.houses:
                if [house, battery] in configuration:
                    battery.house_connections.append(house)
            #print(battery.house_connections)
