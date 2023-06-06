import csv

class Grid:
    """A class that stores all the data to play Crowther's Adventure. It loads
    all the rooms from a game text-file. It also keeps track of the current room
    and the player's inventory."""

    def __init__(self, size: int):
        """Creates the grid with all relevant information on coordinates."""

        # initialize
        self.size: int = size
        self.grid: list[list[int]] = []


        # import dictionaries from gamefile and Synonyms file
        self.load_rooms(f"data/{game}Adv.dat")

        self.load_synonyms()

    def initialize_grid(self) -> None:
        """Function that initializes a grid with the correct sizing. Fills every
        spot with a 0."""

        for height in self.size:
            self.grid.append([])
            for width in self.size:
                self.grid[height].append(0)


    def load_houses(self) -> None:
        """Taken from https://earthly.dev/blog/csv-python/
        """

    #with open("./bwq.csv", 'r') as file:

     # csvreader = csv.reader(file)

     # for row in csvreader:
        #print(row)

if __name__ == '__main__':
    print("hi")
