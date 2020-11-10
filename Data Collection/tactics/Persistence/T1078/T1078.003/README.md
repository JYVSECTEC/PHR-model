# T1078.003 - Local Accounts

## Description

User accounts in Windows can be divided into three categories: default, local and domain accounts. Default accounts include built-in accounts such as Administrator and Guest, which are created automatically and cannot be removed. Accounts can also be categorized into user, administrator and service accounts. User accounts are used by normal users and often have low privileges. Administrator accounts are used by system administrators and have high privileges. Service accounts are created for system services to allow them to access local and network resources.

Adversaries may use user accounts for persistency by creating new accounts that they can use in case access to others is lost.

## Event Mapping

* Event ID 4720: A user account was created

The main method for monitoring user account related activity in Windows is the security audit logs. The user account management events are particularly relevant for the persistence tactic. These events indicate for example if a user account was created, changed or deleted.

The event ID 4270 is generated every time a new user object is created. These events are written to Event Log Security channel.

Audit User Account Management audit policy must be enabled through Windows Group Policy (Policies → Windows Settings → Security Settings → Advanced Audit Policy Configuration → Account Management → Audit User Account Management)

## References

[Mitre ATT&CK source](https://attack.mitre.org/techniques/T1078/003/)


[Event ID 4720](https://docs.microsoft.com/en-us/windows/security/threat-protection/auditing/event-4720)
