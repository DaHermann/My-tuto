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


## SERVEUR DE REDIRECTION SIP


Un serveur de redirection est censé envoyer des réponses 3xx avec les adresses alternatives dans les en-têtes Contact. Disons que Kamailio doit rediriger toutes les requêtes SIP vers le serveur 1.2.3.4, en préservant l'extension numérotée:


    loadmodule “sl.so” 
    request_route {
      rewritehostport(“1.2.3.4”);
      sl_send_reply(“302”, “Moved Temporarily”); 
    }


Lorsque le code de réponse est 3xx, le module prend les adresses dans l'ensemble de destination et crée les en-têtes Contact. L'ensemble de destination comprend l'URI de la demande et des branches supplémentaires.

Fournir plusieurs choix dans une réponse de redirection peut être fait avec :

    loadmodule “sl.so” 
    request_route {
      rewritehostport(“1.2.3.4”);
      append_branch();
      rewritehostport(“2.3.4.5”); sl_send_reply(“302”, “Moved Temporarily”);
    }

La réponse 302 contiendra deux destinations alternatives, aux adresses 1.2.3.4 et 2.3.4.5


## ÉQUILIBREUR DE CHARGE ROUND-ROBIN SIMPLE STATELESS


La logique de routage suivante est souhaitée:

* acheminer uniquement les demandes INVITE, pour le reste envoyer 404 non trouvé
* chaque processus Kamailio doit choisir la destination parmi deux adresses IP de manière circulaire


Chaque processus Kamailio doit stocker des informations sur le dernier serveur utilisé, pour les envoyer au suivant. Cela peut être fait en stockant l'index dans une variable de script stockant la valeur dans la mémoire privée

      loadmodule “sl.so” 
      loadmodule “textops.so”
      loadmodule “pv.so” 
      modparam("pv", "varset", "i=i:0")
      
      request_route {
        if(!is_method(“INVITE”)) { 
          sl_send_reply(“404”, “Not Found”); 
          exit;
        }
        
        $var(i) = ($var(i)+1) mod 2; 
        if($var(i)==1) {
          rewritehostport(“1.2.3.4”); 
        } else {
          rewritehostport(“2.3.4.5”); 
        }
        forward(); 
      }


**Le module pv est chargé pour pouvoir utiliser la pseudo-variable $var(i)**. Le paramètre du module varset est utilisé pour initialiser $var(i) à 0 (zéro) au démarrage (qui est la valeur initiale par défaut, mais il a été ajouté ici pour avoir un exemple explicite).
Sur la base de la valeur de $var(i), le premier (1.2.3.4) ou le deuxième (2.3.4.5) serveur sera utilisé pour le transfert. A chaque renvoi, le $var(i) est incrémenté puis il est appliqué une opération modulo 2 pour rester dans la plage 0 ou 1.
La valeur de $var(i) est stockée dans la mémoire privée, elle est donc spécifique à chaque processus Kamailio. Il persiste également lors du traitement de nombreuses demandes SIP, n'étant pas attaché à une demande, mais faisant partie de l'environnement d'exécution.










