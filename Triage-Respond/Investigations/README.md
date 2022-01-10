# Detailed investigation
Detailed investigation should determine what really has happened, what kind of attack the incident is, what systems are affected, what attack methods the attacker used, and what weaknesses and/or vulnerabilities attacker exploited. 

During the detailed investigation many tasks needs to be performed, and the level of expertise varies in different environments depending on tools and architecture.

Based on the triage analysis, a detailed analysis of the selected systems needs to be carried out to
provide a clearer understanding of how the anomaly occurred and what is the best way to mitigate it.
1. List the systems and their dependencies on other systems
2. Based on the anomaly, ensure secure access to target systems
     * Consider username usage etc. if the attacker has system-level privileges
(usernames may end up in the hands of the attacker)
3. Collect local logs from the system for analysis
4. Find out when the detection/attack occured
     * This can be challenging in the early stages, but you need to find
attacker's first foothold or initial access.
5. Examine firewalls, logs and alerts related to systems
     * Check open sessions in the system
     * Check open sessions in the system
6. Examine netflow-data related to systems
     * Find out where the systems have been connected to
     * Find out where the systems have been connected from
7. Find out the logins to the systems
8. Find out about logins from the system to other locations/systems
9. Using attack-specific checklists or other methods, try to determine the root cause of the attack
(i.e. how, when and what the attacker was able to use to carry out the attack)
     * Document findings, IoCs, interventions and their timestamps, and notes
     * Use attack specific checklists to help the investigation:
        * [Reconnaissance, Phishing, and Social Engineering checklist](https://github.com/JYVSECTEC/PHR-model/tree/master/Triage-Respond/Investigations/recon_phishing_social_engineering_checklist.md)
        * [Malware infection checklist](https://github.com/JYVSECTEC/PHR-model/tree/master/Triage-Respond/Investigations/malware_infection_checklist.md)
        * [Data Breach checklist](https://github.com/JYVSECTEC/PHR-model/tree/master/Triage-Respond/Investigations/data_breach_checklist.md)
        * [DDoS attack checklist](https://github.com/JYVSECTEC/PHR-model/tree/master/Triage-Respond/Investigations/ddos_attack_checklist.md)
        * [Large scale or targeted attack checklist](https://github.com/JYVSECTEC/PHR-model/tree/master/Triage-Respond/Investigations/large_scale_attack_checklist.md)
10. You can also utilize system specific checklists:
     * [Firewall investigation checklist](https://github.com/JYVSECTEC/PHR-model/tree/master/Triage-Respond/Investigations/firewalls_checklist.md)
     * [Network device investigation checklist](https://github.com/JYVSECTEC/PHR-model/tree/master/Triage-Respond/Investigations/network_device_checklist.md)
     * [Server investigation checklist](https://github.com/JYVSECTEC/PHR-model/tree/master/Triage-Respond/Investigations/server_checklist.md)
     * [Workstation investigation checklist](https://github.com/JYVSECTEC/PHR-model/tree/master/Triage-Respond/Investigations/workstation_checklist.md)
11. In addition to the checklists, you might need more detailed investigations depending on nature of the attack and incident. For example, memory forensics might be needed to determine actual methods used by attacker or actual data that attacker was able to access in the system. [Memory Forensics](https://github.com/JYVSECTEC/PHR-model/tree/master/Triage-Respond/Investigations/Memory-Forensics/README.md) helps to start that
