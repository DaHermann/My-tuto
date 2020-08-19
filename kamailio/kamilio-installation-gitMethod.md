
# Installation de Kamailio v5.3


### Prerequis

Connectez vous en tant que root et install les packages requis pour l'installation de kamailio

  * **git**: `apt install git-core`
  
  * **gcc** et **g++** : `apt install gcc g++`
  
  * **flex**: `apt install flex`
  
  * **bison**: `apt install bison`
  
  * **libmysqlclient-dev**: `apt install libmysqlclient-dev` ou  (apt install default-libmysqlclient-dev)
  
  * **make** et **autoconf**: `apt install make autoconf`
  
  * **libssl-dev**: `apt install libssl-dev`
  
  * **libcurl4-openssl-dev**: `apt install libcurl4-openssl-dev`
  
  * **libxml2-dev**: `apt install libxml2-dev`
  
  * **libpcre3-dev**: `apt install libpcre3-dev`
  
  
### Etape 1: MySQL ou MariaDB Server

Il est possible d'utiliser **Mysql** ou **Mariadb sever**, dans notre cas nous allons utiliser **Mysql**.

Installons le avec la cmd suivante:

     apt-get install mysql-server   
     # ou   
     apt-get install default-mysql-server
    

### Etape 3: Obtenir Kamailio des sources de GIT

  * Creer un dossier et se placer à l'interieur de ce dossier
  
        mkdir -p /usr/local/src/kamailio-5.3
        
        cd /usr/local/src/kamailio-5.3
        
        
  * Télécharger des sources de Git en utilisant les cmd suivante
  
        git clone --depth 1 --no-single-branch https://github.com/kamailio/kamailio kamailio
        cd kamailio
        git checkout -b 5.3 origin/5.3
        
  **NB** : si votre version de client git ne prend pas en charge le paramètre de ligne de commande *--no-single-branch*, supprimez-le simplement.
  
  
### Etape 4: Reglages des fichiers Make

  Générer des fichiers de configuration de construction avec la commande suivante:
  
     make cfg

  Puis activer le module MySQL. Editez le fichier **modules.lst**:
  
     nano -w src/modules.lst
    # ou
    vim src/modules.lst
    
  Ajoutez *db_mysql* à la variable *include_modules*
  
    include_modules= db_mysql
  Enregistrez le fichier modules.lst et quittez
  
  **NB** c'est un mécanisme pour activer les modules qui ne sont pas compilés par défaut, tels que lcr, dialplan, presence - 
         ajoutez les modules à la variable include_modules dans le fichier modules.lst, comme:
         
    include_modules= db_mysql dialplan

  On autre altenative est d'ajouter la variable *include_modules* à la compilation, lors de la construction des fichiers *Make cfg*:

    make include_modules="db_mysql dialplan" cfg
    
    
### Etape 5: Compiler Kamailio

   Compiler kamailio avec la cmd:
  
      make all
  
   Vous pouvez obtenir la sortie complète des indicateurs de compilation en utilisant :
  
      make Q=0 all
     

### Etape 6: Installer Kamailio

   Lorsque la compilation est prête, installez Kamailio avec la commande suivante:
  
      make install
      
  * **QUOI ET OU A ÉTÉ INSTALLÉ**
  
    Les binaires et les scripts exécutables ont été installés dans:
    
        /usr/local/sbin
        
    Se sont :

        * kamailio - Kamailio SIP server
        * kamdbctl - script pour créer et gérer les bases de données
        * kamctl - script pour gérer et contrôler le serveur SIP Kamailio
        * kamcmd - CLI - outil de ligne de commande pour l'interface avec le serveur Kamailio SIP
  
    Pour pouvoir utiliser les binaires à partir de la ligne de commande, assurez-vous que `/usr/local/sbin` est défini dans la variable d'environnement PATH. 
    Vous pouvez vérifier cela avec `echo $PATH`. Sinon et que vous utilisez bash, ouvrez `/root/.bash_profile` et à la fin, ajoutez:

         PATH=$PATH:/usr/local/sbin
         export PATH
    
    
    Les modules Kamailio sont installés dans:
         
         /usr/local/lib/kamailio/modules/
    **nb**: Sur les systèmes 64 bits, `/usr/local/lib64` peut être utilisé.
      
    La documentation et les fichiers readme sont installés dans:
    
        /usr/local/share/doc/kamailio/
    
    Les pages de manuel (man) sont installées dans:
    
        /usr/local/share/man/man5/
        /usr/local/share/man/man8/
        
    Le fichier de configuration a été installé dans:
  
        /usr/local/etc/kamailio/kamailio.cfg
         
         
         
         
         
         
    
  
