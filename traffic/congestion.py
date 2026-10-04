def get_congestion_level(vehicle_count):
    if vehicle_count <= 5:
        return "LOW"
    elif vehicle_count <= 10:
        return "MEDIUM"
    else:
        return "HIGH"


# Example vehicle count
vehicle_count = 8

level = get_congestion_level(vehicle_count)

print("Vehicle count:", vehicle_count)
print("Traffic congestion:", level)