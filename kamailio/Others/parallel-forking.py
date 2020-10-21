@@@@------- Parallel forking --------@@@@


@@@@@@@@@@@ C'est Bon @@@@@@@@@@

# Avec alias_db module

modparam("alias_db", "domain_prefix", "sip.")
modparam("alias_db", "append_branches", 1) # permet d'ajouter plusieur branche

request_route{
  
  #------  Winner  ------
	if(is_method("INVITE"))
    route(PARALLEL);
  
  exit;
}

route[PARALLEL]{
  /*
    La fonction prend le R-URI et recherche pour voir s'il s'agit d'un
   alias ou non. S'il s'agit d'un alias pour un utilisateur local, le R-URI est
   remplacé par l'URI SIP de l'utilisateur.
  */
  
	alias_db_lookup("dbaliases");
		
	t_on_failure("parallel");
	route(LOCATION);
}

failure_route[parallel]{
	xlog(" je suis dans le failure route");

	if (t_check_status("486|408")) {
		$rU = "nan";
		xlog(" j'ai changé de user ");
		t_on_failure("no");
		route(LOCATION);
		exit;
	}
}

failure_route[no]{
	xlog("aucune reponse");
	t_reply("408","No body present");
	exit;
}

route[AUTH] {

  # ne pas authentifier si myself
	if(is_method("INVITE")){
		if(src_ip==myself)  # important à ajouter
			return;   # important à ajouter
	}

	if (is_method("REGISTER") || from_uri==myself) {
		# authenticate requests
		if (!auth_check("$fd", "subscriber", "1")) {
			auth_challenge("$fd", "0");
			exit;
		}
		# user authenticated - remove auth header
		if(!is_method("REGISTER|PUBLISH"))
			consume_credentials();
	}
  
}

route[LOCATION] {

#!ifdef WITH_SPEEDDIAL
	# search for short dialing - 2-digit extension
	if($rU=~"^[0-9][0-9]$") {
		if(sd_lookup("speed_dial")) {
			route(SIPOUT);
		}
	}
#!endif

#!ifdef WITH_ALIASDB
	# search in DB-based aliases
	if(alias_db_lookup("dbaliases")) {
		route(SIPOUT);
	}
#!endif

	$avp(oexten) = $rU;
	if (!lookup("location")) {
		$var(rc) = $rc;
		route(TOVOICEMAIL);
		t_newtran();
		switch ($var(rc)) {
			case -1:
			case -3:
				send_reply("404", "Not Found");
				exit;
			case -2:
				send_reply("405", "Method Not Allowed");
				exit;
		}
	}

	# when routing via usrloc, log the missed calls also
	if (is_method("INVITE")) {
		setflag(FLT_ACCMISSED);
	}

	route(RELAY);
	exit;
}
