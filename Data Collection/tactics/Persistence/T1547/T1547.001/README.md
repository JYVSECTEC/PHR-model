# T1547.001 - Registry Run Keys / Startup Folder

## Description

Windows registry includes specific keys called Run and RunOnce, which cause programs to run each time that a user logs on. The difference between Run and RunOnce is that Run is executed every time a user logs on whereas RunOnce key is removed after execution. The value for the keys is a command line that gets executed and it is possible to register multiple programs under any particular key.

While the registry run keys are often used by legitimate software, they are also used by adversaries for establishing persistency on a system. Another common persistence technique the adversaries use is Windows startup folders. Windows startup folder contains shortcuts to an application that starts when the system boots.

## Event Mapping

* Event ID 11: FileCreate
* Event ID 13: RegistryEvent (Value Set)

Detecting the use of registry run keys requires monitoring changes to the relevant registry keys. The paths from registry run keys are:

* HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Run
* HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\RunOnce
* HKEY_LOCAL_MACHINE\Software\Microsoft\Windows\CurrentVersion\Run
* HKEY_LOCAL_MACHINE\Software\Microsoft\Windows\CurrentVersion\RunOnce
* HKEY_LOCAL_MACHINE\Software\Microsoft\Windows\CurrentVersion\RunOnceEx

Changes to the registry keys can be monitored using Sysmon, which generates Event ID 13 when registry key is set.

Windows startup folders are located under individual user’s profiles (C:\Users\USERNAME\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup) and under ProgramData for all users (C:\ProgramData\Microsoft\Windows\Start Menu\Programs\StartUp). Sysmon can be configured to monitor these location for file creation events (ID 11).

## References

[Mitre ATT&CK source](https://attack.mitre.org/techniques/T1547/001/)

[Run and RunOnce Registry Keys](https://docs.microsoft.com/en-us/windows/win32/setupapi/run-and-runonce-registry-keys?redirectedfrom=MSDN)

[Event ID 11](https://docs.microsoft.com/en-us/sysinternals/downloads/sysmon#event-id-11-filecreate)

[Event ID 13](https://docs.microsoft.com/en-us/sysinternals/downloads/sysmon#event-id-13-registryevent-value-set)
