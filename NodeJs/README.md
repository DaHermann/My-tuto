* Install stable Node.js from Ubuntu respository

        sudo apt install nodejs
    
* Once installed, check the Node.js version:

            node --version
            v10.15.2


### 1) As a regular user first the install NVM manager:

    v:0.33
    wget -qO- https://raw.githubusercontent.com/creationix/nvm/v0.33.8/install.sh | bash -
    or
    v:0.40
    curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.40.0/install.sh | bash
    
    
### 2) Update your shell environment:

      source ~/.profile
      
### 3) Check the NVM availablity by checking for its version:

    $ nvm --version
    0.33.8

### 4) Next, list all available Node.js versions:


          $ nvm ls-remote
          ...
                 v12.13.0   (LTS: Erbium)
                 v12.13.1   (Latest LTS: Erbium)
                  v13.0.0
                  v13.0.1
                  v13.1.0
          ->      v13.2.0
  
  
  
#### 5)  Select and take a note of the Node.js version number your wish to install. Once ready execute the following command to install any desired version. For example:

      $ nvm install 13.2.0
      
#### 6)  Check for installed Node.js version:  
      
      $ node -v
      v13.2.0
