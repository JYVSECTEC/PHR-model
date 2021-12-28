# Large-scale attack investigation
A large-scale attack may not be immediately clear from a single detection, but may be identified
as a larger scale through different events. In the case of an organisation, a large-scale attack refers to
an attack that aims to paralyse the operational activities of the organisation on a section-by-section
basis. In a large-scale attack, as in any other incident, it is important to determine what everything is
about before allocating resources to perform different tasks. 

Targeted attacks may also use highly visible attacks as a smokescreen to focus resources on investigating and resolving visible attacks. To investigate:
1. Find out the origin of the first detection
2. Investigate other suspicious findings in various security checks
     * Check firewall logs and alerts
     * Check security alerts on terminals
     * Check your email service alerts
     * Document any findings
3. Find out if there are other indications of compromise
4. Find out if there are open management interfaces from the systems to other systems
5. Find out if the systems have open C&C connections to the Internet
     * Which protocol, IP address, application, service, etc. is used?
     * Find out if there is a corresponding C&C channel open on other systems
     * Document IoC data from C&C connections
6. Identify the priority of the most critical systems in the recovery plan
     * The security team must make a final decision on the order of the investigation
7. Analyze the impact of the attack on different systems and assemble an overall picture
     * Document which services are impacted by the attack
     * Document which systems you no longer have management access to
     * Document which systems have lost reliability
8. Investigate the origin of the attack based on findings from different systems
9. Compile a timeline of the attack
     * Which systems contain IoC data (timestamps of when they first entered the
systems)
     * Try to find out the root-cause of the attack (and how the attacker was successfull on the attack)
10. The security team, and/or Major Inciment Management (MIM) Process, and/or the crisis team should decide on the response and recovery in accordance with the recovery plan.
