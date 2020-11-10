# T1059.001 - PowerShell

## Description

PowerShell is an interactive command-line interface and scripting language built on .NET. It helps system administrators to automate common operating system management tasks and provides the command-line for executing other processes. PowerShell has been included in Windows since Windows 7 and the latest version, PowerShell Core is a fully open-source and cross-platform implementation.

PowerShell has become a popular tool among adversary groups because of its versatility and wide range of capabilities to automate, hide and obscure activities. PowerShell scripts can be hidden into other files, used to run executables from the Internet and even embedded into other applications for execution without the powershell.exe interpreter. PowerShell based offensive testing tools include Empire, PowerSploit and PSAttack.

## Event Mapping

* Event ID 4103: Module Logging
* Event ID 4104: Script Block Logging

PowerShell has support for three types of logging: module logging, script block logging, and transcription. These events are written to the Windows Event Log under the path: Microsoft-windows-PowerShell/Operational. Module logging (Event ID 4103) records pipeline execution details as PowerShell executes, including variable initialization and command invocations. It also records the output of the executed commands. Script block logging (Event ID 4104) records blocks of code as they are executed by the PowerShell engine, capturing the full context of the executed code, including scripts and commands.

Module and script block logging must be enabled through Windows Group Policy (Administrative Templates → Windows Components → Windows PowerShell)

## References

[Mitre ATT&CK source](https://attack.mitre.org/techniques/T1059/001/)

[PowerShell ♥ the Blue Team](https://devblogs.microsoft.com/powershell/powershell-the-blue-team/)
