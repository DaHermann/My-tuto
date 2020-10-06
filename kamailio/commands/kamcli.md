# Some kamcli commands




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
