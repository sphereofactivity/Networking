# Commonly used Powershell Commands

### Introduction
This markdown file will detail commonly used powershell commands for networking and detail their associated use cases.
```
ping
```
- Ping is a basic but essential powershell command to test reachability of a host. The command sends a small packet of information to a server and waits for a response. The response is measured and displayed in the output.

```
ipconfig
```
- Ipconfig is a command that displays all curent TCP/IP network config values and refreshs DHCP and DNS settings.

```
Get-NetIpAddress
```
- Is a command that restrives the IP address configuration including IPv4, IPv6, and the IP interfaces which addresses are associated with.
- This command takes arguments which can be viewed at the documentation here [at the PS documentation](https://learn.microsoft.com/en-us/powershell/module/nettcpip/get-netipaddress?view=windowsserver2022-ps)

```
netstat
```
- Is a command that displays active TCP connections, ports on which the computer is listening, Ethernet statistics, the IP routing table, IPv4 statistics (for the IP, ICMP, TCP, and UDP protocols), and IPv6 statistics (for the IPv6, ICMPv6, TCP over IPv6, and UDP over IPv6 protocols). Used without parameters, this command displays active TCP connections.
- Arguments and syntax can be read [at the PS documentation](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/netstat)
