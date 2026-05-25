---
tags:
  - Gazebo harmonic installation 
  
  
---
# Gazebo Installation


---
## <font color='amber'>**1. Gazebo Jetty Installation**</font>
(to be written)


---
## <font color='amber'>**2. Gazebo Harmoic Installation**</font>

---
### 2.1. Ubuntu and ROS2 platforms

- Gazebo Harmonic requires Ubuntu 24.04 and ROS 2 Jazzy.

- Ensure that both the Ubuntu and ROS 2 versions match the configuration specified above.

- If your Ubuntu version and ROS2 versions are different, figure out the compatible Gazebo version first.

---
### 2.2 Installing from binaries

- Installing Gazebo from binaries on Ubuntu is quite straightforward. Follow the steps below.

####  2.2.1 Install some necessary tools

```bash
sudo apt-get update
sudo apt-get install curl lsb-release gnupg
```

#### 2.2.2 Install Gazebo Harmonic binaries

```bash
sudo curl https://packages.osrfoundation.org/gazebo.gpg --output /usr/share/keyrings/pkgs-osrf-archive-keyring.gpg

echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/pkgs-osrf-archive-keyring.gpg] https://packages.osrfoundation.org/gazebo/ubuntu-stable $(lsb_release -cs) main" | sudo tee /etc/apt/sources.list.d/gazebo-stable.list > /dev/null

sudo apt-get update

sudo apt-get install gz-harmonic
```

### 2.3 To uninstall 
If needed, Gazebo harmonics can be uninstalled as follows:

```bash
sudo apt remove gz-harmonic && sudo apt autoremove
```

### 2.4 Verify installation

```
gz sim --help
```


---
## Reference(s)

[Gazebo Harmonic Binary Installation on Ubuntu/Debian Installation](https://gazebosim.org/docs/harmonic/install_ubuntu/)

[Gazebo Harmonic Installation- Official Site](https://gazebosim.org/docs/harmonic/install/)

