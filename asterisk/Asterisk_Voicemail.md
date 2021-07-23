# Asterisk en tant que serveur de messagerie vocale

## Qu'est-ce que la messagerie vocale ?
  Également appelée « messagerie vocale », la messagerie vocale permet aux appelants de laisser des messages aux abonnés (utilisateurs) du système. Les systèmes de messagerie vocale sont fréquemment utilisés en conjonction avec les systèmes PBX, les téléphones mobiles et les services téléphoniques résidentiels.

  La messagerie vocale comprend plusieurs composants de base. Le processus de collecte de messages est activé lorsqu'un appelant ne parvient pas à joindre un utilisateur du système. L'application de collecte de messages reçoit des données du système téléphonique indiquant quel abonné l'appelant tentait de joindre. L'application diffuse un message d'accueil puis enregistre le message. Le message d'accueil peut être un message d'accueil système standard ou un message sortant personnalisé enregistré par l'abonné.

  Une fois le message enregistré, la composante de notification du système de messagerie vocale prend le relais et informe l'abonné qu'un nouveau message est disponible. Ceci est géré de différentes manières selon le type de système téléphonique avec lequel la plate-forme de messagerie vocale est intégrée. Dans la plupart des cas, le système de messagerie vocale enverra une commande au système en amont (PBX, plate-forme de commutation mobile, etc.), lui indiquant d'activer l'indicateur de message en attente (MWI) pour le téléphone de l'abonné. Le système de notification peut également envoyer un courrier électronique qui peut inclure un fichier audio en pièce jointe du message.

  Lorsque l'abonné reçoit la notification, il accède au message en utilisant l'une de plusieurs méthodes. Les anciens systèmes de messagerie vocale nécessitent que l'abonné appelle une application, s'authentifie à l'aide de son numéro de poste et de son mot de passe et écoute les messages de son magasin de manière séquentielle. Des systèmes plus modernes permettent à l'abonné de consulter ses messages sur son ordinateur de bureau ou son téléphone portable directement en utilisant la « messagerie vocale visuelle ». Si le message a été livré dans un e-mail, l'abonné peut également écouter à l'aide de son ordinateur.

  Une fois que le ou les messages ont été examinés, le système de messagerie envoie une autre commande au système téléphonique en amont, lui demandant d'éteindre l'indicateur de message en attente et/ou de diminuer le nombre de messages.

  La messagerie vocale avancée est un élément clé des plates-formes de « messagerie unifiée », des systèmes qui combinent plusieurs formats de messagerie en un seul point d'accès pour l'abonné. Dans un système de messagerie unifié, la boîte de réception contiendra des messages vocaux, e-mail, fax et parfois texte (IM et/ou SMS). La messagerie unifiée est souvent regroupée dans une plate-forme encore plus complète appelée Unified Communications ou UC.

## Faits et caractéristiques clés
  Tous les systèmes de messagerie vocale sont capables d'enregistrer des messages, d'informer les abonnés des messages en attente et de fournir un accès sécurisé à ces messages. La messagerie vocale est devenue une fonctionnalité standard sur la plupart des systèmes téléphoniques, mais la plupart des fournisseurs la vendent toujours en tant que produit complémentaire ou « complémentaire ».

  Les systèmes de messagerie vocale avancés peuvent transférer les messages directement aux abonnés sous forme de courrier électronique. Dans certains cas, l'abonné devra toujours supprimer les anciens messages du système de messagerie vocale. Des systèmes unifiés plus avancés synchroniseront automatiquement l'état des messages.

  Il existe plusieurs normes d'intégration des systèmes de messagerie vocale aux PBX et autres plates-formes de téléphonie. Il s'agit notamment de simples intégrations « in-band » qui utilisent des tonalités et des intégrations « hors bande » plus complexes qui utilisent diverses technologies. L'une des normes les plus courantes est "System Message Desk Interface" ou SMDI.

## Avantages clés
  Si elle est correctement mise en œuvre, la messagerie vocale peut augmenter la productivité et améliorer le service client.

## Asterisk comme système de messagerie vocale
  Les composants de messagerie vocale standard d'Asterisk facilitent l'assemblage d'une plate-forme de messagerie de classe mondiale. Avec plusieurs options de stockage de messages et la prise en charge de plusieurs techniques d'intégration, le remplacement d'un système de messagerie vocale d'entreprise vieillissant par un serveur Asterisk est simple.

  Pour plus d'informations sur les produits de messagerie vocale basés sur Asterisk, consultez  AsteriskExchange .
