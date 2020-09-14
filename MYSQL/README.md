# ALL MYSQL COMMAND


**To connect to mysql** : `mysqladmin -u USER password YOURNEWPASSWORD`;

**Create a User** : ` CREATE USER 'myuser'@'localhost' IDENTIFIED BY 'mypass';`
                      `CREATE USER 'myuser'@'%' IDENTIFIED BY 'mypass';` #Pour une connection à distance

**Update User Password** : `ALTER USER 'root'@'localhost' IDENTIFIED BY 'new_password';`
