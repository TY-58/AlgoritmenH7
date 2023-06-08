# From: https://www.geeksforgeeks.org/reading-and-writing-json-to-a-file-in-python/
#import json

# Data to be written
dictionary = {
	"name": "sathiyajith",
	"rollno": 56,
	"cgpa": 8.6,
	"phonenumber": "9976770500"
}

# Serializing json
#json_object = json.dumps(dictionary, indent=4)

# Writing to sample.json
#with open("sample.json", "w") as outfile:
#	outfile.write(json_object)

def output_json(grid):
    output_list = []

    output_list.append({
        "district": grid.district,
        "costs-shared": 0,
    })

	for battery in grid.batteries:
		output_list.append({
			"location": f"{battery.location[0]},{battery.location[1]}",
			"capacity": battery.capacity,
			house_list =[]
			for house in battery.house_connections:
				house_list.append(house)
			"houses":
		}



	)

def connected_houses_dict(battery):
	return 0
