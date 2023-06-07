class House:
    """Class for houses
    autoincrement: https://stackoverflow.com/questions/1045344/how-do-you-create-an-incremental-id-in-a-python-class"""

    house_id_counter = 0

    def __init__(self, x_location: int, y_location: int, max_output: int):

        self.id = House.house_id_counter
        self.location = [x_location, y_location]
        self.max_output = max_output
        self.connected = False
        self.battery_connection = None
        House.house_id_counter += 1
