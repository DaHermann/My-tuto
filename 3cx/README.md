# 3cx PBX tutorial


## Installation de 3cx sur debian

liens vers le site officiel : https://www.3cx.fr/docs/manuel/installation-linux/


###  Connectez-vous à la machine via SSH et entrez ces commandes en utilisant sudo :



        sudo apt install gnupg && sudo apt install gnupg2
        
        wget -O- http://downloads-global.3cx.com/downloads/3cxpbx/public.key | apt-key add -

        echo "deb http://downloads-global.3cx.com/downloads/debian stretch main" | tee /etc/apt/sources.list.d/3cxpbx.list

        apt update

        apt install net-tools dphys-swapfile

        apt install 3cxpbx

