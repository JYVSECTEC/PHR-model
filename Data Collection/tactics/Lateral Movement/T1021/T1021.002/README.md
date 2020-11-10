# T1021.002 - SMB/Windows Admin Shares

## Description

Windows has several hidden network shares that are used for administrative purposes. Common administrative shares include disk volumes (e.g. C$), IPC$ for inter process communication, ADMIN$ for remote administration, SYSVOL and NETLOGON for Windows domain administration. Because these shares are hidden, they are not visible in Windows Explorer. They can, however, be listed on command line using the “net use” command. Accessing admin shares requires administrative access on the system.

Adversaries may use these shares to access remote systems over network. Some remote administration tools, such as PsExec, also use admin shares to function. PsExec is a tool included in the Windows Sysinternal suite which can be used to execute programs on remote systems.

## Event Mapping

* Event ID 5140: A network share object was accessed

The use of this technique can be detected by monitoring the event ID 5140 and filtering specifically for share names that match the common admin share names.

Audit File Share audit policy must be enabled through Windows Group Policy (Policies → Windows Settings → Security Settings → Advanced Audit Policy Configuration → Object Access → Audit File Share)

## References

[Mitre ATT&CK source](https://attack.mitre.org/techniques/T1021/002/)

[Event ID 4150](https://docs.microsoft.com/en-us/windows/security/threat-protection/auditing/event-5140)
