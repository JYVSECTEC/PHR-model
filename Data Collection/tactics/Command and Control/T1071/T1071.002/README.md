# T1071.002 - File Transfer Protocols

## Description

Adversaries may communicate using application layer protocols associated with transferring files to avoid detection/network filtering by blending in with existing traffic. Commands to the remote system, and often the results of those commands, will be embedded within the protocol traffic between the client and server.

Protocols such as FTP, FTPS, and TFTP that transfer files may be very common in environments. Packets produced from these protocols may have many fields and headers in which data can be concealed. Data could also be concealed within the transferred files. An adversary may abuse these protocols to communicate with systems under their control within a victim network while also mimicking normal, expected traffic.

## Event Mapping

* Event ID 3: Network connection

Sysmon can be used to monitor process network connection events (ID 3). These events should be filtered by port numbers associated with file transfer protocols (e.g. FTP/21, TFTP/69, SMB/445).

## References

[Mitre ATT&CK source](https://attack.mitre.org/techniques/T1071/002/)

[Event ID 3](https://docs.microsoft.com/en-us/sysinternals/downloads/sysmon#event-id-3-network-connection)
