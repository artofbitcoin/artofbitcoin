# 47 — Remplissage partiel

**Source :** `prototype/hyperliquid_order_lifecycle.py`.

Ce chapitre isole le reliquat ouvert. la quantité exécutée et la quantité restante sont conservées séparément. L’analyse conserve le contexte de la donnée et distingue le comportement du prototype de toute garantie de production.

**Point de vigilance.** Confondre les deux quantités fausse la position et la réconciliation. Cette note est documentaire : aucun audit, test ou déploiement n’est revendiqué.

_Suite : [Réconciliation Hyperliquid](48-hyperliquid-reconcile.md)._
