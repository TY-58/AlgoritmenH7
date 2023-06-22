class House:
    """Class for houses
    autoincrement: https://stackoverflow.com/questions/1045344/how-do-you-create-an-incremental-id-in-a-python-class"""

    house_id_counter: int = 0

    def __init__(self, x_location: int, y_location: int, max_output: int):

        self.id: int = House.house_id_counter
        self.location: [int, int] = [x_location, y_location]
        self.max_output: float = float(max_output)
        self.connected: bool = False
        House.house_id_counter += 1

