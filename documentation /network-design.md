# Network Design

## Overview

This project simulates an enterprise HQ and branch network using Cisco Packet Tracer.

Day 1 established the HQ LAN with departmental VLANs, inter-VLAN routing, DHCP, DNS, and a dedicated server VLAN.

Day 2 extends the network by adding a branch router and implementing OSPF dynamic routing between the HQ and branch networks.

Day 3 adds Layer 2 redundancy, Spanning Tree Protocol, LACP EtherChannel, PortFast, and BPDU Guard.

Day 4 adds network security using extended ACLs to control traffic between VLANs and restrict access to specific services.

Day 5 introduces network monitoring using SNMPv2c and restricts SNMP access using ACL-based security.

Day 6 introduces Python-based network automation using Netmiko.

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

### PortFast and BPDU Guard

PortFast is enabled on end-device access ports on SW-A so that client devices can transition to the forwarding state quickly.

BPDU Guard is enabled on the same end-device ports to protect against unexpected BPDUs and unauthorized Layer 2 connections.

### Access Control Lists

Extended ACLs are used on R1 to control traffic between VLANs.

The ACLs can match:

* Source IP
* Destination IP
* Protocol
* Destination port

An example security policy restricts HR access to the IT network while allowing other traffic.

The HR VLAN can also be restricted to specific services on the server VLAN, such as:

```text
DNS   UDP/53
HTTPS TCP/443
```

Specific permit and deny rules are placed before the general `permit ip any any` rule because ACLs are processed from top to bottom using first-match logic.

ACLs are applied inbound on the corresponding VLAN subinterfaces to filter traffic as it enters R1.

## SNMP Monitoring Design

### SNMP Architecture

Day 5 introduces SNMP-based network monitoring.

The architecture consists of:

```text
SNMP Manager / Monitoring Server
             |
             | SNMP
             |
       Network Devices
       /      |      \
    R1-EDGE CORE-SW  SW-A
```

The network devices operate as SNMP agents.

The monitoring system operates as the SNMP manager.

The manager requests monitoring information from the agents using SNMP.

### SNMP Version

SNMPv2c is used for the monitoring lab.

The configured community string is:

```text
NETMON
```

The community is configured as read-only:

```text
snmp-server community NETMON ro
```

This allows monitoring systems to retrieve information without granting permission to modify device configuration through SNMP.

### SNMP Community String

The community string acts as the shared authentication value for SNMPv2c communication.

For this lab:

```text
NETMON
```

is used as the SNMP community.

Because SNMPv2c community strings are not encrypted, the lab treats SNMP access as something that should be restricted through network controls.

### SNMP Access Control

An ACL is used to restrict which source is allowed to communicate with the SNMP service.

The purpose is to prevent arbitrary hosts from querying network devices using the SNMP community string.

The monitoring server is therefore treated as a trusted monitoring source, while unauthorized sources are denied SNMP access.

### Monitoring Model

```text
              SNMP Manager
                   |
             NETMON / SNMP
                   |
        ┌──────────┼──────────┐
        ↓          ↓          ↓
     R1-EDGE    CORE-SW      SW-A
      Agent      Agent       Agent
```

The design separates:

* Management
* Monitoring
* User traffic

This provides a foundation for centralized network monitoring.

## Network Automation Design

### Automation Architecture

Day 6 introduces a Python-based automation layer.

```text
                 Ubuntu Automation Host
                         |
                         | SSH / Netmiko
                         |
                 Python Automation
                         |
          ┌──────────────┼──────────────┐
          ↓              ↓              ↓
       R1-EDGE        CORE-SW          SW-A
          |
          ↓
     R2-BRANCH-A
```

### Device Inventory

The automation inventory currently contains:

| Device      | Type      | Management IP |
| ----------- | --------- | ------------- |
| R1-EDGE     | Cisco IOS | 192.168.99.1  |
| R2-BRANCH-A | Cisco IOS | 10.0.0.2      |
| CORE-SW     | Cisco IOS | 192.168.99.2  |
| SW-A        | Cisco IOS | 192.168.99.3  |

The inventory is separated from the automation code so devices can be added or removed without changing the collection workflow.

### Automation Commands

The collector is designed to execute:

```text
show ip interface brief
show ip route
show version
```

The same commands can therefore be collected consistently from multiple devices.

### Credential Management

Credentials are loaded through environment variables rather than hard-coded into Python source code.

The `.env` file contains the required credentials and is excluded from Git.

### Dry-Run Mode

The automation framework includes:

```python
DRY_RUN = True
```

Dry-run mode allows the complete automation workflow to be tested without establishing SSH connections or modifying devices.

### Error Handling

Each device is processed independently.

If a device is unreachable, the exception is logged and processing continues with the next device.

This prevents a single device failure from terminating the entire automation run.

### Logging

Automation activity is written to:

```text
logs/automation.log
```

The log records:

* Automation start
* Device processing
* Connection attempts
* Command execution
* Failures
* Report generation
* Automation completion

### Report Generation

The collector is designed to generate individual reports under:

```text
reports/
```

Each report contains device information, collection time, commands, and command output.

Logs and reports are runtime artifacts and are excluded from version control.

### Current Automation Limitation

The existing Packet Tracer network is not directly reachable from the Ubuntu host's physical network interface.

Therefore, actual SSH connections from Netmiko to the Packet Tracer devices have not yet been performed.

The automation framework itself was tested using dry-run execution and simulated connection-failure handling.

A dedicated automation test topology will be created for the next stage so that the Ubuntu host can establish real SSH connections to Cisco devices.

