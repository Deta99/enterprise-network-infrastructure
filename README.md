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
* Least-privilege access control

## Project Progress

| Stage | Implementation                      | Status |
| ----- | ----------------------------------- | ------ |
| Day 1 | Enterprise LAN + VLANs + DHCP + DNS | ✅      |
| Day 2 | OSPF + Branch Network               | ✅      |
| Day 3 | STP + EtherChannel                  | ✅      |
| Day 4 | ACLs + Network Security             | ✅      |
| Day 5 | Monitoring + SNMP                   | 🔜     |
| Day 6 | Network Automation                  | 🔜     |
| Day 7 | WAN + Multi-Site Design             | 🔜     |

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
