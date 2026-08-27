---
date:
  created: 2026-08-24
  posted: 2026-08-24

author:
  name: Mujeeb
  description: Creator

readtime: 10

categories:
  - Wifi
  
tags:
    - OpenWRT
    - OpenWifi
    - Open-sdr
    
       
---

# <font color='green'>Open Wifi Part 2: Building Networks with Open Wi-Fi Platforms</font>

A practical look at what we can build on top of OpenWrt and openwifi platforms, from Wi-Fi mesh and multi-hop networks to long-range and mobile networking.
<!-- more -->

This article covers the networking protocols, routing mechanisms, and COTS radio systems that can turn these Wi-Fi platforms into mesh, MANET, drone, and wide-area networks. OpenWrt itself supports Wi-Fi mesh technologies such as 802.11s and BATMAN-adv.


---
## <font color='green'>1. Wi-Fi Operating Modes: AP, Client, Mesh and More</font>

A Wi-Fi interface can operate in different **modes**, depending on how it participates in the network.

The most important modes are:

| Mode | Purpose |
|---|---|
| **AP (Access Point)** | Provides Wi-Fi connectivity to client devices |
| **Client / Station (STA)** | Connects to another AP as a Wi-Fi client |
| **Ad-hoc (IBSS)** | Direct Wi-Fi network between devices without an AP |
| **Mesh (802.11s)** | Allows Wi-Fi nodes to form a multi-hop wireless mesh |
| **Monitor** | Passively captures Wi-Fi frames; mainly used for analysis/research |
| **AP + Client** | Device simultaneously provides an AP and connects to another AP |
| **WDS / 4-address** | Extends Layer-2 connectivity between APs |


### AP Mode

In **AP mode**, the Wi-Fi device acts as an access point.

```text
       Phone
         │
       Laptop
         │
         ▼
    ┌─────────┐
    │   AP    │
    └─────────┘
         │
      Network
```

This is the conventional mode used by Wi-Fi routers and access points.

### Client / Station Mode

In **client (STA) mode**, the device connects to an existing AP.

```text
┌─────────┐             ┌─────────────┐
│ Client  │ ──────────► │     AP      │
└─────────┘             └─────────────┘
```

This is how a laptop, phone, or another Wi-Fi device normally connects to a Wi-Fi network.

### Ad-hoc Mode

In **ad-hoc (IBSS) mode**, devices communicate directly with each other without a traditional AP.

```text
Device A ───── Device B
    │              │
    └──── Device C ┘
```

This is a peer-to-peer Wi-Fi network, but it is different from 802.11s mesh.

### Mesh Mode

In **802.11s mesh mode**, Wi-Fi devices become mesh points and can communicate with other mesh points.

```text
       Mesh Node A
        /        \
       /          \
 Mesh Node B ─── Mesh Node C
       \          /
        \        /
       Mesh Node D
```

Traffic can therefore travel through **multiple wireless hops**.

This is the mode that becomes particularly interesting when building larger networks with OpenWrt.

### Selecting Right Hardware for OpenWrt

OpenWrt can configure a supported Wi-Fi interface to operate in different modes, but **the available modes and features depend on the Wi-Fi chipset and driver**.

For example:

```text
OpenWrt
   ↓
Wi-Fi Driver
   ↓
Supported hardware capabilities
   ↓
AP / Client / Mesh / Monitor / ...
```

Therefore, when choosing hardware for an OpenWrt project, we should not only ask:

> **"Does this device support Wi-Fi?"**

We should ask:

> **"Which Wi-Fi operating modes does this hardware and driver support?"**

For example, if we want to build a wireless mesh, **802.11s/mesh support is an important hardware and driver requirement**.

The following sections will focus on the networking technologies that can be built using these Wi-Fi modes, starting with **802.11s mesh**.

---
## <font color='green'>2. Wi-Fi Mesh with 802.11s</font>

Start with the basic problem:

A normal Wi-Fi network looks like this:

```text
                 AP
              /  |  \
             /   |   \
          Phone Laptop Drone
```

The **AP is the central point**. The clients communicate through it.

But suppose we want to place Wi-Fi nodes across a large area, and we don't want every node to have a cable back to a central AP:

```text
       Node A ───── Node B ───── Node C
                             
                         Node D
```

Now the nodes themselves need to communicate with each other.

This is what **802.11s Wi-Fi mesh** is designed for.

### What 802.11s Actually Does

802.11s allows Wi-Fi devices to operate as **mesh points** and establish wireless links with other mesh points.

For example:

```text
       Mesh A
        /   \
       /     \
   Mesh B ── Mesh C
       \       /
        \     /
         Mesh D
```

A packet can therefore travel over multiple Wi-Fi hops:

```text
A → B → C → D
```

The important idea is:

> **In normal Wi-Fi, clients connect to an AP. In 802.11s, the Wi-Fi nodes can also connect to each other and form the mesh itself.**

### Where OpenWrt Fits

OpenWrt provides the software platform used to configure and run the mesh node.

```text
OpenWrt
    ↓
Linux Wi-Fi stack
    ↓
Wi-Fi driver
    ↓
Wi-Fi hardware
    ↓
802.11s wireless mesh
```

But **OpenWrt does not magically make any Wi-Fi hardware capable of mesh**.

The chipset and driver must support the required 802.11s functionality.

### What About Routing?

This is where an important distinction appears.

Imagine:

```text
       A
      / \
     B   C
      \ /
       D
```

802.11s provides the **wireless mesh links** between these nodes.

But the network still needs to determine things such as:

> "If A wants to reach D, which neighbor should A send the packet to?"

This is the **routing/forwarding problem**.

That's where things such as **BATMAN-adv** and **Babel** come in.

Think of the layers as:

```text
        Applications
             ↓
       IP Networking
             ↓
    Routing / Forwarding
      BATMAN-adv / Babel
             ↓
          802.11s
     Wi-Fi Mesh Links
             ↓
       Wi-Fi Hardware
             ↓
        RF / Antenna
```

The key distinction is:

> **802.11s answers: "How can these Wi-Fi nodes form a wireless mesh?"**

> **BATMAN-adv / Babel answer: "How should traffic travel through that mesh?"**

### 802.11s Is Not the Same as "Mesh Wi-Fi" Marketing

A consumer "mesh Wi-Fi" system often means several APs working together to provide coverage and roaming.

**802.11s is more specific:** it is a Wi-Fi standard for **mesh networking between the Wi-Fi nodes themselves**.

For example:

```text
Normal AP network:

Client ── Wi-Fi ── AP ── Network
```

versus:

```text
802.11s mesh:

Node A ── Wi-Fi ── Node B ── Wi-Fi ── Node C
```

That distinction becomes important when building **multi-hop networks**, especially for applications such as rural connectivity and drones.

---
## <font color='green'>3. Mesh Routing: BATMAN-adv and Babel</font>

Once the Wi-Fi nodes can talk to each other, there is another problem:

> **If there are several possible paths, who decides which path a packet should take?**

For example:

```text
       A
      / \
     B   C
     |   |
     D---E
```

Suppose **A wants to reach E**.

It could go:

```text
A → C → E
```

or:

```text
A → B → D → E
```

If the link between C and E fails, the network should be able to use the other path.

This is the job of **mesh routing / forwarding**.

### Where 802.11s Fits

802.11s provides the **wireless mesh links** between the nodes:

```text
A ─── B
│     │
C ─── D
```

Routing then decides **which neighbor to use to reach a destination**.

So:

```text
802.11s
   ↓
"These nodes can communicate wirelessly"

Routing
   ↓
"Use this neighbor to reach the destination"
```

This is why 802.11s and routing protocols such as BATMAN-adv or Babel are **different things**.

---

### BATMAN-adv: L2 Mesh

**BATMAN-adv** operates at **Layer 2**.

A useful mental model is:

> **BATMAN-adv creates an L2/Ethernet-like mesh over the underlying Wi-Fi links.**

For example:

```text
        A ── Wi-Fi ── B ── Wi-Fi ── C
```

BATMAN-adv can make this behave like a single virtual Layer-2 network:

```text
             L2 / Ethernet-like network
        ┌──────────────────────────────┐
        │                              │
        A ───────── B ───────── C
        │                              │
        └──────────────────────────────┘
```

The applications do not need to know that the packet/frame may travel through several intermediate nodes.

BATMAN-adv handles the forwarding:

```text
Application
     ↓
Ethernet frame
     ↓
  BATMAN-adv
     ↓
 Wi-Fi link
     ↓
 Next mesh node
     ↓
 ...
     ↓
Destination
```

So when we say **"BATMAN-adv is an Ethernet overlay over Wi-Fi"**, this is the idea:

```text
        Ethernet / L2
             ↓
        BATMAN-adv
       (L2 mesh layer)
             ↓
            Wi-Fi
             ↓
         Radio
```

It does **not** mean that we need physical Ethernet cables.

---

### Babel: L3/IP Routing

**Babel** works at **Layer 3**, at the IP level.

Its mental model is:

> **"For this IP destination, which neighboring node should I send the packet to?"**

For example, Node A might know:

```text
Destination       Next hop

10.0.0.20         Node B
10.0.0.30         Node C
10.0.0.40         Node B
```

If A wants to send a packet to `10.0.0.40`, it sends it to **Node B**, and Babel's routing information determines the appropriate next hops through the network.

Conceptually:

```text
Application
     ↓
     IP
     ↓
   Babel
     ↓
 Wi-Fi link
     ↓
 Next node
```

---

### BATMAN-adv vs Babel

The easiest way to remember the difference is:

```text
BATMAN-adv
     ↓
"L2 mesh"
     ↓
"How do I forward this Ethernet frame
 through the mesh?"

Babel
     ↓
"L3 routing"
     ↓
"Which next hop should I use
 for this IP destination?"
```

| | BATMAN-adv | Babel |
|---|---|---|
| Layer | **L2** | **L3** |
| Works with | Ethernet frames | IP packets |
| Mental model | Virtual L2/Ethernet mesh | IP routed network |
| Routing/forwarding | Below IP | At IP level |

### Putting It Together

A Wi-Fi mesh network can therefore be thought of as:

```text
                Applications
                     ↓
                    IP
             ┌───────┴────────┐
             ↓                ↓
        BATMAN-adv          Babel
        L2 mesh            L3 routing
             ↓                ↓
             └──────┬─────────┘
                    ↓
                 802.11s
              Wi-Fi mesh links
                    ↓
               Wi-Fi hardware
                    ↓
                 RF / Antenna
```

The important mental model is:

> **802.11s provides the wireless mesh connectivity.**

> **BATMAN-adv provides an L2 mesh over those links.**

> **Babel provides L3/IP routing over those links.**

They are therefore **different layers solving different problems**, rather than three competing types of Wi-Fi mesh.

---
## <font color='green'>4. MANET and FANET: Ad-hoc Networks for Mobile and Flying Nodes</font>

So far, we have considered a **fixed Wi-Fi mesh**:

```text
       A
      / \
     B───C
      \ /
       D
```

The nodes stay roughly where they are, so the network topology is relatively stable.

Now imagine the nodes are moving:

```text
       Drone A
          \
           \
        Drone B

                    Drone C
                       \
                        \
                       Drone D
```

As the drones move, the wireless links between them can **appear, disappear, and change quality**.

This is where **MANET** comes in.

### MANET

**MANET (Mobile Ad-hoc Network)** is a network where:

- There is no fixed network infrastructure required.
- Nodes communicate wirelessly with each other.
- Nodes can move.
- The network automatically adapts as the topology changes.

For example:

```text
Before:

A ─── B ─── C ─── D


After B moves:

A       B       C ─── D
 \             /
  ────────────
```

The network needs to discover the new connectivity and find usable paths.

The important idea is:

> **A MANET is not just a mesh. It is a mesh/network whose nodes and links can change dynamically.**

### FANET

**FANET (Flying Ad-hoc Network)** is a MANET specifically involving **flying nodes, typically drones/UAVs**.

```text
MANET
  │
  ├── Cars
  ├── Ground robots
  ├── Mobile devices
  └── Other mobile nodes
       
FANET
  │
  └── Drones / UAVs
```

FANETs are particularly dynamic because drones can:

- Move quickly
- Change direction
- Move in three dimensions
- Spread apart or come together
- Continuously change their neighboring drones

For example:

```text
             Drone A
              /   \
             /     \
        Drone B   Drone C
             \     /
              \   /
             Drone D
```

As the drones move, the topology may become:

```text
             Drone A

        Drone B          Drone C
             \            /
              \          /
               Drone D
```

The network therefore needs to **adapt its forwarding/routing decisions as the topology changes**.

### How This Relates to Wi-Fi Mesh

MANET and FANET are **networking concepts**, not Wi-Fi modes.

We can build them using different wireless technologies.

For example, a Wi-Fi-based FANET could be:

```text
OpenWrt
   ↓
Wi-Fi
   ↓
Mesh / MANET routing
   ↓
Multi-hop drone network
```

The underlying Wi-Fi could use something such as **802.11s**, while routing mechanisms such as **BATMAN-adv or Babel** determine how traffic moves through the network.

Alternatively, we can use a **dedicated COTS MANET radio**, where the radio and much of the mobile networking functionality are already integrated.

### The Mental Model

Keep these concepts separate:

> **Wi-Fi mesh** → wireless nodes can communicate with each other.

> **802.11s** → one standardized way of creating a Wi-Fi mesh.

> **MANET** → the nodes and network topology can change dynamically.

> **FANET** → a MANET where the nodes are flying vehicles such as drones.

So a drone network can be a:

```text
                 FANET
                   ↓
            MANET / Routing
                   ↓
        ┌──────────┴──────────┐
        ↓                     ↓
   Wi-Fi / 802.11s       COTS MANET Radio
        ↓                     ↓
   Radio hardware        Radio hardware
```

This distinction becomes important when deciding whether to **build a drone network from OpenWrt + Wi-Fi components** or use a **ready-made COTS MANET radio**.


---
## <font color='green'>5. COTS MANET Radios</font>

If our goal is to **build a MANET or FANET**, we do not necessarily need to build the wireless system ourselves.

A **COTS (Commercial Off-The-Shelf) MANET radio** is a ready-made radio designed specifically for **mobile, multi-hop wireless networking**.

The important difference is that the radio already combines much of what we would otherwise have to assemble ourselves:

```text
        COTS MANET Radio
        ┌─────────────────────┐
        │                     │
        │  Radio              │
        │  Multi-hop network  │
        │  Routing            │
        │  Network management │
        │                     │
        └──────────┬──────────┘
                   │
                  RF
                   │
                Antenna
```

We don't start with a generic Wi-Fi chipset and then figure out how to turn it into a mobile ad-hoc network.

Instead, the **MANET functionality is already part of the product**.

### Why Use One?

This is useful when **our goal is to build the network, not to develop the wireless technology**.

For example, with a drone network we may care about:

- Drone-to-drone communication
- Telemetry
- Command and control
- Video
- Position information
- Multi-hop connectivity

We may not want to spend our time implementing and debugging the underlying radio and MANET protocols.

A COTS MANET radio gives us a much more ready-to-use starting point:

```text
Our drone application
          ↓
     COTS MANET radio
          ↓
   Multi-hop wireless
          ↓
      Other drones
```

### COTS MANET Radio vs OpenWrt + Wi-Fi

There are two very different approaches.

**Build it ourselves with OpenWrt:**

```text
OpenWrt
   ↓
Wi-Fi hardware
   ↓
Wi-Fi mesh / routing software
   ↓
Our network
```

We choose the hardware, Wi-Fi mode, mesh mechanism, routing protocol, and other networking components.

**Use a COTS MANET radio:**

```text
COTS MANET radio
        ↓
  Built-in wireless
  + multi-hop networking
        ↓
      Our network
```

Much more of the wireless networking system is already integrated.

### The Trade-off

The main advantage is:

> **Less development work.**

The main disadvantage is:

> **Less control over the underlying wireless implementation.**

With OpenWrt + Wi-Fi, we have considerable freedom to choose and configure the networking stack.

With a COTS MANET radio, the manufacturer has already made many of those decisions for us.

So the choice is roughly:

```text
             More control
                  ↑
                  │
       OpenWrt + Wi-Fi
                  │
                  │
                  │
       COTS MANET radio
                  │
                  ↓
             Less work
```

For example, **Doodle Mesh Rider** is a commercial COTS MANET radio system. It is useful when we want a ready-made multi-hop wireless network rather than building the entire networking system ourselves.

The important mental model is:

> **OpenWrt + Wi-Fi:** we assemble the networking system.

> **COTS MANET radio:** much of the networking system is already built into the radio.


---
## <font color='green'>6. Doodle Mesh Rider: A COTS MANET Example</font>

**Doodle Mesh Rider** is a practical example of the COTS MANET-radio approach.

Instead of taking OpenWrt, a Wi-Fi chipset, 802.11s, and a routing protocol and assembling the system ourselves, Mesh Rider is sold as an **integrated wireless networking system** designed for multi-hop communication.

The basic idea is:

```text
       Drone / Vehicle A
              │
        Mesh Rider
              │
          wireless
              │
       Drone / Vehicle B
              │
        Mesh Rider
              │
          wireless
              │
       Drone / Vehicle C
```

Each radio can participate in the network, and traffic can be forwarded through intermediate nodes.

### Why It Is Different from OpenWrt + Wi-Fi

With an OpenWrt-based system, we might build:

```text
OpenWrt
   ↓
Wi-Fi hardware
   ↓
802.11s
   ↓
BATMAN-adv / Babel
   ↓
Multi-hop network
```

With Mesh Rider, the manufacturer provides the integrated wireless networking system:

```text
Mesh Rider radio
   ↓
Built-in multi-hop networking
   ↓
Other Mesh Rider radios
```

We therefore do not need to separately assemble the Wi-Fi mesh and routing stack just to get a working mobile multi-hop network.

### Why This Is Useful for Drones

For a drone project, this changes the question from:

> **"How do I build a MANET?"**

to:

> **"How do I use a MANET radio as the communication system for my drones?"**

That can be a much better approach when our actual research is about:

- Drone coordination
- Telemetry
- Command and control
- Video
- Distributed drone applications
- Autonomous systems

rather than wireless protocol development.

### The Trade-off

Mesh Rider gives we a **much more integrated and ready-to-use system**, but we give up some of the control we would have with an open software stack.

```text
OpenWrt + Wi-Fi
    ↑
    │ More control
    │ More components to configure
    │ More development work
    ↓
Mesh Rider
    ↑
    │ More integrated
    │ Less development work
    │ Less control over internals
```

So Mesh Rider is a good example of the broader idea behind **COTS MANET radios**:

> **Buy the wireless networking system as a product and concentrate on the application that runs over it.**


---
## <font color='green'>7. Long-Range Wireless Links</font>

A normal Wi-Fi mesh is not automatically a **long-range network**.

The basic problem is simple:

> **If two nodes are too far apart for a reliable Wi-Fi link, mesh routing cannot help.**

For example:

```text
Node A ─────────────── Node B

        too far apart
        → no usable link
```

A mesh only works when neighboring nodes can actually communicate:

```text
A ─── B ─── C ─── D
```

If we want to cover a very large area, we therefore need to think about **the wireless link itself**, not just the routing protocol.

### How Do We Get Longer Range?

There are several ways to create a longer wireless link:

- Use a radio designed for longer-range communication.
- Use lower-frequency bands where appropriate.
- Use higher-gain directional antennas.
- Increase the effective link budget.
- Place radios at elevated locations such as towers or rooftops.
- Use intermediate nodes to create multiple shorter links.

For example:

```text
House A
   │
 Long-range wireless link
   │
Tower / Relay
   │
 Long-range wireless link
   │
House B
```

Or, instead of one extremely long link:

```text
A ───── B ───── C ───── D
  link     link     link
```

Each individual link can be shorter, while the overall network covers a much larger area.

### Long Range vs Mesh

These are different concepts.

**Long-range radio:**

> "How far can two nodes communicate?"

**Mesh:**

> "Can multiple nodes forward traffic for each other?"

They can be combined:

```text
        Long-range link
A ───────────────────── B
                         \
                          \ Long-range link
                           \
                            C
```

This gives us a **long-range multi-hop network**.

### OpenWrt Approach

With OpenWrt, we can build a system using suitable long-range-capable Wi-Fi hardware:

```text
OpenWrt
   ↓
Wi-Fi / radio hardware
   ↓
Long-range wireless link
   ↓
Mesh / routing software
   ↓
Other nodes
```

However, OpenWrt itself does **not** make ordinary Wi-Fi long-range.

The actual range depends on the radio, frequency, transmit power, antenna, antenna gain, receiver sensitivity, channel bandwidth, terrain, obstacles, and regulatory limits.

### COTS MANET Approach

A COTS MANET radio can provide another approach:

```text
COTS MANET radio
        ↓
Long-range wireless link
        ↓
Other MANET radios
```

The advantage is that the manufacturer has already designed the radio and networking system for this type of communication.

### The Important Mental Model

Don't think:

> **"Mesh = long range."**

Think:

```text
                Network coverage
                       ↑
          ┌────────────┴────────────┐
          │                         │
     Long-range links          Multiple hops
          │                         │
      Radio + RF              Mesh / routing
          │                         │
          └────────────┬────────────┘
                       ↓
                 Large coverage
```

A large-area network is therefore usually a combination of **appropriate radio links + suitable node placement + multi-hop networking**.

This distinction becomes especially important for **rural networks and drone networks**, where the distances between nodes can be much greater than those of a typical indoor Wi-Fi network.

### Examples of Long-Range COTS Radios

There are several commercial radios designed specifically for **long-range, mobile, multi-hop networking**.

Some examples are:

- **Doodle Labs Mesh Rider**: a family of long-range mesh radios designed for drones, vehicles, robotics, and other mobile platforms. Doodle Labs describes its current tactical Mesh Rider systems as providing high-throughput, long-range connectivity and multi-hop mesh networking. :contentReference[oaicite:0]{index=0}
- **Silvus StreamCaster**: a family of commercial MANET radios designed for mobile, multi-node wireless networks.
- **Rajant BreadCrumb**: commercial wireless mesh nodes designed for dynamic networks and mobile applications.

These are **not simply ordinary Wi-Fi routers with a longer antenna**. They are purpose-built wireless networking products that integrate the radio and networking functionality needed for multi-node communication.

For example, a Doodle Mesh Rider network can look like:

```text
             Mesh Rider
              Drone A
                 │
              wireless
                 │
             Mesh Rider
              Drone B
                 │
              wireless
                 │
             Mesh Rider
              Drone C
```

The radios can form a multi-hop network, allowing traffic to travel through intermediate nodes.

Doodle Labs' documentation also shows Mesh Rider radios being used in **point-to-point, single-relay, and multi-node relay configurations** for UAV and ground-control applications. :contentReference[oaicite:1]{index=1}

### Long Range Is Not One Fixed Number

It is important not to think of a COTS radio as having one guaranteed range.

The actual range depends on:

- Radio frequency
- Transmit power
- Antenna type and gain
- Antenna height
- Line of sight
- Terrain
- Trees and buildings
- Channel bandwidth
- Required throughput
- Number of hops

For example, Doodle Labs' field measurements show substantially different ranges depending on the environment and configuration. Their documentation reports a **3.2 km link at 5 Mbps in a wooded environment** in one test, while their current tactical Mesh Rider product information describes deployments reaching **hundreds of kilometers under appropriate conditions**. 

So the correct question is not:

> **"How many kilometers does this radio reach?"**

but:

> **"What range and throughput can this radio achieve with the antenna, frequency, altitude, terrain, and network configuration I will actually use?"**

That distinction becomes especially important for **drone networks**, where altitude and line-of-sight can dramatically change the achievable range.



---
## <font color='green'>8. Example Scenario: Drone Networks- Putting the Pieces Together</font>

Now we can put the previous concepts together.

Suppose we have several drones that need to communicate with each other:

- Telemetry
- Command and control
- Video
- Position information
- Data between drones

The drones may move around, so the wireless links between them can change.

For example:

```text
        Drone A
        /      \
       /        \
   Drone B ─── Drone C
       \        /
        \      /
         Drone D
```

If Drone A cannot directly reach Drone D, traffic can travel through another drone:

```text
Drone A → Drone B → Drone D
```

If the drones move, the available paths can change:

```text
Before:

A ─── B ─── C ─── D


After:

A ─── B          C ─── D
       \          /
        \────────/
```

The network therefore needs to **discover available links and adapt its routing as the drones move**.

### Building the Drone Network with OpenWrt

One approach is to build the network from OpenWrt and Wi-Fi components:

```text
OpenWrt
   ↓
Wi-Fi hardware
   ↓
802.11s
   ↓
BATMAN-adv / Babel
   ↓
Multi-hop drone network
```

Here:

- **OpenWrt** provides the networking platform.
- **Wi-Fi hardware** provides the wireless link.
- **802.11s** can provide the Wi-Fi mesh.
- **BATMAN-adv or Babel** can provide the multi-hop forwarding/routing.
- Our drone application runs on top of the resulting network.

This gives us a lot of flexibility, but we have to select compatible hardware and configure the different components ourselves.

### Building the Drone Network with a COTS MANET Radio

The other approach is to use a dedicated **COTS MANET radio** on each drone.

```text
Drone A                  Drone B
┌──────────────┐        ┌──────────────┐
│ Drone        │        │ Drone        │
│ application  │        │ application  │
│              │        │              │
│ MANET radio  │◄──────►│ MANET radio  │
└──────────────┘        └──────────────┘
         \                    /
          \                  /
           ───── Drone C ───
```

The radio already provides much of the wireless networking required to create the multi-hop network.

Examples include:

- **Doodle Mesh Rider**
- **Silvus StreamCaster**
- **Rajant BreadCrumb**

The attraction is that we can concentrate on the **drone system itself**, rather than implementing the underlying MANET networking.

### Which Approach?

The choice is essentially:

```text
             Drone Network
                  │
        ┌─────────┴─────────┐
        ↓                   ↓
 OpenWrt + Wi-Fi       COTS MANET Radio
        │                   │
   More control        More integrated
   More flexibility    Less development
   More configuration  Less control
```

If our research is about **drone networking, coordination, autonomy, telemetry, or applications**, a COTS MANET radio may be the more practical choice.

If we want to **experiment with the networking stack itself**, OpenWrt + Wi-Fi gives us much more freedom.

The key idea is:

> **We do not have to build the wireless technology just because we want to build a drone network. We can use an existing Wi-Fi/mesh stack or buy an integrated MANET radio and focus on the drone system above it.**


---
## <font color='green'>9. Example Scenario: Community and Rural Networks Without Telcos</font>

Imagine houses spread across a large rural or forested area:

```text
        House A

                         House B


              House C


                                  House D
```

The houses may be too far apart for ordinary Wi-Fi, and there may be no convenient fiber or cellular coverage.

One approach is to build a **community-owned wireless network** where the houses themselves become network nodes.

```text
House A ───── House B ───── House C
    \                         /
     ─────── House D ─────────
```

Each house can provide connectivity for its neighbors, allowing traffic to travel across multiple wireless hops.

### What Is Needed?

There are two main approaches.

**OpenWrt-based network:**

```text
OpenWrt
   ↓
Long-range Wi-Fi hardware
   ↓
802.11s / Wi-Fi mesh
   ↓
BATMAN-adv / Babel
   ↓
Multi-hop community network
```

Or use **COTS MANET / mesh radios**:

```text
House A
   ↓
COTS mesh radio
   ↓
House B
   ↓
COTS mesh radio
   ↓
House C
```

The second approach can be attractive when we want a working network without having to assemble and configure the complete wireless networking stack ourselves.

### The Important Physical Constraint

Mesh networking does **not** remove the need for a usable wireless link.

If two houses are 20 km apart and cannot communicate reliably:

```text
House A ─────────────────── House B
              ✕
         no usable link
```

We need an intermediate node:

```text
House A ─── Relay ─── House B
```

The relay might be placed on:

- A hill
- A tower
- A rooftop
- A tall building
- Another house

This is how a community can extend coverage across a much larger area.

### A Larger Network

For example:

```text
             Relay / Tower
              /         \
             /           \
        House A          House B
          |                  |
        House C            House D
             \             /
              \           /
               House E
```

The network can then provide connectivity across the community without every house requiring a direct connection to a central site.

### The Mental Model

The important distinction is:

> **The wireless technology provides the links.**

> **The mesh/routing system connects those links into one network.**

> **The community provides the physical nodes and infrastructure.**

So a rural community network might be built from:

```text
             Community Network
                    ↓
        ┌───────────┴───────────┐
        ↓                       ↓
 OpenWrt + Wi-Fi          COTS Mesh Radio
        ↓                       ↓
 Long-range links         Long-range links
        ↓                       ↓
        └───────────┬───────────┘
                    ↓
              Multi-hop network
```

The result is a network that can operate **without requiring a commercial cellular provider at every location**, provided that the community can deploy and maintain the required radio nodes and backhaul connections.

---
## <font color='green'>10. Putting It Together: Choosing the Right Approach</font>

By now, there are several different ways to build a multi-hop wireless network.

The important thing is to choose the **level at which we want to work**.

### Option 1: OpenWrt + Wi-Fi Mesh

Use this when we want to build the network ourselves using open software and supported Wi-Fi hardware.

```text
OpenWrt
   ↓
Wi-Fi hardware
   ↓
802.11s
   ↓
BATMAN-adv / Babel
   ↓
Multi-hop network
```

This gives us a lot of flexibility.

We can control the networking software, routing, configuration, and network behavior.

The trade-off is that **we have to put the pieces together**, and the Wi-Fi hardware must support the modes and features we need.

### Option 2: OpenWrt + Long-Range Wi-Fi

If the nodes are far apart, we need appropriate radio hardware and antennas.

```text
OpenWrt
   ↓
Long-range Wi-Fi hardware
   ↓
Wireless link
   ↓
Mesh / routing
   ↓
Other nodes
```

Here, OpenWrt is still the networking platform, but the physical Wi-Fi system has to be suitable for the required distance.

### Option 3: COTS MANET Radio

If we don't want to build the wireless networking system ourselves, use an integrated MANET radio.

```text
Our application
       ↓
COTS MANET radio
       ↓
Multi-hop wireless network
       ↓
Other radios
```

Examples include:

- Doodle Mesh Rider
- Silvus StreamCaster
- Rajant BreadCrumb

This is often the most practical approach when **the wireless network is infrastructure for our application**, rather than the subject of our research.

### The Mental Model

The choices can be summarized as:

```text
                    What are we trying to control?
                              │
              ┌───────────────┴───────────────┐
              ↓                               ↓
        The network itself              The application
              │                               │
              ↓                               ↓
      OpenWrt + Wi-Fi                 COTS MANET radio
              │
      ┌───────┴────────┐
      ↓                ↓
   802.11s       Other Wi-Fi
      ↓            approaches
 BATMAN-adv /
   Babel
```

The overall idea is:

> **OpenWrt gives us an open networking platform.**

> **Wi-Fi hardware gives us the wireless link.**

> **802.11s can provide Wi-Fi mesh connectivity.**

> **BATMAN-adv or Babel can provide multi-hop forwarding/routing.**

> **COTS MANET radios provide a more integrated alternative when we don't want to assemble these pieces ourselves.**



---

## Relevant Link(s)

[OpenWrt Official Website](https://openwrt.org/)

[Openwifi TSN: Wi-Fi on system-on-chip](https://openwifi.tech)

