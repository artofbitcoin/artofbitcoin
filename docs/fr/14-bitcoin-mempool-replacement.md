# 14 — Remplacement et priorité mempool

**Source :** `prototype/bitcoin_mempool_policy.py`.

Ce chapitre isole la compétition entre transactions. la politique compare frais, dépendances et règles de remplacement avant d’accepter une nouvelle version. L’analyse conserve le contexte de la donnée et distingue le comportement du prototype de toute garantie de production.

**Point de vigilance.** Une interface doit signaler la différence entre remplacement local et inclusion confirmée. Cette note est documentaire : aucun audit, test ou déploiement n’est revendiqué.

_Suite : [Suite](15-suite.md)._
