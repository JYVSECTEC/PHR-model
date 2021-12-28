# Time Series Analysis

Time series analysis tools can be used to detect anomalies or patterns in a time series dataset. A time series dataset would be for example a log, where events are in time-based order and are recorded when the event occurs. In this case, the measurements are gathered in irregular time intervals, where as a sensor that records a measurement every second would gather at regular time intervals. The most common use cases for time series analysis would be network traffic analysis or system event logs analysis.

### Tools
* [STUMPY](https://github.com/TDAmeritrade/stumpy) - A Python library for constructing matrix profiles, which enable pattern discovery, anomaly detection etc.
* [tslearn](https://github.com/tslearn-team/tslearn) - A machine learning toolkit for time series related data, makes preprocessing and training machine learning algorithms with time series data more streamlined and easier.

# Log Anomaly Detection

The amount of log data available in organization's environments can be overwhelming. Even if alarms about specific log entries are configured, malicious activity may disguise itself as a normal log entry. In log anomaly detection, machine learning models are used to parse through large files in search for anomalies or patterns that may indicate unusual behaviour. 

## Deep learning in anomaly detection

Automating log analysis with deep learning eliminates the need to create a large amount of rules for each new IoC / malicious IP address. With good domain expertise, the deep learning model could adapt to the target network traffic well and raise alerts on potentially malicious activity to administrators.

### Components of an anomaly detection model
* Streaming log entries from multiple systems
    * [Elastic Beats](https://www.elastic.co/beats/) - Lightweight data shippers to Logstash or Elasticsearch
* Centralized service for log data
    * [Elasticserch, Logstash and Kibana or ELK stack](https://www.elastic.co/elastic-stack) - Combining multiple open-source products for searching and visualizing data
* A log parser
    * [Logparser](https://github.com/logpai/logparser) - Toolkit for automated log parsing. Can extract fields from raw log messages according to a defined structure.
* Preprocessing / feature engineering logs for machine learning
    * [Loglizer](https://github.com/logpai/loglizer) - A log analysis toolkit by the same developers as Logparser, provides a way to extract relevant features for machine learning algorithms from structured logs.
* A machine learning model, that calculates a score for log events. The score is used to determine if the event is a anomaly or not. This can either be a machine learning algorithm or a deep learning neural network. The machine learning algorithms are quick to deploy and require less computing power, however they may not adapt to a target environment as flexibly as a neural network, which could lead to more false alarms.
    * [A universal transformer](https://github.com/tensorflow/tensor2tensor/blob/master/tensor2tensor/models/research/universal_transformer.py) trained with either TensorFlow or PyTorch
    * An outlier detection algorithm, like k-nearest neighbors or isolation forest
* A visualization of the anomaly (for exmaple frequency and location of network traffic)
* A whitelist database to prevent false alarms

### Open-source anomaly detection tools and systems

* [Log Anomaly Detector](https://github.com/AICoE/log-anomaly-detector) - Uses Word2Vec and SOM (Self-organizing map) for unsupervised learning. Grafana visualization for metrics and a "fact store", where false positives are registered.
* [PyOD](https://github.com/yzhao062/pyod) - Python toolkit for anomaly detection with multiple pre-defined machine learning models
* [PyODDS](https://github.com/datamllab/pyodds) - Anomaly detection system similar to PyOD, but aims to provide usage for developers not familiar with machine learning too. The system queries data straight from a database for analysis and visualization.
* [PySAD](https://github.com/selimfirat/pysad) - Streaming anomaly detection, integrations to PyOD models
* [Cyber Log Accelerator](https://github.com/rapidsai/clx) - Utilize graphical processing units (GPUs) to accelerate log analysis.

**Automated log analysis tools**

**Windows Event Logs**
* [APT-Hunter](https://github.com/ahmedkhlief/APT-Hunter) - A useful tool for a threat hunter, where PowerShell script for gathering windows event log data is provided and then analyzed with a Python script, where for example common executables used by attackers are searched and the number of logins is documented.
* [DeepBlue](https://github.com/sans-blue-team/DeepBlueCLI) - Another useful PowerShell script, where specific log event ID's are searched for in Windows EVTX log files and a description of why it might indicate malicious activity is provided. 