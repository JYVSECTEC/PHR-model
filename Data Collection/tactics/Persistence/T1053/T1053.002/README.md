# T1053.002 - At (Windows)

## Description

At.exe is a Windows command line tool for scheduling a command, a script, or a program to run at a specified date and time. An adversary may use at.exe in Windows environments to execute programs at system startup or on a scheduled basis for persistence.

## Event Mapping

* Event ID 4698: A scheduled task was created
* Event ID 4702: A scheduled task was updated

Windows generates event ID 4698 when at.exe is used to schedule task. Event ID 4702 when a scheduled task is updated. These events are written to Event Log Security channel.

Audit Other Object Access Events audit policy must be enabled through Windows Group Policy (Policies → Windows Settings → Security Settings → Advanced Audit Policy Configuration → Object Access → Audit Other Object Access Events)

## References

[Mitre ATT&CK source](https://attack.mitre.org/techniques/T1053/002/)

[How To Use the AT Command to Schedule Tasks](https://support.microsoft.com/en-us/help/313565/how-to-use-the-at-command-to-schedule-tasks)

[Event ID 4698](https://docs.microsoft.com/en-us/windows/security/threat-protection/auditing/event-4698)

[Event ID 4702](https://docs.microsoft.com/en-us/windows/security/threat-protection/auditing/event-4702)
