# Feature Extractor

### Introduction

Feature extractor is a Dockerized tool that can be used to enrich an organization's collected data using open source threat intelligence APIs. The tool can be quickly setup, confingured and run with a couple of commands. The motivation for the tool is to make the work of analysts quicker by aiding in the process of deciding relevance of various IoCs (indicators of compromise). The open source code for the tool is provided in GitLab https://gitlab.com/CinCan/wp1/tree/master/feature_extractor and the docker container can be downloaded from DockerHub https://hub.docker.com/r/cincan/feature_extractor. The tool provides access to a variety of OSINT APIs, including:

* AbuseIPDB
* Censys
* DShield
* EmergingThreats
* GoogleSafebrowsing
* Greynoise
* MISPWarningLists2
* OTXQuery
* PhishTank
* Shodan
* Threatcrowd
* VirusTotal

If a potentially malicious file has been downloaded or a potential attacker IP is discovered, the file hash or the IP address can be supplied to the feature extractor. The feature extractor queries the above-mentioned APIs and compiles the returned results into an HTML report. The results contain information if the provided file or IP address is malicious or not. 

### Usage

Most of the APIs require API keys for usage, which need to be manually requested from each API and configured in the tool. Docker commands and necessary configurations can be found in the README https://gitlab.com/CinCan/tools/-/tree/feature-extractor/feature_extractor. You can also follow this blog tutorial, where IoCs are extracted from a WannaCry executable https://cincan.io/blog/2020_05_25_wannacry/. The dockerized tool of extracting IoCs from file can also be sent to a Cortex server for analysis by Cortex analyzers, check this blog for a tutorial https://cincan.io/blog/2020_06_10_dockerized_cortex_and_ioc_strings/. 

In short, IoCs can be given to analyze.py Python script in format of:
```bash
./analyze.py datatype:data
```
where datatatype is ip, domain, url, fqdn, hash or mail. For example:
```bash
./analyze.py url:https://www.iltalehti.fi
./analyze.py ip:8.8.8.8
```

The IoCs can be read from a newline separated file or in jsonl format. The tool can also read CSV - files provided by ioc_parser tool https://github.com/armbues/ioc_parser

An example docker run command after configuration:
```bash
sudo docker run -v $(pwd)/docker_volume:/data -v $(pwd)/samples:/samples cincan/feature_extractor:dev --path /data --injsonl /samples/jsonl_input 
```
