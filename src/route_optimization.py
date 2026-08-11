import csv

file_path = "data/vehicle_data.csv"

with open(file_path, "r") as file:
    data = csv.DictReader(file)

    print("ROUTE OPTIMIZATION")
    print("------------------")

    for vehicle in data:
        vehicle_id = vehicle["vehicle_id"]
        latitude = vehicle["latitude"]
        longitude = vehicle["longitude"]

        print("Vehicle ID:", vehicle_id)
        print("Current Location:", latitude, longitude)
        print("Suggested Route: Nearest available route")
        print("------------------")