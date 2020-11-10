# T1078.002 - Domain Accounts

## Description

User accounts in Windows can be divided into three categories: default, local and domain accounts. Default accounts include built-in accounts such as Administrator and Guest, which are created automatically and cannot be removed. Accounts can also be categorized into user, administrator and service accounts. User accounts are used by normal users and often have low privileges. Administrator accounts are used by system administrators and have high privileges. Service accounts are created for system services to allow them to access local and network resources.

Adversaries can accomplish privilege escalation using existing unprivileged user or service accounts. 

## Event Mapping

* Event ID 4672: Special privileges assigned to new logon

The main method for monitoring user account related activity in Windows is the security audit logs. User account privilege escalation is captured by several Windows audit events

The event ID 4672 is generated when a new logon session has sensitive privileges assigned to it. This event is an indicator that a user account has escalated privileges. These events are written to Event Log Security channel.

Audit Special Logon policy audit policy must be enabled through Windows Group Policy (Policies → Windows Settings → Security Settings → Advanced Audit Policy Configuration → Logon/Logoff → Audit Special Logon)

## References

[Mitre ATT&CK source](https://attack.mitre.org/techniques/T1078/002/)


[Event ID 4672](https://docs.microsoft.com/en-us/windows/security/threat-protection/auditing/event-4672)
