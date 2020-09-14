# ALL MYSQL COMMAND


**To connect to mysql** : 

    mysqladmin -u USER password YOURNEWPASSWORD;
    
### USER mysql

**Create a User** : 
      
        CREATE USER 'myuser'@'localhost' IDENTIFIED BY 'mypass';
        #ou
        CREATE USER 'myuser'@'%' IDENTIFIED BY 'mypass';` // Pour une connection à distance

**Update User Password** : 
    
      ALTER USER 'root'@'localhost' IDENTIFIED BY 'new_password';

**Give all privillage to a user** : 

      GRANT ALL ON *.* TO 'myuser'@'localhost';
      # then
      flush privileges;

### DATABASES mysql

**Show databases** :

    SHOW DATABASES;

**Create Database** :

    CREATE DATABASE mydatabase;
    
**Change Database** : 

    USE mydatabase
    
**Show Tables** : 

    SHOW TABLES;
    
**shows information on all columns of a table** :

    DESCRIBE myTable;
    
    
    
    
    
