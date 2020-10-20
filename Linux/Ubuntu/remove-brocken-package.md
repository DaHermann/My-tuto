# Remove brocken package


Here are the steps.

# 1
Find your package in `/var/lib/dpkg/info`, for example using: `ls -l /var/lib/dpkg/info | grep <package>`

# 2
Move the package folder to another location, like suggested in the blog post I mentioned before.

    sudo mv /var/lib/dpkg/info/<package>.* /tmp/
    
# 3   
Run the following command to remove the package:

    sudo dpkg --remove --force-remove-reinstreq <package>


