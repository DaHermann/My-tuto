
# Installation de Kamailio v5.3


## Prerequis

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
  
  * **unixodbc-dev pour ODBC ODBC** : `apt install unixodbc-dev`
  
  * **Pour websocket** : `apt-get install libunistring-dev` and `apt install libwebsocketpp-dev`


  
  
## Etape 1: MySQL ou MariaDB Server

Il est possible d'utiliser **Mysql** ou **Mariadb sever**, dans notre cas nous allons utiliser **Mysql**.

Installons le avec la cmd suivante:

     apt-get install mysql-server   
     # ou   
     apt-get install default-mysql-server
    

## Etape 2: Obtenir Kamailio des sources de GIT

  * Creer un dossier et se placer à l'interieur de ce dossier
  
        mkdir -p /usr/local/src/kamailio-5.3
        
        cd /usr/local/src/kamailio-5.3
        
        
  * Télécharger des sources de Git en utilisant les cmd suivante
  
        git clone --depth 1 --no-single-branch https://github.com/kamailio/kamailio kamailio
        cd kamailio
        git checkout -b 5.3 origin/5.3
        
  **NB** : si votre version de client git ne prend pas en charge le paramètre de ligne de commande *--no-single-branch*, supprimez-le simplement.
  
  
## Etape 3: Reglages des fichiers Make

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

    make include_modules="db_mysql dialplan tls websocket" cfg
    
    
## Etape 4: Compiler Kamailio

   Compiler kamailio avec la cmd:
  
      make all
  
   Vous pouvez obtenir la sortie complète des indicateurs de compilation en utilisant :
  
      make Q=0 all
     

## Etape 5: Installer Kamailio

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
        
   
## Etape 6: Créer une base de données MySQL

   Pour créer la base de données *MySQL*, vous devez utiliser le script de configuration de la base de données. 
   Modifiez d'abord le fichier kamctlrc pour définir le type de serveur de base de données:
   
      nano -w /usr/local/etc/kamailio/kamctlrc
      
   Localisez la variable *DBENGINE* et définissez-la sur *MYSQL* :
    
    DBENGINE=MYSQL
    
   *Vous pouvez changer d'autres valeurs dans le fichier kamctlrc, au moins il est recommandé de changer les mots de passe par défaut pour les utilisateurs à créer    pour se connecter à la base de données.*

  Notez que la ligne existante avec `DBENGINE` ou d'autres attributs peut être commentée, 
  décommentée en supprimant le caractère `#` au début de la ligne, puis enregistrer et quittez.
  
  
  Exécutez le script pour créer la base de données utilisée par Kamailio:
  
     /usr/local/sbin/kamdbctl create
     
  Vous pouvez appeler ce script sans aucun paramètre pour obtenir de l'aide pour l'utilisation. Il vous sera demandé le nom de domaine que Kamailio va servir 
  (par exemple, monServeurSip.com) et le mot de passe de l'utilisateur `root` de MySQL. Le script créera une base de données nommée `kamailio` 
  contenant les tables requises par Kamailio. Vous pouvez modifier les paramètres par défaut dans le fichier kamctlrc mentionné ci-dessus.
  
  Le script ajoutera deux utilisateurs dans MySQL:

    * kamailio - (mot de passe par défaut *kamailiorw*) - qui a les droits d'accès complets à la base de données kamailio
    * kamailioro - (mot de passe par défaut *kamailioro*) - qui a des droits d'accès en lecture seule à la base de données kamailio

  **IMPORTANT : modifiez les mots de passe de ces deux utilisateurs en quelque chose de différent des valeurs par défaut fournies avec les sources.**

         
         
## Etape 6: Modifier le fichier de configuration de Kamailio
    
  Éditez le fichier de configuration de kamailio avec la cmd
  
    nano /usr/local/etc/kamailio/kamailio.cfg
 
  Ajoutez les lignes en haut du fichier de configuration juste apres `#!KAMAILIO`, cela va vous permettre d'utiliser `MYSQL`:
   
    #!define WITH_MYSQL
    #!define WITH_AUTH
    #!define WITH_USRLOCDB
    
   *Si vous avez changé le mot de passe de l'utilisateur kamailio de MySQL, vous devez mettre à jour la valeur des paramètres db_url.*
         
    
    
## Etape 7: Exécuter Kamailio
  
  
  Il existe quelques variantes pour démarrer /arrêter/redémarrer Kamailio, celles recommandées étant via le script `init.d` ou l'unité `systemd`, selon ce que le   système d'exploitation Debian est configuré pour utiliser.

  * **Init.d Script**

    Pour installer le script `init.d`, exécutez-le dans le répertoire du code source de Kamailio:
    
        make install-initd-debian
    Suivez toutes les instructions qui peuvent être imprimées par la commande ci-dessus.  
   
    Ensuite, vous pouvez démarrer / arrêter Kamailio à l'aide des commandes suivantes:

        /etc/init.d/kamailio start
        /etc/init.d/kamailio stop

  * **Systemd Unit**
   
    Pour installer l'unité `systemd`, exécutez dans le répertoire de code source Kamailio:

        make install-systemd-debian
    Suivez toutes les instructions qui peuvent être imprimées par la commande ci-dessus.

    Ensuite, vous pouvez `démarrer/arrêter` Kamailio à l'aide des commandes suivantes:
    
        systemctl start kamailio
        systemctl stop kamailio
        
    Vous devrez peut-être éditer edit `/usr/local/etc/kamailio/kamctlrc` et définir les attributs `PID_FILE` et `STARTOPTIONS`.
    
      Vous pouvez utiliser ensuite:
      
        kamctl start
        kamctl stop


  * **Ligne de commande**

    Kamailio peut être démarré à partir de la ligne de commande en exécutant le binaire avec des paramètres spécifiques. Par exemple:

      - *Démarrer Kamailio*
       
            /usr/local/sbin/kamailio -P /var/run/kamailio/kamailio.pid -m 128 -M 12

      - *Arrêter Kamailio*

            killall kamailio
            # ou
            kill -TERM $(cat /var/run/kamailio/kamailio.pid)


## Etape 8: Kamailio est prêt

  Maintenant, tout est en place. Vous pouvez démarrer le service VoIP, créer de nouveaux comptes et configurer les téléphones.

  Un nouveau compte peut être ajouté à l'aide de l'outil kamctl via:
  
      kamctl add username password
  
  
  **Si `SIP_DOMAIN` n'a pas été défini dans le fichier `kamctlrc`, utilisez l'une des options suivantes**
  
   - *Exécuter dans le terminal:*

         export SIP_DOMAIN=monserveursip.com
         kamctl add username password
   
  - *Ou éditez `/usr/local/etc/kamailio/kamctlrc` et ajoutez:* 
   
         SIP_DOMAIN=monserveursip.com
         
  - *ou donnez le nom d'utilisateur avec le domaine dans le paramètre kamctl add ...:
   
        kamctl add username@monserveursip.com password
    
    
    **Au lieu de `monserveursip.com`, il faut lui donner le vrai domaine du service SIP ou l'adresse IP de Kamailio.**
    
    
   ### * * Kamailio est Bien fonctionnel vous pouvez enregistrer tous vos utilisateurs et utliser kamailio * *

 
  ## Maintenance de Kamailio

    
   Le processus de maintenance est très simple pour le moment. Vous devez être root et exécuter les commandes suivantes:
   
     cd /usr/local/src/kamailio-5.3/kamailio
     git pull origin
     make all
     make install
     /etc/init.d/kamailio restart
     
   
  Vous avez maintenant la dernière version de Kamailio v5.3.x en cours d'exécution sur votre système.
  
  
  
  # FIN d'installation
