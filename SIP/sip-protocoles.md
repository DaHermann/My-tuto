# Les protocoles SIP


## INVITE
   
   Lorsqu'un client agent utilisateur souhaite **lancer une session** (par exemple, **audio**, **vidéo** ou **jeu**), il formule une **requête INVITE**. 
   La requête INVITE demande à un    serveur d'établir une session. Cette demande peut être transmise par des **mandataires**, 
   arrivant éventuellement à un ou plusieurs UAS qui peuvent potentiellement accepter l'invitation. 
   Ces UAS devront fréquemment demander à l'utilisateur d'accepter l'invitation. Après un certain temps, ces UAS peuvent accepter l'invitation 
   (ce qui signifie   que la session doit être établie) en envoyant une réponse **2xx**.
   
   Si l'invitation n'est pas acceptée, une réponse **3xx**, **4xx**, **5xx** ou **6xx** est envoyée, en fonction de la raison du rejet. 
   Avant d'envoyer une réponse finale, l'UAS peut également envoyer des réponses provisoires (**1xx**) pour informer l'UAC de l'état d'avancement du contact 
   avec l'utilisateur appelé.


## INVITE re-INVITE

   
   Cette modification peut impliquer **la modification d'adresses ou de ports, l'ajout d'un flux multimédia, la suppression d'un flux multimédia, etc**.
   Ceci est accompli en envoyant une nouvelle demande INVITE dans la même boîte de dialogue qui a établi la session. 
   Une demande INVITE envoyée dans une boîte de dialogue existante est connue sous le nom de re-INVITE.

   Ressources:
   
   Notez qu'un seul **re-INVITE** peut modifier le dialogue et les paramètres de la session en même temps.

   re-INVITE a causé beaucoup de problèmes si nous ne savons pas exactement ce qui se passe avec UAC / UAS au moment où re-INVITE se produit.


## ACK

   
   Le protocole ACK est utilisé pour faciliter un échange de messages fiable pour les INVITE
   
   * L'appelant envoie une INVITE
   * L'appelé envoie un **200 OK** pour **accepter l'appel**
   * L'appelant envoie un **ACK** pour indiquer que la prise de contact est terminée et qu'**un appel va être établi**.
   
   Si le premier message INVITE comprend une description d'appel SDP, le 200OK inclut le SDP de l'appelé.


## CANCEL

   Le protocole CANCEL permet d'annuler une invitation
   
   La demande CANCEL, comme son nom l'indique, est **utilisée pour annuler une demande précédente envoyée par un client**. 
   Plus précisément, il demande à l'UAS de cesser de traiter la demande et de générer une réponse d'erreur à cette demande. 
   CANCEL n'a aucun effet sur une demande à laquelle un UAS a déjà donné une réponse finale.

   
   Pour cette raison, **il est plus utile d'annuler les demandes auxquelles un serveur peut mettre longtemps à répondre**. 
   Pour cette raison, CANCEL est préférable pour les demandes INVITE, qui peuvent prendre beaucoup de temps pour générer une réponse. 
   Dans cet usage, un UAS qui reçoit une demande CANCEL pour un INVITE, mais qui n'a pas encore envoyé de réponse finale, «arrêterait de sonner», 
   puis répondrait à l'INVITE avec une réponse d'erreur spécifique (un **487**).


## BYE

   Le protocole BYE permet de raccrocher une session
   
   Il est utilisée pour terminer une session spécifique ou une tentative de session. Dans ce cas, 
   la session spécifique est celle avec l'UA homologue de l'autre côté du dialogue. Lorsqu'un BYE est reçu dans un dialogue, 
   toute session associée à ce dialogue DEVRAIT se terminer. Un UA NE DOIT PAS envoyer un BYE en dehors d'un dialogue. 
   L'UA de l'appelant PEUT envoyer un BYE pour les dialogues confirmés ou les premiers dialogues, et l'UA de l'appelé PEUT envoyer un BYE sur 
   les dialogues confirmés, mais NE DOIT PAS envoyer un BYE sur les premiers dialogues.
   
   

## REGISTER
   
   REGISTER permet d'enregistrer un emplacement auprès d'un serveur d'enregistrement SIP
   
   L'enregistrement implique l'envoi d'une demande REGISTER (**demande d'enregistrement, d'inscription**) à un type spécial d'**UAS** 
   connu sous le nom de **registar**. 
   Un registar agit en tant que **frontal du service de localisation pour un domaine**, lisant et écrivant des mappages basés sur le contenu des demandes **REGISTER**.
   Ce service de localisation est ensuite généralement consulté par un serveur proxy qui est responsable du routage des demandes pour ce domaine.
   

## OPTIONS
























