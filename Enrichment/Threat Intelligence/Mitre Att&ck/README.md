# Mitre Att&ck


https://attack.mitre.org/


**Worth noticing:**


- When adding autamatically tehnique IDs with rules, rules need to be specific enough. 


**How this tool integrates to our PHR model:**


Adding/Mapping tehnique IDs to our detections, we will get bigger view about what is going on. We can detect different attack phases. By knowing who is introducer and what tehniques are commonly used, we might be able to stop attack chain. Also helps us to choose controls that we need to be able to detect/prevent attacks. 


**Use case:** Enrichment alerts


**Question:** How enrichment with Mitre Att&ck can help us


We get logs from multiple places, it is hard to determine which alerts are false or true positives, or what does these alerts actually mean. To make it easier for analyzer to make decisions/understand the situation we can encrich our alerts data for certain tehnique IDs  


**Use case:** Enrichment reports


Requires a shift in analyst thinking. Changing from indicators to behaviors. So basically from reports we try to map what happened by translating behaviour to tactic. Forces analytics to learn techinal side of reports.
