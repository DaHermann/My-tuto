
#!define WITH_MYSQL
#!define WITH_AUTH
#!define WITH_USRLOCDB
#!define WITH_NAT
#!define WITH_MYSQL
#!define WITH_AUTH
#!define WITH_USRLOCDB
#!define WITH_NAT
#!define WITH_WEBSOCKETS


#------------------- WINNER PART ---------------------------

#!ifdef WITH_WEBSOCKETS 
#!substdef "!MY_IP_ADDR!192.168.70.120!g"
#!substdef "!MY_TCP_PORT!5061!g"
#!substdef "!MY_UDP_PORT!5060!g"
#!substdef "!MY_TCP_ADDR!tcp:MY_IP_ADDR:MY_TCP_PORT!g"
#!substdef "!MY_UDP_ADDR!udp:MY_IP_ADDR:MY_UDP_PORT!g"

#!substdef "!MY_WS_PORT!8090!g"
#!substdef "!MY_WSS_PORT!4443!g"
#!substdef "!MY_WS_ADDR!tcp:MY_IP_ADDR:MY_WS_PORT!g"
#!substdef "!MY_WSS_ADDR!tls:MY_IP_ADDR:MY_WSS_PORT!g"
#!endif

#------------------- / WINNER PART ---------------------------

...

/* number of SIP routing processes for all TCP/TLS sockets */
# tcp_children=8

#!ifdef WITH_WEBSOCKETS
tcp_accept_no_cl=yes
#!endif

/* uncomment the next line to disable the auto discovery of local aliases
 * based on reverse DNS on IPs (default on) */
# auto_aliases=no

...

#------------------- WINNER PART ---------------------------

#!ifdef WITH_WEBSOCKETS
listen=MY_TCP_ADDR
listen=MY_UDP_ADDR
listen=MY_WS_ADDR
#!ifdef WITH_TLS
listen=MY_WSS_ADDR
#!endif
#!endif
#------------------- / WINNER PART ---------------------------

...

#!ifdef WITH_MYSQL
loadmodule "db_mysql.so"
#!endif


loadmodule "jsonrpcs.so"
loadmodule "kex.so"
loadmodule "corex.so"
loadmodule "tm.so"
loadmodule "tmx.so"
loadmodule "sl.so"
loadmodule "rr.so"
loadmodule "pv.so"
loadmodule "maxfwd.so"
loadmodule "usrloc.so"
loadmodule "registrar.so"
loadmodule "textops.so"
loadmodule "siputils.so"
loadmodule "xlog.so"
loadmodule "sanity.so"
loadmodule "ctl.so"
loadmodule "cfg_rpc.so"
loadmodule "acc.so"
loadmodule "counters.so"
loadmodule "textopsx.so"  # ---WINNEER
loadmodule "sdpops.so" # ---WINNEER
...

#!ifdef WITH_NAT
loadmodule "nathelper.so"
loadmodule "rtpengine.so" # WINNER
#!endif

...

#---------- WINNER PART --------------------------------

#!ifdef WITH_WEBSOCKETS
loadmodule "xhttp.so"
#loadmodule "msrp.so"  # Only required if using MSRP over WebSockets
loadmodule "websocket.so"
#!endif

#------------------------------------------

...


/* Main SIP request routing logic
 * - processing of any incoming SIP request starts with this route
 * - note: this is the same as route { ... } */
request_route {

	# per request initial checks
	route(REQINIT);

#------------------WINNER NAT PART ---------------
#!ifdef WITH_WEBSOCKETS
	if (nat_uac_test(64)) {
		# Do NAT traversal stuff for requests from a WebSocket
		# connection - even if it is not behind a NAT!
		# This won't be needed in the future if Kamailio and the
		# WebSocket client support Outbound and Path.
		force_rport();
		if (is_method("REGISTER")) {
			fix_nated_register();
		} else {
			if (!add_contact_alias()) {
				xlog("L_ERR", "Error aliasing contact <$ct>\n");
				sl_send_reply("400", "Bad Request");
				exit;
			}
		}
	}
#!endif
#------------------WINNER NAT PART ---------------

	
	# NAT detection
	route(NATDETECT);
	
	...
}


route[WITHINDLG] {
	if (!has_totag()) return;

	# sequential request withing a dialog should
	# take the path determined by record-routing
	if (loose_route()) {

#!ifdef WITH_WEBSOCKETS
		if ($du == "") {
			if (!handle_ruri_alias()) {
				xlog("L_ERR", "Bad alias <$ru>\n");
				sl_send_reply("400", "Bad Request");
				exit;
			}
		}
#!endif
		route(DLGURI);
		if (is_method("BYE")) {
			setflag(FLT_ACC); # do accounting ...
			setflag(FLT_ACCFAILED); # ... even if the transaction fails
		} else if ( is_method("ACK") ) {
			# ACK is forwarded statelessly
			route(NATMANAGE);
		} else if ( is_method("NOTIFY") ) {
			# Add Record-Route for in-dialog NOTIFY as per RFC 6665.
			record_route();
		}
		route(RELAY);
		exit;
	}
	
	...
}



#!ifdef WITH_WEBSOCKETS
onreply_route {
	if ((($Rp == MY_WS_PORT || $Rp == MY_WSS_PORT)
		&& !(proto == WS || proto == WSS))) {
		xlog("L_WARN", "SIP response received on $Rp\n");
		drop;
	}
	if (nat_uac_test(64)) {
		# Do NAT traversal stuff for replies to a WebSocket connection
		# - even if it is not behind a NAT!
		# This won't be needed in the future if Kamailio and the
		# WebSocket client support Outbound and Path.
		add_contact_alias();
	}
}

event_route[xhttp:request] {
	set_reply_close();
	set_reply_no_connect();
	
	if ($Rp != MY_WS_PORT
#!ifdef WITH_TLS
	    && $Rp != MY_WSS_PORT
#!endif
	) {
		xlog("L_WARN", "HTTP request received on $Rp\n");
		xhttp_reply("403", "Forbidden", "", "");
		exit;
	}

	xlog("L_DBG", "HTTP Request Received\n");

	if ($hdr(Upgrade)=~"websocket"
			&& $hdr(Connection)=~"Upgrade"
			&& $rm=~"GET") {

		# Validate Host - make sure the client is using the correct
		# alias for WebSockets
		if ($hdr(Host) == $null || !is_myself("sip:" + $hdr(Host))) {
			xlog("L_WARN", "Bad host $hdr(Host)\n");
			xhttp_reply("403", "Forbidden", "", "");
			exit;
		}

		# Optional... validate Origin - make sure the client is from an
		# authorised website.  For example,
		#
		# if ($hdr(Origin) != "http://communicator.MY_DOMAIN"
		#     && $hdr(Origin) != "https://communicator.MY_DOMAIN") {
		#	xlog("L_WARN", "Unauthorised client $hdr(Origin)\n");
		#	xhttp_reply("403", "Forbidden", "", "");
		#	exit;
		# }

		# Optional... perform HTTP authentication

		# ws_handle_handshake() exits (no further configuration file
		# processing of the request) when complete.
		if (ws_handle_handshake())
		{
			# Optional... cache some information about the
			# successful connection
			exit;
		}
	}

	xhttp_reply("404", "Not Found", "", "");
}

event_route[websocket:closed] {
	xlog("L_INFO", "WebSocket connection from $si:$sp has closed\n");
}

#!endif
