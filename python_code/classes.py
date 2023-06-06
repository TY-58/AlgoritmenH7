from loaders import load_houses, load_batteries

class Grid:
    """A class that stores all the data to play Crowther's Adventure. It loads
    all the rooms from a game text-file. It also keeps track of the current room
    and the player's inventory."""

    def __init__(self, size: int):
        """Creates the grid with all relevant information on coordinates."""

        # initialize
        self.size: int = size
        self.grid: list[list[int]] = []
        self.initialize_grid()


        # import dictionaries from gamefile and Synonyms file
        #self.load_houses(f"data/{game}Adv.dat")

        #self.load_synonyms()

    def initialize_grid(self) -> None:
        """Function that initializes a grid with the correct sizing. Fills every
        spot with a 0."""

        for height in range(self.size):
            self.grid.append([])
            for width in range(self.size):
                self.grid[height].append(0)


    def process_houses(self, district: int) -> None:
        """ Loads
        """
        houses_data = load_houses(district)

        return None

    def process_batteries(self, district: int) -> None:
        """ Loads
        """
        batteries_data = load_batteries(district)

        return None

if __name__ == '__main__':
    grid = Grid(10)
    print(grid.grid)

    yo = load_houses(1)
    print(yo)
