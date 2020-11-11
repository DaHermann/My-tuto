#-------------- Secure kamailio against attacks -----------------

#----- Flood attacks ------

#!define WITH_ANTIFLOOD

#----- Encripting the signaling -----

#!define WITH_TLS

/* La communication Tls est asynchrone par défaut, selon la configuration de la couche TCP du noyau. 
Les opérations TLS de cryptage et de décryptage nécessitent plus de ressources en termes de CPU et de mémoire, 
donc si le trafic sur TLS est important, assurez-vous d'utiliser un serveur assez puissant.
*/

#----- Dictionary attacks ------

modparam(“htable”, "htable", "userban=>size=8;autoexpire=920;initval=0;")

route[AUTH] { 
  
  #!ifdef WITH_AUTH
  #!ifdef WITH_IPAUTH
        if((!is_method("REGISTER")) && allow_source_address()) {
              # source IP allowed
              return; 
        }
  #!endif
        if( $sht(userban=>$var(srcip)::$au::auth_count) >= 3 ) {
              $var(exp) = $Ts - 900; 
              if($sht(userban=>$var(srcip)::$au::last_auth) > $var(exp)) {
                    xdbg("auth - [$ci] [$cs $rm] [$fu -> $ru ($tu)]: User blocked - IP: $var(srcip)\n");
                    sl_send_reply("403", "Try later");
                    exit;
              } else {
                    $sht(userban=>$var(srcip)::$au::auth_count) = 0;
              } 
        }
        if(!(is_present_hf("Authorization") || is_present_hf("Proxy-Authorization"))) { 
              auth_challenge("$fd", "0");
              exit; 
        }
        # authenticate requests
        if (!auth_check("$fd", "subscriber", "1")) {
              $var(auth_count) = $shtinc(userban=>$var(srcip)::$au::auth_count); 
              if( $var(auth_count) >= 3)
                    xlog("many failed auth in a row - [$rm] from <$fu> src ip: $var(srcip)\n");   
                    $sht(userban=>$var(srcip)::$au::last_auth) = $Ts;
              auth_challenge("$fd", "0");
              exit;
        }
        $sht(userban=>$var(srcip)::$au::auth_count) = $null;
        # user authenticated - remove auth header 
        if(!is_method("REGISTER|PUBLISH")) {
              consume_credentials(); 
        }
  #!endif
        return;
  } 
