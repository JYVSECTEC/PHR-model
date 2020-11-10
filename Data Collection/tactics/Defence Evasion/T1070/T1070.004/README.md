# T1070.004 - File Deletion

## Description

Adversaries often create files and download tools or malware to target systems for execution. These files can cause detection by security defenses or leave clues to investigators. To prevent this, adversaries may delete the files over the course of an intrusion or at the end as part of the post-intrusion cleanup process.

Operating systems have built-in tools for deleting files, such as the DEL function in Windows cmd.exe or Remove-Item cmdled in PowerShell. There are also many external tools which can be used to delete files. One such tool known to be used by adversary groups is the Windows Sysinternals SDelete.

## Event Mapping

* Event ID 23: FileDelete

Sysmon generates event ID 23 when a file is deleted.

## References

[Mitre ATT&CK source](https://attack.mitre.org/techniques/T1070/004/)


[Event ID 23](https://docs.microsoft.com/en-us/sysinternals/downloads/sysmon#event-id-23-filedelete-a-file-delete-was-detected)
