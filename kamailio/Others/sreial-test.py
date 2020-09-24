# @@@@@@@@@@@@@@@@@@@@@@ TEST DE SERIAL FORKING @@@@@@@@@@@@@@@@@@



# @@@@@@@@@@@@@@@@@@@@@@ ÇA PASSE PAS @@@@@@@@@@@@@@@@@@
# Winner functions
route[WINS]{
	sql_query("locA", "select * from location where username=$rU", "res_loc");

/*
	$var(num) = 0;
	while( $var(num)<$dbr(res_loc=>rows) ){

		xlog();

	}
*/
	xlog("voici les location $dbr(res_loc=>rows)");
	sql_result_free("res_loc");
}

route[SERIAL_F]{
	if(is_method("INVITE")){
		seturi("sip:$rU@$rd");
		append_branch("sip:$rU@$rd", "1.0");
		#append_branch("sip:$rU@$rd", "0.5");
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

# @@@@@@@@@@@@ ÇA PASSE PAS @@@@@@@@@@@@@@@@@@@@@#

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




