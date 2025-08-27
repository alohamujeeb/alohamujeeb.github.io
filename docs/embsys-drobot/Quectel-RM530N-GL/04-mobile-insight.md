# Mobileinsight
MobileInsight is an open-source tool that lets researchers, developers, and engineers access and analyze low-level cellular network information directly from mobile devices.


---
## 1. Linux Installation

### Install Dependencies
MobileInsight is built on top of ```pyserial``` and ```crcmod```.

The GUI of MobileInsight requires ```matplotlib``` and ```wxPython```. 

``` console
#for python modules
pip install pyserial
pip install crcmod
pip install matplotlib

#for linux tools: wxPython 
apt-get install python-wxgtk3.0
```


### Install Mobilinsight
Ref: [github installation page](https://github.com/mobile-insight/mobileinsight-core#)

Step 1: Download the git repository to a local folder.

``` console
https://github.com/mobile-insight/mobileinsight-core.git
```

Step 2: Run installation script (but do not execute with root priviledge):
``` console
./install-ubuntu.sh  #do not use sudo
```

- The install script will install MobileInsight package to PYTHONPATH
- install MobileInsight GUI to /usr/local/bin/mi-gui, and run an offline analysis example at the end.



## Useful links

[mobileinsight- github](https://github.com/mobile-insight)
