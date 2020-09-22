# Kamailio Configuration File Structure (Structure du fichier de configuration de Kamailio)



## OVERVIEW OF CONFIGURATION FILE (APERÇU DU FICHIER DE CONFIGURATION)


Le fichier de configuration est du texte brut, analysé au démarrage par Kamailio, qui construit un arbre d'exécution en mémoire pour l'utiliser à l'exécution.
Il est nommé par défaut kamailio.cfg et déployé dans `/usr/local/etc/kamailio/kamailio.cfg` par la procédure d'installation. L'appel Kamailio charge le fichier de configuration à partir de différents chemins, avec des noms différents, il suffit de fournir le chemin complet au paramètre de ligne de commande "-f".
Dans l'arborescence des sources, située dans `utils/misc/vim/`, se trouvent les fichiers qui fournissent la coloration syntaxique pour vim et sa famille d'éditeurs (par exemple, gvim, kvim) - un fichier readme dans ce dossier donne les instructions rapides sur la façon d'installer. 
Sur le web, vous pouvez trouver un fichier de coloration syntaxique pour mcedit (l'éditeur du gestionnaire de fichiers Midnight Commander). La coloration syntaxique est très utile pour repérer les différents éléments des fichiers de configuration, tels que les commentaires, les jetons spéciaux, les valeurs, etc.
Dans ce chapitre, nous examinons la structure générique du fichier de configuration et ses principaux composants, puis nous aborderons plus en détail les éléments fonctionnels.


## SPECIAL COMPONENTS ()
