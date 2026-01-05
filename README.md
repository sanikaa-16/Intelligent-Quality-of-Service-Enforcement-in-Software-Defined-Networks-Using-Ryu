# Intelligent-Quality-of-Service-Enforcement-in-Software-Defined-Networks-Using-Ryu

## Overview

This project implements an intelligent Software Defined Networking (SDN) controller using the RYU framework that dynamically enforces Quality of Service (QoS) policies based on real-time traffic classification. The controller integrates a machine learning model to classify network flows and assigns them to appropriate priority queues at runtime.

Unlike static QoS mechanisms, this system continuously monitors live traffic statistics, adapts to changing flow behavior, and enforces network policies without restarting active flows.

---

## System Architecture

The system consists of a Mininet-based network topology connected to an Open vSwitch (OVS) instance managed by a RYU controller. The controller periodically polls flow statistics, extracts traffic features, performs ML-based classification, and dynamically updates flow rules to enforce QoS.

---

## Key Features

- Dynamic QoS enforcement using OpenFlow
- Machine learning-based traffic classification
- Periodic flow statistics polling
- Runtime flow reclassification and queue reassignment
- Hysteresis mechanism to prevent queue oscillations
- Automatic cleanup of inactive flows
- Scalable and stable controller design

---

## Machine Learning Model

- Model: Random Forest Classifier  
- Training: Offline (pre-trained model loaded at runtime)
- Features:
  - Packet count
  - Byte count
  - Flow duration
  - Throughput
  - Packet rate
- Output Classes:
  - High priority traffic
  - Medium priority traffic
  - Best-effort traffic

The trained model is loaded into the controller at startup and used during each polling interval.

---

## Technologies Used

- RYU SDN Framework
- OpenFlow 1.3
- Mininet
- Open vSwitch (OVS)
- Python 3
- scikit-learn
- iperf / iperf3
- matplotlib (for analysis and visualization)

---

## Project Structure

.
├── ryu_qos_controller.py
├── qos_classifier_random_forest.pkl
├── plot_throughput.py
└── README.md

---

## Setup Instructions

## Prerequisites

```bash
sudo apt update
sudo apt install mininet openvswitch-switch iperf python3-pip
pip3 install ryu scikit-learn joblib matplotlib
Running the Controller
ryu-manager ryu_qos_controller.py
Expected output includes successful model loading and installation of the table-miss flow entry.
Running Mininet
sudo mn --topo single,3 --controller remote --switch ovs
Generating Traffic
h3 iperf -s &
h1 iperf -c h2 -u -b 25M -t 20
During traffic generation, the controller dynamically classifies flows and assigns queues based on predicted traffic priority.
Results and Observations
High-priority flows consistently achieve higher throughput
QoS enforcement adapts dynamically to traffic behavior
Hysteresis mechanism prevents frequent queue switching
Stable controller behavior observed during extended runs
No packet loss due to controller-driven flow updates
Traffic analysis scripts can be used to generate throughput and queue-wise performance graphs.
Future Work
Online learning and adaptive model updates
Multi-switch and multi-path topology support
Latency and jitter-aware classification
Integration with NFV-based services
Real-time visualization dashboard
