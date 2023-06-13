from cable import Cable
from house import House

#Fred: de routes die gelegd worden kloppen niet met de routes die in de cable.routes staan. NOg niet gevonden waar het aan ligt

class Cable_route:
    """B"""
    def __init__(self, grid, configuration):
        """f"""

        self.grid = grid
        self.configuration = configuration
        self.lay_cables(configuration)

    def make_route(self, house, battery):
        """F"""
        cable_route = []

        start_location = house.location
        end_location = battery.location
        cable_route.append([start_location[0], start_location[1]])
        #print(start_location)
        #print(end_location)

        x_direction = abs(int(end_location[0] - start_location[0]))
        y_direction = abs(int(end_location[1] - start_location[1]))

        x_location = start_location[0]
        y_location = start_location[1]

        check = True

        if start_location[0] > end_location[0]:
            for x_counter in range(x_direction):
                if x_location != start_location[0]:
                    check = self.check_surroundings(x_location, y_location)
                cable_route.append([x_location, y_location])
                x_location -= 1
                    
        elif start_location[0] < end_location[0]:
            for x_counter in range(x_direction):
                if x_location != start_location[0]:
                    check = self.check_surroundings(x_location, y_location)
                #check = self.check_surroundings(x_location, y_location)
                cable_route.append([x_location, y_location])
                x_location += 1
            
        if start_location[1] > end_location[1]:
            for y_counter in range(y_direction + 1):
                
                if y_location != start_location[1]:
                    check = self.check_surroundings(x_location, y_location)
                #check = self.check_surroundings(x_location, y_location)
                cable_route.append([x_location, y_location])
                y_location -= 1
                                
        elif start_location[1] < end_location[1]:
            for y_counter in range(y_direction + 1):
                
                if y_location != start_location[1]:
                    check = self.check_surroundings(x_location, y_location)
                #check = self.check_surroundings(x_location, y_location)
                cable_route.append([x_location, y_location])
                y_location += 1

        return cable_route

    #prints statement where path crosses with houses
    def check_surroundings(self, x_location, y_location):
        for combination in self.configuration:
            house = combination[0]
            #print(house.location[1], house.location[0])
            if house.location[0] == x_location and house.location[1] == y_location:
                print("This path crosses a house at x, y: ", x_location, y_location)
                return False
        return True

    def lay_cables(self, configuration):
        """f"""
        count = 0
        for combination in configuration:
            route = self.make_route(combination[0], combination[1])
            cable = Cable(route)
            self.grid.cables.append(cable)
            count += 1
        print(count)

