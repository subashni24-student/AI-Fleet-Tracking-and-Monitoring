import csv

file_path = "data/vehicle_data.csv"

with open(file_path, "r") as file:
    data = csv.DictReader(file)

    print("DRIVER MONITORING")
    print("-----------------")

    for vehicle in data:
        vehicle_id = vehicle["vehicle_id"]
        speed = int(vehicle["speed"])

        print("Vehicle ID:", vehicle_id)
        print("Speed:", speed, "km/h")

        if speed > 80:
            print("Driver Alert: Please reduce speed")
        else:
            print("Driver Status: Normal")

        print("-----------------")