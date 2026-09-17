# 13 — Règles de politique mempool

**Source :** `prototype/bitcoin_mempool_policy.py`.

Ce chapitre isole la distinction politique-consensus. le modèle sépare les transactions relayées par politique locale de celles valides selon le consensus. L’analyse conserve le contexte de la donnée et distingue le comportement du prototype de toute garantie de production.

**Point de vigilance.** Le refus par un nœud ne prouve pas que la transaction est invalide partout. Cette note est documentaire : aucun audit, test ou déploiement n’est revendiqué.

_Suite : [Remplacement et priorité mempool](14-bitcoin-mempool-replacement.md)._
