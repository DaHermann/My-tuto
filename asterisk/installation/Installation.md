
# Download Locations


Project | Location
| --- | --- |
Asterisk |	https://downloads.asterisk.org/pub/telephony/asterisk/asterisk-14-current.tar.gz
libpri |	https://downloads.asterisk.org/pub/telephony/libpri/libpri-current.tar.gz
dahdi-linux	| https://downloads.asterisk.org/pub/telephony/dahdi-linux/dahdi-linux-current.tar.gz
dahdi-tools |	https://downloads.asterisk.org/pub/telephony/dahdi-tools/dahdi-tools-current.tar.gz
dahdi-complete	| https://downloads.asterisk.org/pub/telephony/dahdi-linux-complete/dahdi-linux-complete-current.tar.gz


# Intallation de Asterisk sur Debian 10

    cd /usr/local/src 
    
## installer les headers linux
 
    apt install linux-headers-$(uname -r)
    
## Télecharger les différents Project

   * Dahdi
          
          wget https://downloads.asterisk.org/pub/telephony/dahdi-linux-complete/dahdi-linux-complete-current.tar.gz
      
          tar -zxvf dahdi-linux-complete-current.tar.gz
    
   * Libpri

          wget https://downloads.asterisk.org/pub/telephony/libpri/libpri-current.tar.gz
      
          tar -zxvf libpri-current.tar.gz
      
   * Asterisk

          wget https://downloads.asterisk.org/pub/telephony/asterisk/asterisk-18-current.tar.gz
          
          tar -zxvf asterisk-18-current.tar.gz
      
      
 ## Installer les Prerequis asteristersk
 
         cd asterisk-18.5.0/
         
         ./contrib/scripts/install_prereq install
      
 ## Installer Dahdi
 
     cd ../

     cd dahdi-linux-complete-3.1.0+3.1.0/

     make 

     make install

     make install-config
         
         
 ## Installer Libpri
 
        
     cd ../

     cd libpri-1.6.0/

     make 

     make install
         
   ## Installer Asterisk
   
     cd ../

     cd asterisk-18.5.0/
    
     ./configure
     
     
  Apres celà le resultat obtenu est :
 
 
      configure: Menuselect build configuration successfully completed

                     .$$$$$$$$$$$$$$$=..      
                  .$7$7..          .7$$7:.    
                .$$:.                 ,$7.7   
              .$7.     7$$$$           .$$77  
           ..$$.       $$$$$            .$$$7 
          ..7$   .?.   $$$$$   .?.       7$$$.
         $.$.   .$$$7. $$$$7 .7$$$.      .$$$.
       .777.   .$$$$$$77$$$77$$$$$7.      $$$,
       $$$~      .7$$$$$$$$$$$$$7.       .$$$.
      .$$7          .7$$$$$$$7:          ?$$$.
      $$$          ?7$$$$$$$$$$I        .$$$7 
      $$$       .7$$$$$$$$$$$$$$$$      :$$$. 
      $$$       $$$$$$7$$$$$$$$$$$$    .$$$.  
      $$$        $$$   7$$$7  .$$$    .$$$.   
      $$$$             $$$$7         .$$$.    
      7$$$7            7$$$$        7$$$      
       $$$$$                        $$$       
        $$$$7.                       $$  (TM)     
         $$$$$$$.           .7$$$$$$  $$      
           $$$$$$$$$$$$7$$$$$$$$$.$$$$$$      
             $$$$$$$$$$$$$$$$.                

     
     make menuselect
     
     make
     
     make install
      
      
      
 resultat de fin d'installation 
 
 
       +---- Asterisk Installation Complete -------+
       +                                           +
       +    YOU MUST READ THE SECURITY DOCUMENT    +
       +                                           +
       + Asterisk has successfully been installed. +
       + If you would like to install the sample   +
       + configuration files (overwriting any      +
       + existing config files), run:              +
       +                                           +
       + For generic reference documentation:      +
       +    make samples                           +
       +                                           +
       + For a sample basic PBX:                   +
       +    make basic-pbx                         +
       +                                           +
       +                                           +
       +-----------------  or ---------------------+
       +                                           +
       + You can go ahead and install the asterisk +
       + program documentation now or later run:   +
       +                                           +
       +               make progdocs               +
       +                                           +
       + **Note** This requires that you have      +
       + doxygen installed on your local system    +
       +-------------------------------------------+
 
 
 ## Creation d'un Asterisk User

    
    sudo groupadd asterisk
    sudo useradd -r -d /var/lib/asterisk -g asterisk asterisk
    sudo usermod -aG audio,dialout asterisk
    sudo chown -R asterisk.asterisk /etc/asterisk
    sudo chown -R asterisk.asterisk /var/{lib,log,spool}/asterisk
    sudo chown -R asterisk.asterisk /usr/lib/asterisk


Set Asterisk default user to asterisk:

    $ sudo vim /etc/default/asterisk
    
    AST_USER="asterisk"
    AST_GROUP="asterisk"

    $ sudo vim /etc/asterisk/asterisk.conf
    
    runuser = asterisk ; The user to run as.
    rungroup = asterisk ; The group to run as.
  

Restart asterisk service after making the changes:

     sudo systemctl restart asterisk
      
      
 Enable asterisk service to start on system  boot:
 
 
     sudo systemctl enable asterisk
 
       
Tchek status of asterisk

     systemctl status asterisk
     

     ● asterisk.service - LSB: Asterisk PBX
        Loaded: loaded (/etc/init.d/asterisk; generated; vendor preset: enabled)
        Active: active (exited) since Fri 2020-10-09 14:48:02 UTC; 1min 19s ago
          Docs: man:systemd-sysv-generator(8)

     Oct 09 14:48:02 SERVEUR-5 systemd[1]: asterisk.service: Failed to reset devices.li
     Oct 09 14:48:02 SERVEUR-5 systemd[1]: Starting LSB: Asterisk PBX...
     Oct 09 14:48:02 SERVEUR-5 asterisk[5531]: Starting Asterisk PBX: asteriskUnable to
     Oct 09 14:48:02 SERVEUR-5 asterisk[5531]: .
     Oct 09 14:48:02 SERVEUR-5 systemd[1]: Started LSB: Asterisk PBX.
     
   
Test to see if you can connect to Asterisk CLI:
     
     asterisk -rvv

      
      
