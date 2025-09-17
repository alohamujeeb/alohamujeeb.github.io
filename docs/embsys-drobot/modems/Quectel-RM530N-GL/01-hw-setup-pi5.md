---
tags:
  - quectel
  - RM530N-GL
  - raspberry pi
---

# Hardware setup & connections
This section explains how to connect the RM530N-GL module to a Raspberry Pi board, covering the necessary hardware wiring and interface details.

---
**Note:** 

5G RM530N-GL modem supports TWO types of interfaces to the host computer; USB and PCIe

- ❌ This project does not use the PCIe connection to interface the HAT with the Raspberry Pi 5.
- ✅ Instead, the USB interface is used to connect the HAT to the Raspberry Pi 5.


---
## 1. Three hardware modules
The hardware setup described here is made up of three modules integrated into a single system

| Component | Image(click to enlarge) | Description |
|:--|:--:|:--|
| 5G RM530N-GL | <a href="images/component-1-RM530.png"><img src="images/component-1-RM530.png" width="100" height="100"/></a> | A Sub-6GHz & mmWave 5G module |
| RM530N-GL 5G HAT+| <a href="images/component-2-Hat.jpg"><img src="images/component-2-Hat.jpg" width="100" height="100"/></a> | RM530N-GL Cap  to 5G HAT+ |
| RPi-5 | <a href="images/component-3-Pi5-with-hat-mounted.jpg"><img src="images/component-3-Pi5-with-hat-mounted.jpg" width="100" height="100"/></a> | Raspberry Pi 5 on which cap is mounted |

Description:

1. **5G RM530N-GL:**
A 5G modem responsible for mobile network communication. However, it requires additional components to function properly, including a SIM card and antennas. 
[Quectel 5G RM530N-GL](https://www.quectel.com/product/5g-rm530n-gl/)

2. **RM530N-GL 5G HAT+:**
This HAT acts as a bridge between the modem and the target computer (e.g. Raspberry Pi 5). It provides the necessary interfaces for both sides: a SIM slot and other supports for the modem, and USB/PCIe interfaces to connect with the target computer.
[Waveshre-RM50N-GL_5G_Hat+](https://www.waveshare.com/wiki/RM530N-GL_5G_HAT+#RM5xx_Series_Module)

3. **Target Computer (e.g. Raspberry Pi 5):**
The main computing unit where the HAT is mounted. Once connected, the system becomes a complete, functional solution for 5G communication.

In short:
**"Modem is mounted on the HAT, and the Hat is mounted on RPi-5"**

---
## 2. Additional modules 

Antenna and SIM cards are two important additional units that must be connected to the assembled board. The antenna enables wireless communication, while the SIM card provides access to a mobile network.

- **Antenna:**
An essential hardware component for enabling wireless communication. The antenna, along with its connecting cables, must be attached directly to the modem to ensure proper signal reception and transmission.

- **SIM Card:**
Required to connect to a mobile network. The SIM card is inserted into the slot provided on the HAT, allowing the system to authenticate with a telecommunications operator.

### Pictures of antenna and sim-card slot
Click to enlarge

| Antenna and Wires | SIM-card slot | 
|:--|:--:|
| <a href="images/antenna-and-wires.jpg"><img src="images/antenna-and-wires.jpg" width="100" height="100"/></a> | <a href="images/SIM-slot.jpg"><img src="images/SIM-slot.jpg" width="100" height="100"/></a> | 

---
## 3. Assembling the hardware

Follow the instructions provided in the link below to complete the hardware assembly.

[Waveshre-RM50N-GL_5G_Hat+](https://www.waveshare.com/wiki/RM530N-GL_5G_HAT+#RM5xx_Series_Module)


Connection pictures (Click to enlarge):

| ❌PCIe Connection (NOT used in this project) | ✅ USB Connection (used in this project) | 
|:--|:--:|
| <a href="images/PCIe_TO_5G_HAT+_Hard22.png"><img src="images/PCIe_TO_5G_HAT+_Hard22.png" width="100" height="100"/></a> | <a href="images/usb-modem-and-sim.jpeg"><img src="images/usb-modem-and-sim.jpeg" width="100" height="100"/></a> | 

---
## 4. Final assembled board

Below are some images of the fully assembled product, ready for use:

| Piture type | Image(click to enlarge) | Description |
|:--|:--:|:--|
| USB on Pi-5 | <a href="images/usb-pi.jpeg"><img src="images/usb-pi.jpeg" width="100" height="100"/></a> | Shows the USB ports on the Raspberry Pi 5. |
| SIM and USB on Cap | <a href="images/usb-modem-and-sim.jpeg"><img src="images/usb-modem-and-sim.jpeg" width="100" height="100"/></a> | Shows the SIM card slot and USB modem on the cap. |
| Cap Mounting on PI-5 | <a href="images/side-view-cap.jpeg"><img src="images/side-view-cap.jpeg" width="100" height="100"/></a> | Shows how the cap is mounted onto the Raspberry Pi 5. |

---
## 5. Some useful links

[Quectel 5G RM530N-GL](https://www.quectel.com/product/5g-rm530n-gl/)

[Waveshre-RM50N-GL_5G_Hat+](https://www.waveshare.com/wiki/RM530N-GL_5G_HAT+#RM5xx_Series_Module)

[Hubtronics-RM530N-GL PCIe to 5G Hat+](https://www.hubtronics.in/rm530n-gl-5g-hat-plus?srsltid=AfmBOor0o1-OiXnwroMSHIjHqa-Fa92hwIS_DCLU8MhuV3YA5WxNgYaD)

