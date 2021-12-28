# Workstation checklist
* What has been done on the workstation before the incident?
     * Email activity
     * New files
     * Web browsing and downloads
     * Programmes executed
     * Latest user logins
* Check Security event logs (%system root%\system32\winevt\logs\security.evtx)
     * Check at least Event IDs: 4624, 4625, 4634, 4648, 4672, 4720
     * Check RDP logins (Event IDs 4778 and 4779)
     * Document any anomalies from normal use
* Is it ransomware?
     * If yes, are the user files encrypted?
     * If yes, which files and from which file path?
     * Document any findings
* When was the last time the workstation was restarted?
* Check if there are any applications on your workstation that start automatically
    * Document application data
* Check for scheduled tasks (Scheduled task etc.)
    * Document any scheduled tasks
* Are workstations running new processes or applications?
     * If yes, can the process be identified as a process of a non-approved application/binary?
         * If yes, what network connections does the process have?
         * If yes, what files does the process use?
         * If yes, under which permissions is the process run?
         * If yes, from which file path is the application/binary process started?
     * If not, do existing processes have open network connections to the Internet?
         * If yes, what are the identifiers of the connections (IP, TCP/UDP, port)?
     * If not, do existing processes have open network connections to services on the internal network?
         * If yes, what are the normal user activities?
         * If yes, what seems abnormal?
     * Document any findings
* Check the register for any anomalies
     * Document any findings
* Are any workstation maintenance tools (Powershell, etc.) used on the workstation?
     * If yes, are these approved administrative measures?
     * If not, what tool has been used and what has been done with it?
     * Document any findings
* Is there any external media (USB, etc.) connected to the workstation?
