# 45 — Fenêtre anti-rejeu Hyperliquid

**Source :** `prototype/hyperliquid_signed_nonce.py`.

Ce chapitre isole la validité temporelle. la demande est limitée par une fenêtre afin de réduire l’acceptation tardive. L’analyse conserve le contexte de la donnée et distingue le comportement du prototype de toute garantie de production.

**Point de vigilance.** La fenêtre doit rester compatible avec les délais du relai. Cette note est documentaire : aucun audit, test ou déploiement n’est revendiqué.

_Suite : [Cycle de vie d’un ordre](46-hyperliquid-order.md)._
