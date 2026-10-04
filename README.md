# AI-Powered Traffic Flow Optimization System

## Congestion Reduction and Adaptive Traffic Signal Timing Using YOLO and SUMO Simulation

## Project Overview

The AI-Powered Traffic Flow Optimization System is a prototype system designed to analyze traffic conditions and evaluate adaptive traffic signal timing.

The system uses a pretrained YOLO11n model to detect vehicles from traffic video. The detected vehicles are counted and classified into different congestion levels. Based on the congestion level, an appropriate green-light duration is selected.

The adaptive signal control is evaluated using SUMO (Simulation of Urban Mobility) and TraCI. The performance of the adaptive signal is compared with a fixed-time signal using measured waiting time in the configured simulation scenario.

## Objectives

- Detect vehicles from traffic video using pretrained YOLO11n.
- Count cars, motorcycles, buses, and trucks.
- Classify traffic congestion as LOW, MEDIUM, or HIGH.
- Select adaptive green-light duration based on congestion level.
- Simulate traffic signal control using SUMO.
- Use TraCI to connect Python with SUMO.
- Compare fixed and adaptive signal control.
- Evaluate the measured waiting time.

## System Workflow

Traffic Video
?
YOLO11n Vehicle Detection
?
Vehicle Counting
?
Congestion Classification
?
Adaptive Green-Time Selection
?
SUMO Traffic Simulation
?
Performance Evaluation

## Technologies Used

- Python
- YOLO11n
- Ultralytics
- PyTorch
- OpenCV
- SUMO
- TraCI
- Visual Studio Code

## Vehicle Detection

The project uses the pretrained YOLO11n model for vehicle detection.

The following vehicle classes are considered:

- Car
- Motorcycle
- Bus
- Truck

## Congestion Classification

| Vehicle Count | Congestion Level | Green Time |
|---|---|---|
| 0–5 | LOW | 20 seconds |
| 6–10 | MEDIUM | 40 seconds |
| 11+ | HIGH | 60 seconds |

These values are prototype parameters used for evaluating the adaptive signal logic in the simulation.

## SUMO Simulation

SUMO (Simulation of Urban Mobility) is used to simulate a four-way traffic intersection.

The simulation contains traffic flows from different directions and evaluates fixed and adaptive signal control.

Python communicates with SUMO through TraCI.

## Adaptive Signal Control

The adaptive signal controller selects the green-light duration according to the detected congestion level.

- LOW congestion ? 20 seconds
- MEDIUM congestion ? 40 seconds
- HIGH congestion ? 60 seconds

## Results

The configured SUMO simulation produced the following results:

| Signal Control | Measured Waiting Time |
|---|---:|
| Fixed Signal | 2600 seconds |
| Adaptive Signal | 2376 seconds |

The measured difference was **224 seconds**.

The adaptive signal scenario showed an approximate **8.62% reduction in measured waiting time**.

This result is specific to the configured simulation scenario.

## Advantages

- Uses computer vision for vehicle detection.
- Provides congestion-based adaptive signal timing.
- Combines YOLO with traffic simulation.
- Allows comparison between fixed and adaptive signal control.
- Provides a prototype approach for traffic-flow optimization.

## Current Scope and Future Enhancements

The current project is a prototype evaluated using traffic video and SUMO simulation.

Future enhancements may include:

- Real-time camera feeds.
- More advanced congestion prediction.
- Larger and more complex road networks.
- Additional traffic conditions and vehicle types.
- Integration with real traffic signal hardware.
- Real-world deployment and testing.

## Conclusion

The project demonstrates an AI-based approach for traffic-flow optimization using pretrained YOLO11n for vehicle detection and SUMO for traffic simulation.

The configured simulation showed that adaptive signal control reduced the measured waiting time compared with the fixed signal scenario.

## Author

**Vedagiri Vishnu Lavanya Supraja**

Department of CSE-AIML
St. Ann's College of Engineering and Technology, Autonomous
Academic Year 2026–2027
