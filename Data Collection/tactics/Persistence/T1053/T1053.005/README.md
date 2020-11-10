# T1053.005 - Scheduled Task

## Description

Windows has a built-in component called Task Scheduler for performing automated tasks on a chosen computer. It executes tasks based on a trigger that can be based on features such as specific time or schedule, user logging in, system boot, or specific event happening on the system. The action that the task executes can be showing a message, sending email, executing command or firing a COM handle. Task Scheduler can be managed through graphical user interface taskschd.msc or command-line tools schtasks.exe and at.exe.

An adversary may use Windows Task Scheduler to execute programs at system startup or on a scheduled basis for persistence. Adversary may, for example, create a scheduled tasks that downloads and executes malicious code to regain foothold even if the malicious process is interrupted or its code removed.

## Event Mapping

* Event ID 4698: A scheduled task was created
* Event ID 4702: A scheduled task was updated

Windows generates event ID 4698 when Task Scheduler is used to schedule a task. Event ID 4702 when a scheduled task is updated. These events are written to Event Log Security channel.

Audit Other Object Access Events audit policy must be enabled through Windows Group Policy (Policies → Windows Settings → Security Settings → Advanced Audit Policy Configuration → Object Access → Audit Other Object Access Events)

## References

[Mitre ATT&CK source](https://attack.mitre.org/techniques/T1053/005/)

[Task Scheduler for developers](https://docs.microsoft.com/en-us/windows/win32/taskschd/task-scheduler-start-page)

[Event ID 4698](https://docs.microsoft.com/en-us/windows/security/threat-protection/auditing/event-4698)

[Event ID 4702](https://docs.microsoft.com/en-us/windows/security/threat-protection/auditing/event-4702)
