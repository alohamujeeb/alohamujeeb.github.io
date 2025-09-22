---
tags:
  - bridges
---

# Bridging and Forwarding Techniques in Linux Networking

Protocol bridges are software or hardware components that connect different network protocols or transports, enabling seamless data transfer between incompatible communication methods.

---
## 1. Introduction

Network bridges come in two main categories:

1. Layer 2 bridges, which operate at the Data Link layer to connect Ethernet segments by forwarding frames based on MAC addresses — essentially making multiple physical or virtual networks act as one LAN.

2. Protocol bridges, which operate at higher layers (Layer 4 and above) and connect different network protocols or transports — for example, converting UDP to TCP or bridging serial ports to network sockets.

In this section, we focus on protocol bridges and their diverse use cases in modern networking.

**My Note:**<br>

- Layer 2 bridging is a formal and standard concept in networking.

- Protocol bridging is a common, practical term to describe bridging beyond Layer 2, but not an official standard category.

----
## 2. List of tools and techniques
Below is a list of common network and protocol bridging tools and techniques, along with typical use cases and whether they support bidirectional communication.


| Bridge Type       | Description      | Example Use Case    | Bidirectional? |
|------------|------------|-----------------|---------------|
| UDP → TCP Bridge             | Converts UDP packets to TCP streams and vice versa | Forward UDP sensor data reliably over TCP    | No (usually)  |
| TCP → TCP Bridge (Proxy)     | Forwards TCP connections from one port to another  | Simple TCP proxy or port forwarder            | Yes           |
| Serial Port → TCP Bridge     | Bridges serial devices (e.g., `/dev/ttyS0`) to TCP | Remote access to serial devices over network  | Yes           |
| UNIX Socket → TCP Bridge     | Bridges local UNIX domain socket to TCP socket      | Container socket forwarding or local IPC      | Yes           |
| IPv4 → IPv6 Bridge           | Converts IPv4 connections to IPv6 and vice versa   | Legacy-IPv4 to modern IPv6 service access     | Yes           |
| TCP → SSL/TLS Bridge         | Adds SSL/TLS encryption to plain TCP connections   | Secure legacy TCP connections                  | Yes           |
| Raw Socket → TCP/UDP Bridge  | Bridges raw network packets to TCP/UDP sockets      | Specialized packet forwarding or monitoring   | Yes           |
| PTY (Pseudo-terminal) Bridge | Connects pseudo terminals for virtual serial ports | Emulates serial ports for applications        | Yes           |
| File → Network Bridge        | Sends file contents over a network socket           | File transfer via TCP/UDP                      | No            |
| Network → File Bridge        | Receives network data and saves to a file           | Packet capture or logging                      | No            |
| Multicast → Unicast Bridge   | Converts multicast streams to unicast               | Deliver multicast streams over unicast networks| No            |
| TCP Load Balancer (Round Robin) | Distributes TCP connections across backend servers | Basic load balancing for TCP services          | Yes           |
| Port Knocking Handler        | Listens on ports and triggers scripts                | Firewall port opening based on knock sequences| No            |
| Virtual Network Interface Bridge | Bridges virtual interfaces (e.g., `tap`, `tun`)  | VPN tunnels and container networking           | Yes           |
| UDP Multicast Forwarder      | Forwards multicast UDP packets to multiple endpoints| Streaming media or device discovery            | No            |

---
## 3. Additional resources on this website
This site covers many of the topics listed above in greater detail. Feel free to explore more!<br>
For your convenience, relevant links and references are provided at the end of this page.

---
## Relevant links
[Data Pipelining](datapiping.md)

