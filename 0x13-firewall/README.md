# 0x13. Firewall
`DevOps` `SysAdmin` `Security`

![Screenshot](firewall.png)

## Warning!
Be very careful with firewall rules! For instance, if you ever deny port 22/TCP and log out of your server, you will not be able to reconnect to your server via SSH.
When you install UFW, port 22 is blocked by default, so you should unblock it immediately before logging out of your server.

### Task:
* Block all incoming traffic and allow outgoing.
  * except the following TCP ports for incomming traffic:
    * 22 (SSH) to allow connection to our server using ssh on port `22`
    * 443 (HTTPS SSL) to allow traffic between the internet and our webserver.
    * 80 (HTTP) same as HTTPS above but unsecured traffic.

* Port forwarding.
  * Set up a Port Forward Using `ufw`: `redirects port 8080/TCP to port 80/TCP`
    * enable packet forwarding, let’s open `/etc/ufw/sysctl.conf`:
      ```bash
      $ sudo nano /etc/ufw/sysctl.conf
      ```
      * uncomment this line: `net/ipv4/ip_forward=1`
    * configuring Port Forwarding on `ufw`:
      * open this file `/etc/ufw/before.rules`:
        ```bash
        $ sudo nano /etc/ufw/before.rules 
        ```
        * add this `NAT` table at the end of the file after `COMMIT`
          ```bash
          *nat
          :PREROUTING ACCEPT [0:0]
          -A PREROUTING -p tcp --dport 8080 -j REDIRECT --to-port 80
          COMMIT
          ```
    * And the final step is to restart `ufw` service by this command:
      ```bash
      $ sudo systemctl restart ufw
      ```
