# Reconnaissance, phishing, and/or Social Engineering

If the incident involves technical intelligence of the Organization's operations, it must be determined
whether it relates to a past or ongoing incident. Otherwise, the investigation of technical intelligence/recon
may be a waste of resources. It is, of course, sometimes useful to collect analytical data from technical
intelligence/recon in order to determine whether there has been a significant increase in the activity in
question. 

## Reconnaissance checklist
It is important to analyse and document technical intelligence/recon:
1. Date of reconnaissance
2. Destination system
3. Reconnaissance method (port scanning, operating system detection, etc.)
 * Firewall logs
 * System's own log data
 * Netflow-data
4. Protocol and port used
5. Source IP addresses and countries

## Phishing checklists
In the case of spear phishing, it is important to clarify whether it is targeted phishing (spear phishing) or massproduced phishing. In the case of targeted phishing, it is important to analyse and document:
1. Time of arrival of the message
2. Where did the phishing message come from?
3. Has a similar phishing message been used in other parts of the world (is there any
information on this in public sources)?
4. Has the message been sent to others in the organisation?
5. If the message attempts to redirect the user to a scam website
 * Where is it maintained?
 * Is it possible to ask the provider to take it offline?
 * Is it possible to block access to this site from the Organisation's network?
6. If there is an attachment in the message 
 * Is it possible to analyse it with internal tools of the organisation?
 * Is it possible to analyse which application the attachment is using and whether
the attachment is trying to exploit a vulnerability?
7. What method has been used to trick the user into activating malicious code on the
workstation? Can this be mitigated?


For mass-produced phishing messages, it is important to analyse and document:
1. Where did the phishing message come from?
2. Has the message been sent to everyone?
3. Can the message be identified to allow it to be blocked at the mail server?

## Social Engineering checklist
Social engineering can involve the physical collection of information or gaining access to systems and
physical premises. In this situation, it is important to analyse and document:
1. When did this first happen?
2. When was the user contacted?
3. What medium was used to contact the user?
4. What information did the user provide to the contact person?
5. Did the attacker gain access to the protected premises?
 * If yes, is there any additional/unauthorized equipment on the premises? 
   * If yes, is the device connected to the organisation's device?
 * If yes, what is the organization's device used for and what does it have access
to? 
   * If yes, is the device connected to the organisation's network? (i.e. directly to network interface)
* If yes, which device is communicating with the organisation's
network?
  * If yes, does the device have external network connections (e.g. 4G)?

