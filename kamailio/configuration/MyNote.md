# Prise de note


## LES FICHIERS DE CONFIGURATION LES PLUS SIMPLES

  Présenté dans un exemple à l'intérieur d'un chapitre précédent, la configuration la plus simple est:

    request_route { 
        ;
    }


  Il supprime simplement toutes les demandes SIP reçues. Rappelez-vous que les réponses SIP sont acheminées automatiquement en fonction de la pile d'en-tête Via, donc la suppression de tout ce qui est reçu par Kamailio est effectuée par la configuration:
  
      request_route { 
        exit;
      } 
      reply_route {
        drop; 
      }

  Les requêtes SIP nécessitent une action explicite pour être transférées, donc la **exit** de l'exécution de la configuration sans action de transfert équivaut simplement à une suppression, mais l'action **drop** peut être utilisée dans le même but dans le bloc request_route.
  D'autre part, la réponse SIP est automatiquement acheminée en fonction des adresses dans les en-têtes Via, vous devez donc exécuter explicitement l'action «drop» afin de la marquer comme **not-forward** (non en-avant) pour le noyau Kamailio.
  
  
  ## STATELESS FORWARDING


  Construire un redirecteur de requêtes SIP vers un autre serveur SIP situé à l'IP 1.2.3.4 est aussi simple que:
    
    request_route { 
      rewritehostport(“1.2.3.4”); forward();
    }
    
  Les fonctions principales de rewritehostport () remplacent les parties domaine et port dans R-URI par la valeur du paramètre. 
  Le forward () utilise l'adresse dans R-URI pour le relais.
Si vous ne souhaitez pas modifier l'URI de la requête, transférez simplement via UDP vers IP 1.2.3.4, cela peut être encore plus simple: 

    request_route { 
        forward(1.2.3.4);
    }

    
   ## RÉPONDRE AVEC 200 OK TOUJOURS

  * L'envoi de 200 réponses ok à toutes les demandes reçues peut être utile lors du test des performances d'un autre nœud SIP

         loadmodule “sl.so” # chargement du module
         request_route {
            sl_send_reply(“200”, “OK”); #utilisation du module
          }

    Cette fois, nous chargeons un module,**sl, qui est celui qui peut construire et envoyer des réponses pour les requêtes SIP**.


## ÉPONDRE SÉLECTIVEMENT TOUJOURS


Un autre cas d'utilisation pour les tests est de répondre avec différents codes de statut basés sur différents critères. Par exemple, si c'est INVITE, BYE ou CANCEL répondez avec 200 0o, si c'est **MESSAGE** répondez avec 202 Accepté et pour le reste répondez avec 403 Interdit:

    request_route {
    
      if(is_method(“INVITE|BYE|CANCEL”)) { 
        sl_send_reply(“200”, “OK”);
      }else if(is_method(“MESSAGE”)) { 
        sl_send_reply(“202”, “Accepted”);
      }else {
        sl_send_reply(“403”, “Forbidden”);
      } 
      
    }

Le module Textops est chargé pour la fonction is_method(), qui peut tester le type de requête en fonction de l'ID interne, pour un ou plusieurs d'entre eux en même temps. Le noyau exporte le mot-clé **méthode** qui peut être utilisé pour comparer la méthode SIP sous forme de chaîne, donc, d’un point de vue fonctionnel, la configuration ci-dessus équivaut à :


    loadmodule “sl.so” 
    request_route {
      if(method==“INVITE” || method==”BYE” || method==”CANCEL”) {
        sl_send_reply(“200”, “OK”);
      } else if(method==“MESSAGE”) {
        sl_send_reply(“202”, “Accepted”); 
      } else {
        sl_send_reply(“403”, “Forbidden”); 
      }
    }










