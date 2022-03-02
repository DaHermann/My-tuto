# Installation of php 8.1


## First, update your Ubuntu server:


     apt-get update && apt-get upgrade
     

## Add the PHP repository

To install PHP 8.0 you’ll need to use a third-party repository. We’ll use the repository by Ondřej Surý that we previously used.
First, make sure you have the following package installed so you can add repositories:

     apt-get install software-properties-common
     
## Next, add the PHP repository from Ondřej:

     sudo add-apt-repository ppa:ondrej/php
     
And finally, update your package list:

     apt-get update

## Install PHP 8.1

After you’ve added the repository, you can install PHP 8.1 with the following command:

     apt-get install php8.1
     
     
This command will install additional packages:

* libapache2-mod-php8.1
* libpcre2-8-0
* php8.1-cli
* php8.1-common
* php8.1-opcache
* php8.1-readline
…and others.

And that’s it. To check if PHP 8.1 is installed on your server, run the following command:

     php -v
     
Which should return something like this:

     PHP 8.1.1 (cli) (built: Dec 31 2021 07:26:20) (NTS)
     Install PHP 8.1 modules (extensions)
     
You may need additional packages and modules depending on your applications. The most commonly used modules can be installed with the following command:

     apt-get install libapache2-mod-php8.1 php8.1-fpm libapache2-mod-fcgid php8.1-curl php8.1-dev php8.1-gd php8.1-mbstring php8.1-zip php8.1-mysql php8.1-xml
     
     
And that’s all. You can now start using PHP on your Ubuntu server.

If you want to further tweak and configure your PHP, read our instructions below.

