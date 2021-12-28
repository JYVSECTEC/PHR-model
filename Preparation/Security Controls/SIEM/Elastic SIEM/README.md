# Elastic SIEM,  https://www.elastic.co/siem


**Introduction:** " Everything you love about the free and open Elastic Stack — geared toward security information and event management (SIEM). Leverage the speed, scale, and relevance of Elastic SIEM to drive your security operations and threat hunting. "

**Worth noticing:**
-


**Features:**
- Correlation rules, that detect tools, tactics, and procedures indicative of potential threats. Content is aligned with the MITRE ATT&CK knowledge base and ready for immediate implementation. 
- Machine learning
- Pre-built Beats integrations


**Also fits in:** Threat Hunting, Triage

**How this tool integrates to our PHR model:** 
Events, alerts and data we gather with other tools are send to elastic SIEM, where we can analyze situation


**Use case:** Monitoring logins


**Basis:** Our environment has honey accounts & honeypots


**Question:** How will monitoring logins help us


**Answer 1:** If someone even tries to login using honey account or to honey pot, we know that it shouldn't be our employee. 


**Answer 2:** We can monitor also if there is login attempts to people who are on vacation


**Answer 3:** Same user tryng to login tomultiple places at same time is suspicious



**Use case:** Using SIEM for investigation


**Basis:** In our environment we monitor all device logins & admin actions


**Question:** How will SIEM helps us finding breach & investigating


**Answer:** Our SIEM did alett us from suspicious activity, We did find that soon after knocking our honeypot, on other device new account was created. With SIEMs time-line featurewe we're able to find what attacker tried to do with that account. Also our firewall was logging all activity, which we did decrypt with proxy, so we we're able to see on which url/ ip-addresses attacker was accessing. By gathering these evidence IoCs to our MISP, our analyst can form Threat Intelligence