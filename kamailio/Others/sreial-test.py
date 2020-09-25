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










