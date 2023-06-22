# From: https://www.geeksforgeeks.org/reading-and-writing-json-to-a-file-in-python/
import json


def output_json(grid):
	output_list = []

	output_list.append({
	"district": grid.district,
	"costs-shared": grid.total_cost,
	})

	for battery in grid.batteries:
		output_list.append({
		"location": f"{battery.location[0]},{battery.location[1]}",
		"capacity": battery.max_capacity,
		"houses": connected_houses_dict(battery, grid)
		})

	json_object = json.dumps(output_list, indent=4)
	with open("output.json", "w") as outfile:
		outfile.write(json_object)


def connected_houses_dict(battery, grid):
	houses_list = []
	for house in battery.house_connections:
		houses_list.append({
		"location": f"{house.location[0]},{house.location[1]}",
		"output": house.max_output,
		"cables": cable_route(house, grid)
		})

	return houses_list


def cable_route(house, grid):
	route_list = []
	route_formatted = []
	for cable in grid.cables:
		if cable.start_cable() == house.location:
			route_list = cable.route
			break

	for coordinate in route_list:
		route_formatted.append(f"{coordinate[0]},{coordinate[1]}")

	return route_formatted
