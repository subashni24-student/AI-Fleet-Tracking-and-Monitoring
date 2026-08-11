import csv

file_path = "data/vehicle_data.csv"

with open(file_path, "r") as file:
    data = csv.DictReader(file)

    print("FUEL PREDICTION")
    print("----------------")

    for vehicle in data:
        vehicle_id = vehicle["vehicle_id"]
        fuel = int(vehicle["fuel"])

        print("Vehicle ID:", vehicle_id)
        print("Current Fuel:", fuel, "%")

        if fuel < 30:
            print("Prediction: Fuel will be low soon")
        else:
            print("Prediction: Fuel level is normal")

        print("----------------")