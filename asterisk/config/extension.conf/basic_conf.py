#@@@@@@@@@@@@@@@@@@@@@ BASIC EXTENSION.CONF CONFIGURATION to MAKE CALL @@@@@@@@@@@@@@@@@@@@@@@@@#


[general]
static=yes
writeprotect=no
clearglobalvars=no


[globals]
CONSOLE=Console/dsp				; Console interface for demo
IAXINFO=guest					; IAXtel username/password
TRUNK=DAHDI/G2					; Trunk interface
language=fr

[work]
exten => _1XX,1,NoOp(Call from $(CallerID(number)) -> ${EXTEN})
same => n,Dial(PJSIP/${EXTEN},20)
same => n,Hangup()
