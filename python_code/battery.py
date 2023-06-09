class Battery:
    """Class for batteries"""

    battery_id_counter = 0

    def __init__(self, x_location: int, y_location: int, max_capacity: int):

        self.id = Battery.battery_id_counter
        self.location = [x_location, y_location]
        self.max_capacity = max_capacity
        self.house_connections = []
        self.current_capacity = float(max_capacity)

        Battery.battery_id_counter += 1

    def process_batteries_2(self):
        """ This should be done in battery class, not grid. Name can be changed after removed from grid class. """
        pass


    def calculate_current_capacity(self, output):
        """ Calculates the current capacity of the battery. And returns bool."""
       
        if capacity < output:
            return False
        else:
            self.current_capacity -= output

        return True

