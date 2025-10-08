---
search:
  exclude: true
---

# FCTLab Plan (Connectivity & Networking)
(For my reference only)

---
## 0. Stationary vs Mobile system

| Feature | Moving Devices (Robots / Drones) | Stationary Devices (Office Desktops) |
|----------|----------------------------------|---------|
| **Typical link types** | Wi-Fi, Cellular (4G/5G), sometimes P2P  | Wired Ethernet (preferred), Wi-Fi as secondary | 
| **Frequency of network changes** | High (AP handoffs, cell changes, IP churn) | Low (static ports/IPs, steady SSID) | 
| **IP address stability** | Often changes (DHCP, roaming between subnets, NAT) | Usually stable (static or long DHCP leases) | 
| **Handover & roaming** | Frequent — requires fast handoff (802.11r/k/v), cell reselection | Rare or none | 
| **Latency & jitter** | Can vary widely depending on movement and environment | Usually stable and low | 
| **Bandwidth profile** | Bursty and often upload-heavy (video, telemetry) | Download/upload steady (office apps) | 
| **Reliability expectations** | High for autonomy/safety; intermittent disconnects expected | High, but outages are rarer | 
| **Power & hardware constraints** | Battery-powered; limited CPU and antenna space | Mains-powered; fewer constraints | 
| **NAT / firewall traversal** | Common issue (cellular NAT, CGNAT) | Known firewalls, often static |

---
## 2. Our focus

### 2.1 **Component 1: (IP change issue) **<br>

(QUIC & N3IWF are main tools)<br>
Others possibilities exists such WireGuard (VPN)- 

- IP change prone system
- FAST handover (near Real time)

### 2.2 **Component 2: Multiplie links for redenndency***

- Quic already covers it

### 2.3 **Component 3: (Legacy TCP/UDP application over QUIC) **<br>

- Create a TCP<->QUIC bridge
- useful for many tools such as **ffmpeg** or **rtsp** or connecting to **ROS** or other systems


### 2.4 **Component 4: (multipath- aggregation) --MPQUIC**<br>
(after component-2)

- Similar to MPTCP; which is not suitbale in IP-changing scenarios
- Need to do MPQUIC (my own term); to be done at stream level?
- Aggregatio is NOT at packet level (like MPTCP), but it is based on Stream level
(how transport layer in OS will identify streams)??


### 2.5 **Component-5:** (WebRTC for P2P)

- important in teleoperation
- low latency data and low-quality


## 3.Task List







