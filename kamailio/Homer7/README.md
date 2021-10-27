# Installation of Homer 7 on Debian 10

## 1) Install dependencies

       apt install git wget 
        
      wget http://ftp.us.debian.org/debian/pool/main/l/lsb/lsb-release_10.2019051400_all.deb
      
      apt install ./lsb-release_10.2019051400_all.deb
      
      
## 2) Installing homer 7


       cd /usr/src
       wget https://github.com/sipcapture/homer-installer/raw/master/homer_installer.sh
       chmod +x homer_installer.sh
       ./homer_installer.sh

