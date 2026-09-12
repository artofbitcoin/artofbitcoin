# STARK, SNARK et FHE : comparer les garanties

Un STARK fournit une preuve vérifiable d un calcul via une trace, des contraintes et un protocole de proximité. Un SNARK vise souvent une preuve plus compacte mais introduit des choix différents de paramètres et de primitives.

La FHE ne prouve pas à elle seule qu un calcul respecte une politique : elle permet d opérer sur des données chiffrées sous les hypothèses du schéma et de la gestion des clés.

Pour Bitcoin et ses extensions, il faut préciser si l objectif est de prouver un état, de compresser une vérification ou de préserver la confidentialité. Ces objectifs ne sont pas interchangeables.
