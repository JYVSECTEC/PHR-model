# Data Collection

**Introduction:**

Data collection is a process of identifying the data sources for the TTPs identified in the Hypothesis step and collection of the data from the target systems. Identification of the data sources requires knowledge about the techniques used by the adversaries and the kind of data they produce, for example, files, logs or flow records. The correct mapping of data sources to adversary techniques is crucial for reducing false positives and amount of collected data. The [MITRE ATT&CK](https://attack.mitre.org/) knowledge base is a great starting point for getting information about the adversary tactics, techniques, tools and data sources.

**Tactic, Technique & Event Matrix:**

The matrix below contains adversary technique/sub-technique (row) and tactic categories (column) with the related Windows Event Log IDs. The technique and tactic categories are based on [MITRE ATT&CK Enterprise Matrix](https://attack.mitre.org/matrices/enterprise/).

Techniques descripe the offensively oriented actions that an adversary can use against the target systems.
Techniques can be categorized into tactics, which describe an adversary’s tactical objectives during operations, such as persist, discover targets or move laterally. In other words, techniques describe how an adversary performs an action and tactics describes why they do it.

|Technique| Sub-Technique                           | [Execution](tactics/Execution/README.md) | [Persistence](tactics/Persistence/README.md)        | [Privilege Escalation](tactics/Privilege%20Escalation/README.md)                      |[Defence Evasion](tactics/Defence%20Evasion/README.md)|[Credential Access](tactics/Credential%20Access/README.md)| [Discovery](tactics/Discovery/README.md)|[Lateral Movement](tactics/Lateral%20Movement/README.md)| [Command and Control](tactics/Command%20and%20Control/README.md)|
|---| ------------------------------ | ---- | ---------- | ----------------------------- | ------------- | ---------- | ---------- | ------------- | ---------- |
|Command and Scripting Interpreter| Windows Command Shell |[ID 1](tactics/Execution/T1059/T1059.003/README.md)|  |  |  |  |  |  |
|| PowerShell |[ID 4103,4104](tactics/Execution/T1059/T1059.001/README.md)|  |  |  |  |  |  |
|| Visual Basic |[ID 1](tactics/Execution/T1059/T1059.005/README.md)|  |  |  |  |  |  |
|Scheduled Task/Job| At (Windows) ||[ID 4698, 4702](tactics/Persistence/T1053/T1053.002/README.md)|[ID 4698, 4702](tactics/Privilege%20Escalation/T1053/T1053.002/README.md)|  |  |  |  |
|| Scheduled Task ||[ID 4698, 4702](tactics/Persistence/T1053/T1053.005/README.md)|[ID 4698, 4702](tactics/Privilege%20Escalation/T1053/T1053.005/README.md)|  |  |  |  |
|Boot or Logon Autostart Execution| Registry Run Keys / Startup Folder |  |[ID 13, 11](tactics/Persistence/T1547/T1547.001/README.md)|  |  |  |  |  |
|Valid Accounts| Default Accounts |  |[ID 4720](tactics/Persistence/T1078/T1078.001/README.md)|[ID 4672](tactics/Privilege%20Escalation/T1078/T1078.001/README.md)|  |  |  |  |
|| Domain Accounts |  |[ID 4720](tactics/Persistence/T1078/T1078.002/README.md)|[ID 4672](tactics/Privilege%20Escalation/T1078/T1078.002/README.md)|  |  |  |  |
|| Local Accounts |  |[ID 4720](tactics/Persistence/T1078/T1078.003/README.md)|[ID 4672](tactics/Privilege%20Escalation/T1078/T1078.003/README.md)|  |  |  |  |
|Create or Modify System Process| Windows Service |  |  |[ID 7045, 4697](tactics/Privilege%20Escalation/T1543/T1543.003/README.md)| |  |  |  |
|Indicator Removal on Host| File Deletion |  |  |  |[ID 23](tactics/Defence%20Evasion/T1070/T1070.004/README.md)|  |  |  |
|Deobfuscate/Decode Files or Information|-|  |  |  |[ID 4103](tactics/Defence%20Evasion/T1140/README.md)|  |  |  |
|OS Credential Dumping|LSASS Memory|  |  |  |  |[ID 7](tactics/Credential%20Access/T1003/T1003.001/README.md)|  |  |
|Input Capture|Keylogging|  |  |  |  |[ID 12](tactics/Credential%20Access/T1056/T1056.001/README.md)|  |  |
|Brute Force|Password Spraying|  |  |  |  |[ID 4625, 4771](tactics/Credential%20Access/T1110/T1110.003/README.md)|  |  |
|Account Discovery|Local Account|  |  |  |  |  |[ID 1](tactics/Discovery/T1087/T1087.001/README.md)|  |
||Domain Account|  |  |  |  |  |[ID 1](tactics/Discovery/T1087/T1087.002/README.md)|  |
|System Network Configuration Discovery|-|  |  |  |  |  |[ID 1](tactics/Discovery/T1016/README.md)|  |
|File and Directory Discovery|-|  |  |  |  |  |[ID 4103](tactics/Discovery/T1083/README.md)|  |
|Lateral Tool Transfer|-|  |  |  |  |  |  |[ID 5140](tactics/Lateral%20Movement/T1570/README.md)|
|Remote Services| Remote Desktop Protocol |  |  |  |  |  |  |[ID 4624](tactics/Lateral%20Movement/T1021/T1021.001/README.md)|
||SMB/Windows Admin Shares|  |  |  |  |  |  |[ID 5140](tactics/Lateral%20Movement/T1021/T1021.002/README.md)|
|Application Layer Protocol|Web Protocols|  |  |  |  |  |  |  |[ID 3](tactics/Command%20and%20Control/T1071/T1071.001/README.md)|
||File Transfer Protocols|  |  |  |  |  |  |  |[ID 3](tactics/Command%20and%20Control/T1071/T1071.002/README.md)|

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

# Other log sources
Also other logs are useful that are not collectible from Windows environment.

* DNS logs give you understanding on domains queried in the environment, and can be used to in threat hunting
* Proxy logs give you visibility of endpoints Internet HTTP/HTTPS related traffic (if your environment includes this functionality)
* Netflow data give you visibility of IP/Port level conversations between endpoints (both internal and external conversations)
* Firewall logs give you visibility on what kind of traffic has been allowed and what has been blocked  
* Application level logs (i.e. web server or email server) give you visibility on activities happening on application level
