# T1140 - Deobfuscate/Decode Files or Information

## Description

File/information obfuscation can prevent signature-based security software from detecting the execution and make post-incident investigation harder. Common obfuscation techniques include encoding, compressing and encryption. Command-line interfaces have many built-in features that can be used for obfuscation information, such as environment variables, aliases and ability to receive commands from standard input stream.

Detecting obfuscation can be challenging using traditional string matching techniques, since the obfuscated data does not usually contain predictable patterns. One way to detect obfuscation is to look for suspicious escape characters, e.g. '''^''' and '''"''' included in commands. Another approach is to use statistical methods to analyze entropy and frequency of characters to detect anomalies.

## Event Mapping

* Event ID 4103: Module Logging

PowerShell can interpret commands encoded using the base64-encoding. PowerShell module logging (ID 4103) records the options used with execution as well as de-obfuscated commands.

## References

[Mitre ATT&CK source](https://attack.mitre.org/techniques/T1140/)
