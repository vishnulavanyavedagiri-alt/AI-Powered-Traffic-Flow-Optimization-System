from ultralytics import YOLO


def get_congestion_level(vehicle_count):
    if vehicle_count <= 5:
        return "LOW"
    elif vehicle_count <= 10:
        return "MEDIUM"
    else:
        return "HIGH"


def get_green_time(congestion):
    if congestion == "LOW":
        return 20
    elif congestion == "MEDIUM":
        return 40
    elif congestion == "HIGH":
        return 60
    else:
        return 30


# Load YOLO model
model = YOLO("yolo11n.pt")

# Read traffic video
results = model("traffic.mp4", stream=True)

# Process video
for result in results:

    vehicle_count = 0

    for box in result.boxes:

        class_id = int(box.cls[0])

        # Vehicle classes:
        # 2 = car
        # 3 = motorcycle
        # 5 = bus
        # 7 = truck

        if class_id in [2, 3, 5, 7]:
            vehicle_count += 1

    congestion = get_congestion_level(vehicle_count)

    green_time = get_green_time(congestion)

    print(
        "Vehicles:",
        vehicle_count,
        "| Congestion:",
        congestion,
        "| Green time:",
        green_time,
        "seconds"
    )