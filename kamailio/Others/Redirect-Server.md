

## SERVER de redirection


      route[INVITE_REDICTOR]{
          if(is_method("INVITE")){
        #!ifdef REWRITE_IP_ADDRESS
            if(!lookup("location") && from_uri==myself){
              if(!($rU=~"^(\+|00)[1-9][0-9]{2,3}$")){ # verification pstn
                #rewritehostport("192.168.50.130");
                $rd = REWRITE_IP_ADDRESS;
                sl_send_reply("302","Not local User, redirection");
                exit;
              }
            }else if(!lookup("location") && !from_uri==myself){
              sl_send_reply("404", "Correspondant injoignable");
              exit;
            }
        #!endif
          }
        }
