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

Le plan d'appel dans extensions.conf est organisé en sections, appelées contextes. Les contextes sont l'unité organisationnelle de base du plan d'appel, et en tant que tels, ils maintiennent les différentes sections du plan d'appel indépendantes les unes des autres. Vous pouvez utiliser les contextes pour séparer les fonctionnalités et les caractéristiques, renforcer les limites de sécurité entre les différentes parties de notre plan d'appel, ainsi que pour fournir différentes classes de service à des groupes d'utilisateurs.

### Contextes Dialplan
La syntaxe d'un contexte est exactement la même que celle de tout autre titre de section dans les fichiers de configuration. Il suffit de placer le nom du contexte entre crochets. Par exemple, nous définissons ici un contexte appelé "nan" et un autre appelé "users".
**[nan]** 
**[users]** 

### Extensions du plan de numérotation
Dans chaque contexte, on peut définir une ou plusieurs extensions. Une extension est simplement un ensemble d'actions nommées. Asterisk exécutera chaque action, en séquence, lorsque le numéro de l'extension est composé. La syntaxe d'une extension est la suivante :

        exten => numero,priorité,application([parametre[,parametre2...]])
        
Exemple:

        exten => 6001,1,Dial(PJSIP/demo-alice,20)
        
        
        
        
