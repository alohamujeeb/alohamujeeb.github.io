---
tags:
  - Gazebo installation  
  
---
# Gazebo Installation
This section contains:

```
1. Gazebo Jetty Instllation on Ubuntu 24.04
2. Gazebo Harmonic Instllation on Ubuntu 24.04
3. Gazebo Server Instllation on Ubuntu 24.04
```


---
## <font color='amber'>**1. Gazebo Jetty Installation**</font>

---
### 1.1. Ubuntu and ROS2 platforms

- Gazebo Jetty requires Ubuntu 24.04 and ROS2 Jazzy.
- Ensure that both the Ubuntu and ROS 2 versions match the configuration specified above.
- If your Ubuntu version and ROS2 versions are different, figure out the compatible Gazebo version first.

---
### 1.2 Installing from binaries

####  1.2.1 Install some necessary tools

```bash
sudo apt-get update
sudo apt-get install curl lsb-release gnupg
```

####  1.2.2 Install Gazebo Jetty binaries

Then install:
```bash
sudo curl https://packages.osrfoundation.org/gazebo.gpg --output /usr/share/keyrings/pkgs-osrf-archive-keyring.gpg

echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/pkgs-osrf-archive-keyring.gpg] https://packages.osrfoundation.org/gazebo/ubuntu-stable $(lsb_release -cs) main" | sudo tee /etc/apt/sources.list.d/gazebo-stable.list > /dev/null

sudo apt-get update
sudo apt-get install gz-jetty
```

### 1.3 To uninstall 
If needed, Gazebo Jetty can be uninstalled as follows:

```bash
sudo apt remove gz-jetty && sudo apt autoremove
```

### 1.4 Verify installation

```
gz sim --versions
```


---
## <font color='amber'>**2. Gazebo Harmoic Installation**</font>
- Installing Gazebo from binaries on Ubuntu is quite straightforward. Follow the steps below.


---
### 2.1. Ubuntu and ROS2 platforms

- Gazebo Harmonic requires Ubuntu 24.04 and ROS2 Jazzy.
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
gz sim --versions
```

### 2.5 Verify installation

---
## <font color='amber'>**3. Server-only installation**</font>

- Gazebo has TWO parts: 

1. a simulation server (the real **simulator engine**)
2. a GUI client (visualization window)

- The server runs:

		- physics
		- collisions
		- sensors
		- plugins
		- transport topics
		- world updates
		- simulation clock

- The GUI only:

		- renders graphics
		- shows camera view
		- lets humans interact visually

- Because robotics often does NOT need visualization; hence it is more efficient to do **simpler installation**

- For headless and CI environments where the GUI is not needed, the ```gz-sim10-server``` package provides a lightweight alternative. 

- It installs only the Gazebo simulation server **(gz-sim-server)** without any GUI or Qt dependencies, resulting in a significantly smaller installation footprint.

```bash
sudo apt-get install gz-sim10-server
```


---
## Reference(s)

### Gazebo Jetty
[Gazebo Jetty Instllation- Official Site](https://gazebosim.org/docs/jetty/install/)

[Gazebo Jetty Binary Installation on Ubuntu/Debian](https://gazebosim.org/docs/latest/install_ubuntu/)

### Gazebo Harmonic
[Gazebo Harmonic Installation- Official Site](https://gazebosim.org/docs/harmonic/install/)

[Gazebo Harmonic Binary Installation on Ubuntu/Debian](https://gazebosim.org/docs/harmonic/install_ubuntu/)


