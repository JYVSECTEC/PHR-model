# Prepare, Hunt, and Respond
Prepare, Hunt, and Respond - Conceptual model against cyber attacks by [JYVSECTEC](https://jyvsectec.fi)

## Overview
The idea behind the conceptual model is to represent a comprehensive model for organizations to defend against modern cyber attacks. The model "PREPARE, HUNT, AND RESPOND" will be evolving from the initial release to encompass more detailed information and examples of tools and techniques to each section. The goal is to gather the best publicly available information, solutions, and tools to represent how different sections of the model can be done. 

![Prepare, Hunt, and Respond - Conceptual model against cyber attacks](https://raw.githubusercontent.com/JYVSECTEC/PHR-model/master/_images/Prepare_Hunt_Respond.png "Prepare, Hunt, and Respond - Conceptual model against cyber attacks")

[Download the PDF version](https://github.com/JYVSECTEC/PHR-model/blob/master/Prepare_Hunt_Respond_Poster.pdf)

JYVSECTEC and our experts have gained a lot experience and knowledge by organizing cyber exercises and trainings for government and private companies past 10 years. This experience has helped us to create a new comprehensive model how organizations should be prepared against cyber attacks and cyber crimes. Our aim is to provide detailed information and examples how each section of the model can be implemented in organizations. The goal of the model is to integrate traditional cyber security with incident response and threat hunting as a one complete model for preventing, hunting, and responding to threats. Important part of the model is to utilize continuous development of the organization’s capabilities to defend the business services or other critical functionalities.

This model is made available for everyone to utilize in their organization and we are more than happy to welcome any criticism, improvements, ideas, notes, and feedback of the model. If you have any input, please leave an issue on this Github page.

## 1. [Preparations](https://github.com/JYVSECTEC/PHR-model/tree/master/Preparation)
The model starts with preparations that are critical for an organization to be able to protect their critical assets and business services. These preparations include (but are not limited to) essential processes, technologies, and procedures to manage the environment and prepare for handling the attacks.

## 2. [Hypotheses](https://github.com/JYVSECTEC/PHR-model/tree/master/Hypotheses)
The second section "Hypotheses" encompasses identified threats and attacking vectors against organization. The threats and attacking vectors should be analyzed using TTPs (Tactics, Techniques, and Procedures) that the potential threat actor might use against the organization. The TTPs should be identified and prioritized based on the organization's identified risks. Threat modelling is a recommended method for identifying the TTPs.

## 3. [Data Collection](https://github.com/JYVSECTEC/PHR-model/tree/master/Data%20Collection)
The third section "Data Collection" is a set of identified data sources and types that help to detect if the TTPs in hypotheses section are used against an organization. These data sources should be specified as precisely as possible so there is no need to collect extensive amounts of log data for threat hunting and incident response processes. Also, identifying the essential data based on potential attack vectors and methods helps an organization to utilize the most suitable playbooks in threat hunting and checklists on incident response analysis. The "Data collection" section also includes automated malware analysis of different samples that are gathered from various data sources. The automated malware analysis can encompass multiple methods (i.e. AI, automated workflows for malware analysis, sandboxing) to detect potential malicious files and activities in the environment.

## 4. [Enrichment](https://github.com/JYVSECTEC/PHR-model/tree/master/Enrichment)
The fourth section "Enrichment" is a set of information that can be used to enrich collected data with organization-specific information. The "Enrichment" section also includes threat intelligence that is utilized to proactively to detect known malicious IoCs (Indicators of Compromise) and TTPs from the environment. Threat intelligence should tightly integrate to an organization's threat hunting and incident response activities, to help identify threat actors and attack vectors. Enrichment can also be tools and solutions to give more information on the malware analysis. Also, for example, IPAM information can used to link IP addresses and domain names to organization's assets automatically.

## 5. [Threat Hunting](https://github.com/JYVSECTEC/PHR-model/tree/master/Threat%20Hunting)
The fifth section "Threat Hunting" is comprised of threat hunting workflows that are used, either manually or automatically, to identify threats hiding in an organization's environment. The Threat Hunting is a set of actions performed to find methods used by adversaries. These methdos can include (but is not limited to) use of legitimate credentials, sysadmin tools (i.e. Powershell, WMI, and others), services, and systems to conduct the actions on their objectives.

## 6. [Triage / Respond](https://github.com/JYVSECTEC/PHR-model/tree/master/Triage-Respond)
The sixth section "Triage / Respond" describes how detected malicious activities are handled in the organization. The detection can come as an automated alert from security controls, SOC or users, or it can be detected during threat hunting activities performed in the environment. The incident response starts with triage process where an Incident Response Team member should quickly analyze the nature of the incident (i.e. what has happened, where has it happened, when did the first indications happen). After that, the impact against organization's business services should be evaluated. Depending on the organization's decision, the category and priority for the incident should be determined. Once the criticalness against business services has been determined, the allocation of the resources should be defined for further analysis of the incident. The detailed analysis of the incident can be a quick process, or it may take days or even weeks depending on the nature of the incident. During the detailed analysis, it is vital to collect evidence and IoCs of the attack for making proper decisions how to contain the attack and how to establish countermeasures against it. Also, the actions taken during the investigation and analysis are important to document within the incident tracking system so it is possible to review who has done what during the analysis after the attack .

## 7. [Eradicate / Recover](https://github.com/JYVSECTEC/PHR-model/tree/master/Eradicate-Recover)
The seventh section "Eradicate / Recover" are the actions for isolating and recovering from attack. The aim is to ensure secure operations of the business continuity, confidentiality, and integrity of the data affected by the attack. During the containment and recovery, thorough documentation of actions performed must be done. Also, all the evidence that has been found from the systems and environment needs to be stored in a secure location. The IoCs that had been identified of the incident should documented and used as a tool to understand more thoroughly how the attack happened and how to prevent similar incidents in the future.

## 8. [Lessons Learned](https://github.com/JYVSECTEC/PHR-model/tree/master/Lessons%20Learned)
The eighth section "Lessons Learned" should be a comprehensive analysis of the whole incident. It should include complete review of the threat hunting and incident response activities performed before detection and after the detection. The idea is to use post-analysis as tool to continuously develop the capabilities of the organization and identify detection gaps, data sources or faulty architecture. Also, post-analysis should be used as a method to develop new threat hunting playbooks, modify existing tools and guidelines, and update documentation. The post-analysis can also identify new, relevant assets for the organization and gaps in personnel's expertise which should be addressed with proper training and exercises.

## 9. [Improvements](https://github.com/JYVSECTEC/PHR-model/tree/master/Improvements)
The improvements are a vital part of the model for organization to improve their capabilities based the incident that has been handled. The improvements should be identified during the lessons learned section to enhance either organization’s environment or processes.


# Main contributors
The model has been created as a part of Ministry of Education and Culture of Finland funded [CYBERDI](https://jyvsectec.fi/2018/10/cyberdi/) project. The work has been done by specialists of JYVSECTEC and Finland's Police University College.

![JYVSECTEC](https://raw.githubusercontent.com/JYVSECTEC/PHR-model/master/_images/JYVSECTEC_by_jamk.png) ![JAMK University of Applied Sciences](https://raw.githubusercontent.com/JYVSECTEC/PHR-model/master/_images/jamk-logo1.png "JAMK")

![Police University College](https://raw.githubusercontent.com/JYVSECTEC/PHR-model/master/_images/polamk-logo1.png "Police University College") ![Ministry of Education and Culture of Finland](https://raw.githubusercontent.com/JYVSECTEC/PHR-model/master/_images/OKM-logo1.png "Ministry of Education and Culture of Finland")
