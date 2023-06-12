class Cable:
    """Class for cables"""

    cable_id_counter = 0

    def __init__(self, route: list[list[int,int]]):

        self.id = Cable.cable_id_counter
        self.route = route
        Cable.cable_id_counter += 1

    def cable_length(self):
        
        return len(self.route) - 1

    def start_cable(self):
        return self.route[0]

    def end_cable(self):
        return self.route[-1]
