# Firewall checklist
* Identify possible alerts on the systems involved in the incident (if IDS/IPS functionality, check those)
     *  If alerts are found, find out what the alert means and document which system the alarm is related to
* Find out how the systems associated with the incident are being connected from thefirewall logs
     * Document abnormal traffic on a system-by-system basis (where/whom, protocol, port information, possible application information, other information)
* Identify the open network connections (sessions) of the systems involved in the incident
     * Document open network connections (IP-src, IP-dst, protocol, port information, possible application information, other information)
* Find out the firewall rules for the systems involved in the anomaly
     * What are the rules allowing?
     * Is there something different in the rules? Should the rule be in place? Does it allow only needed traffic?
* Find out if there have been any changes to the firewall rules for exception-related systems
     * What the changes concern
     * When the changes were made
     * Who has made the changes
