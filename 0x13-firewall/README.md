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
