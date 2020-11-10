# T1071.001 - Web Protocols

## Description

Adversaries may use standard application layer protocols that are used in every IT environment to blend their command and control traffic within normal network communications.

Protocols such as HTTP and HTTPS that carry web traffic may be very common in environments. HTTP/S packets have many fields and headers in which data can be concealed. An adversary may abuse these protocols to communicate with systems under their control within a victim network while also mimicking normal, expected traffic.

## Event Mapping

* Event ID 3: Network connection

Sysmon can be used to monitor process network connection events (ID 3). These events should be filtered by process name or destination IP to only include suspicious network activity, such as processes that shouldn't normally communicate to Internet or that are communicating with unusual destinations.

## References

[Mitre ATT&CK source](https://attack.mitre.org/techniques/T1071/001/)

[Event ID 3](https://docs.microsoft.com/en-us/sysinternals/downloads/sysmon#event-id-3-network-connection)
