    def lay_cables(grid: Grid, configuration: list[list[House, Battery]]):
        """
        A function that lays all the cables from houses to the matched batteries.
        """

        for combination in configuration:
            route: list[list[int, int]] = self.make_route(combination[0], combination[1])
            cable: Cable = Cable(route)
            grid.grid.cables.append(cable)


    def get_directions(grid: Grid, x_location: int, y_location: int, end_location: list[int, int]) -> list[str]:
        """
        Gets all possible directions from current position.
        Batteries other than the destination battery are not allowed to move over.
        """

        directions: list[str] = []

        if y_location > 0 and (grid.grid[y_location-1][x_location] != 2 or [x_location, y_location-1] == end_location):
            directions.append('d')
        if y_location < 50 and (grid.grid[y_location+1][x_location] != 2 or [x_location, y_location+1] == end_location):
            directions.append('u')
        if x_location > 0 and (grid.grid[y_location][x_location-1] != 2 or [x_location-1, y_location] == end_location):
            directions.append('l')
        if x_location < 50 and (grid.grid[y_location][x_location+1] != 2 or [x_location+1, y_location] == end_location):
            directions.append('r')

        return directions
