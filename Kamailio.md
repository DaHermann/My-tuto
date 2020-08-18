# Comment installer kamailio sur Ubuntu 18.04 | 16.04
  
  
  ### Etape 1:  installer Mariadb Serveur (c'est une base de donnée mysql)
  
  Pour installer Mariadb lancez la cmd suivante :  
  
     sudo apt install mariadb-server mariadb-client

  Puis lancer ces cmd :
  
    sudo systemctl stop mariadb.service 
    sudo systemctl start mariadb.service 
    sudo systemctl enable mariadb.service 
  
  Ensuite securisez Mysql en creant *un mot de passe* root:
  
    sudo mysql_secure_installation 
  
  Repondez au question suivantes ...
  
    * Enter current password for root (enter for none): Tapez Enter
    * Set root password? [Y/n]: Y
    * New password: Entrez un mot de Passe
    * Re-enter new password: Repetez le mot de passe
    * Remove anonymous users? [Y/n]: Y
    * Disallow root login remotely? [Y/n]: Y
    * Remove test database and access to it? [Y/n]:  Y
    * Reload privilege tables now? [Y/n]:  Y
  
  Maintenant testez une connexion mysql :

     sudo mysql -u root -p
    

  ### Etape 2: Télécharger et configurer la dernière version de Kamailio
  
    
   * Mettez à jour les packages d'ubuntu et install kamailio
   
    sudo apt update
    sudo apt install kamailio kamailio-mysql-modules kamailio-websocket-modules
    
    
   Affichez la version de kamailio en faisant:
   
      kamailio -V
      
      
  ### Etape 3: Configurer Kamailio
  
    
   Ouvrez les fichiers de configuratiion par defaut de kamailio 
          Tapez la cmd : 
          
    sudo nano /etc/kamailio/kamctlrc
   
   Puis decommentez **SIP_DOMAIN** et **DBENGINE**
   
    # The Kamailio configuration file for the control tools.
    #
    ## your SIP domain
     SIP_DOMAIN=kamailio.example.com
    ## chrooted directory
    #
    # If you want to setup a database with kamdbctl, you must at least specify
    # this parameter.
     DBENGINE=MYSQL
    ## database host
    ## database read only user
    
   Apres le changement, enregistrer le fichier et creer la base de donnée de kamailio en tapant:
   
    kamdbctl create

  <div class="bg-blue-light mb-2">
  Si vous obtenez **accès refusé pour root@localhost**, suivez les étapes ci-dessous pour résoudre
  
  * Connectez-vous au serveur MariaDB en exécutant les commandes ci-dessous.
                              
        sudo mysql -u root
  
  
  * Cela devrait vous permettre d'accéder au serveur de base de données. 
    Après cela, exécutez les commandes ci-dessous pour désactiver l'authentification du plugin pour l'utilisateur root.
    
        use mysql;
        update user set plugin='' where User='root';
        flush privileges;
        exit
        
  * Redémarrez et exécutez les commandes ci-dessous pour définir un nouveau mot de passe.
  
        sudo systemctl restart mariadb.service

  **Maintenant relancez la cmd ` kamdbctl create ` pour creer la base de donnée kamailio  et un utilisateur .**
  
  </div>
    
    
  Lorsque vous y êtes invité, répondez avec les paramètres ci-dessous:

    Enter character set name: 
    latin1
    INFO: creating database kamailio ...
    INFO: granting privileges to database kamailio ...
    INFO: creating standard tables into kamailio ...
    INFO: Core Kamailio tables succesfully created.
    Install presence related tables? (y/n): y
    INFO: creating presence tables into kamailio ...
    INFO: Presence tables succesfully created.
    Install tables for imc cpl siptrace domainpolicy carrierroute
        drouting userblacklist htable purple uac pipelimit mtree sca mohqueue
        rtpproxy rtpengine? (y/n): y
    INFO: creating extra tables into kamailio ...
    INFO: Extra tables succesfully created.
    Install tables for uid_auth_db uid_avp_db uid_domain uid_gflags
        uid_uri_db? (y/n): y
    INFO: creating uid tables into kamailio ...
    INFO: UID tables succesfully created.
      


  Ensuite, ouvrez le fichier `/etc/kamailio/kamailio.cfg` en exécutant les commandes ci-dessous:

    sudo nano /etc/kamailio/kamailio.cfg
    
  Ajoutez ensuite les lignes ci-dessous après la ligne **#!KAMAILIO**
  
    #!define WITH_MYSQL
    #!define WITH_AUTH
    #!define WITH_USRLOCDB
    #!define WITH_ACCDB
    
  Enregistrez le fichier et quittez.
  
  
  
  
    
    
    
