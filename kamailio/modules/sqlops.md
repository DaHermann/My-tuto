# Module sqlops

## load the module

    loadmodule "sqlops"


## mod param

    modparam("sqlops","sqlcon","cb=>mysql://kamailio:kamailiorw@localhost/kamailio")
    
    
## Using

    ...
    sql_query("ca", "select * from domain", "ra");
    xlog("number of rows in table domain: $dbr(ra=>rows)\n");
    sql_result_free("ra");
    ...
