# ACCOUNTING USING SIREMIS


Siremis comprend des composants permettant de générer des enregistrements complets des données d'appel et un petit moteur de tarification permettant de fixer le coût en fonction de la correspondance du préfixe le plus long.
Tous deux sont basés sur des procédures stockées par MySQL et peuvent être créés au cours de l'assistant d'installation. En même temps, la structure des tables des bases de données acc et missed_calls est mise à jour, afin de pouvoir stocker les attributs supplémentaires tels que configurés pour le module acc dans le fichier par défaut kamailio.cfg, plus une colonne supplémentaire nommée cdr_id, pour conserver une référence à l'enregistrement correspondant dans la table cdrs.
Au cours de l'assistant d'installation, à l'étape 2. Configuration de la base de données, vous devez cocher l'option pour :

  * **Mise à jour de la base de données SIP** (en bas de la page, au-dessus des boutons Précédent - Suivant, voir la capture d'écran suivante)

<img src="" >


Sachez que cette option supprime les anciens tableaux d'accès et d'appels manqués, donc assurez-vous que vous n'y avez pas d'enregistrements de valeur.
Si vous voulez vérifier quelles instructions SQL sont exécutées par cette option, regardez dans le dossier Siremis :
  `siremis/modules/ser/mod.install.siremis.sql`
Les enregistrements comptables peuvent être consultés sur SIP Admin Menu => Accounting Services => Accounting List - la vue par défaut ne montre que plusieurs attributs, pour les voir tous pour chaque enregistrement, cliquez sur la colonne Id.

<img src="" >


## CALL DATA RECORDS (LES ENREGISTREMENTS DES DONNÉES D'APPEL)


Les CDR peuvent être créés en appelant la procédure stockée kamailio_cdrs(). La procédure a été ajoutée par l'assistant d'installation et peut être exécutée en externe via cron.d ou des applications similaires. Elle peut également être exécutée à partir de kamailio.cfg en chargeant les modules rtimer et sqlops et en définissant une exécution par bloc de route périodique. Les prochains snippets doivent être ajoutés dans kamailio.cfg :




