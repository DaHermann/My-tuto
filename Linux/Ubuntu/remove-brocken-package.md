# Remove brocken package



Tape this command to :

    mv /var/lib/dpkg/info/PAQUET.* /tmp/
    
    dpkg --remove --force-remove-reinstreq PAQUET
  
