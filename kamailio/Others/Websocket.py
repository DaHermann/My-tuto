#---- WINNER PART ---------------

# *** To enable Websocket:
#     - enable Webscket
#!define WITH_WEBSOCKETS
# 
#
# *** To enable Rtpengine:
#     - enable Rtpengine
#!define WITH_RTPENGINE
#
#



#----------- WINNER PART ---------------
#!ifdef WITH_WEBSOCKETS
#!substdef "!MY_IP_ADDR!192.168.50.130!g"
#!substdef "!MY_WS_PORT!8090!g"
#!substdef "!MY_WSS_PORT!4443!g"
#!substdef "!MY_WS_ADDR!tcp:MY_IP_ADDR:MY_WS_PORT!g"
#!substdef "!MY_WSS_ADDR!tls:MY_IP_ADDR:MY_WSS_PORT!g"
#!endif

listen=MY_IP_ADDR
#!ifdef WITH_WEBSOCKETS
listen=MY_WS_ADDR
#!ifdef WITH_TLS
listen=MY_WSS_ADDR
#!endif
#!endif



#!ifdef WITH_WEBSOCKETS
tcp_accept_no_cl=yes
#!endif



#!ifdef WITH_WEBSOCKETS
loadmodule "xhttp.so"
#loadmodule "msrp.so"  # Only required if using MSRP over WebSockets
loadmodule "websocket.so"
#!endif


#!ifdef WITH_NAT
...
# single rtproxy
#!ifdef WITH_RTPENGINE
modparam("rtpengine", "rtpengine_sock", "udp:localhost:2223")
#!endif
#!endif


# Caller NAT detection
route[NATDETECT] {
#!ifdef WITH_NAT
	force_rport();
	if (nat_uac_test("19")) {
		if (is_method("REGISTER")) {
			fix_nated_register();
		} else {
			if(is_first_hop()) {
				set_contact_alias();
			}
		}
		setflag(FLT_NATS);
	}
#------------------WINNER NAT PART ---------------
#!ifdef WITH_WEBSOCKETS
	if (nat_uac_test(64)) {
		# NAT traversal  WebSocket
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

#!endif
	return;
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
