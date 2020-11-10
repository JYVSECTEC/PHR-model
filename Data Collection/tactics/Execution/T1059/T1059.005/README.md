# T1059.005 - Visual Basic

## Description

Visual Basic is a programming language created by Microsoft with interoperability with many Windows technologies such as Component Object Model and the Native API through the Windows API. Derivative languages based on VB have also been created, such as Visual Basic for Applications (VBA) and VBScript.

Adversaries can use Visual Basic scripts for speeding up operations and ability to bypass process monitoring mechanisms by interacting through the operating system APIs. Adversaries can download scripts from the Internet and execute them without creating files on the system. VBA scripts can also be hidden inside other files, such as Office documents or PDF files, which execute the script when a user opens the file.

## Event Mapping

* Event ID 1: Process creation

Visual Basic script execution can be detected by monitoring Sysmon process creation events (ID 1), where the command line parameters contain file extensions asociated with Visual Basic scripts (.vbs, .vbe, .wsf, .wsf).

## References

[Mitre ATT&CK source](https://attack.mitre.org/techniques/T1059/005/)

