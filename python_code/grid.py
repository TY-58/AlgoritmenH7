import random
from loaders import load_houses, load_batteries
from battery import Battery
from cable import Cable
from house import House
from visualize import Gridplot
from json_output import output_json
from operator import itemgetter
from greedy_match import Greedy_configuration
from cable_route import Cable_route


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
        self.configuration = []
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
        Comment: shouldn't unpacking the houses move to house class?
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

            final_location = self.battery_found(x_location, y_location)
            route.append(final_location)

            cable = Cable(route)
            self.cables.append(cable)

            current_house.connected = True

            for battery in self.batteries:
                if battery.location == final_location:
                    battery.house_connections.append(current_house)
                    battery.current_capacity -= float(current_house.max_output)
                    break

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

        print(directions)
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

    def exceeds_battery(self, battery, house):
        if battery.current_capacity < float(house.max_output):
            return True
        else:
            return False

    def match_house(self, house_id):
        house = get_house(house_id)
        distance_list_batteries = self.get_distance_batteries(house_id)

        return 0


    def get_distance_batteries(self, house_id):
        house = self.get_house(house_id)
        distance_list =[]
        for battery in self.batteries:
            distance = abs(battery.location[0] - house.location[0]) + abs(battery.location[1] + house.location[1])
            distance_list.append([battery, distance])

        sorted_list = sorted(distance_list, key=itemgetter(1))
        return sorted_list

    def get_house(self, house_id):
        for house in self.houses:
            if house.id == house_id:
                return house

    def try_configuration(self):
        configuration = []
        house_list = self.houses

        for house in sorted(house_list,key=lambda _: random.random()):
            distance_list_batteries = self.get_distance_batteries(house.id)
            battery_number = random.randint(0,4)
            try_battery = distance_list_batteries[battery_number][0]
            error_counter = 0

            while self.exceeds_battery(try_battery, house):
                battery_number = random.randint(0,4)

                # configuration cannot work anymore, try again
                #if battery_number == 4:
                #    return []

                try_battery = distance_list_batteries[battery_number][0]
                error_counter += 1
                if error_counter > 50:
                    return []

            configuration.append([house, try_battery])
            try_battery.current_capacity -= float(house.max_output)

        return configuration


    def make_configuration(self):

        configuration_check = []
        while configuration_check == []:
            configuration_check = self.try_configuration()

        return configuration_check


if __name__ == '__main__':
    grid_1 = Grid(51,1)
    grid_1.process_houses()
    grid_1.process_batteries()
    #grid_1.lay_cables()
    #sorted_house_list = Greedy(grid_1)

    #for cable in grid_1.cables:
        #print(cable.cable_length(), cable.start_cable(), cable.end_cable())

    #call visualize here since this is where grid information is stored
    #grid_1_visual = Gridplot(grid_1)
    #grid_1_visual.make_plot()

    sum = 0
    for house in grid_1.houses:
        sum += float(house.max_output)
    #grid_1.print_grid()

    #for battery in grid_1.batteries:
    #    print(battery.house_connections)

    #output_json(grid_1)

    x = Greedy_configuration(grid_1)
    config = x.make_configuration()
    cb = Cable_route(grid_1, config)
    prnit(grid_1.cables)
