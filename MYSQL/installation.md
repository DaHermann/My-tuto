# Mysql installation


## Install mysql on debian

### Step 1 — Adding the MySQL Software Repository

      apt update
      
      apt install gnupg
      
Then :

      cd /tmp
      wget https://dev.mysql.com/get/mysql-apt-config_0.8.13-1_all.deb

Ready to install Mysql:

      dpkg -i mysql-apt-config*
      
      apt update
      
      
### Step 2 — Installing MySQL

      apt install mysql-server
      
   Now show mysql status:
   
      systemctl status mysql
      
      
### Step 3 — Securing MySQL

      mysql_secure_installation
      
      
### Step 4 – Testing MySQL

    mysqladmin -u root -p version
    
    
    
    
Tuorial's link : 

https://www.digitalocean.com/community/tutorials/how-to-install-the-latest-mysql-on-debian-10


# Install unxODBC et Mysql ODBC-connector

What is ODBC?

ODBC is an open specification for providing application developers with a predictable API with which to access Data Sources. Data Sources include SQL Servers and any Data Source with an ODBC Driver. 


## Download and install unxODBC

      apt update
      
      apt upgrade
      
      apt install build-essential

### Downloading unxODBC


      wget ftp://ftp.unixodbc.org/pub/unixODBC/unixODBC-2.3.9.tar.gz
 
 then : 
 
      tar xvzf unixODBC-2.3.9.tar.gz
      
      cd unixODBC-2.3.9/
      
      
### Installing unxODBC


       ./configure --prefix=/usr/local/unixODBC
       
       make
       
       make install
       
After installing :

      cd /usr/local/unixODBC/bin/
      
      ls
      
unixODBC Tutorials link:

https://www.osradar.com/install-odbc-ubuntu-debian/



## Download and install Mysql ODBC-connector

link : 
https://dev.mysql.com/get/Downloads/Connector-ODBC/8.0/mysql-connector-odbc-setup_8.0.26-1debian10_amd64.deb


### Downlad

      wget https://dev.mysql.com/get/Downloads/Connector-ODBC/8.0/mysql-connector-odbc-setup_8.0.26-1debian10_amd64.deb
      
### Installing 

      apt install ./mysql-connector-odbc-setup*
