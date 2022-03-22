# UPnP Device Finder
 
 **UPnP** is a technology that allows devices in the same network to **advertise their capabilities and presence**, so that users 
 like you and me can find an Apple TV or Chromecast, or connect an XBOX controller without entering the IP address of 
 the device, thanks to a service known as **Simple Service Discovery Protocol** or **SSDP**.
 
 This is a **Python** script that sends an `ssdp:all` search request (`M-SEARCH`) using the `socket` library in Python.
 
 Here's an article that explains how SSDP works, and how you can make your own requests: 
 https://medium.com/@danny.jamesbuckley/ssdp-how-to-find-local-devices-a24f73ce4262.
 
 There are **no dependencies** on this project, other than you need a Python 3 installation on your device.
 
 Run [raw_ssdp_req.py](raw_ssdp_req.py), and it will send out a **multicast** request to all devices in your network. 
 If any of them respond, the contents of their response will be displayed.
