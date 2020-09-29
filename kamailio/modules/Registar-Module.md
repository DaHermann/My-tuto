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
