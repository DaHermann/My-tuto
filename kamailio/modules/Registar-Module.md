# REGISTAR MODULE


## Fonctions

### save(domain, [, flags [, uri]])

La fonction traite un **message REGISTER**. Elle peut ajouter, supprimer ou modifier les enregistrements usrloc en fonction des contacts et des dates d'expiration des HF dans le message REGISTER. 
En cas de succès et lorsqu'elle est appelée depuis le **REQUEST_ROUTE**, **200 OK** seront renvoyés, listant tous les contacts qui sont actuellement en usrloc. 
En cas d'erreur, un message d'erreur sera envoyé avec une courte description dans la phrase de raison.

La signification des paramètres est la suivante :

  * **domain** - Domaine logique au sein du bureau d'enregistrement. Si une base de données est utilisée, il doit s'agir du nom de la table qui stocke les contacts.

  * **flags** (acultatif) - la valeur peut être un OU bit par bit des drapeaux suivants :

       * **0x01** - enregistrer les contacts uniquement dans le cache mémoire sans aucune opération sur la base de données ;

       * **0x02** - ne pas générer de réponse SIP à la requête REGISTER en cours. Lorsqu'il est utilisé dans **ONREPLY_ROUTE**, ce paramètre est obsolète.

       * **0x04** - stocker et maintenir un contact par AoR. S'il existe d'autres adresses de contact pour l'AoR qui ne correspondent pas à l'enregistrement actuel, supprimez-les. Ce mode assure un contact par AoR (utilisateur).

Les drapeaux peuvent être donnés en format décimal ou hexa.

  * **uri** (facultatif - le paramètre flags doit être défini et peut être 0 pour le comportement par défaut) - l'URI SIP doit être utilisé à la place de l'URI de l'en-tête To. Il peut s'agir d'une chaîne dynamique avec des pseudo-variables.

Codes de retour :

*  **-1** - erreur.

   **1** - contacts insérés.

   **2** - contacts mis à jour.

   **3** - contacts supprimés.

   **4** - contacts retournés.

Cette fonction peut être utilisée à partir de **REQUEST_ROUTE** et **REPLY_ROUTE**.

**EXEMPLE**

    ...
    save("location");
    save("location", "0x01");
    save("location", "0x00", "sip:test@kamailio.org");
    ...
    
    
## lookup(domain [, uri])

La fonction extrait le nom d'utilisateur de la demande d'information et tente de trouver tous les contacts pour le nom d'utilisateur dans **usrloc**. S'il n'y a pas de tels contacts, **-1** sera renvoyé. S'il existe de tels contacts, **Request-URI** sera écrasé par le contact qui a la valeur q la plus élevée et, éventuellement, le reste sera ajouté au message (selon la valeur du paramètre **append_branches**).

Si l'option **method_filtering** est activée, la fonction de recherche retournera uniquement les contacts qui supportent la méthode de la demande traitée.

La signification des paramètres est la suivante :

 * **domain** - Nom de la table qui doit être utilisée pour la recherche.

 * **uri** (facultatif) - URI SIP à utiliser à la place de R-URI. Il peut s'agir d'une chaîne dynamique avec des pseudo-variables.

Codes de retour :

* **1** - contacts trouvés et retournés.

  **-1** - aucun contact trouvé.

  **-2** - contacts trouvés, mais méthode non prise en charge.

  **-3** - erreur interne lors du traitement.

Cette fonction peut être utilisée à partir de **REQUEST_ROUTE, FAILURE_ROUTE**.

**EXEMPLE**

     ...
    lookup("location");
    switch ($retcode) {
        case -1:
        case -3:
            sl_send_reply("404", "Not Found");
            exit;
        case -2:
            sl_send_reply("405", "Not Found");
            exit;
    };
    ...
