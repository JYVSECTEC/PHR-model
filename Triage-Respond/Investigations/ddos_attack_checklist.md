# Distributed Denial of Service Attack 
In the case of denial of service attacks, the situation is often critical from the moment of detection. For
this reason, it is important to accurately identify the characteristics of the denial of service attack in
order to maximise the effectiveness of mitigation. 

Analysis and documentation of the denial of service
attack is important:
1. Identify target system(s) and service(s) under attack
2. Start date and time
3. Is it volumetric (high traffic amount or lot of user connection)?
 * If yes, it is important to find out what type of traffic is
   * Is the traffic similar (protocol, application, etc.) to the normal traffic of
the service?
 * If yes, it is important to identify the traffic profile that differs from the normal
traffic of the service
   * Protocol, port, application specific features (e.g. DNS header information,
HTTP header information)
   * Attack traffic volume: bits per second and packets per second
   * Other possible differences from normal traffic
4. Is this other kind of denial of service attack?
 * If yes, is there a specific type of traffic to the service?
 * If yes, is there a publicly known vulnerability in the service that allows denial of
service?
   * If so, is there any public knowledge of how to counteract this
vulnerability?
* If yes, is the attack using HTTP(s) traffic?
   * If yes, is the HTTP method POST?
   * If yes, is there a form on the site that the attack will use?
   * If yes, is the HTTP method GET?
   * If yes, is the HTTP method something other than GET or POST?
