# T1003.001 - LSASS Memory

## Description

Windows stores credentials in several databases and processes. Security Account Manager (SAM) is a database that stores user accounts and security descriptors for users on the local computer. Passwords are stored in SAM as LM or NTML hashes. When a user logs on, the credentials are stored in Local Security Authority Subsystem Service (LSASS) process, which is part of Local Security Authority (LSA) subsystem. LSA maintains information about all aspects of local security in a system and Its components run in the context of the Lsass.exe process. These credential materials can be harvested by an administrative user or SYSTEM.

Many tools exist for accessing credential data stored in SAM or LSASS, such as ProcDump or Mimikatz. Mimikatz is a Windows tool developed by Benjamin Delpy to learn more about Windows credentials. It can be used to extract plaintext passwords, hashes, pin codes and Kerberos tickets directly from memory. While Mimikatz binary can be directly executed on a target system, more sophisticated methods exist that allow executing Mimikatz from memory or remotely.

## Event Mapping

* Event ID 7: Image loaded

One approach on detecting Mimikatz is to look for specific Windows DLL modules it loads when executed. This approach is effective since it is not dependent on which process loads the code or whether Mimikatz is executed from disk or memory.

Sysmon event ID 7 records DDL modules loaded into a processes.

## References

[Mitre ATT&CK source](https://attack.mitre.org/techniques/T1003/001/)


[Event ID 7](https://docs.microsoft.com/en-us/sysinternals/downloads/sysmon#event-id-7-image-loaded)
