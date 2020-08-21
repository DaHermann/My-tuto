# DESCRIPTION

    kamctl is a shell script to control Kamailio SIP server It can be used to manage users, domains, aliases and other server options.

## COMMANDS

  * **Daemon Commands:**

    `start` Start Kamalio

    `restart`Restart Kamalio

    `stop` Stop Kamalio

    `online` Display online users

    `monitor` Show server's internal status

    `ping <uri>` Ping <uri> with SIP OPTIONS

    `Access` control list (acl) management commands:

    `acl show [<username>]` Show user membership

    `acl grant <username> <group>` Grant user membership (*)

    `acl revoke <username> [<group>]` Grant user membership(s) (*)

  * **Least cost routes (lcr) management command:**
    
    `lcr dump` Show in memory gateways and routes tables
    
    `lcr reload`  Reload lcr gateways and routes

  * **Carrierroute tables('cr') management commands:**
  
    `cr show` Show tables

    `cr reload` Reload tables

    `cr dump` Show in memory tables

    `cr addrt <routing_tree_id> <routing_tree>` Add a tree

    `cr rmrt <routing_tree>`  Remove a tree

    `cr addcarrier` <carrier> <scan_prefix> <domain> <rewrite_host> <prob> <strip> <rewrite_prefix> <rewrite_suffix> <flags> <mask> <comment>
      Add a carrier (prob, strip, rewrite_prefix, rewrite_suffix, flags, mask and comment are optional arguments)

    `cr rmcarrier <carrier> <scan_prefix> <domain>` Remove a carrier

  * **Remote-Party-ID (RPID) management commands:**

    `rpid add <username> <rpid>`Add rpid for a user (*)

    `rpid rm <username>`  Set rpid to NULL for a user (*)

    `rpid show <username>`  Show rpid of a user

  * **Subscriber management commands:**
    
    `add <username> <password>` Add a new subscriber (*)

    `passwd <username> <passwd>`  Change user's password (*)

    `rm <username>` Delete a user (*)

  * **Commands to manage 'trusted':**
    
    `trusted show`  Show db content

    `trusted dump`  Show cache content

    `trusted reload`Reload db table into cache

    `trusted add <src_ip> <proto> <from_pattern> <tag>` Add a new entry (from_pattern and tag are optional arguments)

    `trusted rm <src_ip>` Remove all entres for the given src_ip

  * **Dispatcher management commands:**
 
    `dispatcher show` Show dispatcher gateways

    `dispatcher reload` Reload dispatcher gateways

    `dispatcher dump` Show in memory dispatcher gateways

    `dispatcher addgw <setid> <destination> <flags> <description>`  Add gateway

    `dispatcher rmgw <id>`  Delete gateway

  * **Cisco restart command:**

    `cisco_restart <uri>` Restart phone configured for <uri>

  * **User location('ul') or aliases management commands:**

    `ul show` [<username>] Show in-RAM online users

    `ul show --brief` Show in-RAM online users in short format

    `ul rm` <username> [<contact URI>]  Delete user's usrloc entries

    `ul add` <username> <uri> Introduce a permanent usrloc entry

    `ul add` <username> <uri> <expires> Introduce a temporary usrloc entry

    `ul add` <username> <uri> <expires> <path>  Introduce a temporary usrloc entry including a path

  * **Fifo commands:**

    `fifo`  Send raw FIFO command
    

    #### FILES

        /etc/kamailio/.kamctlrc
        /usr/local/etc/kamailio/.kamctlrc
        ~/.kamctlrc
