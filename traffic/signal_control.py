def get_green_time(congestion):
    if congestion == "LOW":
        return 20
    elif congestion == "MEDIUM":
        return 40
    elif congestion == "HIGH":
        return 60
    else:
        return 30


# Test the traffic signal system
congestion = "HIGH"

green_time = get_green_time(congestion)

print("Traffic congestion:", congestion)
print("Green light time:", green_time, "seconds")