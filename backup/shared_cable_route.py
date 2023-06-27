from __future__ import annotations

from code.classes.cable import Cable

MINIMUM_DISTANCE: int = 102

class Shared_cable_route:
    """
    A class for deciding the routes for the cables from houses to batteries.
    Takes a grid and a configuration as input and adds cables to the grid.
    Uses shared cables for houses matched to the same battery.
    Every cable from a house to a battery is processed as a single cable.
    """


    def __init__(self, grid: Grid, configuration: list[list[House, Battery]]):
        """
        Takes grid and configuration as input.
        Center routes are central cables to which house cables try to connect
        in order to share cables wherever is possible.
        Every battery has one specific center route.
        """

        self.grid: Grid = grid
        self.configuration: list[list[House, Battery]] = configuration
        self.lay_cables()


    def find_center_location(self, battery: Battery) -> list[int, int]:
        """
        Function that takes a battery as input and returns the center location
        of all houses that are matched with the battery.
        """

        x_location: int = 0
        y_location: int = 0

        for house in battery.house_connections:
            x_location += house.location[0]
            y_location += house.location[1]

        # Take mean of both x location and y location, rounded to an integer.
        center_location: list[int, int] = [round(x_location / len(battery.house_connections)), round(y_location / len(battery.house_connections))]

        return center_location


    def get_center_cable(self, battery: Battery) -> Cable:
        """
        Function that takes a battery as input, retrieves the center location and
        returns a cable from the center location to the battery.
        """

        start_location: list[int, int] = self.find_center_location(battery)
        end_location: list[int, int] = battery.location

        cable: Cable = Cable(self.make_route(start_location, end_location, battery))

        for battery in self.grid.batteries:
            if start_location != end_location and start_location == battery.location:
                cable.route.pop(0)

        return cable


    def make_route(self, start_location: list[int, int], end_location: list[int, int], battery: Battery) -> list[list[int, int]]:
        """
        Creates route from start_location to end_location. This is either from a
        house to the center route or from the center location to a battery.
        Gets battery as input because route should not pass any other batteries
        than inputted battery. Route moves horizontally first, and then vertically.
        If route encounters other battery, move around it.
        There occur four pieces of similar looking code, but they all make a
        different move on the grid and need multiple different inputs.
        """

        # Create list that will be filled with coordinates that are passed on route
        cable_route: list[list[int, int]] = []

        # Get horizontal distance and save direction (left or right) as sign
        x_direction: int = int(end_location[0] - start_location[0])
        if x_direction > 0:
            x_sign = 1
        else:
            x_sign = -1

        # x_direction should be a positive number to iterate in for loop
        x_direction = abs(x_direction)

        # Same for vertical direction
        y_direction: int = int(end_location[1] - start_location[1])
        if y_direction > 0:
            y_sign = 1
        else:
            y_sign = -1

        y_direction = abs(y_direction)

        # Get a list of all batteries other than relevant battery
        other_battery_locations: list[Battery] = self.get_locations_other_batteries(battery)

        x_location: int = start_location[0]
        y_location: int = start_location[1]
        cable_route.append(start_location)

        x_counter: int = 0
        y_counter: int = 0

        # First move horizontally, check if route should move to the left
        if start_location[0] > end_location[0]:

            # Move horizontally for entire x_direction
            while x_counter < x_direction:
                x_location -= 1

                # If other battery is encountered, move around it
                if [x_location, y_location] in other_battery_locations:

                    # First, take a step back
                    x_location += 1

                    # If route is already on the right vertical coordinate, move around
                    if y_location == end_location[1]:
                        y_location += 1
                        cable_route.append([x_location, y_location])

                        x_location -= 1
                        cable_route.append([x_location, y_location])

                        x_location -= 1
                        cable_route.append([x_location, y_location])

                        y_location -= 1
                        cable_route.append([x_location, y_location])

                        # Took two steps in horizontal direction
                        x_counter += 2

                    # If not, moves in correct vertical direction for one coordinate
                    else:
                        y_location += y_sign
                        y_direction -= 1
                        cable_route.append([x_location, y_location])

                # Else perform a normal move
                else:
                    cable_route.append([x_location, y_location])
                    x_counter += 1

        # Move to the right, works analogous to the code above
        if start_location[0] < end_location[0]:
            while x_counter < x_direction:
                x_location += 1

                if [x_location, y_location] in other_battery_locations:
                    x_location -= 1

                    if y_location == end_location[1]:
                        y_location += 1
                        cable_route.append([x_location, y_location])

                        x_location += 1
                        cable_route.append([x_location, y_location])

                        x_location += 1
                        cable_route.append([x_location, y_location])

                        y_location -= 1
                        cable_route.append([x_location, y_location])

                        x_counter += 2
                    else:
                        y_location += y_sign
                        y_direction -= 1
                        cable_route.append([x_location, y_location])
                else:
                    cable_route.append([x_location, y_location])
                    x_counter += 1

        # After horizontal movement, check whether vertical movement is up or down
        if start_location[1] > end_location[1]:
            while y_counter < y_direction:

                y_location -= 1

                # Because we are already on the right x location, we always have to move around
                if [x_location, y_location] in other_battery_locations:
                    y_location += 1

                    x_location += 1
                    cable_route.append([x_location, y_location])

                    y_location -= 1
                    cable_route.append([x_location, y_location])

                    y_location -= 1
                    cable_route.append([x_location, y_location])

                    x_location -= 1
                    cable_route.append([x_location, y_location])

                    y_counter += 2

                # Perform a normal move
                else:
                    cable_route.append([x_location, y_location])
                    y_counter += 1

        # Moving up works analogous to moving down
        if start_location[1] < end_location[1]:
            while y_counter < y_direction:
                y_location += 1
                if [x_location, y_location] in other_battery_locations:
                    y_location -= 1

                    x_location += 1
                    cable_route.append([x_location, y_location])

                    y_location += 1
                    cable_route.append([x_location, y_location])

                    y_location += 1
                    cable_route.append([x_location, y_location])

                    x_location -= 1
                    cable_route.append([x_location, y_location])

                    y_counter += 2

                else:
                    cable_route.append([x_location, y_location])
                    y_counter += 1

        # Finally, return list of all coordinates that the route passed
        return cable_route


    def get_closest_location_cable(self, house_location: list[int, int], center_cable: Cable) -> list[int, int]:
        """
        Function that finds closest location on the center route for a given house.
        Returns location on the center route that is closest to input house.
        """

        # Take upper bound for the minimum distance
        minimum_distance: int = MINIMUM_DISTANCE
        closest_location: list[int, int] = []

        for location in center_cable.route:
            distance: int = abs(house_location[0] - location[0]) - 1 + abs(house_location[1] - location[1]) - 1

            if distance < minimum_distance:
                minimum_distance = distance
                closest_location = location

        return closest_location


    def get_locations_other_batteries(self, battery_input: Battery) -> list[list[int, int]]:
        """
        Find and return locations of all batteries but the inputted battery.
        """

        battery_locations: list[list[int, int]] = []
        for battery in self.grid.batteries:
            if battery != battery_input:
                battery_locations.append(battery.location)

        return battery_locations


    def get_connected_cable(self, center_cable: Cable, house_cable: Cable) -> Cable:
        """
        Connects the cable from a house to the center route with the center
        and creates a new cable from the house to the battery.
        """

        counter: int = 0
        for location in center_cable.route:
            if location == house_cable.route[-1]:

                # House cable could already be connected to the battery
                if counter + 1 > center_cable.cable_length():

                    return house_cable

                else:

                    return Cable(house_cable.route + center_cable.route[counter+1:])

            counter += 1


    def lay_cables(self):
        """
        Lays all cables: for every battery, find center route, and lay route for
        every house matched to the battery. Finally, add cables to the grid.
        """
        self.grid.cables: list[Cable] = []
        for battery in self.grid.batteries:

            # Finds center location of all houses matched to battery
            self.find_center_location(battery)

            # Finds route between center location and battery
            center_cable: Cable = self.get_center_cable(battery)

            for house in battery.house_connections:

                # Finds closest location on center route and lay cable between house and center route
                route_location: list[int, int] = self.get_closest_location_cable(house.location, center_cable)
                house_cable: Cable = Cable(self.make_route(house.location, route_location, battery))

                # Connects both parts of the cable into one cable from house to battery
                cable: Cable = self.get_connected_cable(center_cable, house_cable)

                # Raise errors if start is not house location or end is not battery location
                if not cable.route[0] in [x.location for x in self.grid.houses]:
                    raise ValueError("gaat fout")
                if not cable.route[-1] in [x.location for x in self.grid.batteries]:
                    raise ValueError("gaat fout")

                for loc in range(len(cable.route) - 1) :
                    if abs(cable.route[loc][0] - cable.route[loc + 1][0]) + abs(cable.route[loc][1] - cable.route[loc + 1][1]) != 1:
                        raise ValueError ("gaat fout")

                # Process cable in the grid
                self.grid.cables.append(cable)