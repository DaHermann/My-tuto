# Installation de KVM

## Check Virtualization Support on Ubuntu 20.04

  *  Before you begin with installing KVM, check if your CPU supports hardware virtualization: 

          egrep -c '(vmx|svm)' /proc/cpuinfo
