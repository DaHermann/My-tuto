# Mysql installation


## Install mysql on debian

### Step 1 — Adding the MySQL Software Repository

      apt update
      
      apt install gnupg
      
Then :

      cd /tmp
      wget https://dev.mysql.com/get/mysql-apt-config_0.8.13-1_all.deb

Ready to install Mysql:

      sudo dpkg -i mysql-apt-config*
      
      apt update
      
      
### Step 2 — Installing MySQL

      apt install mysql-server
      
   Now show mysql status:
   
      systemctl status mysql
      
      
### Step 3 — Securing MySQL

      mysql_secure_installation
      
      
### Step 4 – Testing MySQL

    mysqladmin -u root -p version
