# 12 — Reprise après réorganisation

**Source :** `prototype/bitcoin_reorg_detector.py`.

Ce chapitre isole la reconstruction après divergence. le flux identifie les données à invalider et celles à rejouer après changement de chaîne. L’analyse conserve le contexte de la donnée et distingue le comportement du prototype de toute garantie de production.

**Point de vigilance.** Une reprise partielle peut laisser un solde ou un événement fantôme. Cette note est documentaire : aucun audit, test ou déploiement n’est revendiqué.

_Suite : [Règles de politique mempool](13-bitcoin-mempool.md)._
