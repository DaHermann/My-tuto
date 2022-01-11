# Installation of composer


## Install PHP

    sudo apt update
     
    sudo apt install wget php-cli php-zip unzip
    
    
## Download composer 

    wget -O composer-setup.php https://getcomposer.org/installer
    
## Install composer globally

    sudo php composer-setup.php --install-dir=/usr/local/bin --filename=composer
    


## Install composer Localy
 
 
    sudo php composer-setup.php --install-dir=/path/to/project
