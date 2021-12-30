# Development Tools


  Install the following tools:

  * Docker and Docker Compose
  * Homebrew only for MacOS users
  * VirtualBox
  * Vagrant

## Installation of pyenv
  
  **Step #1: Update and Install Dependencies**
  
          apt update -y
  
          apt install -y make build-essential libssl-dev zlib1g-dev \
          libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev\
          libncursesw5-dev xz-utils tk-dev libffi-dev liblzma-dev python-openssl\
          git
      
   **Step #2: Clone the Repository**
      
      
      git clone https://github.com/pyenv/pyenv.git ~/.pyenv
      
      
   **Step #3: Configure the Environment**
   
      echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bashrc
      echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bashrc
      echo -e 'if command -v pyenv 1>/dev/null 2>&1; then\n eval "$(pyenv init -)"\nfi' >> ~/.bashrc
      
      exec "$SHELL"
      
      
   **Step #4: Verify the Installation**
   
      pyenv install --list
   
   
   
   
## Installing Docker and Docker Compose on Ubuntu 18.04

  **Step #1:Install packages to allow apt to use a repository over HTTPS:**

            sudo apt-get install apt-transport-https ca-certificates curl software-properties-common

  Add Docker’s official GPG key:

            curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -

   Add the Docker repository to APT sources:

            sudo add-apt-repository  "deb [arch=amd64] https://download.docker.com/linux/ubuntu  $(lsb_release -cs) stable"

   Next, update the package database with the Docker packages from the newly added repo:

            sudo apt-get update

  **Step #2 :Install Docker Community Edition(CE).**
  
   Update the apt package index.

            sudo apt-get update

   Install the latest version of Docker CE

            sudo apt-get -y install docker-ce

   Docker should now be installed, the daemon started, and the process enabled to start on boot. Check that it's running:

            sudo systemctl status docker

   Verify that Docker CE is installed correctly by running the hello-world image.

             sudo docker run hello-world

   Executing Docker without sudo

   If you want to avoid typing sudo whenever you run the docker command, add your user to the docker group:

              sudo usermod -aG docker ${USER}

   To apply the new group membership, you can log out of the server and back in, or you can type the following:

              su - ${USER}

   You will be prompted to enter your user's password to continue. Afterwards, you can confirm that your user is now added to the docker group by typing:

              id -nG

  **Step #3:Installing docker-compose**
  
   Run this command to download the Docker Compose version 1.17:

               sudo curl -L https://github.com/docker/compose/releases/download/1.17.0/docker-compose-`uname -s`-`uname -m` -o /usr/local/bin/docker-compose

   Apply executable permissions to the binary:

              sudo chmod +x /usr/local/bin/docker-compose

   Test the installation.

              docker-compose --version
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
