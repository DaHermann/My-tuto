# Installation de KVM

## Check Virtualization Support on Ubuntu 20.04

  *  1. Before you begin with installing KVM, check if your CPU supports hardware virtualization: 

                   egrep -c '(vmx|svm)' /proc/cpuinfo
          
  *  2. Now, check if your system can use KVM acceleration by typing:

                   sudo kvm-ok
          
  *  3. To install cpu-checker, run the following command:

                   sudo apt install cpu-checker
          
  *  4. When the installation completes, restart the terminal.


## Install KVM on Ubuntu 20.04

### Step 1: Install KVM Packages

  *  1. First, update the repositories:

                   sudo apt update
           
  *  2. Then, install essential KVM packages with the following command:

                   sudo apt install qemu-kvm libvirt-daemon-system libvirt-clients bridge-utils
           
  *   3. When prompted, type Y, press ENTER, and wait for the installation to finish.

### Step 2: Authorize Users

  *  1. Only members of the libvirt and kvm user groups can run virtual machines. Add a user to the libvirt group by typing:

                   sudo usermod -aG libvirt $USER

  *  2. Now do the same for the kvm group:

                   sudo usermod -aG kvm $USER

### Step 3: Verify the Installation

  *  1. Confirm the installation was successful by using the virsh command:

                   virsh list --all
          
  *  2. Or use the systemctl command to check the status of libvirtd:

                   sudo systemctl status libvirtd
     
  *  4. If the virtualization daemon is not active, activate it with the following command:
  
                   sudo systemctl enable --now libvirtd

## Creating a Virtual Machine on Ubuntu 20.04

*  1. Before you choose one of the two methods listed below, install virt-manager, a tool for creating and managing VMs:
    
                   sudo apt install virt-manager
       
 * 2. Type Y and press ENTER. Wait for the installation to finish.

##  Method 1: Virt Manager GUI

  *  Start virt-manager with:
 
         sudo virt-manager

