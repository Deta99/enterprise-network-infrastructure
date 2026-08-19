# Enterprise Network Infrastructure

## Overview

A continuously evolving enterprise network infrastructure lab built with Cisco Packet Tracer.

The project simulates an enterprise HQ and multi-site environment while progressively implementing routing, switching, network services, security, redundancy, monitoring, and automation concepts.

## Current Architecture

```text
                         R1-EDGE
                        /        \
                       /          \
                  CORE-SW        R2-BRANCH-A
                /    |    \           |
             SW-A   SW-B   SW-C      SW-D
                                     |
                                Branch LAN

                 Multi-Site WAN Routers
                       R1 / R2 / R3 / R4
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
* PortFast
* BPDU Guard
* LACP EtherChannel

### Network Services

* DHCP
* DNS
* IPv4 subnetting

### Routing & WAN

* OSPF
* OSPF Area 0
* Router IDs
* Passive interfaces
* Dynamic route learning
* Multi-site WAN connectivity

### Network Security

* Extended ACLs
* Traffic filtering by source, destination, and service
* ACL first-match processing

### Network Monitoring

* SNMPv2c
* Read-only SNMP communities
* SNMP access restriction using ACLs
* Basic network monitoring concepts

### Automation

* Network automation concepts
* Python / SSH automation concepts
* Device inventory and error handling
* Automation verification and idempotency

## Project Progress

| Stage | Implementation                      | Status |
| ----- | ----------------------------------- | ------ |
| Day 1 | Enterprise LAN + VLANs + DHCP + DNS | ✅      |
| Day 2 | OSPF + Branch Network               | ✅      |
| Day 3 | STP + EtherChannel                  | ✅      |
| Day 4 | ACLs + Network Security             | ✅      |
| Day 5 | Monitoring + SNMP                   | ✅      |
| Day 6 | Network Automation Concepts         | ✅      |
| Day 7 | WAN + Multi-Site Design             | ✅      |

## Repository Structure

```text
enterprise-network-infrastructure/
│
├── README.md
├── packet-tracer/
├── configs/
├── documentation/
└── topology/
```

## Tools

* Cisco Packet Tracer
* Cisco IOS
* Git / GitHub

## Objective

Build a realistic, progressively expanding enterprise network while demonstrating practical configuration, troubleshooting, documentation, and infrastructure engineering skills.

