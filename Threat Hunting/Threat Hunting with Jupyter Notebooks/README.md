**Introduction:** 

Jupyter Notebooks are a useful tool for faster and easily documentable threat hunting. Jupyter Notebook servers can be quickly deployed locally in a desktop or in a remote server. Installation options include using the [Anaconda data science distribution platform for easy installation of data-analysis and machine learning libraries](https://jupyter.org/install) or by [downloading premade Docker images in order to run a Docker container.](https://jupyter-docker-stacks.readthedocs.io/en/latest/index.html)

**Benefits:**
* Jupyter Notebooks are JSON - formatted documents, and so templates can be easily made by scripts, which would be called when a threat hunter starts a new hunt. This simplifies and eases the start of a hunting process and helps unify the results of different hunting processes. 
* Markdown documents can be inserted between programming code to provide notes for the threat hunter or be shared with other team members 

**Use cases:**
Jupyter runs code in kernels. Each kernel can have a different programming language and different libraries installed. Switching kernels is quick, so the jupyter environment is really flexible. The most common programming language used in Jupyter Notebooks is Python, but there is also support for .NET Interactive, where C# code and PowerShell scripts can be run on the same notebook. [Installation for .NET kernels can be found here](https://devblogs.microsoft.com/dotnet/net-interactive-is-here-net-notebooks-preview-2/). The .NET Interactive notebooks could be used to run for example [DeepBlueCLI](https://github.com/sans-blue-team/DeepBlueCLI), which is a PowerShell module for threat hunting Windows XML Event (EVTX) logs.  

[The example notebook](threat_hunting_IDS2018.ipynb) contains a threat hunting example from [IDS 2018 dataset](https://www.unb.ca/cic/datasets/ids-2018.html), where EVTX logs were compiled to Elasticsearch, and Elasticsearch data is queried and processed locally in the notebook. From the event logs, a hunter needs to find indications of infiltration, using windows event codes. An example for running DeepBlue on EVTX log files is provided [in the notebook here.](threat_hunting_deepblue.ipynb)

**Frameworks:**
* [HELK](https://github.com/Cyb3rWard0g/HELK) - An open source threat hunting platform, streaming multiple Elastic Beats data sources into Elasticsearch, Logstash and Kibana (ELK) stack with options for Big Data analytics, SIGMA rule creation and hunting with Jupyter Notebooks.
* [MSTIC Jupyter and Python Security Tools](https://github.com/microsoft/msticpy) - Microsoft Threat Intelligence's library for hunting in Jupyter Notebooks, provides ability to query log data from multiple sources, enriching data with OSINT or Azure data and perform analysis with multiple tools such as anomalous session detection and time series decomposition. Data can be visualized with interactive timelines and process trees. 