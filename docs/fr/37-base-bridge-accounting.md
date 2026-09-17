# 37 — Comptabilité du bridge Base

**Source :** `prototype/base_deposit_withdrawal.py`.

Ce chapitre isole le rapprochement des montants. le contrôle sépare quantité demandée, frais, quantité livrée et éventuel reliquat. L’analyse conserve le contexte de la donnée et distingue le comportement du prototype de toute garantie de production.

**Point de vigilance.** Les frais doivent être explicitement attribués pour éviter un faux déficit. Cette note est documentaire : aucun audit, test ou déploiement n’est revendiqué.

_Suite : [Frontière HyperEVM-HyperCore](38-hyperevm-boundary.md)._
