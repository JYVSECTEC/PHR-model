# Server checklist
* Make sure you have a management connection to the system
     * Take into account the username/privileges with which you connect, so that the attacker does not gain access to, for example, the root user information of the entire environment.
* Check if new users or user groups have been created
     * Document new users and user groups
* Check if the user rights have been modified
     * Document any changes
* Check if there are new applications on the system or at system startup
     * Document the data for new applications
* Check if there are new disk partitions on the system
     * Document the distribution and its contents
* Check for changes in network configurations
     * Document any changes
* Check if there are any abnormal processes or services in the system (for services, it is important to check also for non-running ones)
     * Document any deviating processes and services
     * Investigate the origin of anomalous processes and/or services (where the process was started, where the executable came from, which user started the process)
* Check if the system has automated time-based actions (e.g. Scheduled tasks, cron jobs, etc.)
     * Document any time-based actions
     * Find out what time-based actions do and when
* Check what changes have been made to the system and its configurations
     * Document any changes
* Check if there are any changes in the system data
     * Document any changes
* Check whether the attacker has left any tools/files of his own on the system
     * Document any findings
     * Use a separate investigation workstation to examine the tools/files in more detail
* Go through the local system logs
     * User logins
     * Security logs
     * Remote access
     * Other possible issues related to the incident
     * Collect local logs from the system (.evtx for Windows, /var/log/* for Linux or other log data for the service/application)
     * Document any anomalies in the incident
* Find out when the abnormal activity in the system started
      * Document the exact time and reason for the abnormal activity
* Find out what happened (new files, network connections, user activities, etc.) before the abnormal behaviour started
      * Document any findings
* Find out what happened (new files, network connections, user activities, etc.) when theabnormal behaviour started
      * Document any findings
