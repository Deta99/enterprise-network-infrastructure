# IP Addressing Plan

## VLAN Addressing

| VLAN | Department | Network | Subnet Mask | Gateway |
|------|------------|---------|-------------|---------|
| 10 | IT | 192.168.10.0/24 | 255.255.255.0 | 192.168.10.1 |
| 20 | HR | 192.168.20.0/24 | 255.255.255.0 | 192.168.20.1 |
| 30 | Finance | 192.168.30.0/24 | 255.255.255.0 | 192.168.30.1 |
| 40 | Sales | 192.168.40.0/24 | 255.255.255.0 | 192.168.40.1 |
| 50 | Servers | 192.168.50.0/24 | 255.255.255.0 | 192.168.50.1 |
| 99 | Management | 192.168.99.0/24 | 255.255.255.0 | 192.168.99.1 |

## DHCP

Client VLANs 10, 20, 30, and 40 use DHCP provided by R1-EDGE.

The following address ranges are excluded from DHCP:

- 192.168.10.1 - 192.168.10.20
- 192.168.20.1 - 192.168.20.20
- 192.168.30.1 - 192.168.30.20
- 192.168.40.1 - 192.168.40.20

These ranges are reserved for infrastructure and statically configured devices.

## Server Addressing

| Device | IP Address | Subnet Mask | Gateway | VLAN |
|--------|------------|-------------|---------|------|
| DNS Server | 192.168.50.10 | 255.255.255.0 | 192.168.50.1 | 50 |

The DNS server uses a static IP address to ensure that network clients can consistently reach the service.

## DNS

The DNS server is located in VLAN 50 at:

192.168.50.10

Internal DNS records are configured to provide hostname resolution for network services.
