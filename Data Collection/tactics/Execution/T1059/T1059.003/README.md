# T1059.003 - Windows Command Shell

## Description

Command-line interface (CLI) is a way to interact with computer systems by issuing commands using lines of text either locally or via a remote session. It is a common feature across many operating systems, including Windows and Unix-type operating systems such as Linux and macOS. Adversaries often use command-line interface to execute built-in commands in operating systems and launch external software.

## Event Mapping

* Event ID 1: Process creation

According to MITRE ATT&CK, data sources for command-line interface are process and process command-line parameter monitoring. Both data sources are captured by Sysmon event ID 1. The events should be filtered by process name being "cmd.exe", which is the main command interpreter for Windows.

## References

[Mitre ATT&CK source](https://attack.mitre.org/techniques/T1059/003/)

[Event ID 1](https://docs.microsoft.com/en-us/sysinternals/downloads/sysmon#event-id-1-process-creation)
