#Development Tools


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
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
