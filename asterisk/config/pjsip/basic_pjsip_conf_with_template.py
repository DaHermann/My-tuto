[nan-school]
type=transport
protocol=udp
bind=0.0.0.0

;================ Templating ======
[ENDPOINT](!)
type=endpoint
transport=nan-school
;context=client
disallow=all
allow=ulaw

[AUTH](!)
type=auth
auth_type=userpass

[AOR](!)
type=aor
max_contacts=1


;================== Numero du contexte " Client  "

;===============121

[121](ENDPOINT)
context=client
auth=121
aors=121

[121](AUTH)
password=blabla
username=121

[121](AOR)
contact=sip:121@192.168.70.133:5060

;===============124

[124](ENDPOINT)
context=client
auth=124
aors=124

[124](AUTH)
password=blabla
username=124

[124](AOR)
contact=sip:124@192.168.70.133:5060


;=========================================== Projet Asterisk 1 ===================================

;================= Numero de l'Administration =====================
;===============1001
[1001](ENDPOINT)
context=ADMIN
auth=1001
aors=1001

[1001](AUTH)
password=secret
username=1001

[1001](AOR)
contact=sip:1001@192.168.70.133:5060

;===============1002
[1002](ENDPOINT)
context=ADMIN
auth=1002
aors=1002

[1002](AUTH)
password=secret
username=1002

[1002](AOR)
contact=sip:1002@192.168.70.133:5060

;===============1003
[1003](ENDPOINT)
context=ADMIN
auth=1003
aors=101003010031

[1003](AUTH)
password=secret
username=1003

[1003](AOR)
contact=sip:1003@192.168.70.133:5060

;===============1004
[1004](ENDPOINT)
context=ADMIN
auth=1004
aors=1004

[1004](AUTH)
password=secret
username=1004

[1004](AOR)
contact=sip:1004@192.168.70.133:5060

;================= Numero du Dévéloppement =====================

;===============301
[301](ENDPOINT)
context=DEV
auth=301
aors=301

[301](AUTH)
password=secret
username=301

[301](AOR)
contact=sip:301@192.168.70.133:5060

;===============302
[302](ENDPOINT)
context=DEV
auth=302
aors=302

[302](AUTH)
password=secret
username=302

[302](AOR)
contact=sip:302@192.168.70.133:5060

;===============303
[303](ENDPOINT)
context=DEV
auth=303
aors=303

[303](AUTH)
password=secret
username=303

[303](AOR)
contact=sip:303@192.168.70.133:5060

;===============304
[304](ENDPOINT)
context=DEV
auth=304
aors=304

[304](AUTH)
password=secret
username=304

[304](AOR)
contact=sip:304@192.168.70.133:5060

;===============305
[305](ENDPOINT)
context=DEV
auth=305
aors=305

[305](AUTH)
password=secret
username=305

[305](AOR)
contact=sip:305@192.168.70.133:5060

;===============306
[306](ENDPOINT)
context=DEV
auth=306
aors=306

[306](AUTH)
password=secret
username=306

[306](AOR)
contact=sip:306@192.168.70.133:5060



;================= Numero de la securité resau =====================

;===============7001
[7001](ENDPOINT)
context=SECU
auth=7001
aors=7001

[7001](AUTH)
password=secret
username=7001

[7001](AOR)
contact=sip:7001@192.168.70.133:5060

;===============7002
[7002](ENDPOINT)
context=SECU
auth=7002
aors=7002

[7002](AUTH)
password=secret
username=7002

[7002](AOR)
contact=sip:7002@192.168.70.133:5060

;===============7003
[7003](ENDPOINT)
context=SECU
auth=7003
aors=7003

[7003](AUTH)
password=secret
username=7003

[7003](AOR)
contact=sip:7003@192.168.70.133:5060


