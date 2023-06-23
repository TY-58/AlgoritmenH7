
print("Welcome! Our problem is divided into two seperate problems: matching houses to batteries (configuration) and laying cables from the houses to the batteries.")

configuration_version: int = get_int("Firstly, which configuration version do you want to run: random (type 1) or greedy (type 2)?")

cable_route_version: int = get_int("And which cable route version do you want to use: random (type 1), greedy (type 2), or shared cables (type 3)?")

iteration: int = get_int("How many times do you want to run it?")

if cable_route_version == 3:
    hillclimber: str = get_string("Do you want to apply hillclimber afterwards (type y/n)?")

    if hillclimber == 'y':
        hill_iterations: int = get_int("How many iterations of hillclimber do you want to run?")
