# 57 — Ancêtre commun lors d’un reorg

**Source :** `prototype/bitcoin_reorg_detector.py`.

Ce chapitre isole la recherche de l’ancêtre commun. le détecteur compare les chaînes jusqu’à un point partagé avant de qualifier les blocs remplacés. L’analyse conserve le contexte de la donnée et distingue le comportement du prototype de toute garantie de production.

**Point de vigilance.** Sans ancêtre commun identifié, la réconciliation ne doit pas produire de résultat final. Cette note est documentaire : aucun audit, test ou déploiement n’est revendiqué.

_Suite : [UTXO et invalidation après reorg](58-bitcoin-utxo-reorg.md)._
