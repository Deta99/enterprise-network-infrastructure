# Network Design

## Overview

This project implements a simulated enterprise LAN using Cisco Packet Tracer.

The network is designed to provide departmental segmentation, centralized network services, inter-VLAN communication, and structured IP addressing.

## Network Architecture

The network consists of:

- 1 edge router
- 1 core switch
- 3 access switches
- Multiple departmental endpoints
- 1 server

### Architecture

```text
                         R1-EDGE
                            |
                         802.1Q
                          TRUNK
                            |
                        CORE-SW
                      /    |    \
                   TRUNK  TRUNK  TRUNK
                    /       |       \
                  SW-A     SW-B     SW-C
```

## VLAN Design

| VLAN | Name       | Purpose            |
|------|------------|--------------------|
| 10   | IT         | IT department      |
| 20   | HR         | Human Resources    |
| 30   | Finance    | Finance department |
| 40   | Sales      | Sales department   |
| 50   | Servers    | Network services   |
| 99   | Management | Network management |

## Network Technologies

- VLAN segmentation
- 802.1Q trunking
- Router-on-a-Stick
- Inter-VLAN routing
- DHCP
- DNS
- IPv4 subnetting
- Cisco IOS
- Cisco Packet Tracer

## Design Decisions

### VLAN Segmentation

Departments are separated into individual VLANs to create distinct broadcast domains and provide a foundation for implementing access control policies.

### Router-on-a-Stick

A single router interface uses 802.1Q subinterfaces to provide Layer 3 gateway functionality for multiple VLANs.

### DHCP

DHCP is provided by the edge router for client VLANs to automatically assign IP addresses, default gateways, and DNS information.

### Server VLAN

Servers are separated into VLAN 50 and use static addressing so that network services remain predictable and accessible through known addresses.
