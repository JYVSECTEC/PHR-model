# T1016 - System Network Configuration Discovery

## Description

System Network Configuration Discovery is a technique where the adversary looks for details about the network configuration of the target system. Many native Windows tools exist for querying information about the network configuration, such as ipconfig for IP, DNS and network adapter information, arp for displaying the ARP-table content and route for displaying the routing table. PowerShell has cmdlets that display similar information, such as Get-NetAdapter, Get-NetIPAddress and Get-NetRoute.

## Event Mapping

* Event ID 1: Process creation

Tools used in this technique can be detected by monitoring the specific process command-line arguments (e.g. ipconfig or route print) from Sysmon Event ID 1.

## References

[Mitre ATT&CK source](https://attack.mitre.org/techniques/T1016/)

[ipconfig](https://docs.microsoft.com/en-us/windows-server/administration/windows-commands/ipconfig)

[Route](https://docs.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2012-r2-and-2012/ff961510(v=ws.11))

[Event ID 1](https://docs.microsoft.com/en-us/sysinternals/downloads/sysmon#event-id-1-process-creation)
