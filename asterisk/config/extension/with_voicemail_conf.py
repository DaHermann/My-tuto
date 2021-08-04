
[client] ;Context
exten => _1XX,1,NoOp(attention il y a un appel en cours )
same => n,Dial(PJSIP/${EXTEN},20) ; Appeler
same => n,Voicemail(${EXTEN}@school)
same => n,Hangup() ; Racrocher


exten => _200,1,NoOp(Je suis dans la boite vocal)
same => n,Set(CHANNEL(language)=fr)
same => n, VoiceMailMain(${EXTEN}@school,s)
same => n, Hangup()


[orange] ;Context Orange
exten => _07XXXXXXXX,1,NoOp(attention il y a un appel en cours )
same => n,Dial(PJSIP/${EXTEN},20) ; Appeler
same => n,Hangup() ; Racrocher

exten => _200,1,NoOp(Je suis dans la boite vocal)
same => n,Set(CHANNEL(language)=fr)
same => n, VoiceMailMain(${EXTEN}@work,s)
same => n, Hangup()
