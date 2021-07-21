# CONFIGURATION D'APPEL 

Pour configurer un appel avec asterisk, deux fichers d'asterisk seront utilisés:

`/etc/asterisk/pjsip.conf` et  ` /etc/asterisk/extension.conf`

## configuration de pjsip.conf

` pjsip.conf ` est le fichier où est configuré les diferents utilisateurs:

* **[Phone-1]** :  est le nom d'utilisateur ou le nom du compte.
* **type = friend** : permet d'emmettre et de recevoir des appels
* **host = dynamic** : point de terminaison dont a nessecaire pour l'enregistrement
* **context = internal_context** : debute un contexte dans extension.conf
* **secret = 45HJHBHb@hd/#** mot de passe du compte

### Exemple:

    [Phone-1]
    type = friend
    host = dynamic
    context = nan
    etc...
    
https://github.com/DaHermann/My-tuto/blob/master/asterisk/config/pjsip/basic_pjsip_conf.py
 
 
## configuration de extension.conf
