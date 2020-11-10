# T1083 - File and Directory Discovery

## Description

File and Directory Discovery tactic category involves the adversary searching files or directories from local system or network share. The goal is usually to access sensitive information or to conduct reconnaissance.

Adversaries can utilize native Windows Cmd tools, for example dir or tree to enumerate the filesystem. PowerShell has the Get-Item and Get-ChildItem that can be used to browse and search the filesystem. Some adversaries have also written custom tools that use the Windows API to gather file and directory information.

## Event Mapping

* Event ID 4103: Module Logging

PowerShell file and directory listing cmdlets Get-Item and Get-ChildItem execution can be detected by monitoring PowerShell module logging events (ID 4103).

[Mitre ATT&CK source](https://attack.mitre.org/techniques/T1083/)

[Get-Item](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.management/get-item?view=powershell-7)

[Get-ChildItem](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.management/get-childitem?view=powershell-7)
