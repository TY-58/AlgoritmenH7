class Battery:
    """
    Class for batteries. Every battery contains an id, location, max_capacity,
    a list of houses that it is connected to and a current_capacity, which is dynamic.
    """

    battery_id_counter = 0


    def __init__(self, x_location: int, y_location: int, max_capacity: int):
        """
        Takes a location and a max_capacity as input.
        When initialized, current_capacity is max_capacity.
        """

        self.id = Battery.battery_id_counter
        self.location = [x_location, y_location]
        self.max_capacity = max_capacity
        self.house_connections = []
        self.current_capacity = float(max_capacity)

        Battery.battery_id_counter += 1


    def calculate_current_capacity(self, output):
        """
        Checks if current_capacity is overwritten by ouput.
        Updates current_capacity if there is still capacity.
        """

        if capacity < output:
            return False
        else:
            self.current_capacity -= output

        return True