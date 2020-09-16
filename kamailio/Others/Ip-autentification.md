# Autantification IP

      #IP authorization and user authentication
      route[AUTH] {
      #!ifdef WITH_AUTH

      #!ifdef WITH_IPAUTH

        if( (!is_method("REGISTER")) && allow_source_address_group() ){
          # source IP allowed
          return;
        }else if((!is_method("REGISTER")) && !from_uri==myself){
          sl_send_reply("403", "Formelement Interdit"); 
            exit;
        }
      #!endif

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
        # if caller is not local subscriber, then check if it calls
        # a local destination, otherwise deny, not an open relay here
        if (from_uri!=myself && uri!=myself) {
          sl_send_reply("403","Not relaying");
          exit;
        }

      #!else

        # authentication not enabled - do not relay at all to foreign networks
        if(uri!=myself) {
          sl_send_reply("403","Not relaying");
          exit;
        }

      #!endif
        return;
      }
