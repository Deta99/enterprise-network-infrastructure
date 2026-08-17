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

## Result

The HQ and branch networks successfully communicate through OSPF dynamic routing.

Layer 2 redundancy was successfully implemented and tested using STP and LACP EtherChannel.

PortFast and BPDU Guard were successfully configured and verified on end-device access ports.

Extended ACLs were successfully implemented to restrict inter-VLAN and service-level access while maintaining normal connectivity for permitted traffic.

