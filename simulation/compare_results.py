import traci


SUMO_CMD = [
    "C:/Program Files (x86)/Eclipse/Sumo/bin/sumo.exe",
    "-c",
    "simulation/traffic.sumocfg"
]

TLS_ID = "center"
SIMULATION_STEPS = 300


def run_simulation(signal_type):
    traci.start(SUMO_CMD)

    print()
    print("Running", signal_type, "simulation...")

    total_waiting_time = 0

    for step in range(SIMULATION_STEPS):

        traci.simulationStep()

        # Fixed signal: keep 40 seconds
        if signal_type == "FIXED":
            traci.trafficlight.setPhaseDuration(
                TLS_ID,
                40
            )

        # Adaptive signal
        elif signal_type == "ADAPTIVE":

            vehicle_count = traci.vehicle.getIDCount()

            if vehicle_count <= 5:
                green_time = 20
            elif vehicle_count <= 10:
                green_time = 40
            else:
                green_time = 60

            if step % 50 == 0:
                traci.trafficlight.setPhaseDuration(
                    TLS_ID,
                    green_time
                )

                print(
                    "Time:",
                    step,
                    "| Vehicles:",
                    vehicle_count,
                    "| Green:",
                    green_time
                )

    # Get waiting time from vehicles still in simulation
    vehicle_ids = traci.vehicle.getIDList()

    for vehicle_id in vehicle_ids:
        total_waiting_time += (
            traci.vehicle.getAccumulatedWaitingTime(vehicle_id)
        )

    traci.close()

    return total_waiting_time


# -----------------------------
# Fixed signal
# -----------------------------

fixed_waiting = run_simulation("FIXED")

print()
print("FIXED SIGNAL WAITING TIME:", fixed_waiting, "seconds")


# -----------------------------
# Adaptive signal
# -----------------------------

adaptive_waiting = run_simulation("ADAPTIVE")

print()
print(
    "ADAPTIVE SIGNAL WAITING TIME:",
    adaptive_waiting,
    "seconds"
)


# -----------------------------
# Comparison
# -----------------------------

print()
print("==============================")
print("FINAL COMPARISON")
print("==============================")

print(
    "Fixed signal:",
    fixed_waiting,
    "seconds"
)

print(
    "Adaptive signal:",
    adaptive_waiting,
    "seconds"
)

if fixed_waiting > 0:

    improvement = (
        (fixed_waiting - adaptive_waiting)
        / fixed_waiting
    ) * 100

    print(
        "Difference:",
        round(improvement, 2),
        "%"
    )