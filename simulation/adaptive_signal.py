from ultralytics import YOLO
import traci


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


# -----------------------------
# 1. YOLO vehicle detection
# -----------------------------

model = YOLO("yolo11n.pt")

results = model("traffic.mp4", stream=True)

first_result = next(results)

vehicle_count = 0

for box in first_result.boxes:
    class_id = int(box.cls[0])

    if class_id in [2, 3, 5, 7]:
        vehicle_count += 1


congestion = get_congestion_level(vehicle_count)
green_time = get_green_time(congestion)

print()
print("YOLO vehicle count:", vehicle_count)
print("Initial congestion:", congestion)
print("Initial green time:", green_time, "seconds")


# -----------------------------
# 2. Start SUMO
# -----------------------------

sumo_cmd = [
    "C:/Program Files (x86)/Eclipse/Sumo/bin/sumo.exe",
    "-c",
    "simulation/traffic.sumocfg"
]

traci.start(sumo_cmd)

print("Connected to SUMO!")

tls_id = "center"


# -----------------------------
# 3. Run adaptive simulation
# -----------------------------

print("Starting adaptive traffic simulation...")

for step in range(300):

    traci.simulationStep()

    # Check traffic every 50 seconds
    if step % 50 == 0:

        vehicles_in_simulation = traci.vehicle.getIDCount()

        print(
            "Simulation time:",
            step,
            "seconds | Vehicles:",
            vehicles_in_simulation
        )

        # Simple adaptive rule
        if vehicles_in_simulation <= 5:
            congestion = "LOW"
        elif vehicles_in_simulation <= 10:
            congestion = "MEDIUM"
        else:
            congestion = "HIGH"

        green_time = get_green_time(congestion)

        traci.trafficlight.setPhaseDuration(
            tls_id,
            green_time
        )

        print(
            "Congestion:",
            congestion,
            "| Green time:",
            green_time,
            "seconds"
        )


# -----------------------------
# 4. Calculate waiting time
# -----------------------------

vehicle_ids = traci.vehicle.getIDList()

total_waiting_time = 0

for vehicle_id in vehicle_ids:
    total_waiting_time += traci.vehicle.getAccumulatedWaitingTime(
        vehicle_id
    )

print()
print(
    "Adaptive signal total waiting time:",
    total_waiting_time,
    "seconds"
)


# -----------------------------
# 5. Close SUMO
# -----------------------------

traci.close()

print("Adaptive simulation completed!")
print("Connection closed.")