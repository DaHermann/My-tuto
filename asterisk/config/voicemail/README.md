# VOICEMAIL CONFIGURATION

## extension.conf

[work]
exten => _1X[1-9],1,NoOp(Call from $(CallerID(number)) -> ${EXTEN})
same => n,Dial(PJSIP/${EXTEN},8)
same => n,set(${CHANNEL(language)=fr})
same => n,VoiceMail(${EXTEN})
same => n,Hangup()


;===================================== VoiceMailMain
exten => _100,1,NoOp(## VoiceMail Access ##)
same => n,Set(CHANNEL(language)=fr)
same => n,VoiceMailMain(${EXTEN},s)
same => n,Hangup()


## voicemail.conf


[default]
; Note: The rest of the system must reference mailboxes defined here as mailbox@default.
101 => 1234
102 => 1234,Sip phone 1
103 => 1234,Sip phone 2
104 => 1234,Linphone
