# 46 — Cycle de vie d’un ordre

**Source :** `prototype/hyperliquid_order_lifecycle.py`.

Ce chapitre isole les transitions d’ordre. le modèle distingue création, acceptation, remplissage partiel, annulation et clôture. L’analyse conserve le contexte de la donnée et distingue le comportement du prototype de toute garantie de production.

**Point de vigilance.** Chaque transition doit être déterministe et observable dans le journal. Cette note est documentaire : aucun audit, test ou déploiement n’est revendiqué.

_Suite : [Remplissage partiel](47-hyperliquid-order-partial.md)._
