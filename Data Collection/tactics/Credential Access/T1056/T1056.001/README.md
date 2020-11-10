# T1056.001 - Keylogging

## Description

Keylogging is the most widely used input capture method, where the adversary installs a software that records user’s keystrokes and sends them back to the adversary. Other common methods include presenting fake credential prompts to user, injecting code to login pages or wrapping the Windows default credential provider.

## Event Mapping

* Event ID 12: RegistryEvent (Object create and delete)

Windows stores credential provider definitions in registry location:

* HKLM\Software\Microsoft\Windows\CurrentVersion\Authentication\CredentialProviders

Creation of new credential provider can be detected by monitoring Sysmon registry modification events for the CredentialProviders location.

## References

[Mitre ATT&CK source](https://attack.mitre.org/techniques/T1056/001/)


[Event ID 12](https://docs.microsoft.com/en-us/sysinternals/downloads/sysmon#event-id-12-registryevent-object-create-and-delete)
