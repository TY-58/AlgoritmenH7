def lay_cables(grid: Grid, configuration: list[list[House, Battery]]):
    """
    A function that lays all the cables from houses to the matched batteries.
    """

    for combination in configuration:
        route: list[list[int, int]] = self.make_route(combination[0], combination[1])
        cable: Cable = Cable(route)
        grid.grid.cables.append(cable)
