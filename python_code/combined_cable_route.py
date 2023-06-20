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
        return center_location

    def get_center_route(self, battery):
        """f"""

        start_location = self.find_center_location(battery)
        end_location = battery.location
        cable = Cable(self.make_route(start_location, end_location, battery))
        #self.grid.cables.append(cable)
        return cable


    def make_route(self, start_location, end_location, battery):
        """."""
        cable_route = []

        x_direction = int(end_location[0] - start_location[0])
        if x_direction > 0:
            x_sign = 1
        else:
            x_sign = -1
        x_direction = abs(x_direction)

        y_direction = int(end_location[1] - start_location[1])
        if y_direction > 0:
            y_sign = 1
        else:
            y_sign = -1
        y_direction = abs(y_direction)

        other_battery_locations = self.get_locations_other_batteries(battery)

        x_location = start_location[0]
        y_location = start_location[1]
        cable_route.append(start_location)

        x_counter = 0
        y_counter = 0

        if start_location[0] > end_location[0]:
            while x_counter < x_direction:
                x_location -= 1

                if [x_location, y_location] in other_battery_locations:
                #    print([x_location, y_location])
                    x_location += 1

                    if y_location == end_location[1]:
                        y_location += 1
                        cable_route.append([x_location, y_location])

                        x_location -= 1
                        cable_route.append([x_location, y_location])

                        x_location -= 1
                        cable_route.append([x_location, y_location])

                        y_location -= 1
                        cable_route.append([x_location, y_location])

                        x_counter += 2
                    else:

                        y_location += y_sign
                        y_direction -= 1

                else:
                    cable_route.append([x_location, y_location])
                    x_counter += 1

        elif start_location[0] < end_location[0]:
            while x_counter < x_direction:
                x_location += 1

                if [x_location, y_location] in other_battery_locations:
                    #print([x_location, y_location])
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

        if start_location[1] > end_location[1]:
            while y_counter < y_direction:

                y_location -= 1
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

                else:
                    cable_route.append([x_location, y_location])
                    y_counter += 1
                    cable_route.append([x_location, y_location])

        elif start_location[1] < end_location[1]:
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

        return cable_route


    def lay_cables(self):
        """f"""

        for battery in self.grid.batteries:
            self.find_center_location(battery)
            center_cable = self.get_center_route(battery)
            #self.grid.cables.append(center_cable)

            for house in battery.house_connections:
                route_location = self.get_closest_location_cable(house.location, center_cable)
                #print(route_location)
                house_cable = Cable(self.make_route(house.location, route_location, battery))
                cable = self.get_connected_cable(center_cable, house_cable)
                print('begin')
                print(house_cable.route)
                print(center_cable.route)
                print(cable.route)
                print('eind')
                if not cable.route[0] in [x.location for x in self.grid.houses]:
                    print(house_cable.route)
                    print(center_cable.route)
                    print(cable.route)
                    raise ValueError("gaat fout")
                if not cable.route[-1] in [x.location for x in self.grid.batteries]:
                    print(house_cable.route)
                    print(center_cable.route)
                    print(cable.route)
                    raise ValueError("gaat fout")

                self.grid.cables.append(cable)


    def get_closest_location_cable(self, house_location, center_cable):
        """Calc distance between house and center cable."""

        minimum_distance = 102
        closest_location = []
        for location in center_cable.route:
            distance = abs(house_location[0] - location[0]) - 1 + abs(house_location[1] - location[1]) - 1

            if distance < minimum_distance:
                minimum_distance = distance
                closest_location = location

        return closest_location

    def get_locations_other_batteries(self, battery_input):

        battery_locations = []
        for battery in self.grid.batteries:
            if battery != battery_input:
                battery_locations.append(battery.location)

        return battery_locations

    def get_connected_cable(self, center_cable, house_cable):

        counter = 0
        for location in center_cable.route:
            if location == house_cable.route[-1]:
                if counter + 1 > center_cable.cable_length():
                    #print('uitzondering!', house_cable.route, center_cable.route)
                    return house_cable
                else:
                    return Cable(house_cable.route + center_cable.route[counter+1:])
            counter += 1
