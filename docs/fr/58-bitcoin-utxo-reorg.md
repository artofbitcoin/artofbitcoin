# 58 — UTXO et invalidation après reorg

**Source :** `prototype/bitcoin_utxo_validator.py`.

Ce chapitre isole l’invalidation des sorties orphelines. les sorties issues d’une branche abandonnée sont retirées de l’état accepté avant nouveau calcul. L’analyse conserve le contexte de la donnée et distingue le comportement du prototype de toute garantie de production.

**Point de vigilance.** Conserver une sortie orpheline comme disponible crée un risque de double comptage. Cette note est documentaire : aucun audit, test ou déploiement n’est revendiqué.

_Suite : [Finalité d’un message Base](59-base-message-finality.md)._
