# IP Addressing Plan

## HQ Networks

| VLAN | Name | Network | Gateway |
|------|------|---------|---------|
| 10 | IT | 192.168.10.0/24 | 192.168.10.1 |
| 20 | HR | 192.168.20.0/24 | 192.168.20.1 |
| 30 | Finance | 192.168.30.0/24 | 192.168.30.1 |
| 40 | Sales | 192.168.40.0/24 | 192.168.40.1 |
| 50 | Servers | 192.168.50.0/24 | 192.168.50.1 |
| 99 | Management | 192.168.99.0/24 | 192.168.99.1 |

## Branch Network

| Network | Gateway | Purpose |
|---------|---------|---------|
| 192.168.100.0/24 | 192.168.100.1 | Branch LAN |

## Router-to-Router Link

| Device | Interface | IP Address | Network |
|--------|-----------|------------|---------|
| R1-EDGE | Fa0/1 | 10.0.0.1/30 | 10.0.0.0/30 |
| R2-BRANCH-A | Fa0/0 | 10.0.0.2/30 | 10.0.0.0/30 |

## Server

| Device | IP Address | VLAN | Purpose |
|--------|------------|------|---------|
| DNS Server | 192.168.50.10 | 50 | DNS |

## DHCP

Client VLANs use DHCP provided by R1.

The following addresses are excluded from the DHCP pools:

```text
192.168.10.1 - 192.168.10.20
192.168.20.1 - 192.168.20.20
192.168.30.1 - 192.168.30.20
192.168.40.1 - 192.168.40.20
```

These addresses are reserved for gateways, infrastructure, and potential static assignments.
