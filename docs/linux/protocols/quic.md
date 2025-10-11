---
tags:
  - quic
---

# QUIC Protocol

## 1. Introduction
This section introduces the QUIC protocol (Quick UDP Internet Connections), describing its main objectives and comparing it with traditional transport protocols like TCP and UDP.

- At the transport layer, TCP and UDP are the most widely used Internet protocols. 
- TCP provides reliable, connection-oriented communication, making it suitable for scenarios where data loss is unacceptable. 
- In contrast, UDP is a connectionless protocol designed for low-latency applications where occasional data loss is tolerable.

## 1.1. Challenges in mobility devices 
With the rise of mobile internet usage, traditional TCP struggles to handle these scenarios gracefully, often requiring a full connection restart.

- Connection Break on IP Address Change
- Slow Handshake Process
- Poor congestion control

## 1.2 QUIC as modern day solution

**QUIC is a protocol developed based on the lessons learned from the history of TCP and UDP. It combines the reliability of TCP with the speed and flexibility of UDP.** QUIC introduces several innovations aimed at improving internet performance, especially for modern web and mobile applications.

- **Faster Connection Establishent:** It offers faster connection establishment with 0-RTT or 1-RTT handshakes, reducing latency significantly compared to TCP.

- **IP Independence:** QUIC supports connection migration, allowing seamless transitions between networks (e.g., switching from Wi-Fi to mobile data) without dropping the connection. This feature is specially important in today's mobility systems where IP changes are normal scenarios.

- **Multiplexed Streams:** In single QUIC connection, multiple data streams can be created for different purposes (e.g. text, video, audio), each with its own connection requirments. In TCP, we had to create multiple TCP sessions for each independent data streams.

- **Less Head-of-Line blocking:** It enables stream multiplexing over a single connection, which eliminates head-of-line blocking at the transport layer—a major limitation in TCP.

---
## 2. Feature 1 (QUIC for IP independence)
- 
- TCP is built directly on top of the **IP layer** and adds mechanisms for reliability, such as acknowledgments and retransmissions- .

- QUIC is built on top of **UDP**, and it implements its own reliability mechanisms at the application layer. 

- Since **TCP is tightly bound to the IP address**, any change in IP (e.g., due to network switching) causes the connection to break. This requires a full re-establishment of the connection, leading to performance overhead and a non-seamless experience.

- **QUIC**, on the other hand, uses a **connection ID (or token)** to identify a session instead of relying on the IP:PORT tuple. This allows the session to persist across IP changes without breaking.

- This feature is known as **Connection Migration** in QUIC terminology, and it is one of the protocol's **biggest advantages over TCP**, especially in mobile and wireless environments.

(picture to be added here)


---
## 3. Feature 2 (QUIC for multiplexed data channels)

- One of QUIC's key advantages over TCP is its support for stream multiplexing without head-of-line (HoL) blocking at the transport layer. 

- In TCP, when multiple streams are multiplexed over a single connection, a packet loss in one stream can block the delivery of data in all other streams, due to TCP’s in-order delivery requirement. 

- This can significantly degrade performance, especially on unreliable or high-latency networks. QUIC solves this by handling each stream independently within the same connection.

- Packet loss affecting **a particular stream** does not block or delay the others, resulting in more efficient and responsive communication. This particularly important for web browsing, where multiple resources are loaded in parallel.

(a picture to be added here)


---
## 4. Feature 3 (Different stream types)

- In QUIC, data can be transmitted over two types of channels: **streams and datagrams**. 

- **Streams** provide reliable, ordered delivery similar to TCP, making them suitable for tasks like file transfers or web page loading. 

- **Datagrams**, on the other hand, offer unreliable, unordered delivery—much like traditional UDP—ideal for real-time applications such as gaming or video conferencing where low latency is more important than reliability. 

- QUIC allows both types of data transmission to **coexist within a single connection**, giving applications the flexibility to use the most appropriate method for each use case.

(a picture to be added here)

---
## 5. Feature 4 (Built-in encryption)

- QUIC **integrates TLS** directly into the protocol, providing encryption by default for all connections. 

- Unlike TCP, which relies on a separate handshake for TLS (e.g., in HTTPS), QUIC **combines the transport and encryption handshakes**, reducing round-trip time and startup latency. 

- This integration ensures that all QUIC **traffic is secure**, with features like forward secrecy, authentication, and integrity protection built in from the start—enhancing both performance and security.

- In TCP, TLS is optional and implemented through external libraries or protocols (like HTTPS). In contrast, QUIC makes it **mandatory.**

---
## 6. Feature 5 (Multipath support)

- This feature is **experimentsl and under development** in most libraries (as of 2025). 

- QUIC is being extended to support multipath communication, allowing a single connection to use multiple network paths simultaneously (e.g., Wi-Fi + 5G). This can improve bandwidth, resilience, and seamless handover across networks.

---
## 7. QUIC vs MPCTP

### 7.1 Similarities

| Feature                                             | QUIC | MPTCP |
|-----------------------------------------------------|------|-------|
| Multipath support                                   | Yes (emerging) | Yes (core feature) |
| Improves connection reliability                     | Yes  | Yes   |
| Enables use of multiple network interfaces          | Yes  | Yes   |
| Optimized for mobile/multi-network environments     | Yes  | Yes   |

### 7.2 Differences
| Aspect     | QUIC     | MPTCP     |
|---------|-------------|------|
| Transport Layer Base     | UDP-based         | TCP-based         |
| Encryption     | Mandatory (TLS 1.3 built-in)      | Optional (external TLS)           |
| Deployment     | User space (easier deployment)    | Kernel space (harder to deploy)   |
| Multipath Standardization       | In progress (IETF drafts)     | Standardized (RFC 6824)  |
| Stream Multiplexing             | Yes (independent streams)      | No (single stream per subflow)    |
| Head-of-Line Blocking           | Avoided           | Present (TCP behavior)     |
| Connection Migration            | Supported via Connection ID       | Tied to TCP session/subflows      |
| Performance in Mobile Networks  | High (optimized)     | Good, with TCP limitations         |
| Application Compatibility       | Requires QUIC-aware apps/libraries| Transparent to apps (like TCP)     |


### <font color='red'> 7.3 MPTCP dependence on IP</font>

**1. MPTCP and Subflows:**<br>
Multipath TCP (MPTCP) allows a single TCP connection to use multiple network interfaces (subflows) simultaneously. Each subflow is tied to an IP address pair (source and destination).

**2. IP Address Change on One Interface:**<br>
If one interface's IP address changes (for example, due to moving from one Wi-Fi network to another), MPTCP can detect that the subflow tied to the old IP is no longer usable. However, if there are other active subflows on different IP addresses, MPTCP can seamlessly switch traffic to those subflows, maintaining the session without interruption.

**3. Both Interfaces Change IPs Without New Subflows:**<br>
If after some time, the other interface also changes its IP address, and MPTCP does not establish new subflows using the updated IP addresses, the original subflows become invalid. Since the MPTCP session depends on at least one active and reachable subflow, if all subflows are unusable, the session cannot continue.

**4. Session Timeout and Connection Loss:**<br>
Without any valid subflows, MPTCP will eventually time out. The connection will be lost, and the application will need to establish a new connection.

<font color='green'>**This is where QUIC shines**:</font><br>
QUIC is truly independenct of IP andif some or all IPs change, still the connection is intact.


---
<font color='red'>**(still under construction---please come back in a couple days for updated section)**</font>


---
## Quic programming links
This site contains material on how to writing programs using QUIC protocol.
Explore more at: 
	
- [QUIC in GO: Quic-Go Programming](../../programming/frameworks/quicgo101/index.md)
- [QUIC in Python example](../../programming/frameworks/quicgo101/01-hello-world-python-quic.md)