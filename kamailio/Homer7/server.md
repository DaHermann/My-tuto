
* Configuration Files:

         '/usr/local/homer/etc/webapp_config.json'
         '/etc/heplify-server.toml'

* Start/stop HOMER Application Server:

         'systemctl start|stop homer-app'

* Start/stop HOMER SIP Capture Server:

         'systemctl start|stop heplify-server'

* Start/stop HOMER SIP Capture Agent:
         'systemctl start|stop heplify'

* Access HOMER UI:

         http://51.210.54.81:9080
         [default: admin/sipcapture]

* Send HEP/EEP Encapsulated Packets to:
 
         hep://51.210.54.81:9060

* Prometheus Metrics URL:
 
         http://51.210.54.81:9096/metrics

* Access InfluxDB UI:

         http://51.210.54.81:8888

