# Basic pjsip configuration with template



[simpletrans-udp]
type=transport
protocol=udp
bind=0.0.0.0


[ENDPOINT](!) #Template Endpoint
type=endpoint
transport=simpletrans-udp
context=work
disallow=all
allow=ulaw
allow=gsm

[AUTH](!)  #Template Authentification
type=auth
auth_type=userpass


[AOR](!) #Template Aor
type=aor
max_contacts=1

;===============101
[101](ENDPOINT)
auth=101
aors=101

[101](AUTH)
username=101
password=secret

[101](AOR)
contact=sip:101@192.168.70.88:5060

;===============102

[102](ENDPOINT)
auth=102
aors=102

[102](AUTH)
username=102
password=secret

[102](AOR)
contact=sip:102@192.168.70.88:5060
