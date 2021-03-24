# Intégration en temps réel à l'aide de la base de données Asterisk

Ce tutoriel montre comment utiliser la base de données Asterisk pour charger le profil utilisateur SIP à partir du fichier de configuration de Kamailio. Un cas d'utilisation typique est Kamailio comme routeur proxy SIP pour mettre à l'échelle Asterisk, en gérant l'authentification et l'enregistrement des utilisateurs, laissant un ou une ferme d'Asterisk s'occuper de la gestion des appels (par exemple, IVR, transcodage, passerelle, facturation prépayée, etc.)

Le module d'authentification de Kamailio peut être configuré pour se connecter à n'importe quelle base de données et récupérer le mot de passe à partir d'une table et d'une colonne personnalisées, par conséquent la création d'une vue de la base de données n'est pas vraiment nécessaire, à moins que vous ne le souhaitiez pour d'autres raisons.

Le document ici présente l'installation à partir des sources, utilise MySQL comme serveur de base de données et unixodbc pour Asterisk temps réel. Les étapes sont données pour les systèmes d'exploitation Ubuntu/Debian.


# Architecture

réutiliser autant que possible la configuration par défaut d'Asterisk relatime
gérer l'authentification dans Kamailio
gérer la localisation des utilisateurs dans Kamailio
le routage des appels entre les téléphones locaux est géré par Asterisk
les services média sont gérés par Asterisk en fonction du plan de numérotation d'Asterisk
le routage des autres messages SIP non liés aux appels est géré directement par Kamailio.


## Enregistrement
Kamailio effectue une authentification pour l'enregistrement. En cas de succès, il notifie à Asterisk avec un nouveau REGISTER que le téléphone est disponible sur son IP.

@img

## Initiation d'appel
L'authentification des appels est gérée par Kamailio. Lorsqu'un nouvel appel arrive et qu'il est authentifié, Kamailio le transmet à Asterisk. Si le numéro de destination est en ligne, Asterisk renvoie l'appel à Kamailio puisque le contact de destination est l'IP de Kamailio. Ensuite, Kamailio effectuera une recherche de localisation et enverra l'appel à l'IP du téléphone de destination.

@img



