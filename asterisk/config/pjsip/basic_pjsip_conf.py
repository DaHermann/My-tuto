#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ Simple Configuration of pjsip.conf @@@@@@@@@@@@@@



[simpletrans-udp]
type=transport
protocol=udp
bind=0.0.0.0

;===============103

[102]
type=endpoint
transport=simpletrans-udp
context=work
disallow=all
allow=ulaw
auth=102
aors=102

[102]
type=auth
auth_type=userpass
password=secret
username=102

[103]
type=aor
max_contacts=1
contact=sip:102@192.168.70.88:5060
    
    
;===============103

[103]
type=endpoint
transport=simpletrans-udp
context=work
disallow=all
allow=ulaw
auth=103
aors=103

[103]
type=auth
auth_type=userpass
password=secret
username=103

[103]
type=aor
max_contacts=1
contact=sip:103@192.168.70.88:5060
