#this is our first bit of code, likely not neccesary anymore.

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

    #make route
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

    #make route
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

            #random
    def exceeds_battery(self, battery, house):
        """ Checks if the capacity of the battery is exceeded when a new house is attached. """
        if battery.current_capacity < float(house.max_output):
            return True
        else:
            return False

    
    def lay_cables(self):
        """. Unclear what this function does. """
        for house in self.houses:
            self.make_route(house.id)

       def match_house(self, house_id):
        """. Unclear what this function does. """
        house = get_house(house_id)
        distance_list_batteries = self.get_distance_batteries(house_id)

        return 0