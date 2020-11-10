# T1570 - Lateral Tool Transfer

## Description

Adversaries may transfer tools or other files between systems in a compromised environment. Files may be copied from one system to another to stage adversary tools or other files over the course of an operation. Adversaries may copy files laterally between internal victim systems to support lateral movement using inherent file sharing protocols such as file sharing over SMB to connected network shares or with authenticated connections with SMB/Windows Admin Shares or Remote Desktop Protocol.

Remote file copy can be detected by monitoring file creation and access to network shares on servers and workstations. Analyzing network traffic can also reveal unusual data flows between hosts or uncommon protocols being used.

## Event Mapping

* Event ID 5140: A network share object was accessed

Windows file share access is recorded in event ID 5140. 

Audit File Share audit policy must be enabled through Windows Group Policy (Policies → Windows Settings → Security Settings → Advanced Audit Policy Configuration → Object Access → Audit File Share)

## References

[Mitre ATT&CK source](https://attack.mitre.org/techniques/T1570/)
