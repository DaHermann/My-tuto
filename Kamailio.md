# Comment installer kamailio sur Ubuntu 18.04 | 16.04

### Etape 1: installer apache2 http

  Tapez les cmd pour faire une mise à jours de vos package et l'installation d'apache2
  
    sudo apt update 
    sudo apt install apache2

  Après l'installation d'apache tapez les commandes suivantes pour rendre disponible de server apache:
  
    sudo systemctl stop apache2.service 
    sudo systemctl start apache2.service 
    sudo systemctl enable apache2.service
  
  Vous pouvez verifier que apache2 est bien disponible en faisant dans votre navigateur:
  
  `http://localhost`
  vous verez la page d'acceuil d'apache s'afficher.
  
  
  
  ### Etape 2:  installer Mariadb Serveur (c'est une base de donnée mysql)
  
  Pour installer Mariadb lancez la cmd suivante :  
  
  ` sudo apt install mariadb-server mariadb-client `

  Puis lancer ces cmd :
  
    sudo systemctl stop mariadb.service 
    sudo systemctl start mariadb.service 
    sudo systemctl enable mariadb.service 
  
  Ensuite securisez Mysql en creant *un mot de passe* root:
  
  ` sudo mysql_secure_installation `
  
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

    ` sudo mysql -u root -p `
    

  ### Etape 2: Installer PHP7.2 et ses Modules 
  
  Lancez les commandes suivantes pour ajouter le référentiel tiers ci-dessous pour mettre à niveau vers PHP 7.2
  
    sudo apt-get install software-properties-common
    sudo add-apt-repository ppa:ondrej/php
    
 Puis mettez à jour vers PHP 7.2
 
    sudo apt update




***show users in kamailio db*** 

`kamctl db show subscriber`
