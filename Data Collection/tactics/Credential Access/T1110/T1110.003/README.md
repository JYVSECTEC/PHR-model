# T1110.003 - Password Spraying

## Description

Brute force is a credential access technique where an adversary attempts to access user accounts without knowledge of the password. The adversary may attempt logins with a list of commonly used passwords. This method usually leads to numerous failed logins, which can trigger alarms or account lockouts. A more sophisticated strategy, called password spraying uses a single password or a small list of passwords against many different accounts to avoid triggering account lockouts or alarms.

## Event Mapping

* Event ID 4625: An account failed to log on
* Event ID 4771: Kerberos pre-authentication failed

Brute force attempts can be detected by monitoring operating system authentication logs for an unusually high number of failed logins. Windows logs several authentication failure related events, such as ID 4625 and ID 4771. The event ID 4625 is generated on a local computer when a log on fails. The event ID 4771 is generated on a domain controller when Kerberos Key Distribution Center fails to issue Ticket Grantisng Ticket (TGT). This event occurs when a user fails to authenticate using domain credentials.

Audit Logon policy must be enabled through Windows Group Policy to log event ID 4625 (Policies → Windows Settings → Security Settings → Advanced Audit Policy Configuration → Logon/Logoff → Audit Logon)

Audit Kerberos Authentication Service policy must be enabled through Windows Group Policy to log event ID 4771 (Policies → Windows Settings → Security Settings → Advanced Audit Policy Configuration → Account Logon → Audit Kerberos Authentication Service)

## References

[Mitre ATT&CK source](https://attack.mitre.org/techniques/T1110/003/)

[Event ID 4625](https://docs.microsoft.com/en-us/windows/security/threat-protection/auditing/event-4625)

[Event ID 4771](https://docs.microsoft.com/en-us/windows/security/threat-protection/auditing/event-4771)
