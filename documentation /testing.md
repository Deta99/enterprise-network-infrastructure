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

- IP address
- Default gateway
- DNS server

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

## Verification Commands

Important commands used during testing:

```text
show ip interface brief
show ip route
show ip ospf neighbor
show ip ospf interface
show running-config
ping
nslookup
```

## Result

The HQ and branch networks successfully communicate through OSPF dynamic routing, with the branch network being learned automatically by R1.
