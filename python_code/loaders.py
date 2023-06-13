import csv

def load_houses(district: int) -> list[list[str]]:
    """Loads the correct csv file.
    Taken from https://earthly.dev/blog/csv-python/
    skip header: https://linuxhint.com/skip-header-row-csv-python/"""

    with open(f"../data_grids/district_{district}/district-{district}_houses.csv", 'r') as file:

        csvreader = csv.reader(file)
        next(csvreader)

        data_houses = []
        for row in csvreader:
            data_houses.append(row)

        return data_houses

def load_batteries(district: int) -> list[list[str]]:
    """Loads the correct csv file.
    Taken from https://earthly.dev/blog/csv-python/"""

    with open(f"../data_grids/district_{district}/district-{district}_batteries.csv", 'r') as file:

        csvreader = csv.reader(file)
        next(csvreader)

        data_batteries = []
        for row in csvreader:
            # Position bestaat hier uit twee coordinaten
            x,y = row[0].split(",")
            data_batteries.append([x,y,row[1]])

        return data_batteries
