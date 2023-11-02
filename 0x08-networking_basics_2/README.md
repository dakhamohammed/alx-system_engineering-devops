# 0x08. Networking basics #1

## General

* What is localhost/127.0.0.1
  * What is 0.0.0.0
  * What is /etc/hosts
  * How to display your machine’s active network interfaces

### Tasks:

1. **Task 0: Change your home IP.** `0-change_your_home_IP`
   - Bash script that configures an Ubuntu server with the below requirements.
     - localhost resolves to 127.0.0.2
     - facebook.com resolves to 8.8.8.8

2. **Task 1: Show attached IPs.** `1-show_attached_IPs`
   - Bash script that displays all active IPv4 IPs on the machine it’s executed on.
     - Example:
     ```bash
     user@ubuntu$ ./1-show_attached_IPs | cat -e
     10.0.2.15$
     127.0.0.1$
     user@ubuntu$ 
     ```

