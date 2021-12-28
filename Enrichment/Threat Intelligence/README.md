# Threat Intelligence

**Introduction:** To protect our assests, we need to know who might be targeting us, what tools/techniques they usually use, so that we can then know where to focus our defence.  

**Benefits:**
- Choosing where to focus on defence. Targeted attacks needs targeted defence.
- Detecting new threats
- Identifying threats
- Understaning what is going on
 
**Worth noticing:**

- Where does the information come from? Can it be trusted? Do the attackers have access to the same information?

**Features:**
- Indicators of Compromise (IoCs) - data gathered from logs or files that indicate that potentially malicious activity has happened on a system or a network. IoCs are gathered and shared by automated tools and cybersecurity professionals on multiple platforms. Finding an IoC on your own network does not guarantee that your network has been compromised, but it should definitely guide further investigation.
- Indicators of Attack (IoAs) - are proactive to IoCs, where early signs of malicious activity are searched for before the cyber attack itself has a chance to happen. Defenders could for example receive alarms of multiple failed SSH login attemps and then search the machine's log files for unauthorized access. On a larger scale, social media, news and threat intelligence sources could be monitored for possible cybercrime motivations , cyber attack campaigns or other causes for an organization to anticipate an attack.
- Tactics, techniques and procedures (TTPs) - Gathering of data enables the organization to reveal the possible attackers' motives and the means of executing their attack. This allows the organization to prepare their networkm protection and monitoring platforms accordingly to prevent and detect attacks.

**Use cases**

Data can be easily gathered from different services, but the problem is that it is often in various formats, so the big obstacle is aggregating the data in an easy manner of automation. Data sources should provide data in a specific format, so it can be easily sent to a server, queried, filtered and visualized. Same problem applies to threat intelligence, there are a lot of different data sources publicly available, but the threat data needs to be in an easily shareable format. Platforms such as [Malware information sharing platform](https://www.misp-project.org/) or MISP aims to make sharing threat information as easy as possible.

When data sources are in a specific format and available from a centralized server, they can be used to enhance other tools and services. For example the intrusion detection systems Suricata and Snort rulesets can be downloaded from open threat intelligence sources. AI-powered systems also benefit from large amounts of log data, they could be used to perform anomaly detection and create alerts when something is out of the ordinary.

Whatever threat intelligence sharing tool a organization uses, it has many benefits. [This blog describes simple steps to bring threat intelligence sharing to an organization.](https://www.helpnetsecurity.com/2020/09/21/5-simple-steps-to-bring-cyber-threat-intelligence-sharing-to-your-organization/)

A list of tools to create, download and share threat information:
- [JA3](https://github.com/salesforce/ja3) - Fingerprinting the TLS negotiation between client and server, meaning for example when a user connects to a bank website secured by HTTPS. If a bad actor uses the HTTPS protocol to connect to a command-and-control server, the TLS negotiation can still be fingerprinted using the JA3 method, even though the messages are encrypted. Sharing JA3 fingerprints allows organizations to detect if a device in their network is connecting to a known command-and-control server, that would send directions to malware inside the organizations network.
- [OpenIOC](https://github.com/mandiant/OpenIOC_1.1) - An XML schema for sharing indicators of compromise.
- [Structured Threat Information Expression (STIX)](https://oasis-open.github.io/cti-documentation/stix/intro.html) - A language and serialization format for exchanging threat intelligence. STIX objects can be sent in JSON format, which makes it easy to transfer. 
- [Elastic Common Schema](https://www.elastic.co/blog/introducing-the-elastic-common-schema) - An open source log format specification designed to combine log data from multiple sources into a unified scheme. Different log files following Elastic Common Schema could be combined in Elasticsearch or other server, making alert creation and anomaly detection easier. The use of the schema makes it easy to parse log files, query the server where log files are aggregated and visualize data from different services.
- [YARA](https://github.com/VirusTotal/yara) - Yara is a tool for identifying malware. It specifies binary patterns and text strings, which tell the malware or the malware family the analyzed sample belongs to. Many threat intelligence sources offer easily downloadable YARA rules, which can be used to spot malware on the organization's devices.
