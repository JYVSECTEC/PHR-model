# T1543.003 - Windows Service

## Description

Services in Windows are applications that run in the system background without user interaction. Many of the core operating system features, such as event logging, file serving and printing are run as services. Services are often started automatically when the operating system boots

Services can be executed using LocalSystem account, which enables an adversary with administrator account to escalate privileges to SYSTEM level.

## Event Mapping

* Event ID 7045: A new service was installed in the system
* Event ID 4697: A service was installed in the system

The event ID 7045 is generated in all modern Windows versions when a new service is created. There is also event ID 4697, which is generated in newer versions of Windows (Windows 10 and Server 2016).

Audit Security System Extension policy audit policy must be enabled through Windows Group Policy (Policies → Windows Settings → Security Settings → Advanced Audit Policy Configuration → System → Audit Security System Extension)

## References

[Mitre ATT&CK source](https://attack.mitre.org/techniques/T1543/003/)


[Event ID 4697](https://docs.microsoft.com/en-us/windows/security/threat-protection/auditing/event-4697)
