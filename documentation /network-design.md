# Network Design

## Overview

This project simulates an enterprise HQ and branch network using Cisco Packet Tracer.

Day 1 established the HQ LAN with departmental VLANs, inter-VLAN routing, DHCP, DNS, and a dedicated server VLAN.

Day 2 extends the network by adding a branch router and implementing OSPF dynamic routing between the HQ and branch networks.

Day 3 adds Layer 2 redundancy, Spanning Tree Protocol, LACP EtherChannel, PortFast, and BPDU Guard.

## Network Architecture

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

## VLAN Design

| VLAN | Name       | Purpose            |
| ---- | ---------- | ------------------ |
| 10   | IT         | IT department      |
| 20   | HR         | Human Resources    |
| 30   | Finance    | Finance department |
| 40   | Sales      | Sales department   |
| 50   | Servers    | Network services   |
| 99   | Management | Network management |

## IP Addressing

| Network          | Gateway       | Purpose    |
| ---------------- | ------------- | ---------- |
| 192.168.10.0/24  | 192.168.10.1  | IT         |
| 192.168.20.0/24  | 192.168.20.1  | HR         |
| 192.168.30.0/24  | 192.168.30.1  | Finance    |
| 192.168.40.0/24  | 192.168.40.1  | Sales      |
| 192.168.50.0/24  | 192.168.50.1  | Servers    |
| 192.168.99.0/24  | 192.168.99.1  | Management |
| 192.168.100.0/24 | 192.168.100.1 | Branch     |

### R1-R2 Transit Network

```text
R1-EDGE Fa0/1       10.0.0.1/30
R2-BRANCH-A Fa0/0   10.0.0.2/30
```

## OSPF Design

OSPF process 1 is used for dynamic routing between the HQ and branch.

| Device      | Router ID | Area |
| ----------- | --------- | ---- |
| R1-EDGE     | 1.1.1.1   | 0    |
| R2-BRANCH-A | 2.2.2.2   | 0    |

The R1-R2 point-to-point link forms the OSPF adjacency.

The branch LAN `192.168.100.0/24` is advertised by R2 and learned dynamically by R1.

## Design Decisions

### VLAN Segmentation

Departments are separated into individual VLANs to create distinct broadcast domains and provide a foundation for implementing access control policies.

### Router-on-a-Stick

R1 uses 802.1Q subinterfaces to provide Layer 3 gateway functionality for multiple VLANs over a single physical interface.

### DHCP

R1 provides DHCP services for the client VLANs, automatically assigning IP addresses, default gateways, and DNS information.

### Server VLAN

Servers are isolated in VLAN 50 and use static addressing for predictable access to network services.

### OSPF

OSPF was selected as the dynamic routing protocol to allow routers to automatically exchange routing information as the network expands.

### Passive Interfaces

User-facing LAN interfaces are configured as passive OSPF interfaces because they do not need to form OSPF neighbor relationships.

The R1-R2 transit link remains active for OSPF neighbor formation.

### Spanning Tree Protocol

PVST is used to prevent Layer 2 switching loops.

CORE-SW is configured as the preferred STP root for VLANs 10, 20, 30, 40, 50, and 99.

A redundant Layer 2 path was created between CORE-SW and SW-A to demonstrate STP loop prevention and failover.

### EtherChannel

LACP is configured between CORE-SW and SW-A.

Two physical trunk links are bundled into `Port-channel1`, providing redundancy while allowing the physical links to operate as a single logical connection.

### PortFast

PortFast is enabled on end-device access ports on SW-A so that client devices can transition to the forwarding state without waiting for the normal STP process.

### BPDU Guard

BPDU Guard is enabled on the same end-device ports to protect the network from unexpected BPDUs and unauthorized Layer 2 connections.

