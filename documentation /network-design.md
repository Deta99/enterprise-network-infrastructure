# Network Design

## Overview

This project simulates an enterprise HQ and multi-site network using Cisco Packet Tracer.

Day 1 established the HQ LAN with departmental VLANs, inter-VLAN routing, DHCP, DNS, and a dedicated server VLAN.

Day 2 introduced the branch network and OSPF dynamic routing.

Day 3 added STP and LACP EtherChannel for Layer 2 redundancy.

Day 4 introduced extended ACLs for network security and traffic filtering.

Day 5 introduced SNMPv2c monitoring concepts and access control.

Day 7 extends the environment into a multi-site WAN using multiple routers and OSPF dynamic routing.

## Network Architecture

```text
                         R1-EDGE
                        /        \
                       /          \
                  CORE-SW        R2-BRANCH-A
                /    |    \           |
             SW-A   SW-B   SW-C      SW-D
                                     |
                                Branch LAN


                    Multi-Site WAN

                  R1 -------- R2
                  |            |
                  |            |
                  R3 -------- R4
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

## OSPF Design

OSPF process 1 is used for dynamic routing between the connected sites.

All WAN router links participate in OSPF Area 0.

Each router uses a unique router ID.

Site LAN interfaces are configured as passive OSPF interfaces because they do not need to form OSPF neighbor relationships.

WAN interfaces remain active for OSPF neighbor formation.

## Multi-Site WAN

Day 7 introduced additional routers to create a multi-site WAN environment.

The routers exchange routing information dynamically using OSPF.

Remote networks are learned through OSPF rather than requiring static routes on each router.

This allows the network to scale as additional sites are introduced.

## Switching Design

### STP

PVST is used to prevent Layer 2 loops.

Redundant Layer 2 paths can be placed into a blocking state when required by STP.

### EtherChannel

LACP is used to combine compatible physical links into a logical Port-channel.

This provides increased link capacity and redundancy.

### PortFast and BPDU Guard

PortFast is used on appropriate edge/access ports.

BPDU Guard protects edge ports from unexpected BPDU reception.

## Security Design

Extended ACLs are used to control traffic based on:

* Source network
* Destination network
* Protocol
* TCP/UDP service

ACL entries are processed using first-match logic.

Specific permit/deny rules are placed before broader rules where required.

## Network Monitoring

SNMPv2c is used to introduce network monitoring concepts.

Network devices act as SNMP agents while the monitoring system acts as the SNMP manager.

Read-only SNMP communities are used, with ACLs available to restrict which hosts can query the devices.

## Design Decisions

### VLAN Segmentation

Departments are separated into individual VLANs to create distinct broadcast domains and provide a foundation for access control policies.

### Router-on-a-Stick

R1 uses 802.1Q subinterfaces to provide Layer 3 gateway functionality for multiple VLANs over a single physical interface.

### DHCP

R1 provides DHCP services for the client VLANs, automatically assigning IP addresses, default gateways, and DNS information.

### Server VLAN

Servers are isolated in VLAN 50 and use static addressing for predictable access to network services.

### OSPF

OSPF was selected as the dynamic routing protocol to allow routers to automatically exchange routing information as the network expands across multiple sites.

### Passive Interfaces

User-facing LAN interfaces are configured as passive OSPF interfaces because they do not need to form OSPF neighbor relationships.

WAN router-to-router interfaces remain active for OSPF neighbor formation.

