# Data Collection

**Introduction:**

Data collection is a process of identifying the data sources for the TTPs identified in the Hypothesis step and collection of the data from the target systems. Identification of the data sources requires knowledge about the techniques used by the adversaries and the kind of data they produce, for example, files, logs or flow records. The correct mapping of data sources to adversary techniques is crucial for reducing false positives and amount of collected data. The [MITRE ATT&CK](https://attack.mitre.org/) knowledge base is a great starting point for getting information about the adversary tactics, techniques, tools and data sources.

**Tactic, Technique & Event Matrix:**

The matrix below contains adversary technique (row) and tactic categories (column) with the related Windows Event Log IDs.

| Technique                           | Execution | Persistence        | Privilege Escalation                      | Defence Evasion          | Credential Access       | Discovery       | Lateral Movement    | Command and Control |
| ------------------------------ | ---- | ---------- | ----------------------------- | ------------- | ---------- | ---------- | ------------- | ---------- | 
| Command-Line Interface |ID 1|  |  |  |  |  |  |
| Scripting |ID 1|  |  |ID 4103|  |  |  |
| PowerShell |ID 4103, 4104|  |  |  |  |  |  |
| Scheduled Task |ID 4698, 4702|  |ID 4698, 4702|  |  |  |  |
| Registry Run Keys / Startup Folder |  |ID 13, 11|  |  |  |  |  |
| Valid Accounts |  |ID 4720|ID 4672|  |  |  |  |
| New Service |  |  |  |ID 7045, 4697|  |  |  |
| File Deletion |  |  |  |ID 4103|  |  |  |
| Obfuscated Files or Information |  |  |  |ID 4103|  |  |  |
| Credential Dumping |  |  |  |  |ID 7|  |  |
| Input Capture |  |  |  |  |ID 12|  |  |
| Brute Force |  |  |  |  |ID 4625, 4771|  |  |
| Account Discovery |  |  |  |  |  |ID 1|  |
| System Network Configuration Discovery |  |  |  |  |  |ID 1|  |
| File and Directory Discovery |  |  |  |  |  |ID 4103|  |
| Remote File Copy |  |  |  |  |  |  |ID 5140|ID 5140|
| Remote Desktop Protocol |  |  |  |  |  |  |ID 4624|
| Windows Admin Shares |  |  |  |  |  |  |ID 5140|
| Standard Application Layer Protocol |  |  |  |  |  |  |  |ID 3|
| Commonly Used Port |  |  |  |  |  |  |  |ID 3|

**Tools:**

The following section lists a few commonly used tools for data collection.

***Sysmon***

[System Monitor (Sysmon)](https://docs.microsoft.com/en-us/sysinternals/downloads/sysmon) is a Windows system service and device driver that monitors and logs system activity to Windows Event Log. It is part of Windows Sysinternals collection of tools created by Mark Russinovich. Once installed, Sysmon provides detailed information on many common system activities including:

* Process creation and termination
* File creation and deletion
* Network activity
* Registry modification
* Driver loading
* DLL loading

Sysmon is widely used by the security and threat hunting communities for its ability to generate information about events that the Windows Event Log system does not capture. The [Sysmon-DFIR](https://github.com/MHaggis/sysmon-dfir) repository contains plethora of resources for learning more about how Sysmon can be used for data collection and threat hunting.

***Elastic Beats***

[Elastic Beats](https://www.elastic.co/beats/) are open source data shippers that are installed as agents on servers to send data to Elasticsearch or Logstash. Several Beats exist for different data collection purposes, for example, Filebeat for collecting log files, Winlogbeat for Windows Event Log and Auditbeat for audit data.
