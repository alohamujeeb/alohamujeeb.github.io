---
tags:
  - modemmanager
  - networkmanager
---

Under Construction

# Modem Manager (MM)
ModemManager provides a unified high level API for communicating with mobile broadband modems, regardless of the protocol used to communicate with the actual device (Generic AT, vendor-specific AT, QCDM, QMI, MBIM...).

---
## 1. Need of MM

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
---
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
## 3. Setting up MM 
MM needs to interact with many different modems, each with their quirks, protocols, and required AT command sequences.

### MM detects & talks

Step 1: MM is started
``` console
sudo systemctl start ModemManager
```
Step 2: Plug in a modem (e.g., Quectel RM530N)

Step 3: MM auto-probes the ports
	
- Open each /dev/ttyUSB* port 
- Send some probing AT commands (like ATI, AT+GMM, AT+CGMM, etc.)
- Identify vendor, model, and supported features
- Based on the response, it **maps the modem to a built-in plugin**.


### Modem plugins
ModemManager has many built-in plugins, like:

- quectel
- telit
- sierra
- huawei
- generic

Each plugin knows:

- Which ports are for AT, data, GPS, etc.
- What AT commands to use to initialize
- How to handle PIN, registration, bearer setup, etc.

For Quectel modems like RM530N, the ```quectel``` plugin is typically used.

You can check the plugin being used with:
``` console
mmcli -m 0

mmcli -L  #to see all connected modems 

# to query each one individually
mmcli -m 0
mmcli -m 1
```

---
## 4. State machine
ModemManager follows a state machine.

DISCONNECTED → INITIALIZING → LOCKED → REGISTERED → CONNECTED

It sends AT commands in each state:

- To check SIM status
- Unlock PIN if needed
- Scan/register with network
- Set APN and bring up bearer

---
## 5. mmcli and NM
(this section is under construction)... following is only for my reference to complete this article

mmcli:
``` console
# List modems
mmcli -L

# Show detailed info
mmcli -m 0

# Connect to internet (APN setup)
mmcli -m 0 --simple-connect="apn=your.apn"
```

NM:

If you're using NetworkManager, it will call ModemManager automatically when using a mobile broadband profile.

---
Ignore this section as well...this is yet to be written...some links for my personal reference till I complete this section

for modes
[To be exploredReference](https://spotpear.com/wiki/RM520N-GL.html) 

[2n link](https://forums.quectel.com/t/rg500q-usb-net/25303)

[quectel open doc syste](https://quickopen.readthedocs.io/en/latest/5-usb/UsbNet.html?utm_source=chatgpt.com)

[saeed studio](https://wiki.seeedstudio.com/raspberry_pi_4g_hat_ecm_mobile_internet/)

[saeed 2](https://wiki.seeedstudio.com/raspberry_pi_4g_lte_hat_qmi/)

[MM Plugins-github](https://gitlab.freedesktop.org/mobile-broadband/ModemManager/-/tree/main)




mmcli -L
mmcli -m 0  (for detailed information)
mmcli -i 0  (information is coming from the sim..and not from the network)

sudo mmcli -m 0 --enable
sudo mmcli -m 0 --simple-connect
sudo mmcli -m 0 --connect


ModemManager:
1) start
2) connect to M1:
	mmcli -m 0 --simple-connect="apn=sunsurf"
3) check status: mmcli -m -0
	Status: should be connected (if everything is Ok)... previously "registred"

DSN though ModemManager: 
4) sudo bash -c 'echo -e "nameserver 8.8.8.8\nnameserver 1.1.1.1" > /etc/resolv.conf'
(but it get reset everytime system boots)


If you use NetworkManager:

Set DNS servers through NetworkManager profiles, e.g.:

nmcli connection modify usb0 ipv4.dns "8.8.8.8 8.8.4.4"
nmcli connection modify <connection_name> ipv4.ignore-auto-dns yes
nmcli connection up <connection_name>

Few warnings:
1) If you want to use minicom for AT commands, "stop" the modemmanager first because it also use the same path and you can observe some wrired behaviour.

But under normal operations, modem manager is Ok to run
