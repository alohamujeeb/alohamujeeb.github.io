---
tags:
  - ros concepts
  - DDS
  - Data Distribution Service

---
# Important ROS Concepts
(under construction)

---
## 1. DDS (Data Distribution Service)
- DDS is the communication system used under ROS 2 to let robots exchange data.
- We can think of DDS like a **post office for robots**:

```text
- One robot sends a message
- DDS delivers it to all robots that are interested
- No robot needs to know where other robots are
```


- **DDS is NOT a broker** (unlike [Publisher/Subscriber Model](../pubsub-model.md) )
- In a typical publisher/subscriber system, everything goes through a broker. For example, in MQTT or Kafka; However, in DDS there is direct communicatio between a two nodes.

```text
Publisher → Broker → Subscriber
(in a broker-based system)


Publisher  ─────────▶ Subscriber
(In ROS: direct P2P)
```

- DDS provides:

```text
- discovery (find other nodes)
- message delivery rules
- reliability (guarantees / QoS)
- serialization of data

- But NOT routing through a broker.
```

--- 
## 2. DDS variants
- We can think of ROS2 communication like messaging apps, where all robots need to “chat” with each other.
- ROS2 gives them different “chat systems” to do it.
- Lets consider that **DDS is a kind of WhatsApp**
- DDS variant is **Same WhatsApp idea, different companies making it**. We can swap them like changing phone brands, not changing the app.
- **DDS variants = different implementations of the same communication system**

```text
(DDS from different vendors based on OMG)
(OMG = Object Management Group that defines the rules for software systems)


- Fast DDS (default in many ROS2 )
- Cyclone DDS (very common, simpler, stable)
- RTI Connext DDS (industrial / enterprise, very reliable)
- OpenSplice DDS (older, less common now)
```

<!-- to be done laters
---
### 3. RMW (ROS Middleware Interface)
- We can think of ROS2 communication like messaging apps, where all robots need to “chat” with each other.
- ROS2 gives them different “chat systems” to do it.
- **Non-DNS = Different messenging systems than WhatsApp; such as Telegram or email **
- 

```text
- RMW is the middle layer between ROS 2 and the communication system (DDS or others).
- It is the “adapter” that lets ROS2 use different communication systems without changing ROS code.


ROS 2 Node ->  RMW layer -> DDS / Zenoh / etc.
```



| Option | Type | Description |
|---|---|---|
| ROS 2 over ZeroMQ | Experimental | Uses message queues instead of DDS; research/experimental backend |
| ROS 2 over Zenoh | Modern distributed middleware | Uses `rmw_zenoh`; good for cloud + edge robotics |
| ROS 2 micro-ROS | Embedded systems | Uses micro XRCE-DDS; lightweight communication for microcontrollers |
-->



<!-- 
Build & Deploy: colcon, launch
Runtime control: ros2cli, lifecycle nodes
Visualization: RViz2, rqt
Simulation: Gazebo
Data & debugging: rosbag2, TF2 tools
Navigation: Nav2 tools
Middleware: DDS (Cyclone/FastDDS)
Performance analysis: ros2_tracing
Embedded robotics: micro-ROS


===================
Must-have core concepts
DDS (Data Distribution Service) – underlying communication middleware
ROS 2 Daemon – CLI cache helper for faster graph queries
ROS 2 CLI (ros2cli)
Nodes – executable processes in ROS 2
Topics – pub/sub commun[Publisher/Subscriber Model](../pubsub-model.md)ication channels
Messages (Interfaces) – data structure definitions
Services – request/response communication
Actions – long-running tasks with feedback
ROS Graph – network of all nodes and connections


---
Very useful (next level clarity)
Publisher / Subscriber – roles of nodes in topics
Client / Server – roles in services
Action Client / Server – roles in actions
RMW (ROS Middleware layer) – abstraction over DDS implementations
Executors – how ROS runs callbacks in nodes
Callback – function triggered by events (messages, timers)
rqt Framework: Qt-based modular GUI toolkit for runtime debugging (topic inspection, graphing, service calls, parameter tuning).
rosbag2 Official ROS 2 tool for recording and replaying data for debugging, testing, and dataset collection.
TF2 Tools: Core transform system tools for debugging robot coordinate frames and spatial relationships in real time.
--- 
Optional but good for completeness
Parameters – runtime configuration of nodes
Launch system – running multiple nodes together
Workspace (colcon) – build environment structure
Package – unit of ROS code organization
micro-ROS: micro-ROS Agent


=============

-->

--- 
## References

#### [Publisher/Subscriber Model](../pubsub-model.md)
#### [What is ROS and related topics](../index.md)



