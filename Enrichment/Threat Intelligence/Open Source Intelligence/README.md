# Open Souce Intelligence (OSINT)

**Introduction:** 

OSINT is the gathering of intelligence from free and open sources, usually utilizing an API. [OSINT Framework](https://osintframework.com/) provides a huge list of available sources ranging from username search engines to geolocation tools. The website [Cyber Threat Feeds](https://www.cyberthreatfeeds.com/) provides links to sources specific to threat intelligence. [Threatfeeds](https://threatfeeds.io/) contains a simplified list of free and open source threat intelligence feeds. The list contains minimal information about the feeds: who manages the feed, how many IoCs are contained and when it was last updated. 

Some tools provide easy command line access to multiple OSINT sources, for example [the Harpoon tool](https://github.com/Te-k/harpoon). 

**Benefits:**

- Easy to access source of information, most sources follow REST API guidelines
- APIs are often utilized and updated by other cybersecurity professionals worldwide

**Worth noticing:**
- APIs may require a an API key, which is provided after registration
    - APIs may also impose usage restrictions that are lifted when premium access is purchased

**Use cases:**
- Uploading a suspicious file to VirusTotal to scan it from multiple different virus databases, see [Upload file to Virustotal notebook for an example](upload_file_to_virustotal.ipynb)
- Querying IP addresses for geolocation etc. information
    - See the [Jupyter Notebook for an example](analyze_ip_address.ipynb)
    - Usually more useful for whitelisting IP addresses due to attackers using proxies.
- A defender could download a daily threat feed for example from [Mrlooquer threat feed](https://iocfeed.mrlooquer.com/), which provides IPv4 and IPv6 Indicators of Compromise (IoCs) and parse if the IP addresses listed in the feed are found in the defender's network logs. The threat feed is available in JSON or CSV format.
- Gathering new domain registrations in order to prepare for possible phishing attacks where domains closely related to other common domains (amazon vs amazoon) are registered.
    - The latest four days of newly registered domains can be downloaded from [WhoisDS](https://whoisds.com/newly-registered-domains)
    - Some countries provide a publicly accessible database of their domain's registrations. In Finland, Traficom provides a database of finnish domain registration data, which includes the holder, postal code and area and registrar of the domain. Check the [notebook](finnish_domains.ipynb) for instructions on how to load finnish domain registrations in OData format to Pandas Dataframes in Python

**Combining intelligence sources**

- Combining multile threat intelligence sources using [https://github.com/InQuest/ThreatIngestor](ThreatIngestor). The tool aims to easily automate gathering of IoCs from multiple intelligence sources with minimal configuration. The tool provides examples of parsing Twitter feeds and SQS queues to generate YARA rules which are sent to a MISP operator. The image from ThreatIngestor documentation provides an example of how much is possible to automate with a single configuration file: [ThreatIngestor](https://inquest.readthedocs.io/projects/threatingestor/en/latest/_images/mermaid-everything.png)

**List of open source threat intelligence**

**IP addresses and websites**
- [AbuseIPDB](https://www.abuseipdb.com/) - User reported IP addresses and hostnames. Reports contain log lines as comment and category of abuse

**Indicators of compromise and threat information**
- [AlienVault Open Threat Exchange](https://otx.alienvault.com/) - An API for latest threats and IoCs. Features Direct Connect agents which provide a way to update intrusion detection systems and firewalls with new threat data from subscriptions. 
- [Yara Rules](https://github.com/Yara-Rules/rules) - A repository of Yara signatures, which can be easily imported to MISP

**[Abuse.ch](https://abuse.ch/) - Community-driven projects which mostly provide blocklists:**
    - [MalwareBazaar](https://bazaar.abuse.ch/browse/) - Search malware samples by hash, ClamAV signature, tag or malware family.
    - [FeodoTracker](https://feodotracker.abuse.ch/) - An IP blocklist, designed to block command-and-control (C2) servers used by Dridex, Heodo and Trickbot. There are a number of [different blocklists available](https://feodotracker.abuse.ch/blocklist/), ranging from how "aggressive" they are. The more aggressive ones may cause a high number of false positive cases, while the more passive ones only provide IP addresses of active C2 servers. If you are running Suricata or Snort intrusion detection systems (IDS), the blocklists are available as premade rulesets, which you can download and easily put into use in your own IDS.
    - [SSL Blacklist](https://sslbl.abuse.ch/) - Contains a blacklist of SHA1 fingerprints of SSL certificates that have been associated with C2 servers. The certificates can be associated with multiple servers, so another C2 IP address blacklist is available with IP address and port combinations. [JA3](https://github.com/salesforce/ja3), which is a method that creates easily shareable SSL/TLS client fingerprints, blocklist is also available. Like in the feodoro blocklist, these blocklist also contain "aggressive" versions and Suricata/Snort rulesets.
    - [URLhaus](https://urlhaus.abuse.ch/) - A database of malware URLs. The [API section](https://urlhaus.abuse.ch/api/) provides database dumps, daily MISP events and ClamAV signature databases.
    - [ThreatFox](https://threatfox.abuse.ch/) - A platform for sharing IoCs. IoCs not older than 90 days are available for download. Older IoC data can be downloaded from data dumps. Like the URLhaus database, ThreatFox also provides Daily MSIP events. 
