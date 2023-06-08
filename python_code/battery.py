class Battery:
    """Class for batteries"""

    battery_id_counter = 0

    def __init__(self, x_location: int, y_location: int, max_capacity: int):

        self.id = Battery.battery_id_counter
        self.location = [x_location, y_location]
        self.max_capacity = max_capacity
        self.house_connections = []
        self.current_capacity = max_capacity

        Battery.battery_id_counter += 1
