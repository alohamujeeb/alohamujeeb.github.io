---
tags:
  - ROS2 CLI
---

# ROS 2 Command Line Interface (CLI)

- This document is a short reference of CLI features of the `ros2` command.
- I am using this doc as a high-level cheat sheet for quick lookup.
- It lists the most common ROS 2 CLI commands.
- This is not about programming or writing nodes.

---

## 1. Package & workspace basics

| Action | Command |
|---|---|
| List packages | `ros2 pkg list` |
| Find package path | `ros2 pkg prefix <package_name>` |
| Create package | `ros2 pkg create <name> --build-type ament_python` |
| Build workspace | `colcon build` |
| Source workspace | `source install/setup.bash` |

---

## 2. System control

| Action | Command |
|---|---|
| Check ROS daemon status | `ros2 daemon status` |
| Start ROS daemon | `ros2 daemon start` |
| Stop ROS daemon | `ros2 daemon stop` |
| List installed interfaces | `ros2 interface list` |
| Source ROS environment | `source /opt/ros/jazzy/setup.bash` |
| Check ROS distribution | `echo $ROS_DISTRO` |
| Check ROS environment variables | `printenv | grep ROS` |

---

## 3. Runtime inspection & quick testing

| Action | Command |
|---|---|
| List nodes | `ros2 node list` |
| List topics | `ros2 topic list` |
| Show topic info | `ros2 topic info /topic_name` |
| View topic data | `ros2 topic echo /topic_name` |
| Publish message | `ros2 topic pub /topic std_msgs/msg/String "{data: 'hello'}"` |
| Publish once | `ros2 topic pub --once /topic std_msgs/msg/String "{data: 'hello'}"` |
| List services | `ros2 service list` |
| Call service | `ros2 service call /service_name <type> <args>` |
| List actions | `ros2 action list` |
| Show action info | `ros2 action info /action_name` |
| Send goal to action | `ros2 action send_goal /action_name <type> <values>` |
| Cancel action goal | `ros2 action cancel /action_name` |


---
## 4. std_msgs/msg Types

| Message | Field | Example |
|---|---|---|
| `String` | `string data` | `{data: "hello"}` |
| `Int8` | `int8 data` | `{data: 1}` |
| `Int16` | `int16 data` | `{data: 100}` |
| `Int32` | `int32 data` | `{data: 42}` |
| `Int64` | `int64 data` | `{data: 100000}` |
| `Float32` | `float32 data` | `{data: 3.14}` |
| `Float64` | `float64 data` | `{data: 2.71828}` |
| `Bool` | `bool data` | `{data: true}` |
| `Empty` | (no field) | `{}` |
| `Header` | timestamp + frame info | `{stamp: ..., frame_id: "map"}` |


---
## 5. References

- [Publisher/Subscriber Model](../pubsub-model.md)
- [ROS Concepts](./ros2-concepts.md)
