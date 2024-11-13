## INSTALL DOCKER


* Linux Mint 21

      https://linuxiac.com/how-to-install-docker-on-linux-mint-21/


* Linux mint 22

      https://linuxiac.com/how-to-install-docker-on-linux-mint-22/


* Posgres SQL

      docker run --name postgres_container -e POSTGRES_PASSWORD=postgres -p 5432:5432 -d postgres

* PgAdmin

           docker run --name pgadmin-container -p 5050:80 -e PGADMIN_DEFAULT_EMAIL=admin@db.com -e PGADMIN_DEFAULT_PASSWORD=admin@123 -d dpage/pgadmin4
