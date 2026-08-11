import csv

file_path = "data/vehicle_data.csv"

with open(file_path, "r") as file:
    data = list(csv.DictReader(file))

print("================================")
print(" AI VEHICLE FLEET DASHBOARD")
print("================================")

print("Total Vehicles:", len(data))

for vehicle in data:
    print("\nVehicle ID:", vehicle["vehicle_id"])
    print("Speed:", vehicle["speed"], "km/h")
    print("Fuel:", vehicle["fuel"], "%")
    print("Location:", vehicle["latitude"], vehicle["longitude"])

    if int(vehicle["speed"]) > 80:
        print("Status: HIGH SPEED ALERT")
    elif int(vehicle["fuel"]) < 30:
        print("Status: LOW FUEL ALERT")
    else:
        print("Status: NORMAL")

print("\n================================")
print("Dashboard Monitoring Completed")
print("================================")