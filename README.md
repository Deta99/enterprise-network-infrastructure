# Enterprise Network Infrastructure

A simulated enterprise LAN designed and implemented using **Cisco Packet Tracer**, demonstrating VLAN segmentation, 802.1Q trunking, inter-VLAN routing, DHCP, DNS, structured IPv4 addressing, and network troubleshooting.

## Project Overview

This project simulates the network infrastructure of a small enterprise with multiple departments and centralized network services.

The network was designed to provide:

- Department-level network segmentation
- Inter-VLAN communication
- Centralized DHCP and DNS services
- Dedicated server and management VLANs
- Structured IPv4 addressing
- Layer 2 trunking between network devices
- Layer 3 routing using Router-on-a-Stick
- Network verification and troubleshooting

The objective was not only to configure the network, but also to understand the reasoning behind the architecture and verify connectivity through structured testing.

---

## Network Architecture

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
                 / | \    / | \    / | \
                PCs PCs   PCs PCs  PCs PCs
                            |
                       Server VLAN
```

### Devices

| Device | Role |
|--------|------|
| R1-EDGE | Layer 3 gateway, inter-VLAN routing, DHCP |
| CORE-SW | Core Layer 2 switching |
| SW-A | Access switch |
| SW-B | Access switch |
| SW-C | Access switch |
| Server | DNS and network services |

---

## VLAN Architecture

| VLAN | Name | Purpose | Network |
|------|------|---------|---------|
| 10 | IT | IT department | 192.168.10.0/24 |
| 20 | HR | Human Resources | 192.168.20.0/24 |
| 30 | Finance | Finance department | 192.168.30.0/24 |
| 40 | Sales | Sales department | 192.168.40.0/24 |
| 50 | Servers | Network services | 192.168.50.0/24 |
| 99 | Management | Network management | 192.168.99.0/24 |

Each department is assigned to its own VLAN, creating separate broadcast domains and providing a foundation for future security policies and access control.

---

## Technologies & Concepts

### Layer 2

- VLANs
- 802.1Q trunking
- Access ports
- Core/access switch architecture
- Broadcast domain segmentation
- Spanning Tree Protocol (PVST)

### Layer 3

- IPv4 subnetting
- Inter-VLAN routing
- Router-on-a-Stick
- 802.1Q router subinterfaces
- Default gateways

### Network Services

- DHCP
- DNS
- Static server addressing

### Tools

- Cisco Packet Tracer
- Cisco IOS

---

## Inter-VLAN Routing

Inter-VLAN communication is implemented using **Router-on-a-Stick**.

R1-EDGE uses a single physical interface with multiple 802.1Q subinterfaces:

| Subinterface | VLAN | Gateway |
|--------------|------|---------|
| Fa0/0.10 | 10 | 192.168.10.1 |
| Fa0/0.20 | 20 | 192.168.20.1 |
| Fa0/0.30 | 30 | 192.168.30.1 |
| Fa0/0.40 | 40 | 192.168.40.1 |
| Fa0/0.50 | 50 | 192.168.50.1 |
| Fa0/0.99 | 99 | 192.168.99.1 |

This allows hosts in different VLANs to communicate through the Layer 3 gateway.

---

## DHCP

R1-EDGE provides DHCP services for the client VLANs:

- VLAN 10 — IT
- VLAN 20 — HR
- VLAN 30 — Finance
- VLAN 40 — Sales

Each DHCP scope provides:

- IP address
- Subnet mask
- Default gateway
- DNS server

### Address Reservation

The `.1 - .20` range is excluded from DHCP for each client subnet.

This leaves addresses available for infrastructure and statically configured devices.

Example:

```text
192.168.10.1      Gateway
192.168.10.2-20   Reserved
192.168.10.21+    DHCP clients
```

---

## DNS

A dedicated server is placed in VLAN 50.

```text
IP Address: 192.168.50.10
Gateway:    192.168.50.1
VLAN:       50
```

The server provides internal DNS resolution for network services.

Clients receive `192.168.50.10` as their DNS server through DHCP.

---

## Server VLAN

Network services are isolated into a dedicated server VLAN rather than being placed directly inside a user department.

This provides:

- Predictable addressing
- Separation from user networks
- Easier future access-control implementation
- Centralized network services

---

## Network Verification

The configuration was verified using Cisco IOS show commands and end-to-end connectivity tests.

### VLAN Verification

```text
show vlan brief
```

Used to verify:

- VLAN existence
- VLAN names
- Access-port assignments

### Trunk Verification

```text
show interfaces trunk
```

Used to verify 802.1Q trunk operation between:

- R1-EDGE and CORE-SW
- CORE-SW and SW-A
- CORE-SW and SW-B
- CORE-SW and SW-C

### Router Verification

```text
show ip interface brief
```

Used to verify that all router subinterfaces were operational.

### DHCP Verification

```text
show ip dhcp binding
```

Used to verify DHCP leases assigned to client devices.

### Connectivity Testing

Connectivity was tested between:

- Different departmental VLANs
- Client VLANs and the server VLAN
- Devices within the same VLAN across different access switches

### DNS Testing

DNS resolution was verified using:

```text
nslookup server
```

---

## Troubleshooting Methodology

A simulated Finance connectivity failure was used to practice structured network troubleshooting.

The troubleshooting process followed a layered approach:

```text
Endpoint
   ↓
Access Port
   ↓
VLAN Assignment
   ↓
Trunk
   ↓
Core Switch
   ↓
Router
   ↓
Destination VLAN
```

For a VLAN-specific connectivity issue, the first checks include:

```text
show vlan brief
show interfaces trunk
show ip interface brief
show ip route
```

This approach helps isolate problems instead of changing multiple configurations simultaneously.

---

## Repository Structure

```text
enterprise-network-infrastructure/
│
├── README.md
│
├── packet-tracer/
│   └── enterprise-lan.pkt
│
├── configs/
│   ├── R1-EDGE.txt
│   ├── CORE-SW.txt
│   ├── SW-A.txt
│   ├── SW-B.txt
│   └── SW-C.txt
│
└── documentation/
    ├── network-design.md
    ├── ip-addressing.md
    └── testing.md
```

---

## Key Learning Outcomes

Through this project, I practiced:

- Designing a multi-switch enterprise LAN
- Creating and implementing VLAN segmentation
- Configuring access and trunk ports
- Implementing Router-on-a-Stick
- Configuring inter-VLAN routing
- Deploying DHCP scopes
- Implementing internal DNS
- Designing structured IPv4 addressing
- Verifying network operations using Cisco IOS
- Troubleshooting connectivity using a layered methodology

---

## Future Improvements

The current implementation provides the foundation for a larger enterprise network.

Planned improvements include:

- OSPF dynamic routing
- Redundant network paths
- EtherChannel
- Spanning Tree optimization
- ACL-based traffic filtering
- Port security
- DHCP snooping
- Dynamic ARP Inspection
- Network monitoring with SNMP
- Syslog
- Network automation using Python/Ansible
- Multi-site WAN architecture

---

## Author

**Amer Zaatari**

Computer & Networking Engineering

Focused on networking, backend engineering, infrastructure, and automation.
