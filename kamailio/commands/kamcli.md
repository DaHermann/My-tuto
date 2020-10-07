# kamcli commands

Les nouvelles commandes pour kamcli peuvent être implémentées sous forme de plugins, chaque commande étant implémentée dans un fichier situé dans `kamcli/commandes/`.

Parmi les commandes implémentées :

* **acc** - manage accounting records
* **address** - manage permissions address records
* **aliasdb** - manage database aliases
* **avp** - manage avp user preferences
* **config** - manage configuration file for kamcli
* **db** - manage kamailio database content
* **dialog** - manage active calls (dialog)
* **dialplan** - manage dialplan records
* **dispatcher** - manage load balancer (dispatcher)
* **domain** - manage domain records
* **dlgs** - manage dlgs module
* **group** - manage group membership records (acl)
* **htable** - manage htable module
* **moni** - continuous refresh of the values for a list of statistics
* **mtree** - manage memory trees (mtree)
* **pike** - manage pike module
* **pkg** - private memory (pkg) management
* **ps** - print the details for kamailio running processes
* **pstrap** - store runtime details and gdb backtraces for running processes with ps
* **rpc** - interact with kamailio via jsonrpc control commands (alias of jsonrpc)
* **rpcmethods** - return the list of available RPC methods (commands)
* **rtpengine** - manage RTPEngine records and instances
* **shm** - shared memory (shm) management
* **shv** - manage $shv(name) variables
* **shell** - run in interactive shell mode
* **speeddial** - manage speed dial records
* **srv** - server management commands (sockets, aliases, ...)
* **stats** - get kamailio internal statistics
* **subscriber** - manage SIP subscribers
* **tcp** - management commands for TCP connections
* **tls** - management commands for TLS profiles and connections
* **trap** - store runtime details and gdb backtraces for running processes
* **uacreg** - manage uac remote registration records
* **ul** - manage user location records
* **uptime** - print the uptime for kamailio instance


### some commands


        kamcli -d --help
        kamcli -d --config=kamcli/kamcli.ini --help

        kamcli subscriber show
        kamcli subscriber add test test00
        kamcli subscriber show test
        kamcli subscriber show --help
        kamcli -d subscriber passwd test01 test10
        kamcli -d subscriber add -t no test02 test02
        kamcli -d subscriber setattrs test01 rpid +123
        kamcli -d subscriber setattrnull test01 rpid

        kamcli -d jsonrpc --help
        kamcli -d jsonrpc core.psx
        kamcli -d jsonrpc system.listMethods
        kamcli -d jsonrpc stats.get_statistics
        kamcli -d jsonrpc stats.get_statistics all
        kamcli -d jsonrpc stats.get_statistics shmem:
        kamcli -d jsonrpc --dry-run system.listMethods

        kamcli -d config raw
        kamcli -d config show main db
        kamcli -d -no-default-configs config show main db

        kamcli -d db connect
        kamcli -d db show -F table version
        kamcli -d db show -F json subscriber
        kamcli -d db showcreate version
        kamcli -d db showcreate -F table version
        kamcli -d db showcreate -F table -S html version
        kamcli -d db clirun "describe version"
        kamcli -d db clishow version
        kamcli -d db clishowg subscriber


        kamcli -d ul showdb
        kamcli -d ul show
        kamcli -d ul rm test
        kamcli -d ul add test sip:test@127.0.0.1

        kamcli -d stats
        kamcli -d stats usrloc
        kamcli -d stats -s registered_users
        kamcli -d stats usrloc:registered_users
