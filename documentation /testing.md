# Network Testing

## Objective

Network testing was performed to verify VLAN segmentation, trunking, inter-VLAN routing, DHCP, DNS, and end-to-end connectivity.

## VLAN Verification

Command:

show vlan brief

Expected results:

- VLAN 10 → IT
- VLAN 20 → HR
- VLAN 30 → Finance
- VLAN 40 → Sales
- VLAN 50 → Servers
- VLAN 99 → Management

Access ports were verified to ensure that each endpoint was assigned to the correct VLAN.

## Trunk Verification

Command:

show interfaces trunk

The following links were configured as 802.1Q trunks:

- R1-EDGE ↔ CORE-SW
- CORE-SW ↔ SW-A
- CORE-SW ↔ SW-B
- CORE-SW ↔ SW-C

## Inter-VLAN Routing

Router-on-a-Stick was verified using the following router subinterfaces:

- Fa0/0.10 → 192.168.10.1
- Fa0/0.20 → 192.168.20.1
- Fa0/0.30 → 192.168.30.1
- Fa0/0.40 → 192.168.40.1
- Fa0/0.50 → 192.168.50.1
- Fa0/0.99 → 192.168.99.1

Connectivity was tested between multiple departmental VLANs and the server VLAN.

## DHCP Testing

Client devices in VLANs 10, 20, 30, and 40 were configured to obtain their network settings automatically.

The following parameters were successfully provided by DHCP:

- IP address
- Subnet mask
- Default gateway
- DNS server

Verification command:

show ip dhcp binding


## DNS Testing

The DNS service was enabled on the server at:

192.168.50.10

DNS resolution was tested using:

nslookup server

Hostname resolution successfully returned the server's IP address after enabling the DNS service.

## End-to-End Connectivity

Connectivity was tested between:

- IT → HR
- IT → Finance
- IT → Sales
- Client VLANs → Server VLAN
- Devices within the same VLAN across different access switches

## Troubleshooting Exercise

A simulated Finance connectivity failure was analyzed using a layered troubleshooting methodology.

The troubleshooting process included:

1. Verify the endpoint configuration.
2. Verify the access VLAN.
3. Verify the switch trunk.
4. Verify VLAN propagation.
5. Verify the Layer 3 gateway.
6. Verify routing.

This demonstrated the ability to isolate problems by working from the endpoint toward the network core and Layer 3 infrastructure.
