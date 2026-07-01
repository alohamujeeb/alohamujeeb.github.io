---
tags:
  - RVIZ installation  
  - RVIZ2 installation  
  
---
# RViz2 Installation

## 1. RViz2 as part of ROS2 package

- RViz2 is distributed as part of ROS 2 and is not released as a standalone software package.
- It is **installed automatically with the ROS2 Desktop installation**.
- it is **not included in the ROS2 Core or ROS2 Base installations**.

[Ros2 Installation](../ros/ros2/ros2-install.md)


---
## 2. Separate Installation

- If required, RViz2 can be installed separately using the package:

```
sudo apt install ros-<distro>-rviz2

# ROS 2 Jazzy (Ubuntu 24.04)
sudo apt install ros-jazzy-rviz2

# ROS 2 Humble (Ubuntu 22.04)
sudo apt install ros-humble-rviz2

# ROS 2 Foxy (Ubuntu 20.04)
sudo apt install ros-foxy-rviz2
```



