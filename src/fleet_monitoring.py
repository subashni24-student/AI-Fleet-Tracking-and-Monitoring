import csv

file_path = "data/vehicle_data.csv"

with open(file_path, "r") as file:
    data = csv.DictReader(file)

    print("FLEET MONITORING")
    print("----------------")

    for vehicle in data:
        vehicle_id = vehicle["vehicle_id"]
        speed = int(vehicle["speed"])
        fuel = int(vehicle["fuel"])

        print("Vehicle ID:", vehicle_id)
        print("Speed:", speed, "km/h")
        print("Fuel:", fuel, "%")

        if speed > 80:
            print("Alert: High Speed!")

        if fuel < 30:
            print("Alert: Low Fuel!")

        print("----------------")