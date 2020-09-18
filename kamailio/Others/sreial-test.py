# @@@@@@@@@@@@@@@@@@@@@@ TEST DE SERIAL FORKING @@@@@@@@@@@@@@@@@@



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
