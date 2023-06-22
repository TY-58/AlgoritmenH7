COST_PER_UNIT: int = 9

class Cable:
    """
    Class for cables. Every cable has an id, a route that is a list of locations
    and a total cost of the cable.
    """

    cable_id_counter = 0


    def __init__(self, route: list[list[int,int]]):
        """
        Takes a list of lists of length two (list of locations) as input.
        """

        self.id = Cable.cable_id_counter
        self.route = route
        self.cost = self.cable_cost()
        Cable.cable_id_counter += 1


    def cable_length(self):
        """
        Returns the length of the cable.
        """

        return len(self.route) - 1


    def start_cable(self):
        """
        Returns the first location of the cable.
        """

        return self.route[0]


    def end_cable(self):
        """
        Returns the last location of the cable.
        """

        return self.route[-1]


    def cable_cost(self):
        """
        Calculates the cost of the cable and returns it.
        """
        
        return self.cable_length() * COST_PER_UNIT
