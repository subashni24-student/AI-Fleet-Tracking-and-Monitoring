import csv

file_path = "data/vehicle_data.csv"

with open(file_path, "r") as file:
    data = csv.DictReader(file)

    print("VEHICLE TRACKING")
    print("----------------")

    for vehicle in data:
        print("Vehicle ID:", vehicle["vehicle_id"])
        print("Speed:", vehicle["speed"], "km/h")
        print("Fuel:", vehicle["fuel"], "%")
        print("Location:", vehicle["latitude"], vehicle["longitude"])
        print("----------------")