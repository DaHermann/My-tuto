

## Structure

La structure de kamailio.cfg peut être vue comme trois parties:

  * **paramètres globaux**
  * **paramètres des modules**
  * **blocs de routage**

Pour plus de clarté et pour faciliter la maintenance, il est recommandé de les conserver dans cet ordre, même si certains d'entre eux peuvent être mélangés.



### définir

Contrôlez en style C quelles parties du fichier de configuration sont exécutées. Les pièces dans les zones non définies ne sont pas chargées, ce qui garantit une moindre utilisation de la mémoire et une exécution plus rapide.

Directives disponibles:

 * **#!define NAME** - définir un mot-clé
 * **#!define NAME VALUE** - définir un mot-clé avec une valeur
 * **#!ifdef NAME** - vérifie si un mot-clé est défini
 * **#!ifndef** - vérifie si un mot clé n'est pas défini
 * **#!else** - passer à la fausse branche de la région ifdef / ifndef
 * **#!endif** - fin de la région ifdef / ifndef
 * **#!trydef** - ajoute une définition si elle n'est pas déjà définie
 * **#!redefine** - force la redéfinition même si elle est déjà définie
 <br/>

*le nombre de définitions autorisées est désormais défini sur 256*
