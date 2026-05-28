---
tags:
  - OpenRMF Installation (Jazzy)
---
# OpenRMF Installation (Ubuntu 24.04 and ROS2 Jazzy)
This document provides step-by-step instructions for installing OpenRMF on a system running Ubuntu 24.04 with ROS 2 Jazzy.

---
## Step 1: Install ROS2 Jazzy

- OpenRMF is built on top of ROS 2, so ROS 2 must be installed first.
- The required ROS 2 distribution depends on the Ubuntu version you are using (in this case Jazzy, which is for Ubuntu 24.04)
- Follow the instructioners in the ([ROS2 installation guide](../ros/ros2/ros2-install.md)) 
- Make sure that you add the source commands to your ```.bashrc``` file so they are automatically applied in every new terminal session. Also verify that the **talker and listener** test programs run without any issues.
---
## Step 2: Install prerequisite software for OpenRMF
- This section covers installation using Debian/Ubuntu binary packages.
- OpenRMF can also be installed from source, but source installation is not covered in this document.

---
### Step 2a): Enable system python

- OpenRMF may not install correctly when using isolated Python environments such as Conda. It is recommended to use the **system Python (python3)** instead.
- If Conda is enabled, deactivate it before proceeding:

```bash
conda deactivate
```

---
### Step 2b) Install ROS2 development tools

- Install the required ROS 2 development utilities using apt:

```bash
sudo apt update && sudo apt install ros-dev-tools -y
```

---
### Step 2c) Install Gazebo Harmonic

- Gazebo is a 3D simulation tool that can be used with OpenRMF. On Ubuntu 24.04, the supported version is Gazebo Harmonic, which can be installed as follows.

- First, install the required dependencies:

```bash
	sudo apt-get update
	sudo apt-get install curl lsb-release gnupg
```

- Then install Gazeob Harmonic
```bash
sudo curl https://packages.osrfoundation.org/gazebo.gpg --output /usr/share/keyrings/pkgs-osrf-archive-keyring.gpg

echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/pkgs-osrf-archive-keyring.gpg] https://packages.osrfoundation.org/gazebo/ubuntu-stable $(lsb_release -cs) main" | sudo tee /etc/apt/sources.list.d/gazebo-stable.list > /dev/null

sudo apt-get update

sudo apt-get install gz-harmonic

```

- For more details on Gazebo Harmonic installation, refer to the official documentation:[Gazebo Instllation Reference on Ubuntu 24.04](https://gazebosim.org/docs/harmonic/install_ubuntu/)


---
### Step 2d) Install  non-ROS dependencies of Open-RMF packages

- In addition to Gazebo, Open-RMF requires several non-ROS dependencies.

- Install them using the following commands:

```bash
sudo apt update && \
sudo apt upgrade -y && \
sudo apt install -y \
	python3-fastapi \
	python3-requests \
	python3-shapely \
	python3-socketio \
	python3-yaml \
	ros-jazzy-ros-gz-bridge \
	gz-harmonic 
```


---
## Step 3: Install build tools

### Step 3a): Setup ```rosdep```

- rosdep is used to install system dependencies for ROS packages across different distributions. It is typically installed with ros-dev-tools, but must be initialized and updated before use.


```bash
sudo rosdep init # run if first time using rosdep.
rosdep update
```

### Step 3b): Setup ```colcon``` mixin

- colcon is the ROS 2 build tool used for managing and building workspaces, similar in concept to make.

- The following commands add and update the default mixin repository:

```bash
colcon mixin add default https://raw.githubusercontent.com/colcon/colcon-mixin-repository/master/index.yaml
colcon mixin update default
```


---
## Step 4: Install **Core OpenRMF**

- Install the core OpenRMF packages for ROS 2 Jazzy using apt:

```bash
sudo apt update
sudo apt install -y ros-jazzy-rmf-dev
```

---
## Step 5: Build rmf_demos from source

- Next, build and install rmf_demos from source.
- To run demos and additional tooling, clone the required RMF repositories as shown below.


```bash
mkdir -p ~/rmf_ws/src
cd ~/rmf_ws/src

# Clone RMF repositories
git clone -b jazzy https://github.com/open-rmf/rmf_visualization.git
git clone -b jazzy https://github.com/open-rmf/rmf_visualization_msgs.git
git clone -b jazzy https://github.com/open-rmf/menge_vendor.git
git clone -b jazzy https://github.com/open-rmf/nlohmann_json_schema_validator_vendor.git

# Already included in your notes
git clone -b jazzy https://github.com/open-rmf/rmf_utils.git
git clone -b jazzy https://github.com/open-rmf/rmf_ros2.git
git clone -b jazzy https://github.com/open-rmf/rmf_simulation.git
git clone -b jazzy https://github.com/open-rmf/rmf_traffic.git
git clone -b jazzy https://github.com/open-rmf/rmf_traffic_editor.git
git clone -b jazzy https://github.com/open-rmf/rmf_demos.git

cd ~/rmf_ws
colcon build

# Optional: use symlink install symbolic links (avoid duplicating files in the install folder)
# colcon build --symlink-install
```

---
## Step 6: Source the system
- Source ROS 2 and OpenRMF in your ```.bashrc``` file so they are automatically loaded in every new terminal:

```bash
source /opt/ros/jazzy/setup.bash
source ~/rmf_ws/install/setup.bash
```


---
## Step 7: Verify installation



- Open two terminal in Ubuntu, and type following commands

| Terminal 1 | Terminal 2 |
| ----------------------------------------- | ---------- |
|
```ros2 launch rmf_demos_gz office.launch.xml```  |```ros2 run rmf_demos_tasks dispatch_patrol -p coe lounge -n 3 --use_sim_time```|




---
## External Links

[OpenRMF Installaion with Jazzy- external link ](https://faizanmsiddiqui.com/articles/open-rmf-on-ubuntu-2404-with-ros-2-jazzy-jalisco/)

[OpenRMF Installaion with Kilted- external link ](https://faizanmsiddiqui.com/articles/open-rmf-on-ubuntu-2404-with-ros-2-kilted-kaiju/)




