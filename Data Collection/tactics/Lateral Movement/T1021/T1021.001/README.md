# T1021.001 - Remote Desktop Protocol

## Description

Remote desktop is an operating system feature that allows users to log into a system over a network and interact with the graphical user interface of the system remotely. The best known remote desktop solution is the Windows built-in remote desktop implementation called Remote Desktop Services (RDS); however, many third party remote desktop tools also exist for various operating system platforms.

Adversaries with valid credentials can use remote desktop connections to easily move laterally between systems. Remote desktop connections can be detected by monitoring Windows Event Logs.

## Event Mapping

* Event ID 4624: An account was successfully logged on

Successful authentication using remote desktop connection is recorded in the event ID 2624. The logon type 10 (RemoteInteractive) indicates that the user logged in using remote desktop connection.

Audit Logon policy must be enabled through Windows Group Policy (Policies → Windows Settings → Security Settings → Advanced Audit Policy Configuration → Logon/Logoff → Audit Logon)

## References

[Mitre ATT&CK source](https://attack.mitre.org/techniques/T1021/001/)

[Event ID 4624](https://docs.microsoft.com/en-us/windows/security/threat-protection/auditing/event-4624)
