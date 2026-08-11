def predict_fuel_status(fuel):
    if fuel < 30:
        return "Fuel Low - Refueling Required"
    elif fuel < 50:
        return "Fuel Medium"
    else:
        return "Fuel Level Normal"


fuel = int(input("Enter current fuel percentage: "))

print("Prediction:", predict_fuel_status(fuel))