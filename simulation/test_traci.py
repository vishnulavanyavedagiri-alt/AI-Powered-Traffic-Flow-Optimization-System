import traci

sumo_cmd = [
    "C:/Program Files (x86)/Eclipse/Sumo/bin/sumo.exe",
    "-c",
    "simulation/traffic.sumocfg"
]

traci.start(sumo_cmd)

print("Python connected to SUMO!")

traci.simulationStep()

print("SUMO simulation step completed!")

traci.close()

print("Connection closed.")