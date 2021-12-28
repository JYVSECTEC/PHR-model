# DREAD (Damage potential, Reproducibility, Exploitability, Affected users and Discoverability)

DREAD is Microsoft developed threat modeling methodology. Model is used to create risk rating based on threat or vulnerability damage potential, reproducibility, exploitability, affected users and discoverability. Each of these categories is given a rating between 0-10, depending how threat or vulnerability performs on the category. Higher value corresponds to more severe threat/vulnerability. E.g. if vulnerability affects all organization users and its clients users, the affected users category rating could be as high as 10. When each category's rating is calculated, sum of all ratings is added up and divided by 5, which results in a value between 0-10. Value 0 means that threat/vulnerability causes no impact and value 10 means worst possible outcome.

**Benefits**:

<ul>
    <li>Simple to use, since the model does not require many steps.</li>
    <li>Provides mechanism to compare threats/vulnerabilities with each other, so potential fixes can be prioritized based on the rating.</li>
    <li>Vulnerability/threat ratings from long period of time can be used to determine which components have more serious risks compared to others.</li>
</ul>

### References

<ul>
    <li>https://docs.microsoft.com/fi-fi/archive/blogs/david_leblanc/dreadful</li>
    <li>https://wiki.openstack.org/wiki/Security/OSSA-Metrics#DREAD</li>
</ul>
