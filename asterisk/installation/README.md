# Installation d'asterisk



## Etape 1:  Recuperer asterisk depuuis le github


     cd /usr/src
     
     git clone http://gerrit.asterisk.org/asterisk asterisk
     
     cd asterisk/
     

## Etape 2:  installation des dependenses


    contrib/scripts/install_prereq install


## Etape 3: 

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



## Etape 4: 
  
      make menuselect [optional]
    

## Etape 5: 

    make


## Etape 6: 

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
 
    
## Etape 7: Create Asterisk User

    
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
