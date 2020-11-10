# T1087.002 - Domain Account

## Description

Account discovery techniques involve the adversary attempting to discover user accounts of the target system or accounts of the domain environment.

## Event Mapping

* Event ID 1: Process creation

Windows Remote Server Administration Tools (RSAT) bundle includes a tool called Dsquery, which can be used to query Active Directory for users and groups information. Execution of the tool can be detected by monitoring the specific process command-line arguments (dsquery user) from Sysmon Event ID 1.

## References

[Mitre ATT&CK source](https://attack.mitre.org/techniques/T1087/002/)

[Dsquery user](https://docs.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2012-r2-and-2012/cc725702(v=ws.11))

[Event ID 1](https://docs.microsoft.com/en-us/sysinternals/downloads/sysmon#event-id-1-process-creation)
