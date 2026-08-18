# Testing and Verification

## Day 1 — LAN Verification

The initial LAN configuration was tested using:

```text
show ip interface brief
show vlan brief
show interfaces trunk
ping
nslookup
```

### Inter-VLAN Routing

Client connectivity between VLANs was tested through the R1 Router-on-a-Stick configuration.

### DHCP

Client devices successfully received:

* IP address
* Default gateway
* DNS server

### DNS

The DNS server was configured at:

```text
192.168.50.10
```

DNS resolution was tested using:

```text
nslookup
```

A DNS service configuration issue was identified during testing and corrected.

---

# Day 2 — OSPF Verification

## R1-R2 Connectivity

The point-to-point link was configured as:

```text
R1: 10.0.0.1/30
R2: 10.0.0.2/30
```

Connectivity was verified using:

```text
ping 10.0.0.2
```

from R1 and:

```text
ping 10.0.0.1
```

from R2.

Both tests were successful.

## OSPF Neighbor Verification

OSPF adjacency was verified using:

```text
show ip ospf neighbor
```

The R1-R2 adjacency successfully reached:

```text
FULL
```

## Dynamic Route Verification

R2 advertised:

```text
192.168.100.0/24
```

R1 successfully learned the branch network through OSPF.

The routing table was verified using:

```text
show ip route
```

The route appeared with the OSPF designation:

```text
O
```

## Passive Interface Verification

The branch LAN interface on R2 was configured as a passive OSPF interface.

The R1-R2 adjacency remained:

```text
FULL
```

confirming that the router-to-router interface remained active.

## OSPF Failure Testing

An intentional OSPF area mismatch was introduced.

R1 used:

```text
Area 0
```

while the R2 transit interface was temporarily configured for:

```text
Area 1
```

The OSPF adjacency failed as expected.

The configuration was corrected so both interfaces used:

```text
Area 0
```

The adjacency successfully returned to:

```text
FULL
```

The branch route was also restored.

---

# Day 3 — STP and EtherChannel Verification

## STP Root Verification

STP operation was verified using:

```text
show spanning-tree
show spanning-tree vlan 10
```

CORE-SW was confirmed as the STP root for the configured VLANs.

## STP Redundancy Testing

A redundant Layer 2 connection was created between CORE-SW and SW-A.

STP placed the redundant path into a blocking state to prevent a Layer 2 loop.

An active path was then shut down to test failover.

The alternate path successfully transitioned to forwarding, confirming STP redundancy.

## EtherChannel Verification

LACP EtherChannel was configured between CORE-SW and SW-A.

The configuration was verified using:

```text
show etherchannel summary
```

The Port-Channel successfully formed with the configured physical members.

## EtherChannel Troubleshooting

During configuration, Fa0/6 was suspended because its Layer 2 configuration was incompatible with the other EtherChannel member.

The issue was identified from the Cisco error message and traced to a trunk/access configuration mismatch.

After correcting the interface configuration, the physical link successfully joined the EtherChannel.

## EtherChannel Failover Testing

One physical EtherChannel member was intentionally shut down.

The Port-Channel remained operational through the remaining physical member, confirming link-level redundancy.

## PortFast Verification

PortFast was configured on SW-A end-device ports.

Verification was performed using:

```text
show spanning-tree interface fa0/2 detail
```

The output confirmed that the port was operating in PortFast mode.

## BPDU Guard Verification

BPDU Guard was configured on the same end-device access ports.

The configuration was verified using:

```text
show running-config interface fa0/2
```

The configuration confirmed BPDU Guard was enabled.

---

# Day 4 — ACL and Network Security Verification

## HR to IT Restriction

An extended ACL was configured on R1 to prevent HR from accessing the IT VLAN.

```text
Source:      192.168.20.0/24
Destination: 192.168.10.0/24
```

The ACL was applied inbound on the HR subinterface.

Traffic from HR to IT was successfully blocked.

## Server Service Restrictions

Access from HR to the server at:

```text
192.168.50.10
```

was restricted to specific services.

Allowed:

```text
UDP/53   DNS
TCP/443  HTTPS
```

Other traffic to the server was denied.

The ACL used specific permit rules before the broader deny rule, followed by:

```text
permit ip any any
```

to allow unrelated traffic to continue normally.

## ACL Verification

ACL operation was verified using:

```text
show access-lists
```

The ACL displayed hit counters for matching traffic.

Example:

```text
Extended IP access list BLOCK-HR-TO-IT
    10 deny ip 192.168.20.0 0.0.0.255 192.168.10.0 0.0.0.255
    20 permit udp 192.168.20.0 0.0.0.255 host 192.168.50.10 eq domain
    30 permit tcp 192.168.20.0 0.0.0.255 host 192.168.50.10 eq 443
    40 deny ip 192.168.20.0 0.0.0.255 host 192.168.50.10
    50 permit ip any any
```

Testing confirmed that HR traffic to the IT network was blocked, while unrelated permitted traffic continued to work.

## ACL Concepts Verified

The Day 4 testing demonstrated:

* Extended ACL configuration
* Named ACLs
* Inbound ACL application
* Source and destination matching
* TCP/UDP port filtering
* First-match processing
* Specific rules before general rules
* ACL hit counters
* Least-privilege access control

## Verification Commands

Important commands used during the project:

```text
show ip interface brief
show ip route
show ip ospf neighbor
show ip ospf interface
show running-config
show vlan brief
show interfaces trunk
show spanning-tree
show spanning-tree vlan 10
show spanning-tree interface fa0/2 detail
show etherchannel summary
show access-lists
ping
nslookup
```

---

# Day 5 — SNMP Monitoring Verification

## SNMP Configuration

SNMPv2c was configured to provide basic network monitoring capability.

The configured community string was:

```text
NETMON
```

with read-only access:

```text
snmp-server community NETMON ro
```

The `ro` option provides read-only SNMP access.

## SNMP Manager and Agent

The monitoring architecture was tested conceptually using the standard SNMP manager/agent model.

```text
SNMP Manager
     |
     | SNMP
     ↓
SNMP Agent
     |
     ↓
Cisco Device
```

The monitoring server acts as the SNMP manager.

Cisco routers and switches act as SNMP agents.

The manager can request operational information from the agents.

## SNMP Version Verification

SNMPv2c was selected for the lab.

The configuration was verified through the device configuration.

The community string was confirmed as:

```text
NETMON
```

and configured for read-only access.

## SNMP Access Restriction

An ACL was used to restrict SNMP access.

The purpose of the ACL was to prevent unauthorized hosts from querying the network devices using the SNMP community string.

The monitoring server was treated as the trusted source for monitoring traffic.

Unauthorized sources were denied SNMP access.

## ACL and SNMP Interaction

The Day 5 exercise demonstrated that SNMP security should not rely only on the community string.

The community string:

```text
NETMON
```

provides the SNMPv2c access value, while the ACL provides source-based network filtering.

The combined design therefore provides:

```text
Monitoring Server
       |
       | Allowed SNMP
       ↓
   Cisco Device
       ↑
       |
 Unauthorized Host
       |
      DENY
```

## Monitoring Concepts Verified

The Day 5 exercise demonstrated:

* SNMPv2c
* SNMP manager
* SNMP agent
* Community strings
* Read-only SNMP access
* ACL-based SNMP restriction
* Separation of monitoring from normal user traffic
* Basic network monitoring architecture

## Verification Commands

Relevant verification commands included:

```text
show running-config
show access-lists
show ip interface brief
```

The SNMP configuration was checked through the running configuration.

ACL behavior was checked through:

```text
show access-lists
```

---

# Day 6 — Network Automation Verification

## Python Environment

A dedicated Python virtual environment was created for the automation project.

The project uses:

```text
Python 3
Netmiko 4.7.0
python-dotenv 1.2.3
```

The required packages were successfully installed.

## SSH Preparation

R1-EDGE was prepared for SSH automation.

The router hostname was changed from the default:

```text
Router
```

to:

```text
R1-EDGE
```

RSA keys were generated using a 1024-bit modulus.

SSH was verified using:

```text
show ip ssh
```

The resulting configuration reported:

```text
SSH Enabled - version 2.0
```

This confirmed that the router was prepared for SSH-based automation.

## Device Inventory

The Python automation project contains a device inventory with:

```text
R1-EDGE       192.168.99.1
R2-BRANCH-A   10.0.0.2
CORE-SW       192.168.99.2
SW-A          192.168.99.3
```

The inventory is stored separately in:

```text
devices.py
```

This separates device information from the automation logic.

## Environment Variables

Credentials are loaded from:

```text
.env
```

using Python-dotenv.

The credentials are not hard-coded into the automation script.

The `.env` file is excluded from Git.

## Dry-Run Testing

The collector supports:

```python
DRY_RUN = True
```

The first automation test was performed in dry-run mode.

The script successfully processed all devices and identified the commands that would be executed:

```text
show ip interface brief
show ip route
show version
```

No SSH connections were attempted while dry-run mode was enabled.

## Logging Verification

Automation activity was successfully written to:

```text
logs/automation.log
```

The log recorded:

```text
Automation run started
Processing device: R1-EDGE
DRY RUN enabled for R1-EDGE
R1-EDGE - Would run: show ip interface brief
R1-EDGE - Would run: show ip route
R1-EDGE - Would run: show version
...
Automation run finished
```

This confirmed that the logging system was functioning correctly.

## Connection Failure Testing

A real connection test was performed with dry-run mode disabled.

The existing Packet Tracer devices were unreachable from the Ubuntu host.

Netmiko therefore generated TCP connection errors for the configured devices.

The important behavior was that the automation did not terminate after the first failure.

The log recorded failures for:

```text
R1-EDGE
R2-BRANCH-A
CORE-SW
SW-A
```

A temporary invalid device was also used during testing:

```text
INVALID-DEVICE
192.0.2.1
```

The script handled the failure and continued processing the remaining devices.

The run ultimately reached:

```text
Automation run finished
```

This confirmed that exception handling and continue-on-failure behavior were working.

The temporary invalid device was subsequently removed.

## Report Generation

The automation framework contains report-generation logic for individual devices.

Reports are designed to contain:

* Device name
* Device IP
* Collection timestamp
* Command executed
* Command output

Reports are stored under:

```text
reports/
```

These files are runtime artifacts and are excluded from Git.

## Current Connectivity Limitation

The existing Packet Tracer topology is not directly reachable from the Ubuntu host's physical network interface.

The Ubuntu host uses its physical network connection independently from the simulated Packet Tracer topology.

Therefore, Netmiko cannot currently establish a TCP/22 connection directly to the Packet Tracer management addresses.

This prevented full real-device command collection from the existing topology.

The limitation was identified and documented rather than treating the connection failure as an automation-code failure.

## Day 6 Result

The following components were successfully implemented and tested:

* Python virtual environment
* Netmiko
* Python-dotenv
* Device inventory
* SSH preparation
* Multi-device iteration
* Multi-command collection logic
* Dry-run mode
* Logging
* Exception handling
* Continue-on-failure behavior
* Report-generation logic
* Automation execution summary

Actual SSH command execution against Cisco devices will be tested in the next automation-specific network topology.

---

# Overall Project Result

The enterprise network now includes:

* VLAN segmentation
* Inter-VLAN routing
* DHCP
* DNS
* OSPF dynamic routing
* STP/PVST
* LACP EtherChannel
* PortFast
* BPDU Guard
* Extended ACLs
* Service-level filtering
* SNMPv2c monitoring
* ACL-restricted monitoring access
* Python network automation
* Netmiko
* Automation logging
* Error handling
* Report generation

The project has progressed from basic enterprise LAN configuration to network security, monitoring, and automation.

The next stage will focus on creating a dedicated automation test network where the Ubuntu host can establish real SSH connections to Cisco devices and execute automated operational and configuration tasks.

