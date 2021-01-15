# 3cx PBX tutorial


## Installation de 3cx


###  Connectez-vous à la machine via SSH et entrez ces commandes en utilisant sudo :


        wget -O- http://downloads-global.3cx.com/downloads/3cxpbx/public.key | apt-key add -

        echo "deb http://downloads-global.3cx.com/downloads/debian stretch main" | tee /etc/apt/sources.list.d/3cxpbx.list

        sudo apt update

        sudo apt install net-tools dphys-swapfile

        sudo apt install 3cxpbx

