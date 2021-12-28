# Autovola

Autovola is a dockerized system built to automate certain memory forensic processes using Volatility 3. The system is result of this [thesis](https://www.theseus.fi/handle/10024/503247). Autovola is open source project and it can be found from [here](https://github.com/JYVSECTEC/Autovola).

Memory dumps and corresponding ISF files can be uploaded to Autovola. After that users can choose, which Volatility 3 plugins they wants to run on these dumps. Each plugin's output can be viewed later on in a designated analysis page. The page allows users to filter out plugins output using regex. E.g. user can filter processes using PID, PPID or process name and then the page will only display data containing that information. User can also filter out memory dumps by using certain data in plugin output as a search query. 

Autovola does not support Volatility 3 utilities like volshell. The system should be addressed as a centralized storage for memory dumps, where users can do upper analysis by filtering the data they are interested in. E.g. users can upload bunch of dumps from different systems to Autovola and then they can check which of these dumps contain artifact of a specific malware. This way they can determine which of the systems have been infected.
