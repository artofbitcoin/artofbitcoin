# 18 — Dépendances dans le mempool

**Source :** `prototype/bitcoin_mempool_policy.py`.

Ce chapitre isole la relation parent-enfant. le modèle tient compte des transactions dépendantes avant de qualifier une entrée remplaçable ou relayable. L’analyse conserve le contexte de la donnée et distingue le comportement du prototype de toute garantie de production.

**Point de vigilance.** Ignorer l’ancêtre peut faire croire qu’une sortie est immédiatement disponible. Cette note est documentaire : aucun audit, test ou déploiement n’est revendiqué.

_Suite : [Manifeste de recherche Bitcoin](19-bitcoin-manifest.md)._
