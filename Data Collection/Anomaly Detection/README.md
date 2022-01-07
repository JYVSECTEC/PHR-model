# Host/Network Anomaly Detection With Artificial Intelligence

Currently the most applicable methods of AI in cybersecurity would be anomaly detection using either machine learning algorithms or deep learning neural networks.
The anomaly detection would most likely be applied to detect anomalies from logs, these logs could be system logs or network traffic logs depending on the type of the intrusion detection system.
With host-based intrusion detection systems (HIDS) the log detection would be the most appropriate approach. However
with a network-based intrusion detection systems (NIDS) the usage of network logs can be substituded with the raw
network traffic. The captured packets can be used to teach the artificial intelligence system to understand normal
traffic and thus detect anomalies within the network.    
    
In practice an anomaly detection neural network has to be taught to understand the normal situation and to score the
normality somehow. If the score exceeds a chosen threshold the traffic/log is deemed anomalous. The strength of the
anomaly detection approach comes from the fact that anomalous data is not required for the training process. However the
more anomalous data there is, the better the model can be tested.    
     
The biggest problem with anomaly detection is the huge amount of false alarms. Since the model works by choosing an
arbitrary threshold and the model is never taught to seperate anomalies from the normal data, the model is prone to
become too sensitive. The secondary problem is that anomaly detection models are often black boxes, which means the user
cannot see how it comes to the conclusion that the data is anomalous, which requires that the user has to start a
lengthy investigation/analysis on the problem. Together these two problems cause alarm fatigue to the users.    
    
Anomaly detection methods could also be applied to command and control detection. When a malware has breached the network,
it usually communicates to some server for further instructions. These communications can be well masked, but different from normal web traffic.
An anomaly detection model that has learned the usual traffic of a network has the potential to spot these command and control connections,
thus alerting the organization that an intrusion has occurred.    
    
An anomaly detection system requires many components. These components can be integrated in an intrusion detection
environment, but most intrusion detection systems can be only used partly to support to the anomaly detection system.    
    
The minimal version of an anomaly detection system would require data gatherers, preprocessing pipelines, the
detection model, databases and an visualisation/analysis tools for the results.     

![Anomaly detection system sketch](https://github.com/JYVSECTEC/PHR-model/blob/master/Data%20Collection/Anomaly%20Detection/anomdetsketch.png?raw=true)   
    
**Data gathereres**   
The data gatherers are used to obtain the data from the live system. The gatherer depends on the required data. For
example if the system is going to detect anomalies within logs, logstash or GRR can be used to gather the logs.
For network traffic-based anomaly detection something like suricata can be used with mirrored traffic to gather the live
data.    
    
**Data queue**    
The data has to be transferred to a database and/or to the model. Depending on the amount of the data there has to be
some kind of load balancing or queue for the data. This can be achieved with Kafka, Haproxy or just adding the data to a
database before moving it to the model (most likely a bad idea). Often the load balancing is omitted and the anomaly
detection model works as a bottleneck, which might cause delays in the detection and the response. With load balancing
the data could be seperated to multiple computers with the same model.   
    
**Data wrangling, aggregation**    
The data is not always in a format which is optimal for the model nor a database. For example in packet captures from a
network, all the fields of the packets are not required or can be even used in anomaly detection, thus the pcap can be
reduced to smaller size before storing or using it. Data might also require some kind of aggregation, transformation or
windowing. For example the logged data can be windowed to be used in chunks of 5 minutes instead of individual log
lines. Data wrangling is case speific and requires always custom scripts, but there are multiple python libraries to
help (pandas, spark). This system should be scalable and thus spark or similiar is recommended.   
    
**Preprocessing**   
The preprocessing step is always required when it comes to machine learning. The preprocessing step encompasses the data
wrangling/cleaning step, but also expands it to actually making the data ready for the model. For example the
raw/reduced data might include null data or the data fields might be in wrong types. In general models feed on floating
point data and thus everything needs to be preprocessed into a usable form. This step is always case dependant and
requires a custom script (pandas, spark recommended).   
    
**Machine learning, inference**   
The preprocessed data can be fed to the trained model. The model can be any kind of machine learning script, but
tensorflow is known for the great model deployment tools and is recommended.    
    
**Raw/Reduced database**   
All the gathered data should be saved into a database for future model training. Raw data saving allows different
approaches in the future, while reduced/wrangled data can be used to improve the current model.   
    
**The result database**    
The results should be stored to monitor the model's performance and to compare the detected anomalies to the data within
the time frame. Could also be used to detect cyclical anomalies.    
    
**Visualisation**    
Without visualisation of the results and the wrangled data the model is useless. If an anomaly is found the analyst has
to be able to visualize the situation. Arbitrary score from a machine learning model often means nothing to a human.
Grafana can be used to visualize timeseries data. Kibana is a good alternative for log-based data.   
    
**Fact checking**    
With fact checking the raw/reduced data can be transformed to labeled data. When an alarm is fact checked to be an
anomaly it should be labeled as such in the raw database. This way in the future the labeled cases can be used to create
a semi-supervised or even a supervised model. These models are often much more accurate than unsupervised anomaly
detectors.    
     
