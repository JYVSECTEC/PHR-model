# TheHive



https://thehive-project.org/


**Introduction:** " A scalable, open source and free Security Incident Response Platform, tightly integrated with MISP (Malware Information Sharing Platform), designed to make life easier for SOCs, CSIRTs, CERTs and any information security practitioner dealing with security incidents that need to be investigated and acted upon swiftly. "


**Features:**


- Multiple persons can work same time on same case
- Case can have as many task sas you want
- Case can be created from alert / MISP event
- Alerts can come form multiple sources (SIEM, email, IDS, MISP..)
- Export cases to multiple MISP


**Worth noticing:**


- With Cortex can be used to Query analyzers, or Query check if MISP has information about observables
- Can create analysis reports


**Also fits in:**


 Threat Intelligence, Incident Response



**How this tool integrates to our PHR model:**


Can be usedwith MISP to automatically check observables from MISP


**Use case:**

 
**Question:**  How TheHive helps us


**Answer:** We can add/export data/events from multiple sources, like E-mail reports, SIEM, Threat Intel provider, MISP etc... Which observables will be analyzed further with Cortex analzer, like sandboxes, virustotal, MISP, etc.. Then we can import findings to multiple MISP instances. 


**Question:** How automation with TheHive is done?


**Answer:** On our environment we have ElastAlert configured to automatically pick observables from data (like IP addresses, urls..) and then send those to TheHive for further analysis 