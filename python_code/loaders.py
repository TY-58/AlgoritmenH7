import csv

def load_houses(district: int) -> list[list[str]]:
    """Loads the correct csv file.
    Taken from https://earthly.dev/blog/csv-python/"""

    with open(f"../data_grids/district_{district}/district-{district}_houses.csv", 'r') as file:

        csvreader = csv.reader(file)

        data_houses = []
        for row in csvreader:
            data_houses.append(row)

        return data_houses

def load_batteries(district: int) -> list[list[str]]:
    """Loads the correct csv file.
    Taken from https://earthly.dev/blog/csv-python/"""

    with open(f"../data_grids/district_{district}/district-{district}_batteries.csv", 'r') as file:

        csvreader = csv.reader(file)

        data_batteries = []
        for row in csvreader:
            data_batteries.append(row)

        return data_batteries
