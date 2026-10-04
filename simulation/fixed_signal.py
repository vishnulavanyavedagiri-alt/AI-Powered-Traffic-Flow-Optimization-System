import traci


sumo_cmd = [
    "C:/Program Files (x86)/Eclipse/Sumo/bin/sumo.exe",
    "-c",
    "simulation/traffic.sumocfg"
]

traci.start(sumo_cmd)

print("Connected to SUMO!")

tls_id = "center"

# Fixed signal timing
fixed_green_time = 40

print("Fixed green time:", fixed_green_time, "seconds")

# Set fixed signal timing
traci.trafficlight.setPhaseDuration(
    tls_id,
    fixed_green_time
)

print("Fixed signal timing applied!")

# Run simulation
print("Starting fixed-signal simulation...")

for step in range(300):

    traci.simulationStep()

    if step % 50 == 0:
        print("Simulation time:", step, "seconds")


# Calculate waiting time
vehicle_ids = traci.vehicle.getIDList()

total_waiting_time = 0

for vehicle_id in vehicle_ids:
    total_waiting_time += traci.vehicle.getAccumulatedWaitingTime(vehicle_id)

print()
print("Fixed signal total waiting time:", total_waiting_time, "seconds")

traci.close()

print("Fixed-signal simulation completed!")
print("Connection closed.")