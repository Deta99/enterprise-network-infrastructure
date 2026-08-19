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

Connectivity was verified using ping.

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

R1 used Area 0 while the R2 transit interface was temporarily configured for Area 1.

The OSPF adjacency failed as expected.

The configuration was corrected so both interfaces used Area 0.

The adjacency successfully returned to:

```text
FULL
```

The branch route was also restored.

---

# Day 3 — STP and EtherChannel Verification

STP was verified using:

```text
show spanning-tree
show spanning-tree vlan 10
```

Redundant Layer 2 paths were observed, with STP placing the appropriate redundant port into a blocking state.

LACP EtherChannel was verified using:

```text
show etherchannel summary
```

The Port-channel was successfully formed and remained operational when an individual member link was shut down.

PortFast and BPDU Guard behavior were also tested on an edge/access port.

---

# Day 4 — ACL Verification

Extended ACL behavior was tested using controlled traffic between VLANs.

Testing confirmed that:

* Specific traffic could be permitted.
* Restricted traffic could be denied.
* ACL entries followed first-match processing.
* A broad `permit ip any any` placed before a restriction could bypass the intended filtering rule.
* Service-specific rules such as TCP/443 and UDP/53 could be used.

ACL counters were verified using:

```text
show access-lists
```

---

# Day 5 — SNMP Verification

SNMPv2c was configured as a basic network monitoring mechanism.

The SNMP community was configured as read-only:

```text
snmp-server community NETMON ro
```

SNMP access restriction using an ACL was also tested conceptually.

The monitoring design was verified using the following model:

```text
Monitoring Server
       |
       | SNMP
       ↓
Network Device
```

The monitoring server acts as the SNMP manager while the network device acts as the SNMP agent.

SNMP monitoring was evaluated in the context of EtherChannel redundancy, demonstrating that a physical member link can be down while the logical Port-channel remains operational.

---

# Day 6 — Network Automation Verification

Network automation concepts were tested through scenario-based design and troubleshooting.

The automation workflow was defined as:

```text
Inventory
   ↓
Connect
   ↓
Collect current state
   ↓
Make changes
   ↓
Verify
   ↓
Log results
```

Key concepts verified included:

* Device inventory
* SSH-based automation
* Secure credential handling
* Error handling
* Idempotency
* Post-change verification
* Staged deployment

No production configuration changes were automated during this stage.

---

# Day 7 — WAN and Multi-Site Verification

## OSPF Configuration

Four routers were configured with OSPF to provide dynamic routing across the multi-site WAN.

Each router was assigned a unique OSPF router ID.

WAN-facing interfaces were configured to participate in OSPF.

Site LAN interfaces were configured as passive interfaces.

## OSPF Neighbor Verification

OSPF adjacencies were verified using:

```text
show ip ospf neighbor
```

The expected router-to-router adjacencies successfully reached:

```text
FULL
```

## Dynamic Route Verification

Routing tables were checked using:

```text
show ip route
```

Remote site networks were successfully learned through OSPF.

OSPF routes were identified using:

```text
O
```

## Multi-Site Connectivity

Connectivity between the different sites was tested using:

```text
ping
```

Remote networks were reachable through the WAN using dynamically learned OSPF routes.

## Passive Interface Verification

Site LAN interfaces were configured as passive OSPF interfaces.

WAN interfaces remained active for OSPF neighbor formation.

This prevents unnecessary OSPF neighbor relationships on user-facing LANs while maintaining dynamic routing between the sites.

## Day 7 Result

The multi-site WAN successfully provides dynamic routing and end-to-end connectivity between the connected networks.

## Verification Commands

Important commands used throughout the project include:

```text
show ip interface brief
show ip route
show ip ospf neighbor
show ip ospf interface
show spanning-tree
show etherchannel summary
show interfaces trunk
show access-lists
show running-config
ping
nslookup
```

