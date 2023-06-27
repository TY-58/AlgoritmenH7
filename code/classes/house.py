class House:
    """
    Class for houses
    autoincrement: https://stackoverflow.com/questions/1045344/how-do-you-create-an-incremental-id-in-a-python-class
    """


    def __init__(self, x_location: int, y_location: int, max_output: int):
        """ 
        Creates a class for houses and takes the house location and energy output.
        Stores the information in the class.
        """

        self.location = [x_location, y_location]
        self.max_output = float(max_output)
        self.connected = False

