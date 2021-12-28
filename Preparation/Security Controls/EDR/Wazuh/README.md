# Wazuh, https://wazuh.com/
"Wazuh is a free, open source and enterprise-ready security monitoring solution for threat detection, integrity monitoring, incident response and compliance. "


**Worth noticing:**
Wazuh provides necessary security controls, required by standards such as PCI DSS, HIPAA, GDPR and others. 
	

**Also fits in:** Threat hunting, Incident Response Tools and Tracking
	
**How this tool integrates to our PHR model:** 
By combining with other tools, Wazuh really helps to get visibility of endpoint devices. 
	
	
**Use case**: Detecting malicious activity.  
**Basis**: Organization has Windows AD environment, attacker has gained access to it.  
**Question**: How can Wazuh help us to detect malicious activity


Attackers activity was simulated by running certain scripts (APTSimulator, https://github.com/NextronSystems/APTSimulator and https://github.com/endgameinc/RTA), Wazuh gave alert from multiple suspicious activities, also Windows defender did block some activities from those scripts. So with Wazuh you can get hints that something suspicious is going on, for some tehniques you can be 100% sure that it is malicious activity, but sometimes you have to combine that info with threat intelligence data and other info you have. Also to decrease false positives it is really important to tune what files, processes and activities you are logging and what is baseline.