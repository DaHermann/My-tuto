# Basic pjsip configuration with template



[simpletrans-udp]
type=transport
protocol=udp
bind=0.0.0.0


[ENDPOINT](!) #Template Endpoint
type=endpoint
transport=simpletrans-udp
disallow=all
allow=ulaw
allow=gsm

[AUTH](!)  #Template Authentification
type=auth
auth_type=userpass


[AOR](!) #Template Aor
type=aor
max_contacts=1


;================================================= numbers of work context ==================================================================

;===============101
[101](ENDPOINT)
context=work
auth=101
aors=101

[101](AUTH)
username=101
password=secret

[101](AOR)
contact=sip:101@192.168.70.88:5060

;===============102

[102](ENDPOINT)
context=work
auth=102
aors=102

[102](AUTH)
username=102
password=secret

[102](AOR)
contact=sip:102@192.168.70.88:5060
    
    
 ;================================================= numbers of example context ==================================================================
;===============201
[201](ENDPOINT)
context=example
auth=201
aors=201

[201](AUTH)
username=201
password=secret

[201](AOR)
contact=sip:201@192.168.70.88:5060

;===============202

[202](ENDPOINT)
context=example
auth=202
aors=202

[202](AUTH)
username=202
password=secret

[202](AOR)
contact=sip:202@192.168.70.88:5060
