# 0x07. Networking basics #0

## Learning Objectives:

* **OSI Model**
  * What it is
  * How many layers it has
  * How it is organized

* **What is a LAN**
  * Typical usage
  * Typical geographical size

* **What is a WAN**
  * Typical usage
  * Typical geographical size

* **What is the Internet**
  * What is an IP address
  * What are the 2 types of IP address
  * What is localhost
  * What is a subnet
  * Why IPv6 was created

* **TCP/UDP**
  * What are the 2 mainly used data transfer protocols for IP (transfer level on the OSI schema)
  * What is the main difference between TCP and UDP
  * What is a port
  * Memorize SSH, HTTP and HTTPS port numbers
  * What tool/protocol is often used to check if a device is connected to a network

1. **OSI model**
   - OSI (Open Systems Interconnection) is an abstract model to describe layered communication and computer network design. The idea is to segregate the different parts of what make communication possible.
     - File: `0-OSI_model`

2. **Types of network**
   - lAN: connect local devices together.
   - WAN: connects LANs together.
   - Internet: www.google.com :)

3. **MAC and IP address**
   -  MAC address: The unique identifier of a network interface.
   - IP address: Is to devices connected to a network.

4. **UDP and TCP**
   - TCP: It is a protocol that is transferring data in a slow way but surely.
   - UDP: It is a protocol that is transferring data in a fast way and might loss data along in the process.
   - TCP worker: Have you received boxes x, y, z?

5. **TCP and UDP ports**
   - Bash script that displays listening ports:
     - 22 for SSH
     - 80 for HTTP
     - 443 for HTTPS

6. **host on the network**
   - Bash script that pings an IP address passed as an argument.
     - Accepts a string as an argument
     - Displays `Usage: 5-is_the_host_on_the_network {IP_ADDRESS}` if no argument passed
     - Ping the IP 5 times

