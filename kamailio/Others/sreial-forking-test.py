---------------------TEST DE SERIAL FORKING ------------------------



@@@@@@@@@@@@@@@@@@@@@@ ÇA PASSE PAS @@@@@@@@@@@@@@@@@@

# Winner functions
route[SERIAL_F]{
	if(is_method("INVITE")){
		seturi("sip:9000678@$rd");
		append_branch("sip:823456@$rd", "1.0");
		#append_branch("sip:912356@$rd", "0.5");
		xlog("next : t_next_contacts();");

		t_load_contacts();

		t_next_contacts();
		t_on_failure("serial");
		t_relay();
		break;
	}
}
failure_route["serial"]
{
  if (!t_next_contacts()) {
    exit;
  }

  t_on_failure("serial");
  t_relay();
}

---------------------------------------------------------------------------------

 @@@@@@@@@@@@ ÇA PASSE PAS @@@@@@@@@@@@@@@@@@@@@ 

route[WINS_TEST]{

	### Patch ### Read q-value from User-Agent header and use it.
	if(is_method("REGISTER") && is_present_hf("Contact")){

		$var(qval)=$(hdr(User-Agent){param.value,q});
		
		if(($var(qval) != $null) && ($var(qval) != "0") | $var(qval)!="-1.O"){
			#xlog("L_NOTICE", "q-value set by the client is q=$var(qval) - R=$ru ID=$cin");
			xlog("je ne suis pas null");
			$var(newct) = $ct + ';q=' + "$var(qval)";
			remove_hf("Contact");
			#append_hf("Contact: $(var(newct))rn");
		}else{
			xlog("je suis null");
			sql_query("db_connection","select * from location where username=$fU","res_Users");
			$var(usernumb) = $dbr(res_Users=>rows);

			if($var(usernumb)==1 | $var(usernumb)>1){
				# un user trouvé ou plusieurs
				$var(usernumb)= $var(usernumb)+3;
				$var(newct) = $ct + ';q=0.' + '$var(usernumb)';
				remove_hf("Contact");
				#append_hf("Contact: $(var(newct))rn");
				xlog("many Users or One");
			}else{
				# pas de location 
				xlog("no User");
				$var(newct) = $ct + ';q=0.' + 9;
				remove_hf("Contact");
				#append_hf("Contact: $(var(newct))rn");
			}

			xlog("$var(qval)");

		}
	}
}

---------------------------------------------------------------------------------------


 @@@@@@@@@@@@ ÇA PASSE PAS @@@@@@@@@@@@@@@@@@@@@ 

route[UPDATE_Q] {
	#sql_query("db_connection","select * from location","locations");

	#$var(me) = 0;
	#$var(len) = $dbr(locations=>rows);
	#xlog("c'est la longueur $var(len)");

	if(is_method("INVITE")){
		sql_query("db_connection","select * from location where username=$rU","users");

		$var(userlen) = $dbr(users=>rows);
		if($var(userlen)>1){
			$var(i) = 0;
			while($var(i)<$var(userlen)){
				xlog("id = $dbr(users=>[$var(i),0])");
				$var(id) = $dbr(users=>[$var(i),0]);
				$var(q) = ($var(i) + 2);
				sql_query("db_connection","update location set q='0.$var(q)'  where id=$var(id)");
				$var(i) = $var(i) + 1;	
			}
		}	
	}

}

---------------------------------------------------------------------------------


 @@@@@@@@@@@@ ? @@@@@@@@@@@@@@@@@@@@@ 
	
*** AVEC DISPATCHER MODULE ****


loadmodule "dispatcher.so"
...

# ----- dispatcher params ----- 

modparam("dispatcher", "db_url", DBURL) 
modparam("dispatcher", "ds_ping_interval", 1)
modparam("dispatcher", "table_name", "dispatcher")
modparam("dispatcher", "flags", 2) 
modparam("dispatcher", "ds_ping_latency_stats", 1)
modparam("dispatcher", "ds_latency_estimator_alpha", 900)

# requette SQL pour save une adresse ip dans la table dispatcher

INSERT INTO "dispatcher" VALUES(1,1,'sip:192.168.0.1:5060',0,12,'rweight=50;weight=50;cc=1;','');


request_route {
# do checks , indialog etc ...
# dispatch destinations 
route(DISPATCH); 
}

# Dispatch requests
route[DISPATCH] {
     # round robin dispatching on gateways group '1'
     if(!ds_select_dst("1", "4")) {
         send_reply("404", "No destination");
         exit;
     }
     xlog("L_DBG", "--- SCRIPT: going to <$ru> via <$du>\n");
     t_on_failure("RTF_DISPATCH");
     route(RELAY);
     exit;
 }


# Try next destinations in failure route, except if session gets cancelled 
failure_route[RTF_DISPATCH] {
     if (t_is_canceled()) {
         exit;
     }
     # next DST - only for 500 or local timeout
     if (t_check_status("500") or (t_branch_timeout() and !t_branch_replied())) {
         if(ds_next_dst()) {
             t_on_failure("RTF_DISPATCH");
             route(RELAY);
             exit;
         }
     }
 }



---------------------------------------------------------------------------------


  @@@@@@@@@@@@ C'EST BON  @@@@@@@@@@@@@@@@@@@@@ 
	
	
route {

	# CANCEL processing
	if (is_method("CANCEL")) {
		if (t_check_trans()) {
			route(RELAY);
		}
		exit;
	}

	# handle retransmissions
	if (!is_method("ACK")) {
		if(t_precheck_trans()) {
			t_check_trans();
			exit;
		}
		t_check_trans();
	}

	# record routing for dialog forming requests (in case they are routed)
	# - remove preloaded route headers
	remove_hf("Route");
	if (is_method("INVITE|SUBSCRIBE")) {
		record_route();
	}

	# handle registrations
	route(REGISTRAR);

	if ($rU==$null) {
		# request with no Username in RURI
		sl_send_reply("484","Address Incomplete");
		exit;
	}

	# Serial forking
	route(SERIAL);

}


# Writting functionn space

route[SERIAL]{
   $ru = "sip:200@51.210.54.81:5060";
    xlog("ALERT : new request uri $ru \n");
    t_on_failure("1");
    route(LOCATE);
}

failure_route[1] {
    if(t_is_canceled()) {
        exit;
    }
    
    xlog(" an other alternative \n");

    if(t_check_status("486|408")){
        $ru = "sip:203@51.0.0.1:5060";
        xlog(" an other uri $ru \n");
        t_on_failure("2");
        route(LOCATE);
    }
}

failure_route[2] {
    if(t_is_canceled()) {
        exit;
    }
    
    xlog(" an other alternative \n");

    if(t_check_status("486|408")){
        rewriteuri("sip:8002@51.0.0.2:5060");
        xlog(" Rewrited to $ru \n");
        t_on_failure("3");
        route(LOCATE);
        exit;
    }
}

failure_route[3] {
    if(t_is_canceled()) {
        exit;
    }
    xlog( "nobody available \n");
    t_reply("500", "Server error"); 
}

route[LOCATE]{
	if(lookup("location")){
		route(RELAY);
		exit;
	}
	route(RELAY);
	exit;
}





