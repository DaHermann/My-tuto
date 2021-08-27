;=========================================== Projet Asterisk 1 ===================================


[ADMIN] ;Context ADMIN
exten => _1XXX,1,NoOp(attention il y a un appel en cours )
same => n,Set(CHANNEL(language)=fr)
same => n,Dial(PJSIP/${EXTEN},20) ; Appeler
same => n,Voicemail(${EXTEN}@adminMail)
same => n,Hangup() ; Racrocher

include => t-admin ; trunk sip admin

;Boite vocal admin
exten => _1000,1,NoOp(Je suis dans la boite vocal)
same => n,Set(CHANNEL(language)=fr)
same => n, VoiceMailMain(${CALLERID(num)}@adminMail,s)
same => n, Hangup()


[DEV] ;Context DEV
exten => _3XX,1,NoOp(attention il y a un appel en cours )
same => n,Set(CHANNEL(language)=fr)
same => n,Dial(PJSIP/${EXTEN},20) ; Appeler
same => n,Voicemail(${EXTEN}@devMail)
same => n,Hangup() ; Racrocher

include => t-dev ; trunk sip dev

;Boite vocal dev
exten => _300,1,NoOp(Je suis dans la boite vocal)
same => n,Set(CHANNEL(language)=fr)
same => n, VoiceMailMain(${CALLERID(num)}@devMail,s)
same => n, Hangup()


[SECU] ;Context SECU
exten => _7XXX,1,NoOp(attention il y a un appel en cours )
same => n,Set(CHANNEL(language)=fr)
same => n,Dial(PJSIP/${EXTEN},20) ; Appeler
same => n,Voicemail(${EXTEN})
same => n,Hangup() ; Racrocher

include => t-secu ; trunk sip secu

exten => _7000,1,NoOp(Je suis dans la boite vocal)
same => n,Set(CHANNEL(language)=fr)
same => n, VoiceMailMain(${CALLERID(num)}@secuMail,s)
same => n, Hangup()


;========================= Trunck SIP ==============================

[t-admin]
exten => _3XX,1,NoOp(Je suis dans la boite vocal)
same => n,Goto(DEV,${EXTEN},1)
same => n,Hangup()

exten => _7XXX,1,NoOp(Je suis dans la boite vocal)
same => n,Goto(SECU,${EXTEN},1)
same => n,Hangup()

[t-dev]
exten => _1XXX,1,NoOp(Je suis dans la boite vocal)
same => n,Goto(ADMIN,${EXTEN},1)
same => n,Hangup()

exten => _7XXX,1,NoOp(Je suis dans la boite vocal)
same => n,Goto(SECU,${EXTEN},1)
same => n,Hangup()

[t-secu]
exten => _1XXX,1,NoOp(Je suis dans la boite vocal)
same => n,Goto(ADMIN,${EXTEN},1)
same => n,Hangup()

exten => _3XX,1,NoOp(Je suis dans la boite vocal)
same => n,Goto(DEV,${EXTEN},1)
same => n,Hangup()

