---
tags:
  - modemmanager
  - networkmanager
---

Under Construction

# Modem Manager (MM)


## 1. What is MM

- A modem connected to a computer via USB or PCIe interface, is managed by AT commands. 

- **Method 1:** Send AT commands  to a modem using a terminal emulator software such as Putty, or Minicom.
	
	This method is meant only for testing purpose, and not meant to be used everytime we use a modem.

- **Method 2:** Send the AT commands using a program that shields the details from the higher level utilities. MM is THAT program (i.e. replace manual AT command process to a more automated and easier-one)


### What MM does 

- ✅ ModemManager (MM) is a Linux system service (daemon) that manages mobile broadband (3G/4G/5G) modems.

	- 2G / 3G / 4G / LTE / 5G
	- USB, PCIe, or serial modems
	- Interfaces like: /dev/ttyUSB* (AT ports)

### What MM does NOT

- ❌ ModemManager is specifically for cellular modems only; 
It is NOT for:
	
	- Ethernet (wired)
	- Wi-Fi (wireless LAN)
	- Bluetooth

## 2. Higher level managers

In most desktop or embedded Linux systems:

- NetworkManager (NM) is the overall connection manager.
- It delegates modem-related tasks to ModemManager.
- For Wi-Fi, it uses ```wpa_supplicant```.
- For Ethernet, it handles things directly or via ```systemd-networkd```.

### MM is a bridge 
[Modem] <--USB/Serial-->[MM] <--D-Bus API-->[NM]

- Modem: Your 4G/5G hardware (e.g., Quectel RM530N).
- MM: Manages and communicates with the modem (via AT, MBIM, QMI, etc.) over the USB port. 
- NM: Manages overall network connections (including Wi-Fi, Ethernet, and cellular via ModemManager)
- D-Bus is a message bus system used for inter-process communication on Linux.

---
for modes
[To be exploredReference](https://spotpear.com/wiki/RM520N-GL.html) 

[2n link](https://forums.quectel.com/t/rg500q-usb-net/25303)

[quectel open doc syste](https://quickopen.readthedocs.io/en/latest/5-usb/UsbNet.html?utm_source=chatgpt.com)

[saeed studio](https://wiki.seeedstudio.com/raspberry_pi_4g_hat_ecm_mobile_internet/)

[saeed 2](https://wiki.seeedstudio.com/raspberry_pi_4g_lte_hat_qmi/)





