from cable import Cable

class Combined_cable_route:
    """A class for deciding the route for the cables from a house to a battery. """

    def __init__(self, grid, configuration):
        """."""

        self.grid = grid
        self.configuration = configuration
        self.center_routes = []
        self.lay_cables()


    def find_center_location(self, battery):
        """f"""

        x_location = 0
        y_location = 0

        for house in battery.house_connections:
            x_location += house.location[0]
            y_location += house.location[1]

        center_location = [round(x_location / len(battery.house_connections)), round(y_location / len(battery.house_connections))]
        print(center_location)
        return center_location

    def lay_center_route(self, battery):
        """f"""

        start_location = self.find_center_location(battery)
        end_location = battery.location
        cable = Cable(self.make_route(start_location, end_location))
        #self.grid.cables.append(cable)
        return cable


    def make_route(self, start_location, end_location):
        """."""
        cable_route = []

        x_direction = abs(int(end_location[0] - start_location[0]))
        y_direction = abs(int(end_location[1] - start_location[1]))

        x_location = start_location[0]
        y_location = start_location[1]

        if start_location[0] > end_location[0]:
            for x_counter in range(x_direction):

                cable_route.append([x_location, y_location])
                x_location -= 1

        elif start_location[0] < end_location[0]:
            for x_counter in range(x_direction):
                cable_route.append([x_location, y_location])
                x_location += 1

        if start_location[1] > end_location[1]:
            for y_counter in range(y_direction + 1):

                cable_route.append([x_location, y_location])
                y_location -= 1

        elif start_location[1] < end_location[1]:
            for y_counter in range(y_direction + 1):

                cable_route.append([x_location, y_location])
                y_location += 1

        return cable_route


    def lay_cables(self):
        """f"""

        for battery in self.grid.batteries:
            self.find_center_location(battery)
            center_cable = self.lay_center_route(battery)
            self.grid.cables.append(center_cable)

            for house in battery.house_connections:
                route_location = self.get_closest_location_cable(house.location, center_cable)
                house_cable = Cable(self.make_route(house.location, route_location))
                self.grid.cables.append(house_cable)


    def get_closest_location_cable(self, house_location, center_cable):
        """Calc distance between house and center cable."""

        minimum_distance = 102
        closest_location = []
        for location in center_cable.route:
            distance = abs(house_location[0] - location[0]) + abs(house_location[1] - location[1])

            if distance < minimum_distance:
                minimum_distance = distance
                closest_location = location

        return closest_location
