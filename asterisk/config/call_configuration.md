# CONFIGURATION D'APPEL 

Pour configurer un appel avec asterisk, deux fichers d'asterisk seront utilisés:

`/etc/asterisk/pjsip.conf` et  ` /etc/asterisk/extension.conf`

## configuration de pjsip.conf

pjsip.conf est un fichier texte plat composé de sections comme la plupart des fichiers de configuration utilisés avec Asterisk. Chaque section définit la configuration d'un objet de configuration dans res_pjsip ou un module associé.

` pjsip.conf ` est le fichier où est configuré les diferents utilisateurs:

* **[Phone-1]** :  est le nom d'utilisateur ou le nom du compte.
* **type = friend** : permet d'emmettre et de recevoir des appels
* **host = dynamic** : point de terminaison dont a nessecaire pour l'enregistrement
* **context = internal_context** : debute un contexte dans extension.conf
* **secret = 45HJHBHb@hd/#** mot de passe du compte

Chaque section comporte une ou plusieurs options de configuration auxquelles on peut attribuer une valeur en utilisant un signe égal suivi d'une valeur.Ces options et valeurs constituent la configuration d'un composant particulier de la fonctionnalité fournie par les modules Asterisk respectifs de l'objet de configuration.

### Exemple:

    [Phone-1]
    type = friend
    host = dynamic
    context = nan
    etc...
    
Chaque section possède une option de type qui définit le type de section à configurer. Vous le verrez dans chaque exemple de section de configuration ci-dessous.

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
        
Dans ce cas, le numéro de poste est 6001, le numéro de priorité est 1, l'application est Dial(), et les deux paramètres de l'application sont PJSIP/demo-alice et 20.        
        
        
