import traci

sumo_cmd = [
    "C:/Program Files (x86)/Eclipse/Sumo/bin/sumo.exe",
    "-c",
    "simulation/traffic.sumocfg"
]

traci.start(sumo_cmd)

print("Connected to SUMO!")

# Get traffic light IDs
traffic_lights = traci.trafficlight.getIDList()

print("Traffic lights:", traffic_lights)

# Read the current signal state
if traffic_lights:
    tls_id = traffic_lights[0]

    state = traci.trafficlight.getRedYellowGreenState(tls_id)

    print("Traffic light ID:", tls_id)
    print("Current signal state:", state)

traci.close()

print("Connection closed.")