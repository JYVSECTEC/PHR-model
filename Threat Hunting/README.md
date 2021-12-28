# Threat Hunting

Threat hunting is a process for searching active attacks from organization's environment. Threat Hunting often is assosiated to finding attacks that are hidden and not detected by any security controls. Some sources claims that threat hunting is also a process of finding the parts of the attack that are not detected by any control but is a part of Incident Response. In Prepare, Hunt, and Respond model, the threat hunting is considered as a process to find attacks that are not detected in anyway. The hunting should be related to searching specific attack vectors and techniques based on hypotheses that are based on organization's environment and risk assessment. 

Threat hunting requires security controls and measures to have data collected from different systems and endpoints to be able to find threat actors activities in the environment. Threat hunting can partly be automated (especially trying to find known IoCs (Indicators of Compromise)) but is activity performed by humans. Threat hunting can be either continuous process or something that is done periodically (depending on available resources).

## Threat hunting teams
TODO

## Threat hunting types
TODO

## Threat hunting models
TODO

## Threat hunting tools
TODO

### Datasets
Datasets provide a quick way to practice or educate others on threat hunting methods without having to put resources on generating or gathering attack data.

* [IDS 2018](https://www.unb.ca/cic/datasets/ids-2018.html) - A cybersecurity exercise with all operating system log data recorded to EVTX files and network traffic to PCAP files.
* [Mordor Dataset](https://mordordatasets.com/introduction.html) - Security events in JSON format

### Tools

* [Sysmon](https://github.com/SwiftOnSecurity/sysmon-config)
* [Osquery](https://github.com/palantir/osquery-configuration)

### Resources

* [Threat Hunter Playbook](https://threathunterplaybook.com/introduction.html) - contains a Windows knowledge library, which contains information for example about TaskScheduler related logs and it's IDs. The book also contains instructions for pre-hunt data management steps and specific threat hunting playbook examples, where the attacks are divided into MITRE ATT&CK categories.
