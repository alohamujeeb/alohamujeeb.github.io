---
tags:
  - v4l
  - v4l2
---

# Video For Linux (V4L) 


---
## 1. What is V4L and V4L2

- Video4Linux (V4L) is a kernel API (interface) in Linux that lets applications access video devices.

- It provides a standard way for software to:
```
- Capture video from webcams
- Query and modify camera settings
```
- We may think of it as the **driver framework** for video devices in Linux.

- **V4L2 (Video4Linux version 2) is the NEWER version of V4L**.
- Camera vendors need to support the V4L2 standard (via Linux drivers) for their devices to work properly with Linux applications

- Once a video device is successfully connected, the kernel exposes it like:
```
/dev/video0
/dev/video1
```

---
## 2. v4l2-ctl 

- There are utilities built on top of V4L2.
- The most important one is **v4l2-ctl**.
- v4l2-ctl is a command-line utility (from v4l-utils) used to **inspect, configure, and test** V4L2 video devices.
- Following are information that v4l2-ctl can inspect:
	<br> - pixel formats (MJPEG, YUYV, etc.)
	<br> - resolutions
	<br> - frame intervals (FPS)


### Installation of v4l2-ctl

- v4l2-ctl is part of **v4l-utils** package. 

```
sudo apt update
sudo apt install v4l-utils
```

---
## 3. V4L2 system layers

``` mermaid
flowchart LR

subgraph HW["Hardware Layer"]
    CAM["📷 Camera Sensor"]
    CSI["CSI / USB Interface"]
end

subgraph KERNEL["Linux Kernel Space"]
    V4L2DRV["V4L2 Driver"]
    VIDEO_NODE["/dev/video0 (V4L2 device node)"]
end

subgraph USER["User Space"]
    APP["📱 Application\n(OpenCV / FFmpeg / GStreamer / Custom App / V4L2-Ctrl)"]
end

CAM --> CSI
CSI --> V4L2DRV
V4L2DRV --> VIDEO_NODE

APP --> VIDEO_NODE
```


---
## 4. v4l2-ctl quick reference

Device discovery & info:
```
v4l2-ctl --list-devices
v4l2-ctl -d /dev/video0 --info
v4l2-ctl -d /dev/video0 --list-formats-ext
```

Camera control
```
v4l2-ctl -d /dev/video0 --list-ctrls
v4l2-ctl -d /dev/video0 --get-ctrl=brightness
v4l2-ctl -d /dev/video0 --set-ctrl=brightness=120
```

Video format configuration
```
v4l2-ctl -d /dev/video0 --list-formats-ext
v4l2-ctl -d /dev/video0 --set-fmt-video=width=640,height=480
v4l2-ctl -d /dev/video0 --set-fmt-video=width=1280,height=720,pixelformat=MJPG
```

Streaming parameters (provided supported by camera)
```
v4l2-ctl -d /dev/video0 --set-parm=30
v4l2-ctl -d /dev/video0 --set-parm=15
v4l2-ctl -d /dev/video0 --set-parm=60
v4l2-ctl -d /dev/video0 --get-parm
```

---
## 5. Control Streaming Methods

v4l2-ctl lets you choose how frames are transferred between kernel and userspace.

### i. MMAP (memory-mapped buffers) — most common
- Kernel allocates buffers
- Userspace maps them into memory
- Very fast, low overhead

```
v4l2-ctl -d /dev/video0 --stream-mmap --stream-count=100
```

### ii. USERPTR (user-provided buffers)---

```
v4l2-ctl -d /dev/video0 --stream-user --stream-count=100
```

### iii. READ method (simplest, least efficient)

- Frames fetched via read() syscall
- No buffer mapping
- Mostly for: debugging, learning
- Not used in production pipelines

```
v4l2-ctl -d /dev/video0 --stream-read --stream-count=100
```

### iv. Stream with output file (MMAP example)
```
v4l2-ctl -d /dev/video0 \
  --set-fmt-video=width=640,height=480,pixelformat=MJPG \
  --stream-mmap \
  --stream-count=200 \
  --stream-to=video.mjpg
```


---
## 6. A bit about low-level 

- v4l2-ctl is a user-space tool, and it communicates with the camera through V4L2 system calls, mainly:
	<br> **ioctl()** (primary interface for control operations such as setting format, FPS, controls, and starting/stopping streaming)
	<br> **mmap()** (used in streaming to map kernel buffers into user space for efficient zero-copy frame access)
	<br> **read() / write()** (used in simpler or legacy streaming modes, less common today)


- Applications may also use other libraries or media frameworks such as:
	<br> **OpenCV**
	<br> **GStreamer**
	<br> **FFmpeg**
<br>	

- These libraries (OpenCV, Gstreamer, FFmpweg) use the low-level routines ioctl() etc. 

- They typically use V4L2 indirectly via their own capture backends or plugins, which internally rely on V4L2 system calls (mainly ioctl() and mmap()).


### 6.1 V4L2 programmer’s view (ioctl path)


``` mermaid
flowchart LR

APP["Application Code\n(OpenCV / FFmpeg / C/C++ / V4l2-ctl)"]

IOCTL["ioctl() system calls"]

FD["File Descriptor\n(/dev/video0)"]

V4L2["V4L2 Kernel Driver"]

APP --> IOCTL --> FD --> V4L2
```


---
## Relevant links

[Reading camera in Python (Linux Overview)](camera_in_python_linux.md)

