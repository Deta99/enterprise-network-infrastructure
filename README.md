# Enterprise Network Infrastructure

## Overview

A continuously evolving enterprise network infrastructure lab built with Cisco Packet Tracer.

The project simulates an enterprise HQ and branch environment while progressively implementing routing, switching, network services, security, redundancy, monitoring, and automation.

## Current Architecture

```text
                         R1-EDGE
                        /        \
                       /          \
                  CORE-SW        R2-BRANCH-A
                /    |    \           |
             SW-A   SW-B   SW-C      SW-D
                \    /
                 \  /
              EtherChannel
                                     |
                                Branch LAN
```

## Network Segmentation

| VLAN | Name       | Network          |
| ---- | ---------- | ---------------- |
| 10   | IT         | 192.168.10.0/24  |
| 20   | HR         | 192.168.20.0/24  |
| 30   | Finance    | 192.168.30.0/24  |
| 40   | Sales      | 192.168.40.0/24  |
| 50   | Servers    | 192.168.50.0/24  |
| 99   | Management | 192.168.99.0/24  |
| -    | Branch     | 192.168.100.0/24 |

## Implemented Technologies

### Switching & LAN

* VLAN segmentation
* 802.1Q trunking
* Router-on-a-Stick
* Inter-VLAN routing
* STP / PVST
* LACP EtherChannel
* PortFast
* BPDU Guard

### Network Services

* DHCP
* DNS
* IPv4 subnetting

### Routing

* OSPF
* OSPF Area 0
* Router IDs
* Passive interfaces
* Dynamic route learning

### Network Security

* Extended ACLs
* Named ACLs
* Source and destination filtering
* TCP/UDP port filtering
* Inbound ACL application
* First-match ACL processing
* Least-privilege access control

### Network Monitoring

* SNMPv2c
* SNMP manager/agent architecture
* SNMP community strings
* Read-only SNMP access
* ACL-restricted SNMP access

### Network Automation

* Python
* Netmiko
* Python-dotenv
* Device inventory
* Multi-device command execution
* Dry-run automation
* Exception handling
* Logging
* Report generation
* Automation summaries

## Project Progress

| Stage | Implementation                             | Status |
| ----- | ------------------------------------------ | ------ |
| Day 1 | Enterprise LAN + VLANs + DHCP + DNS        | ✅      |
| Day 2 | OSPF + Branch Network                      | ✅      |
| Day 3 | STP + EtherChannel + PortFast + BPDU Guard | ✅      |
| Day 4 | Extended ACLs + Network Security           | ✅      |
| Day 5 | SNMPv2c + Monitoring + SNMP Security       | ✅      |
| Day 6 | Python + Netmiko Network Automation        | ✅      |
| Day 7 | WAN + Multi-Site Design                    | 🔜     |

## Repository Structure

```text
enterprise-network-infrastructure/
│
├── README.md
│
├── configs/
│   ├── CORE_ROUTER.txt
│   ├── CORE-SW.txt
│   ├── RouterD.txt
│   ├── SW-A.txt
│   ├── SW-B.txt
│   └── SW-C.txt
│
├── documentation/
│   ├── ip-addressing.md
│   ├── network-design.md
│   └── testing.md
│
├── network-automation/
│   ├── collect.py
│   ├── devices.py
│   ├── requirements.txt
│   └── .gitignore
│
├── packet-tracer/
│   └── enterprise-lan.pkt
│
└── topology/
    ├── enterprise-network-day1.png
    ├── enterprise-network-day2.png
    └── enterprise-network-day3.png
```

Runtime files such as `.env`, `.venv`, logs, reports, and Python cache files are intentionally excluded from version control.

## Day 6 Automation

The Day 6 automation project uses Python and Netmiko to create a reusable framework for managing multiple Cisco IOS devices.

The device inventory is separated from the automation logic:

```text
R1-EDGE       192.168.99.1
R2-BRANCH-A   10.0.0.2
CORE-SW       192.168.99.2
SW-A          192.168.99.3
```

The collector is designed to execute:

```text
show ip interface brief
show ip route
show version
```

against each device.

The automation framework supports:

* Dry-run mode
* SSH connections through Netmiko
* Environment-based credentials
* Multi-device processing
* Exception handling
* Continue-on-failure behavior
* Logging
* Per-device reports
* Final execution summaries

The existing Packet Tracer topology is currently isolated from the Ubuntu host's network interface, so actual Netmiko SSH execution against these Packet Tracer devices has not yet been performed.

The automation framework itself was tested using dry-run execution and connection-failure testing.

A dedicated automation topology will be introduced in the next stage to test real Ubuntu-to-Cisco SSH automation.

## Tools

* Cisco Packet Tracer
* Cisco IOS
* Python 3
* Netmiko
* python-dotenv
* Git / GitHub
* Ubuntu Linux

## Objective

Build a realistic, progressively expanding enterprise network while demonstrating practical configuration, troubleshooting, documentation, security, monitoring, automation, and infrastructure engineering skills.
