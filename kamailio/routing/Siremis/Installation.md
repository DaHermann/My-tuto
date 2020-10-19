
## Installation

L'installation de Siremis est simple et se fait principalement via un assistant Web. En quelques étapes et moins de 10 minutes, votre site Web Siremis est configuré et prêt à vous offrir une administration facile de votre serveur Kamailio SIP.

Vous devez d'abord installer une version compatible de <a href="https://kamailio.org/docs/tutorials/5.4.x/kamailio-install-guide-git/" >Kamailio SIP Server</a>

**Siremis v5.3.x (devel)**

Dernière version: ***v5.3.0***

### Prerequis

* Apache Web Server
    
      apt-get install apache2
      
      a2enmod rewrite
    
* PHP

Pour php7

      apt-get install php php-mysql php-gd php-curl php-xml libapache2-mod-php php-pear
      
      a2enmod php7.0  #Pour rendre disponible le modules php7 pour apache2
 
Pour le panneau de commande XMLRPC, le paquet XML_RPC pear est nécessaire pour PHP5 ou PHP7 : 

    wget http://pear.php.net/get/XML_RPC-1.5.5.tgz
    pear upgrade XML_RPC-1.5.5.tgz 
  
  
## Téléchargement de Siremis depuis le dépôt GIT

    cd /var/www
    git clone https://github.com/asipto/siremis siremis-5.3.x
    cd siremis-5.3.x
    git checkout -b 5.3 origin/5.3

## Configuration du serveur web Apache

Apache v2.4

Si vous voulez configurer un alias pour Apache 2.4.x, vous pouvez vous lancer : 

    make apache24-conf
    
et vous obtenez l'extrait de configuration imprimé dans le terminal. Comme suit :

    Alias /siremis "/var/www/siremis-5.3.x/siremis"
	<Directory "/var/www/siremis-5.3.x/siremis">
		Options Indexes FollowSymLinks MultiViews
		AllowOverride All
		Require all granted
		<FilesMatch "\.xml$">
			Require all denied
		</FilesMatch>
		<FilesMatch "\.inc$">
			Require all denied
		</FilesMatch>
	</Directory>
Vous pouvez copier&coller ce qui a été imprimé dans le terminal dans le fichier conf d'Apache, dans les paramètres de VirtualHost. 

Pour Apache2 sur Debian/Ubuntu, le fichier de configuration est : 

    /etc/apache2/sites-available/000-default.conf
    
Après le redémarrage du serveur web, SIREMIS sera disponible sous : 

 http//:votre_ip/siremis/. 
 
 Exemple: http://192.168.50.131/siremis/
 
 Si vous souhaitez utiliser un autre alias, modifiez le Makefile et changez la valeur d'URLBASE. 
 
 
 ## Préparer la configuration locale de Siremis
 
 L'étape suivante consiste à créer les fichiers de configuration **.htaccess** et **Siremis**, vous devez lancer la commande prepare. 
 
Apache v2.4

 	make prepare24
 
La sortie ressemble à : 

	siremis-x.y.z# make prepare24
	updating htaccess file...
	updating app.inc file...
	done
	
Assurez-vous que les répertoires suivants ont un accès en écriture pour l'utilisateur du serveur web : 

	
   * siremis/log
   * siremis/session
   * siremis/files
   * siremis/themes/default/template/cpl
   
Sur Debian/Ubuntu, vous pouvez le faire : 

	siremis-x.y.z# make chown
    
N'oubliez pas de redémarrer le serveur web après avoir effectué les modifications dans son fichier de configuration.


## Configuration de la base de données


Le serveur de base de données à utiliser est MySQL.

Vous devez créer un utilisateur MySQL qui a accès à la base de données Siremis, par exemple : 

	GRANT ALL PRIVILEGES ON siremis.* TO siremis@localhost IDENTIFIED BY 'siremisrw';


