
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
      
 
      
      
      
      
      
      